from django import template


import numpy as np
import plotly
import plotly.graph_objects as go
import plotly.express as px

from ratings.templatetags.ratings_tag import colify_div

register = template.Library()


@register.simple_tag
def total_post():
  return "I'm working yes 5 posts zogenaamd"


@register.simple_tag
def get_plotly2():
  layout = {"title": {"text": "Aspects Rated", 'xref': "paper"},
            "font": dict(family='Montserrat', size=16, color='white'),
            "plot_bgcolor": "rgb(30,30,30)",
            "paper_bgcolor": "hsl(0, 0, 18)",
            "yaxis": dict(showline=True, linecolor='white', showgrid=False, title="Mean Rating"),
            'xaxis': dict(showline=True, linecolor='white', showgrid=False, title="Rating")
            }
  marker = {"line": {"color": "#25232C", "width": 0.2},
            "color": "#bb9d52"}

  labels = ['Internet', 'Toilet', 'Shower', 'Noise']
  values = [4500, 2500, 1053, 500]

  fig = go.Figure(data=[go.Pie(labels=labels, values=values)], layout=layout)

  div = plotly.offline.plot(fig,
                            include_plotlyjs=False, output_type='div')

  div = colify_div(div)
  layout['title']['text'] = 'Weekly Mean Rating'
  fig = go.Figure(layout=layout)
  fig.add_trace(go.Scatter(x=list(range(1, 53)), y=np.random.normal(6.5, 2, 52),
                           mode='lines',
                           name='Shower',
                           ))

  fig.add_trace(go.Scatter(x=list(range(1, 53)), y=np.random.normal(6.5, 2, 52),
                           mode='lines',
                           name='Internet',
                           ))

  fig.add_trace(go.Scatter(x=list(range(1, 53)), y=np.random.normal(6.5, 2, 52),
                           mode='lines',
                           name='Toilet',
                           ))

  div += colify_div(plotly.offline.plot(fig,
                                        include_plotlyjs=False, output_type='div'))

  layout['title']['text'] = 'Paupergram Ratings: July'
  layout['yaxis']['title'] = 'Count'
  marker = {"line": {"color": "#25232C", "width": 0.2},
            }
  fig = go.Figure(layout=layout)
  fig.add_trace(go.Histogram(x=np.random.randint(
      low=1, high=11, size=100), name='Internet', marker=marker))
  fig.add_trace(go.Histogram(x=np.random.randint(
      low=1, high=11, size=100), name='Shower', marker=marker))
  fig.add_trace(go.Histogram(x=np.random.randint(
      low=1, high=11, size=100), name='Noise', marker=marker))
  fig.update_layout(barmode='overlay',     xaxis=dict(
      tickmode='linear',
      tick0=0,
      dtick=1
  ))

  fig.update_traces(opacity=0.75)

  div += colify_div(plotly.offline.plot(fig,
                                        include_plotlyjs=False, output_type='div'))

  animals = ['Shower', 'Internet', 'Toilet', 'Noise']
  layout['title']['text'] = 'Ratings  below 6: Last 7 days'
  layout['yaxis']['title'] = 'Count'
  fig = go.Figure([go.Bar(x=animals, y=[1, 13, 3, 6])])
  fig.update_layout(layout)

  div += colify_div(plotly.offline.plot(fig,
                                        include_plotlyjs=False, output_type='div'))

  return div
