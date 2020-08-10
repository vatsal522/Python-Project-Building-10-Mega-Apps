# -*- coding: utf-8 -*-
"""
Created on Sun May  3 01:37:25 2020

@author: 91771
"""


from camera_detector import df
import bokeh
import pandas
from bokeh.plotting import figure
from bokeh.io import output_file,show 
from bokeh.models import HoverTool,ColumnDataSource
  
f=figure(x_axis_type="datetime",height=200,width=500,sizing_mode="scale_width")


df['start_str']=df['Start'].dt.strftime("%Y-%m-%d %H-%M-%S")
df['end_str']=df['End'].dt.strftime("%Y-%m-%d %H-%M-%S")
cds=ColumnDataSource(df)

f.title.text="Year and Close"
f.title.text_color="red"
f.xaxis.axis_label="Time"
f.yaxis.axis_label="IN OR OUT"
f.yaxis.minor_tick_line_color=None
f.ygrid[0].ticker.desired_num_ticks=1





hover=HoverTool(tooltips=[("Start","@start_str"),("End","@end_str")])

f.add_tools(hover)

q=f.quad(left='Start',right='End',bottom=0,top=1,color="Green",source=cds)

output_file("Graph.html")
show(f)
