from django.db import models
from cms.models import CMSPlugin
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
    headline = models.CharField(max_length=255, default='', blank=True, null=True)
    summary = models.CharField(max_length=511, default='', blank=True, null=True)

class BoxedImageModel(CMSPlugin):
    image = image = FilerImageField(on_delete=models.CASCADE)

class GalleryDescriptionModel(CMSPlugin):
    gallery_on_left = models.BooleanField(default=False, blank=True)
