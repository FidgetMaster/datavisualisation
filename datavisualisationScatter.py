import pandas as pd
import plotly.express as px
file = pd.read_csv("CasesData.csv")
graph = px.scatter(file, x = "date", y = "cases", color = "country", title = "Cases Total" )
graph.show()