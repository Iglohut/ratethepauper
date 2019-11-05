from django import template

register = template.Library()


from ..models import LivingAspects, AspectRatings
import time
from django_pandas.io import read_frame
import datetime
import copy

import numpy as np
import plotly
import plotly.graph_objects as go
import plotly.express as px


def colify_div(div, size='half', zoom="100%"):
  # Making bootstrap compatible div
  if size == 'half':
    div = '<div class="col-sm-12  col-xs-12 col-md-6">' + div
    div += "</div>"
  else:
    div = '<div class="col-sm-12  col-xs-12 col-md-12" style="zoom:' + zoom + '">' + div
    div += "</div>"

  return div


def plot_histogram(x, my_title):
  layout = {"title": {"text": "Paupergram of " + my_title, 'xref': "container"},
            "font": dict(family='Montserrat', size=16, color='white'),
            "plot_bgcolor": "rgb(30,30,30)",
            "paper_bgcolor": "hsl(0, 0, 18)",
            "yaxis": dict(showline=True, linecolor='white', showgrid=False, title="Count"),
            'xaxis': dict(showline=True, linecolor='white', showgrid=False, title="Rating", dtick=1, tickmode='linear', tick0=0),
            'shapes': [
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
      )]
  }
  marker = {"line": {"color": "#25232C", "width": 0.2},
            "color": "#bb9d52"}

  data = [go.Histogram(x=x, marker=marker)]
  fig = dict(data=data, layout=layout)

  div = plotly.offline.plot(fig,
                            include_plotlyjs=False, output_type='div', validate=False)
  div = colify_div(div)

  return div


def plotly_lineplot(x, y, title, ylabel, xlabel, linecolor):
  layout = {"title": {"text": title, 'xref': "container"},
            "font": dict(family='Montserrat', size=16, color='white'),
            "plot_bgcolor": "rgb(30,30,30)",
            "paper_bgcolor": "hsl(0, 0, 18)",
            "yaxis": dict(showline=True, linecolor='white', showgrid=False, title=ylabel),
            'xaxis': dict(showline=True, linecolor='white', showgrid=False, title=xlabel)
            }

  data = [go.Scatter(x=x, y=y,
                     mode='lines+markers',
                     name='lines',
                     line=dict(color=linecolor))]

  fig = dict(data=data, layout=layout)

  div = plotly.offline.plot(fig,
                            include_plotlyjs=False, output_type='div', validate=False)

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


def plot_meanbar(mean):
  if mean < 5.6:
    title_judge = 'Pauper!'
  else:
    title_judge = 'Voldoende'

  layout = {"title": {"text": '', 'xref': "container"},
            "font": dict(family='Montserrat', size=16, color='white'),
            "plot_bgcolor": "rgb(30,30,30)",
            "paper_bgcolor": "hsl(0, 0, 18)",
            "yaxis": dict(showline=True, linecolor='white', showgrid=False, title=''),
            'xaxis': dict(showline=True, linecolor='white', showgrid=False, title='')
            }

  data = [go.Indicator(
      mode="gauge+number",
      value=mean,
      domain={'x': [0, 1], 'y': [0, 1]},
      title={'text': "Mean Rating: " + title_judge},
      gauge={'axis': {'range': [0, 10], 'tickwidth': 2},
             'bar': {'color': "#282828"},
             'borderwidth': 2,
             'bordercolor': "hsl(0, 0, 18)",
             'steps': [
          {'range': [0, 5], 'color': '#6f0000'},
          {'range': [5, 8], 'color': '#cc6600'},
          {'range': [8, 10], 'color': '#004000'}],
          'threshold': {
          'line': {'color': "#7f0000", 'width': 4},
          'thickness': 0.9,
          'value': 5.6}


      },

  )]

  fig = dict(data=data, layout=layout)

  div = plotly.offline.plot(fig,
                            include_plotlyjs=False, output_type='div', validate=False)

  div = colify_div(div, size='full', zoom="80%")

  return div


@register.simple_tag
def get_plotly(my_title):

  # Get them data
  if my_title == 'Example':
    # For histogram
    x = np.random.randint(low=1, high=11, size=100)

    # For weekly means
    N = 52
    weeks = list(range(1, N + 1))
    weeks_means = np.random.randint(low=1, high=10, size=N)

  else:
    qs = AspectRatings.objects.all().filter(title=my_title)
    if len(qs) < 1:
      return "<p>There are no ratings yet. You could be the first!</p>"
    df = read_frame(qs)
    df = df.set_index('timestamp')

    # For histogram
    x = list(df['rating'])

    # For weekly means
    # Filter data for last N weeks
    date_N_weeks_ago = datetime.date.today() - datetime.timedelta(weeks=10)
    df = df.loc[date_N_weeks_ago:datetime.date.today() +
                datetime.timedelta(days=1)]

    df['week'] = df.apply(
        lambda row: row.name.isocalendar()[1], axis=1).astype('float')

    df_title_weekmeans = df.groupby(
        'week', as_index=True)['rating'].mean()

    weeks = df_title_weekmeans.index.values
    weeks_means = list(df_title_weekmeans)

  div = plot_meanbar(np.mean(x))
  div += plot_histogram(x, my_title)

  div += plotly_lineplot(weeks, weeks_means, title="Paupermeans of " +
                         my_title, ylabel='Mean Rating', xlabel='Week', linecolor='red')

  return div
