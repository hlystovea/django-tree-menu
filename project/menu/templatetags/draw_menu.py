from django import template
from django.shortcuts import get_object_or_404

from menu.models import Menu

register = template.Library()


def get_tree_menu(menu_slug: str, active_item: str | None) -> dict:
    menu = get_object_or_404(Menu, slug=menu_slug)
    return {'items': menu.items}


@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_slug):
    active_item = context.request.GET.get(menu_slug)
    return get_tree_menu(menu_slug, active_item)
