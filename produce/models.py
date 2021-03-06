from django.db import models
from django.utils.translation import ugettext as _
from django.conf import settings

class ProduceType(models.Model):
    title = models.CharField(_('Type'), max_length=255)
    description = models.TextField(_('Description'))
    image = models.ImageField(_('Image'), blank=True)

    def __unicode__(self):
        return self.title

class GardenItem(models.Model):
    QUANTITY_LITTLE = 0
    QUANTITY_LOT = 10

    quantity_choices = (
        (QUANTITY_LITTLE, _("A little")),
        (QUANTITY_LOT, _("A lot")),
    )

    SIZE_BIG = 0
    SIZE_MEDIUM = 1
    SIZE_SMALL = 2

    size_choices = (
        (SIZE_BIG, _('Big')),
        (SIZE_MEDIUM, _('Medium')),
        (SIZE_SMALL, _('Small'))
    )

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="garden_items")
    produce = models.ForeignKey(ProduceType)
    quantity = models.IntegerField(_('Quantity'), help_text=_('How many do you have?'), choices=quantity_choices)
    is_organic = models.BooleanField(_('Is Organic?'), default=False)
    size = models.IntegerField(_('Size'), choices=size_choices, help_text=_('How big is this item?'))
    description = models.TextField(_('Description'), help_text=_('Extra information...'), blank=True)
    image = models.ImageField(_('Image'), blank=True)