from pathlib import Path
from django.utils.translation import gettext_lazy as _
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from . import apps, models

SECTION_MODULE = _('Flow: Sections')

def _template(*args):
    return Path(apps.FlowThemeConfig.label, 'plugins', *args).as_posix()


class FlowHeroSection1(CMSPluginBase):
    module=SECTION_MODULE
    name=_('Flow: Hero Section 1')
    model = models.HeroSection1Model
    render_template=_template('section', 'hero-section-1.html')
    allow_children=True
    require_parent=False

class FlowIconCarousel1(CMSPluginBase):
    module=SECTION_MODULE
    name=_('Flow: Icon Carousel 1')
    render_template=_template('section', 'icon-carousel-1.html')
    allow_children=True
    child_classes=['ImagePlugin']
    require_parent=False

class BlogSection1(CMSPluginBase):
    module=SECTION_MODULE
    name=_('Flow: Blog Section 1')
    render_template=_template('section', 'blog-section-1.html')
    allow_children=True
    require_parent=False

class BlogSection2(CMSPluginBase):
    module=SECTION_MODULE
    name=_('Flow: Blog Section 2')
    render_template=_template('section', 'blog-section-2.html')
    allow_children=True
    require_parent=False

class AboutSection1(CMSPluginBase):
    module=SECTION_MODULE
    name=_('Flow: About Section 1')
    model=models.TitledSectionModel
    render_template=_template('section', 'about-section-1.html')
    allow_children=True
    require_parent=False
    child_classes=['TwoThirdBlock', 'OneThirdBlock']

class AboutSection2(CMSPluginBase):
    module=SECTION_MODULE
    name=_('Flow: About Section 2')
    model=models.TitledSectionModel
    render_template=_template('section', 'about-section-2.html')
    allow_children=True
    require_parent=False

class TestimonialSection1(CMSPluginBase):
    module=SECTION_MODULE
    name=_('Flow: Testimonial Section 1')
    render_template=_template('section', 'testimonial-section-1.html')
    allow_children=True
    require_parent=False

class CallToActionSection1(CMSPluginBase):
    module=SECTION_MODULE
    name=_('Flow: Call to Action Section 1')
    render_template=_template('section', 'call-to-action-section-1.html')
    allow_children=True
    require_parent=False

class TeamsSection1(CMSPluginBase):
    module=SECTION_MODULE
    name=_('Flow: Teams Section 1')
    render_template=_template('section', 'teams-section-1.html')
    allow_children=True
    require_parent=False

plugin_pool.register_plugin(FlowHeroSection1)
plugin_pool.register_plugin(FlowIconCarousel1)
plugin_pool.register_plugin(AboutSection1)
