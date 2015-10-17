from django.db import models
from django.utils.translation import ugettext as _

class ProduceType(models.Model):
    title = models.CharField(_('Type'), max_length=255)
    description = models.TextField(_('Description'))

class GardenItem(models.Model):
    QUANTITY_LITTLE = 0
    QUANTITY_LOT = 10

    quantity_choices = (
        (QUANTITY_LITTLE, _("A little")),
        (QUANTITY_LOT, _("A lot")),
    )



    produce = models.ForeignKey(ProduceType)
    quantity = models.IntegerField(_('Quantity'), help_text=_('How many do you have?'), choices=quantity_choices)
    is_organic
    size
    description