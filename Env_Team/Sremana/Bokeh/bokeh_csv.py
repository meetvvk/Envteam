import pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show

df=pandas.read_csv("data.csv")
x=df["x"]
y=df["y"]

output_file("line_from_csv.html")

f=figure()

f.line(x,y)

show(f)