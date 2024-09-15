from random import choices

from django.db import models
from cms.models import CMSPlugin, PageContent
from filer.fields.image import FilerImageField

class NavbarBrandModel(CMSPlugin):
    image = FilerImageField(on_delete=models.CASCADE, blank=True, null=True)
    label = models.CharField(max_length=63, default='', blank=True, null=True)

class NavbarSiteNavModel(CMSPlugin):
    start = models.IntegerField(default=0)
    end = models.IntegerField(default=100)
    extra_active = models.IntegerField(default=100)
    extra_inactive = models.IntegerField(default=0)
                               
class HeroSectionImageModel(CMSPlugin):
    image = FilerImageField(on_delete=models.CASCADE, blank=True, null=True)

class BoxedImageModel(CMSPlugin):
    image = image = FilerImageField(on_delete=models.CASCADE)

class GalleryDescriptionModel(CMSPlugin):
    gallery_on_left = models.BooleanField(default=False, blank=True)

class AccordionItemModel(CMSPlugin):
    title = models.CharField(default='', max_length=255)

LINK_TYPES = [
    ('', 'Default'),
    ('btn', 'Button'),
    ('link', 'Link')
]

LINK_VARIANTS = [
    ('', 'Default'),
    ('btn-primary', 'Primary Button'),
    ('btn-secondary', 'Secondary Button'),
    ('btn-accent', 'Accent Button'),
    ('btn-info', 'Info Button'),
    ('btn-success', 'Success Button'),
    ('btn-warning', 'Warning Button'),
    ('btn-error', 'Error Button'),
    ('btn-link', 'Link Button'),
]

LINK_SIZES = [
    ('', 'Default'),
    ('btn-sm', 'Small'),
    ('btn-lg', 'Large'),
]

class LinkModel(CMSPlugin):
    type = models.CharField(max_length=7, choices=LINK_TYPES, default='', blank=True)
    variant = models.CharField(max_length=15, choices=LINK_VARIANTS, default='', blank=True)
    size = models.CharField(max_length=7, choices=LINK_SIZES, default='', blank=True)
    label = models.CharField(max_length=127, blank='')
    link = models.ForeignKey(PageContent, on_delete=models.SET_NULL, null=True, blank=True)