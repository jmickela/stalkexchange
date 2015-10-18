from django.db import models
from django.utils.translation import ugettext as _
from django.conf import settings

from produce.models import ProduceType

class WishlistItem(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="wishlist_items")
    produce = models.ForeignKey(ProduceType)
