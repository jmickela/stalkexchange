from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _

class HomePlot(models.Model):
    OPEN_ACCESS = 1
    NEEDS_PERMISSION = 2

    access_choices = (
        (OPEN_ACCESS, _('Open Access')),
        (NEEDS_PERMISSION, _('Needs Permission to access')),
    )

    LITTLE_SUN = 1
    MEDIUM_SUN = 2
    MANY_SUN = 3

    sun_choices = (
        (LITTLE_SUN, _('Mostly Shade')),
        (MEDIUM_SUN, _('Partly Shady')),
        (MANY_SUN, _('Lots of sun'))
    )

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='home_plots')
    size = models.FloatField(_('Plot Size'), help_text=_('Size of the plot in square feet.'))
    access = models.IntegerField(_('Access Information'), choices=access_choices, help_text=_('Is this plot accessible all the time or only at certain times?'))
    exchange_terms = models.TextField(_('Exchange Terms'), help_text=_('What do you want in exchange for this plot?'))
    sun_exposure = models.IntegerField(_('Sun Exposure'), choices=sun_choices)

    address = models.CharField(_('Street Address'), blank=False, max_length=255)
    city = models.CharField(_('City'), default="Richmond", max_length=255)
    zip = models.CharField(_('Zip Code'), max_length=10)
    state = models.CharField(_('State'), max_length=2, default="CA")


