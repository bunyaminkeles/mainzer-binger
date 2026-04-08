import datetime
from django import template
from businesses.models import LocalBusiness

register = template.Library()


@register.inclusion_tag('businesses/includes/_expert_list.html')
def get_local_experts(category_slug, limit=2):
    """
    Verilen kategori slug'ına sahip, aktif işletmeleri getirir.
    Kullanım: {% load business_tags %}
              {% get_local_experts "hukuk-danismanlik" limit=3 %}
    """
    today = datetime.date.today()
    isletmeler = (
        LocalBusiness.objects
        .filter(
            is_published=True,
            end_date__gte=today,
            category__slug=category_slug,
        )
        .select_related('city', 'category')
        .order_by('name')[:limit]
    )
    return {'isletmeler': isletmeler}
