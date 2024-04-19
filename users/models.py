from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from users.managers import UserManager


class User(AbstractUser):
    first_name = None
    last_name = None

    email = models.EmailField(_("email address"), unique=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    @property
    def active_player(self):
        player = self.players.prefetch_related("game_session").last()
        if player is None or player.game_session.has_ended:
            return None

        return player
