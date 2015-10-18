from django.utils.translation import ugettext as _

import autocomplete_light.shortcuts as al

from .models import GardenItem, ProduceType

# This will generate a PersonAutocomplete class
al.register(ProduceType,
    # Just like in ModelAdmin.search_fields
    search_fields=['title'],
    attrs={
        # This will set the input placeholder attribute:
        'placeholder': _('Enter Produce'),
        # This will set the yourlabs.Autocomplete.minimumCharacters
        # options, the naming conversion is handled by jQuery
        'data-autocomplete-minimum-characters': 1,
        'template': 'fuck',
        'autocomplete_template': 'you',
    },
    # This will set the data-widget-maximum-values attribute on the
    # widget container element, and will be set to
    # yourlabs.Widget.maximumValues (jQuery handles the naming
    # conversion).
    widget_attrs={
        'data-widget-maximum-values': 4,
        # Enable modern-style widget !
        'class': 'modern-style',
        'template': 'fuck',
        'autocomplete_template': 'you',
    },
    choice_template='Fuck',
)