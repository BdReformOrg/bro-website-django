from pathlib import Path
from django.utils.translation import gettext_lazy as _
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from . import apps, models

def _template(*args):
    return Path(apps.BroFrontendConfig.name, 'plugins', *args).as_posix()

@plugin_pool.register_plugin
class NavbarBrand(CMSPluginBase):
    module=_('Navbar')
    model=models.NavbarBrandModel
    render_template=_template('navbar', 'navbar-brand.html')

@plugin_pool.register_plugin
class NavbarSiteNav(CMSPluginBase):
    module=_('Navbar')
    model=models.NavbarSiteNavModel
    render_template=_template('navbar', 'navbar-brand.html')

@plugin_pool.register_plugin
class HeroSectionImage(CMSPluginBase):
    module=_('Section')
    model=models.HeroSectionImageModel
    render_template=_template('sections', 'hero-image.html')

@plugin_pool.register_plugin
class GalleryDescription(CMSPluginBase):
    module=_('Section')
    model=models.GalleryDescriptionModel
    render_template=_template('sections', 'gallery-description.html')
    allow_children=True

@plugin_pool.register_plugin
class ImageDescription(CMSPluginBase):
    module=_('Section')
    model=models.GalleryDescriptionModel
    render_template=_template('sections', 'image-description.html')
    allow_children=True

@plugin_pool.register_plugin
class TitleHighlight(CMSPluginBase):
    module=_('Section')
    render_template=_template('sections', 'title-highlight.html')
    allow_children=True

@plugin_pool.register_plugin
class BoxedImage(CMSPluginBase):
    module=_('Utils')
    model=models.BoxedImageModel
    render_template=_template('utils', 'image-boxed.html')
