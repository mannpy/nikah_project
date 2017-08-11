from django import template
from apps.main.models import Category

register = template.Library()


@register.inclusion_tag('main/category.html')
def get_category_list(cat=None):
    return {'cats': Category.objects.order_by('name'), 'act_cat': cat}
