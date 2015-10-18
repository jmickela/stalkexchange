import autocomplete_light

from .models import WishlistItem

class WishlistForm(autocomplete_light.ModelForm):
    class Meta:
        model = WishlistItem
        exclude = ['owner',]
