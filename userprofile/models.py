from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')
    about = models.TextField(_('About'))
    zip = models.CharField(_('Zip Code'), help_text=_('Your zip code is used to keep search results local'), max_length=5, blank=True)
    photo = models.ImageField(_('Photo'), blank=True)