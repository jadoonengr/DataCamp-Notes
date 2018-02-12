# Perform the necessary imports
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.layouts import widgetbox
from bokeh.models import Slider
from bokeh.layouts import column
import numpy as np
from numpy.random import random

# Create ColumnDataSource: source
x = np.linspace(1,10,100)
y = np.linspace(1,10,100)
source = ColumnDataSource(data={'x':x,'y':y})

# Add a line to the plot
plot.line('x', 'y', source=source)
slider = Slider(title='my slider', start=0, end=10, step=1, value=2)
# Create a column layout: layout
layout = column(widgetbox(slider), plot)

# Add the layout to the current document
curdoc().add_root(layout)