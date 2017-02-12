import os
import json

#j = json.loads('{"one" : "1", "two" : "2", "three" : "3"}')
#print json.dumps(j)

#import plotly
#print (plotly.__version__)
#from plotly.graph_objs import Scatter, Layout
#plotly.offline.plot({
#"data": [
#    Scatter(x=[1, 2, 3, 4], y=[4, 1, 3, 7])
#],
#"layout": Layout(
#    title="hello world"
#)
#})

#import plotly
#import plotly.graph_objs

#plotly.offline.plot({
#"data": [
#    plotly.graph_objs.Bar(x=['food','service','environment'],y=[3.4,4.2,4.3])
#]
#})

#import plotly
#from plotly.graph_objs import Scatter, Layout

#plotly.offline.plot({
#    "data": [Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
#    "layout": Layout(title="hello world")
#})

#from plotly.offline import plot
#from plotly.graph_objs import Scatter

#my_plot_div = plot([Scatter(x=[1, 2, 3], y=[3, 1, 6])], output_type='div')


try:
  from SimpleHTTPServer import SimpleHTTPRequestHandler as Handler
  from SocketServer import TCPServer as Server
except ImportError:
  from http.server import SimpleHTTPRequestHandler as Handler
  from http.server import HTTPServer as Server

# Read port selected by the cloud for our application
PORT = int(os.getenv('PORT', 8001))
# Change current directory to avoid exposure of control files
os.chdir('static')

httpd = Server(("", PORT), Handler)
try:
  print("Start serving at port %i" % PORT)
  httpd.serve_forever()
except KeyboardInterrupt:
  pass
httpd.server_close()

