from django import template

register = template.Library()


from ..models import LivingAspects


import numpy as np
import plotly
import plotly.graph_objects as go
import plotly.express as px


def colify_div(div):
  # Making bootstrap compatible div
  div = '<div class="col-sm-11  col-xs-11 col-md-6">' + div
  div += "</div>"
  return div


def plot_histogram(x, my_title):
  layout = {"title": {"text": "Paupergram of " + my_title, 'xref': "paper"},
            "font": dict(family='Montserrat', size=16, color='white'),
            "plot_bgcolor": "rgb(30,30,30)",
            "paper_bgcolor": "hsl(0, 0, 18)",
            "yaxis": dict(showline=True, linecolor='white', showgrid=False, title="Count"),
            'xaxis': dict(showline=True, linecolor='white', showgrid=False, title="Rating")
            }
  marker = {"line": {"color": "#25232C", "width": 0.2},
            "color": "#bb9d52"}

  fig = go.Figure(
      data=[go.Histogram(x=x, marker=marker)], layout=layout)

  fig.update_layout(
      shapes=[
          # Line Vertical
          go.layout.Shape(
              type="line",
              x0=np.mean(x),
              y0=0,
              x1=np.mean(x),
              y1=int(np.bincount(x).max() * 1.1),
              line=dict(
                  color="red",
                  width=4
              )
          )],
      xaxis=dict(
          tickmode='linear',
          tick0=0,
          dtick=1
      )
  )

  div = plotly.offline.plot(fig,
                            include_plotlyjs=False, output_type='div')

  div = colify_div(div)

  return div


def plotly_lineplot(x, y, title, ylabel, xlabel, linecolor):
  layout = {"title": {"text": title, 'xref': "paper"},
            "font": dict(family='Montserrat', size=16, color='white'),
            "plot_bgcolor": "rgb(30,30,30)",
            "paper_bgcolor": "hsl(0, 0, 18)",
            "yaxis": dict(showline=True, linecolor='white', showgrid=False, title=ylabel),
            'xaxis': dict(showline=True, linecolor='white', showgrid=False, title=xlabel)
            }

  fig = go.Figure(layout=layout)
  fig.add_trace(go.Scatter(x=x, y=y,
                           mode='lines',
                           name='lines',
                           line=dict(color=linecolor)))

  div = plotly.offline.plot(fig,
                            include_plotlyjs=False, output_type='div')

  div = colify_div(div)
  return div


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
  x = np.random.randint(low=1, high=11, size=100)
  div = plot_histogram(x, my_title)

  N = 52
  random_x = list(range(1, N + 1))
  random_y0 = np.random.randint(low=1, high=10, size=N)

  div += plotly_lineplot(random_x, random_y0, title="Paupermean's per week for " +
                         my_title, ylabel='Mean Rating', xlabel='Week', linecolor='red')

  return div
