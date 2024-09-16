from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig

class FlowThemeConfig(AppConfig):
    name='bro.flow_theme'
    label='flow_theme'
    verbose_name=_('Flow Theme Blocks')
