import typing
from typing import Any

from django import template
from django.db.models import F

if typing.TYPE_CHECKING:
    from django.db.models.query import ValuesQuerySet

from menu.models import Item

register = template.Library()


def tree_menu(
    items: 'ValuesQuerySet[Item, dict[str, Any]]',
    target: str | None,
    parent: str | None = None
) -> dict:
    children = [item for item in items if item['parent_slug'] == parent]

    for item in children:
        if target is None:
            item |= {'items': [], 'show': True}
            continue

        target = target if item['slug'] != target else None
        item |= tree_menu(items, target, item['slug'])

    show = any(item['show'] for item in children) or target is None
    children = [item | {'show': show} for item in children]

    return {'items': children, 'show': show}


@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_slug):
    target_item = context.request.GET.get(menu_slug)

    items = Item.objects.filter(
        menu__slug=menu_slug
    ).values(
        'name',
        'slug',
        parent_slug=F('parent__slug'),
        menu_slug=F('menu__slug')
    )

    return tree_menu(items, target_item)
