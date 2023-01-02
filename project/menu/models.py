from django.db import models
from django.utils.translation import gettext_lazy as _


class Menu(models.Model):
    name = models.CharField(
        verbose_name=_('Имя'),
        max_length=100,
        unique=True
    )
    slug = models.SlugField(
        verbose_name=_('Слаг'),
        unique=True
    )

    class Meta:
        ordering = ('name', )
        verbose_name = _('Меню')
        verbose_name_plural = _('Меню')

    def __str__(self):
        return self.name
