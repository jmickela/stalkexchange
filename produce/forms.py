from django import forms
from django.utils.translation import ugettext as _

import autocomplete_light

from .models import GardenItem

class AddProduceForm(autocomplete_light.ModelForm):
    class Meta:
        model = GardenItem
        exclude = ['owner',]

class ProduceSearchForm(autocomplete_light.ModelForm):
    choices = (
        ('gardens', _('Gardens')),
        ('wishlists', _('Wishlists')),
    )

    zip = forms.CharField(required=False, max_length=5, label=_('Zip Code'))
    type = forms.Select(choices=choices)
    class Meta:
        model = GardenItem
        fields = ['produce',]