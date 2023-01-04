from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from menu.models import Item, Menu


class ItemInline(admin.TabularInline):
    model = Item
    show_change_link = True
    verbose_name_plural = _('Вложенные пункты меню')
    prepopulated_fields = {'slug': ('name', )}
    readonly_fields = ('menu', 'parent')


class MixinAdmin(admin.ModelAdmin):
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name', )}
    empty_value_display = _('-пусто-')
    inlines = (ItemInline, )


@admin.register(Item)
class ItemAdmin(MixinAdmin):
    list_display = ('id', 'name', 'slug', 'view_menu', 'view_parent')
    list_display_links = None
    list_filter = ('menu', )
    list_select_related = ('menu', 'parent')

    @admin.display(description=_('Меню'))
    def view_menu(self, obj):
        if obj.menu:
            url = (
                reverse(
                    'admin:menu_menu_change',
                    args=(obj.menu.id, )
                )
            )
            return format_html('<a href="{}">{}</a>', url, obj.menu)
        return ''

    @admin.display(description=_('Родительский пункт меню'))
    def view_parent(self, obj):
        if obj.parent:
            url = (
                reverse(
                    'admin:menu_item_change',
                    args=(obj.parent.id, )
                )
            )
            return format_html('<a href="{}">{}</a>', url, obj.parent)
        return ''

    def save_formset(self, request, form, formset, change) -> None:
        instances = formset.save(commit=False)
        for instance in instances:
            instance.menu = form.cleaned_data['menu']
            instance.save()


@admin.register(Menu)
class CabinetAdmin(MixinAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
