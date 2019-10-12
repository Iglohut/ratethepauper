from django import template

register = template.Library()


from ..models import LivingAspects


import numpy as np
import plotly


@register.simple_tag
def total_aspects(count):
    # return len(LivingAspects.objects.all())
    return "<div>count / 2</div>"


@register.simple_tag
def you_clicked(name):
    new_name = LivingAspects.objects.get(pk=int(name))
    return new_name.description


@register.simple_tag
def get_plotly(my_title):
    fig = {
        "data": [{"type": "bar",
                  "x": np.random.randint(low=-10, high=10, size=100),
                  "y": np.random.randint(low=-10, high=10, size=100)}],
        "layout": {"title": {"text": "Paupergram of " + my_title}}
    }

    div = plotly.offline.plot(fig,
                              include_plotlyjs=False, output_type='div')
    return div
