from pathlib import Path
from django.utils.translation import gettext_lazy as _
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from . import apps, models

def _template(*args):
    return Path(apps.BroFrontendConfig.name, 'plugins', *args).as_posix()

# Section Navbar

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

# Section Content Sections

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
class OneThirdContent(CMSPluginBase):
    module=_('Section')
    model = models.GalleryDescriptionModel
    render_template=_template('sections', 'one-third-content.html')
    allow_children=True

@plugin_pool.register_plugin
class CallToAction(CMSPluginBase):
    module=_('Section')
    render_template=_template('sections', 'call-to-action.html')
    allow_children=True

@plugin_pool.register_plugin
class AccordionContainer(CMSPluginBase):
    module = _('Section')
    render_template = _template('sections', 'accordion-list.html')
    allow_children = True
    child_classes = ['AccordionItem']

@plugin_pool.register_plugin
class AccordionItem(CMSPluginBase):
    module = _('Section')
    model = models.AccordionItemModel
    render_template = _template('sections', 'accordion-item.html')
    allow_children = True
    require_parent = True
    parent_classes = ['AccordionContainer']

@plugin_pool.register_plugin
class CarouselSlide(CMSPluginBase):
    module = _('Section')
    model = models.BoxedImageModel
    render_template = _template('sections', 'carousel-slide.html')
    allow_children = True
    require_parent = True
    parent_classes = ['CarouselContainer']

@plugin_pool.register_plugin
class CarouselContainer(CMSPluginBase):
    module = _('Section')
    render_template = _template('sections', 'carousel-container.html')
    allow_children = True
    child_classes = ['CarouselSlide']

# Section Footer

@plugin_pool.register_plugin
class Footer(CMSPluginBase):
    module = _('Footer')
    render_template = _template('footer', 'footer-container.html')
    allow_children = True

@plugin_pool.register_plugin
class FooterRow(CMSPluginBase):
    module = _('Footer')
    render_template = _template('footer', 'footer-row.html')
    allow_children = True

@plugin_pool.register_plugin
class FooterNav(CMSPluginBase):
    module = _('Footer')
    render_template = _template('footer', 'footer-nav.html')
    allow_children = True

@plugin_pool.register_plugin
class FooterBrand(CMSPluginBase):
    module = _('Footer')
    model = models.NavbarBrandModel
    render_template = _template('footer', 'footer-brand.html')

# Section Utils

@plugin_pool.register_plugin
class BoxedImage(CMSPluginBase):
    module=_('Utils')
    model=models.BoxedImageModel
    render_template=_template('utils', 'image-boxed.html')
