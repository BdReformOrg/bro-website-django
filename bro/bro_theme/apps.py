from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class BroThemeConfig(AppConfig):
    name='bro.bro_theme'
    label='bro_theme'
    verbose_name=_('Bro Theme Blocks')
