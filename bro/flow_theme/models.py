from django.db import models
from cms.plugin_base import CMSPlugin
from filer.fields.image import FilerImageField

class HeroSection1Model(CMSPlugin):
    left_image= FilerImageField(on_delete=models.SET_NULL, related_name='+', null=True, blank=True)
    right_image= FilerImageField(on_delete=models.SET_NULL, related_name='+', null=True, blank=True)
    bottom_left_image= FilerImageField(on_delete=models.SET_NULL, related_name='+', null=True, blank=True)
    bottom_right_image= FilerImageField(on_delete=models.SET_NULL, related_name='+', null=True, blank=True)

class TitledSectionModel(CMSPlugin):
    section_title=models.CharField(max_length=127, default='', blank=True)
