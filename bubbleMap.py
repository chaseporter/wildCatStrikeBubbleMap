import plotly.graph_objects as go

import pandas as pd

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_us_cities.csv')
df = pd.read_csv('parsedTxt2.csv')
# print(df)
df.head()

df['text'] = df['org']
limits = [(0,15),(15,41),(41,54),(54,82),(82,126)]
# darkgray rgb(51, 52, 46)
# colors [h wf t o f]
# off white rgb(227, 237, 223), h
# yellow rgb(255,222,22) wf
# purple rgb(143, 13, 86) t
# orange rgb(253, 144, 20) o
# red orange rgb(239, 76, 57) f
colors = ["rgb(227, 237, 223)", "rgb(255,222,22)", "rgb(143, 13, 86)", "rgb(253, 144, 20)", "rgb(239, 76, 57)"]
cats = ["Healthcare", "Warehouse and Factory", "Transportation", "Other", "Food Service and Distribution"]

fig = go.Figure()

for i in range(len(limits)):
    lim = limits[i]
    df_sub = df[lim[0]:lim[1]]
    fig.add_trace(go.Scattergeo(
        locationmode = 'USA-states',
        lon = df_sub['lon'],
        lat = df_sub['lat'],
        text = df_sub['text'],
        marker = dict(
            size = df_sub['size']*3,
            color = colors[i],
            line_color='rgb(40,40,40)',
            line_width=0.5,
            sizemode = 'area'
        ),
        name = cats[i]))

fig.update_layout(
        # title_text = '2014 US city populations<br>(Click legend to toggle traces)',
        # showlegend = True,
        geo = dict(
            scope = 'usa',
            landcolor = 'rgb(51,52, 46)'
        )
    )

fig.show()