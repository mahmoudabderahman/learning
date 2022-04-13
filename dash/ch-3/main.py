import plotly.graph_objects as go



fig = go.Figure()
fig.layout.title = 'The Figure Title'
fig.layout.xaxis.title= 'The X-axis title'
fig.layout.yaxis.title= 'The Y-axis title'
fig.add_scatter(x=[1, 2, 3], y=[4, 2, 3])
fig.add_scatter(x=[1, 2, 3, 4], y=[4, 5, 2, 3])


fig.show(config={'displaylogo':False,
                'modeBarButtonsToAdd':['drawrect',
                                        'drawcircle',
                                        'eraseshape']})

fig.write_html('html_plot.html',
                config={'toImageButtonOptions':{'format':'svg'}})

fig.write_image('img.svg',
                height=600, width=850)
