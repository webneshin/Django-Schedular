from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel


class User(AbstractUser, BaseModel):
    email = models.EmailField(_("email address"))
