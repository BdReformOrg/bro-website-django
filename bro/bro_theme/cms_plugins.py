from pathlib import Path
from django.utils.translation import gettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import apps, models

SECTION_MODULE = _('Bro: Sections')
UTILS_MODULE = _('Bro: Utils')
CONTENT_MODULE = _('Bro: Content')

def _template(*args):
    return Path(apps.BroThemeConfig.label, 'plugins', *args).as_posix()

class BroHeroSection(CMSPluginBase):
    module=SECTION_MODULE
    model=models.SectionModel
    render_template=_template('sections', 'hero-section.html')
    allow_children=True

class BroSection(CMSPluginBase):
    module=SECTION_MODULE
    model=models.SectionModel
    render_template=_template('sections', 'container-section.html')
    allow_children=True

class BroTwoColumnSection(CMSPluginBase):
    module=SECTION_MODULE
    model=models.SectionModel
    render_template=_template('sections', 'two-column-section.html')
    allow_children=True

class BroTwoThirdColumnSection(CMSPluginBase):
    module=SECTION_MODULE
    model=models.SectionModel
    render_template=_template('sections', 'two-third-column-section.html')
    allow_children=True

class BroPluginGroup(CMSPluginBase):
    module=UTILS_MODULE
    render_template=_template('utils', 'plugin-group.html')
    allow_children=True

class BroContentRow(CMSPluginBase):
    module=UTILS_MODULE
    render_template=_template('utils', 'content-row.html')
    allow_children=True

class BroLinkButton(CMSPluginBase):
    module=CONTENT_MODULE
    model=models.ButtonModel
    render_template=_template('content', 'link-button.html')
    allow_children=True
    text_enabled=True

class BroImage(CMSPluginBase):
    module=CONTENT_MODULE
    model=models.ImageModel
    render_template=_template('content', 'image.html')
    allow_children=False
    text_enabled=True


class BroFooterSubscription(CMSPluginBase):
    module=SECTION_MODULE
    render_template=_template('footer', 'footer-subscription.html')
    allow_children=True

class BroFooterNav(CMSPluginBase):
    module=SECTION_MODULE
    render_template=_template('footer', 'footer-nav.html')
    allow_children=True

class BroFooterRow(CMSPluginBase):
    module=SECTION_MODULE
    model=models.SectionModel
    render_template=_template('footer', 'footer-row.html')
    allow_children=True

class BroFooterContainer(CMSPluginBase):
    module=SECTION_MODULE
    model=models.SectionModel
    render_template=_template('footer', 'footer-container.html')
    allow_children=True

class BroNavbar(CMSPluginBase):
    module=SECTION_MODULE
    model=models.SectionModel
    render_template=_template('navbar', 'navbar-container.html')
    allow_children=True

class BroNavbarBrand(CMSPluginBase):
    module=SECTION_MODULE
    render_template=_template('navbar', 'navbar-brand.html')
    allow_children=True

class BroNavbarMenu(CMSPluginBase):
    module=SECTION_MODULE
    model=models.MenuModel
    render_template=_template('navbar', 'navbar-menu.html')
    allow_children=True

plugin_pool.register_plugin(BroHeroSection)
plugin_pool.register_plugin(BroSection)
plugin_pool.register_plugin(BroTwoColumnSection)
plugin_pool.register_plugin(BroTwoThirdColumnSection)

plugin_pool.register_plugin(BroPluginGroup)
plugin_pool.register_plugin(BroContentRow)

plugin_pool.register_plugin(BroLinkButton)
plugin_pool.register_plugin(BroImage)

plugin_pool.register_plugin(BroFooterContainer)
plugin_pool.register_plugin(BroFooterRow)
plugin_pool.register_plugin(BroFooterNav)
plugin_pool.register_plugin(BroFooterSubscription)

plugin_pool.register_plugin(BroNavbar)
plugin_pool.register_plugin(BroNavbarBrand)
plugin_pool.register_plugin(BroNavbarMenu)

class BroGrid(CMSPluginBase):
    module=SECTION_MODULE
    render_template=_template('grid', 'grid-container.html')
    allow_children=True

class BroGridItem(CMSPluginBase):
    module=SECTION_MODULE
    render_template=_template('grid', 'grid-item.html')
    allow_children=True


plugin_pool.register_plugin(BroGrid)
plugin_pool.register_plugin(BroGridItem)
