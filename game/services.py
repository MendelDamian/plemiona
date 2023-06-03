import random

from django.utils import timezone
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from game import exceptions
from game.consumers import GameConsumer
from game.models import GameSession, Player, Village


class GameSessionConsumerService:
    @staticmethod
    def send_start_game_session(game_session):
        game_consumer = GameConsumer()
        game_consumer.game_session = game_session
        game_consumer.room_group_name = str(game_session.game_code)
        game_consumer.channel_layer = get_channel_layer()

        async_to_sync(game_consumer.channel_layer.group_send)(
            game_consumer.room_group_name,
            {
                "type": "start_game_session",
            },
        )

    @staticmethod
    def send_fetch_resources(player):
        game_consumer = GameConsumer()
        game_consumer.player = player
        game_consumer.player_group_name = str(player.channel_name)
        game_consumer.channel_layer = get_channel_layer()

        async_to_sync(game_consumer.channel_layer.group_send)(
            game_consumer.player_group_name,
            {
                "type": "fetch_resources",
            },
        )

    @staticmethod
    def send_fetch_buildings(player):
        game_consumer = GameConsumer()
        game_consumer.player = player
        game_consumer.player_group_name = str(player.channel_name)
        game_consumer.channel_layer = get_channel_layer()

        async_to_sync(game_consumer.channel_layer.group_send)(
            game_consumer.player_group_name,
            {
                "type": "fetch_buildings",
            },
        )


class GameSessionService:
    @staticmethod
    def get_or_create_game_session(game_code=None):
        if game_code:
            try:
                game_session = GameSession.objects.get(game_code=game_code)
            except GameSession.DoesNotExist:
                raise exceptions.GameSessionNotFoundException

            if game_session.has_started:
                raise exceptions.GameSessionAlreadyStartedException

            if game_session.player_set.count() >= GameSession.MAXIMUM_PLAYERS:
                raise exceptions.GameSessionFullException
        else:
            game_session = GameSession.objects.create(owner=None)

        return game_session

    @staticmethod
    def join_game_session(game_session, nickname):
        if Player.objects.filter(game_session=game_session, nickname=nickname).exists():
            raise exceptions.NicknameAlreadyInUseException

        player = Player.objects.create(game_session=game_session, nickname=nickname)
        if not game_session.owner:
            game_session.owner = player
            game_session.save()

        game_session.player_set.add(player)

        return player

    @staticmethod
    def start_game_session(player):
        game_session = player.game_session
        if player != game_session.owner:
            raise exceptions.NotOwnerException

        if game_session.has_started:
            raise exceptions.GameSessionAlreadyStartedException

        if game_session.player_set.count() < GameSession.MINIMUM_PLAYERS:
            raise exceptions.MinimumPlayersNotReachedException

        game_session.has_started = True
        game_session.ended_at = timezone.now() + GameSession.DURATION
        game_session.save()

        # Start gathering resources for all players
        village_queryset = Village.objects.filter(player__game_session=game_session)
        village_queryset.update(last_resources_update=timezone.now())

        CoordinateService.set_coordinates(game_session)
        GameSessionConsumerService.send_start_game_session(game_session)
        for player in game_session.player_set.all():
            GameSessionConsumerService.send_fetch_resources(player)
            GameSessionConsumerService.send_fetch_buildings(player)


class VillageService:
    @staticmethod
    def upgrade_building(player, building_name):
        if not player.game_session.has_started:
            raise exceptions.GameSessionNotStartedException

        village = player.village
        village.update_resources()

        building = village.get_building(building_name)
        upgrade_costs = building.get_upgrade_cost()

        for resource in upgrade_costs:
            if village.resources[resource] < upgrade_costs[resource]:
                raise exceptions.InsufficientResourcesException

        village.wood -= upgrade_costs["wood"]
        village.clay -= upgrade_costs["clay"]
        village.iron -= upgrade_costs["iron"]

        building.upgrade()
        village.upgrade_building_level(building_name)
        village.save()

        player.refresh_from_db()
        GameSessionConsumerService.send_fetch_resources(player)
        GameSessionConsumerService.send_fetch_buildings(player)


class CoordinateService:
    MAP_SIZE = 32
    AVAILABLE_TILES = (
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4),
        (0, 5),
        (0, 6),
        (0, 7),
        # TODO: Fill rest when map will be ready
    )

    @staticmethod
    def set_coordinates(game_session):
        left_coordinates = set(CoordinateService.AVAILABLE_TILES)

        for player in game_session.player_set.all():
            village = player.village
            village.x, village.y = random.choice(tuple(left_coordinates))
            left_coordinates.remove((village.x, village.y))
            village.save()
