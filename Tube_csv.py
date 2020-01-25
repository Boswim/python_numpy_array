import plotly.graph_objects as go
import pandas as pd
from numpy import genfromtxt

pd1=pd.read_csv('CSV/9.csv', sep=',',index_col=0)


#met regel 14 werkt
fig = go.Figure(go.Heatmap(z=pd1)) 
fig.show()






