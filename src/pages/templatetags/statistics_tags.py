from django import template


import numpy as np
import plotly
import plotly.graph_objects as go
import plotly.express as px

from ratings.templatetags.ratings_tag import colify_div


from django_pandas.io import read_frame
from ratings.models import AspectRatings
import datetime
import copy

register = template.Library()


@register.simple_tag
def total_post():
  return "I'm working yes 5 posts zogenaamd"


@register.simple_tag
def get_plotly2():
  layout = {"title": {"text": "Aspects Rated", 'xref': "container"},
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


class DataPlotler:
  layout = {"title": {"text": "MYTITLE", 'xref': "container"},
            "font": dict(family='Montserrat', size=16, color='white'),
            "plot_bgcolor": "rgb(30,30,30)",
            "paper_bgcolor": "hsl(0, 0, 18)",
            "yaxis": dict(showline=True, linecolor='white', showgrid=False, title="Y-NAME"),
            'xaxis': dict(showline=True, linecolor='white', showgrid=False, title="X-NAME")
            }

  def __init__(self, datatype=None):
    self.div = ''

    # Load REAL rating data
    qs = AspectRatings.objects.all()
    self.df = read_frame(qs)
    self.df = self.df.set_index('timestamp')

  def plot_pie_aspects(self, title):
    # Plots aspects rated in pie distribution chart
    layout = copy.deepcopy(self.layout)
    layout['title']['text'] = title

    values = list(self.df['title'].value_counts())
    labels = self.df['title'].value_counts().index.values

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)], layout=layout)

    self._make_div(fig)

  def plot_weekly_means(self, title, N_weeks=10):
    layout = copy.deepcopy(self.layout)
    layout['title']['text'] = title
    layout['yaxis']['title'] = 'Mean Rating'
    layout['xaxis']['title'] = 'Week'
    layout['xaxis']['dtick'] = 1

    # Filter data for last N weeks
    date_N_weeks_ago = datetime.date.today() - datetime.timedelta(weeks=N_weeks)
    df = self.df.loc[date_N_weeks_ago:datetime.date.today() +
                     datetime.timedelta(days=1)]

    # Make new week variable
    df['week'] = df.apply(
        lambda row: row.name.isocalendar()[1], axis=1).astype('float')

    # Make the figure
    fig = go.Figure(layout=layout)
    # So it is ordered by count
    for title_i in self.df['title'].value_counts().index.values:
      df_title_weekmeans = df[df['title'] == title_i].groupby(
          'week', as_index=True)['rating'].mean()

      weeks = df_title_weekmeans.index.values
      means = list(df_title_weekmeans)
      fig.add_trace(go.Scatter(x=weeks, y=means,
                               mode='lines+markers',
                               name=title_i,
                               ))

    self._make_div(fig)

  def plot_hist_month(self, title):

    layout = copy.deepcopy(self.layout)
    layout['title']['text'] = title + datetime.datetime.now().strftime("%B")
    layout['yaxis']['title'] = 'Count'
    layout['xaxis']['title'] = 'Rating'
    layout['xaxis']['tickmode'] = 'array'
    layout['xaxis']['tickvals'] = list(range(1, 11))

    marker = {"line": {"color": "#25232C", "width": 0.2},
              }

    today = datetime.datetime.today()
    datem = datetime.datetime(today.year, today.month, 1)
    today += datetime.timedelta(days=1)

    df = self.df.loc[datem:today]

    fig = go.Figure(layout=layout)
    for title_i in self.df['title'].value_counts().index.values:
      df_titleratings = list(df[df['title'] == title_i]['rating'])

      fig.add_trace(go.Histogram(x=df_titleratings,
                                 name=title_i, marker=marker))

    fig.update_traces(opacity=0.75)
    self._make_div(fig)

  def plot_onvoldoendes(self, title, N_days=10):
    layout = copy.deepcopy(self.layout)
    layout['title']['text'] = title + 'Last ' + str(N_days) + ' Days'
    layout['yaxis']['title'] = 'Count'
    layout['xaxis']['title'] = 'Rating'

    # Select ratingsbelow 6 for last N days
    date_N_days_ago = datetime.date.today() - datetime.timedelta(days=N_days)
    df = self.df.loc[date_N_days_ago:datetime.date.today() +
                     datetime.timedelta(days=1)]
    df = df[df['rating'] < 6]

    values = list(df['title'].value_counts())
    labels = df['title'].value_counts().index.values

    fig = go.Figure([go.Bar(x=labels, y=values)])
    fig.update_layout(layout)

    self._make_div(fig)

  def plot_mainmeans(self, title):
    layout = copy.deepcopy(self.layout)
    layout['xaxis']['title'] = 'Mean Rating'
    layout['yaxis']['title'] = ''
    layout['title']['text'] = title

    # Extract data
    df_means = self.df.groupby('title', as_index=True)['rating'].mean()

    df_means_onvoldoende = df_means[df_means < 5.6]
    df_means_voldoende = df_means[df_means >= 5.6]

    # Plot
    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=list(df_means_onvoldoende.index.values),
        x=list(df_means_onvoldoende),
        name='Onvoldoende!',
        orientation='h',
        marker=dict(
            color='rgba(246, 78, 139, 0.6)',
            line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
        )
    ))
    fig.add_trace(go.Bar(
        y=df_means_voldoende.index.values,
        x=list(df_means_voldoende),
        name='Voldoende!',
        orientation='h',
        marker=dict(
            color='rgba(0, 100, 0, 0.6)',
            line=dict(color='rgba(0, 100, 0, 1.0)', width=3)
        )
    ))

    fig.update_layout(layout)

    # Red onvoldoende bar
    fig.update_layout(
        shapes=[
            # Line Vertical
            go.layout.Shape(
                type="line",
                x0=5.6,
                y0=-1,
                x1=5.6,
                y1=len(df_means),
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

    self._make_div(fig, size='full')

  def _make_div(self, fig, size='half'):
    div = colify_div(plotly.offline.plot(
        fig, include_plotlyjs=False, output_type='div'), size=size)
    self.div += div

  @property
  def html(self):
    return self.div


@register.simple_tag
def plot_statistics():
  MyDiv = DataPlotler()

  MyDiv.plot_mainmeans(title='ALL TIME SCOREBOARD!')
  MyDiv.plot_pie_aspects(title='Aspects Rated')
  MyDiv.plot_weekly_means(title='Weekly Mean Rating', N_weeks=10)
  MyDiv.plot_hist_month(title="Paupergram Ratings: ")
  MyDiv.plot_onvoldoendes(title="Onvoldoendes: ", N_days=30)

  return MyDiv.html
