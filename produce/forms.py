from django import forms
import autocomplete_light

from .models import GardenItem

class AddProduceForm(autocomplete_light.ModelForm):
    class Meta:
        model = GardenItem
        exclude = ['owner',]

class ProduceSearchForm(autocomplete_light.ModelForm):
    zip = forms.CharField(required=False, max_length=5)

    class Meta:
        model = GardenItem
        fields = ['produce',]