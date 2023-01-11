import numpy as np
from bokeh.io import curdoc
from bokeh.plotting import figure, show
from bokeh.layouts import row, column, gridplot, layout
from bokeh.models import Slider, Div
from bokeh.util.hex import hexbin
from bokeh.transform import linear_cmap
from bokeh.palettes import all_palettes

n = 100000

xs = np.random.normal(0, 1, n)
ys = np.random.normal(0, 1, n)

hb = hexbin(xs, ys, 0.2)

fig = figure(width = 400, aspect_ratio = 1)
fig.background_fill_color = all_palettes['Turbo'][256][0]
fig.grid.visible = False

cmap = linear_cmap('counts', 'Turbo256', 0, np.max(hb['counts']))
ht = fig.hex_tile(source = hb, size = 0.2, color = cmap, line_color = None)

def callback(attr, old, new):
    n = new

    xs = np.random.normal(0, 1, n)
    ys = np.random.normal(0, 1, n)
    
    hb = hexbin(xs, ys, 0.2)
    cmap = linear_cmap('counts', 'Turbo256', 0, np.max(hb['counts']))
    ht.glyph.fill_color = cmap

    ht.data_source.data = hb

s1 = Slider(start = 100, end = 1000000, step = 100, value = 100000, title = 'N', sizing_mode = 'stretch_width')
s1.on_change('value_throttled', callback)

curdoc().add_root(column(Div(text = 'To jest rozklad normalny!'), row(column(s1, width = 200), fig)))