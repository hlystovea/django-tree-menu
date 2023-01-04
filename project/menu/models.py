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


class Item(models.Model):
    name = models.CharField(
        verbose_name=_('Имя'),
        max_length=100
    )
    slug = models.SlugField(
        verbose_name=_('Слаг'),
        unique=True
    )
    menu = models.ForeignKey(
        Menu,
        verbose_name=_('Меню'),
        related_name='items',
        on_delete=models.CASCADE
    )
    parent = models.ForeignKey(
        'menu.Item',
        verbose_name=_('Родительский пункт меню'),
        related_name='items',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ('name', )
        verbose_name = _('Пункт меню')
        verbose_name_plural = _('Пункты меню')
        constraints = [
            models.UniqueConstraint(
                fields=('slug', 'menu'),
                name='slug_menu_uniquetogether'
            )
        ]

    def __str__(self):
        return f'{self.menu}: {self.name}'
