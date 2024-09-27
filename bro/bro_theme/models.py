from django.utils.translation import gettext_lazy as _
from django.db import models
from cms.plugin_base import CMSPlugin
from cms.models import PageContent

from filer.fields.image import FilerImageField

BACKGROUND_COLORS = [
    ('bg-transparent', _('Transparent')),
    ('bg-base-100', _('Base-100')),
    ('bg-base-200', _('Base-200')),
    ('bg-base-300', _('Base-300')),
    ('bg-base-content', _('Base Content')),
    ('bg-primary', _('Primary')),
    ('bg-primary-content', _('Primary Content')),
    ('bg-secondary', _('Secondary')),
    ('bg-secondary-content', _('Secondary Content')),
    ('bg-accent', _('Accent')),
    ('bg-accent-content', _('Accent Content')),
    ('bg-neutral', _('Neutral')),
    ('bg-neutral-content', _('Neutral Content')),
    ('bg-info', _('Info')),
    ('bg-info-content', _('Info Content')),
    ('bg-success', _('Success')),
    ('bg-success-content', _('Success Content')),
    ('bg-warning', _('Warning')),
    ('bg-warning-content', _('Warning Content')),
    ('bg-error', _('Error')),
    ('bg-error-content', _('Error Content')),
]

FOREGROUND_COLORS = [
    ('text-base-100', _('Base-100')),
    ('text-base-200', _('Base-200')),
    ('text-base-300', _('Base-300')),
    ('text-base-content', _('Base Content')),
    ('text-primary', _('Primary')),
    ('text-primary-content', _('Primary Content')),
    ('text-secondary', _('Secondary')),
    ('text-secondary-content', _('Secondary Content')),
    ('text-accent', _('Accent')),
    ('text-accent-content', _('Accent Content')),
    ('text-neutral', _('Neutral')),
    ('text-neutral-content', _('Neutral Content')),
    ('text-info', _('Info')),
    ('text-info-content', _('Info Content')),
    ('text-success', _('Success')),
    ('text-success-content', _('Success Content')),
    ('text-warning', _('Warning')),
    ('text-warning-content', _('Warning Content')),
    ('text-error', _('Error')),
    ('text-error-content', _('Error Content')),
]

BUTTON_TYPES = [
    ('link', _('Plain Link')),
    ('btn', _('Button')),
]

BUTTON_COLORS = [
    ('btn-ghost', _('Transparent')),
    ('btn-primary', _('Primary')),
    ('btn-secondary', _('Secondary')),
    ('btn-accent', _('Accent')),
    ('btn-neutral', _('Neutral')),
    ('btn-info', _('Info')),
    ('btn-success', _('Success')),
    ('btn-warning', _('Warning')),
    ('btn-error', _('Error')),
]

BUTTON_SIZES = [
    ('btn-md', _('Standard')),
    ('btn-lg', _('Large')),
    ('btn-sm', _('Small')),
    ('btn-xs', _('Extra Small')),
]

BUTTON_VARIANTS = [
    ('btn-wide', _('Wide')),
    ('btn-block', _('Block')),
    ('btn-circle', _('Circle')),
    ('btn-square', _('Square')),
]

OBJECT_SCALE_TYPES = [
    ('object-contain', _('Contain')),
    ('object-cover', _('Cover')),
    ('object-fill', _('Fill')),
    ('object-scale-down', _('Scale Down')),
]

class ColorMixin(models.Model):
    class Meta:
        abstract=True

    background_color = models.CharField(max_length=31, choices=BACKGROUND_COLORS, default=None, null=True, blank=True)
    foreground_color = models.CharField(max_length=31, choices=FOREGROUND_COLORS, default=None, null=True, blank=True)

class SectionModel(CMSPlugin, ColorMixin):
    pass

class ButtonModel(CMSPlugin):
    label = models.CharField(max_length=127, default=None, null=True, blank=True)
    external = models.URLField(max_length=2047, default=None, null=True, blank=True)
    internal = models.ForeignKey(PageContent, related_name='+', on_delete=models.SET_NULL, default=None, null=True, blank=True)
    type = models.CharField(max_length=15, choices=BUTTON_TYPES, default=None, null=True, blank=True)
    color = models.CharField(max_length=15, choices=BUTTON_COLORS, default=None, null=True, blank=True)
    size = models.CharField(max_length=15, choices=BUTTON_SIZES, default=None, null=True, blank=True)
    variant = models.CharField(max_length=15, choices=BUTTON_VARIANTS, default=None, null=True, blank=True)
    glass_design = models.BooleanField(default=False, blank=True)
    outline_only = models.BooleanField(default=False, blank=True)
    use_child_plugins = models.BooleanField(default=False, blank=True)

    @property
    def display_name(self):
        if self.label not in [None, '']:
            return self.label
        elif self.internal is not None and self.internal.page_title not in [None, '']:
            return self.internal.page_title
        elif self.internal is not None:
            return self.internal.title
        elif self.external not in [None, '']:
            return self.external
        else:
            return '     '

    @property
    def linked_url(self):
        if self.internal is not None:
            return self.internal.get_absolute_url()
        elif self.external not in [None, '']:
            return self.external
        else:
            return '#'

    @property
    def combined_attribs(self):
        base = f'{self.type} {self.color} {self.size} {self.variant}'
        base += ' glass' if self.glass_design is True else ''
        base += ' btn-outline' if self.outline_only is True else ''
        return base.strip()

class ImageModel(CMSPlugin):
    image = FilerImageField(on_delete=models.SET_NULL, related_name='+', null=True, blank=True, default=None)
    scale_type = models.CharField(max_length=31, choices=OBJECT_SCALE_TYPES, default=None, null=True, blank=True)
    width = models.CharField(max_length=15, default=None, null=True, blank=True)
    height = models.CharField(max_length=15, default=None, null=True, blank=True)
    alt_text = models.CharField(max_length=255, default=None, null=True, blank=True)

    @property
    def combined_classes(self):
        return f'{self.scale_type}'.strip() if self.scale_type not in [None, ''] else ''

    @property
    def get_size(self):
        style = f'width:{self.width};' if self.width not in [None, ''] else ''
        style += f'height:{self.height};' if self.height not in [None, ''] else ''
        return style.strip()

    @property
    def get_alt(self):
        if self.image is None:
            return 'blank'
        if self.alt_text is not None:
            return self.alt_text
        else:
            return self.image.name

class MenuModel(CMSPlugin):
    start_level = models.IntegerField(default=0, blank=True)
    end_level = models.IntegerField(default=100, blank=True)
    extra_inactive = models.IntegerField(default=2, blank=True)
    extra_active = models.IntegerField(default=2, blank=True)
