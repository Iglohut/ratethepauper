from django import template

register = template.Library()


from ..models import LivingAspects


@register.simple_tag
def total_aspects(count):
    # return len(LivingAspects.objects.all())
    return "<div>count / 2</div>"


@register.simple_tag
def you_clicked(name):
    print(name)
    new_name = LivingAspects.objects.get(pk=int(name))
    return new_name.description
