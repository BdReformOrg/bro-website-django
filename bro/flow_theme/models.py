from django.db import models
from cms.plugin_base import CMSPlugin
from cms.models import PageContent
from filer.fields.image import FilerImageField

class HeroSection1Model(CMSPlugin):
    left_image= FilerImageField(on_delete=models.SET_NULL, related_name='+', null=True, blank=True)
    right_image= FilerImageField(on_delete=models.SET_NULL, related_name='+', null=True, blank=True)
    bottom_left_image= FilerImageField(on_delete=models.SET_NULL, related_name='+', null=True, blank=True)
    bottom_right_image= FilerImageField(on_delete=models.SET_NULL, related_name='+', null=True, blank=True)

class TitledSectionModel(CMSPlugin):
    section_title=models.CharField(max_length=127, default='', blank=True)

class FlowLinkModel(CMSPlugin):
    label = models.CharField(max_length=1023, default=None, null=True, blank=True)
    external_link = models.CharField(max_length=1023, default='', blank=True)
    internal_link = models.ForeignKey(PageContent, on_delete=models.SET_NULL, null=True, blank=True, default=None)

    @property
    def get_label(self):
        if self.label is not None:
            return self.label
        elif self.internal_link is None:
            return self.external_link
        else:
            if self.internal_link.page_title is not None:
                return self.internal_link.page_title
            else:
                return self.internal_link.title

    @property
    def get_link(self):
        if self.internal_link is None:
            return self.external_link
        else:
            return self.internal_link.get_absolute_url()
            
