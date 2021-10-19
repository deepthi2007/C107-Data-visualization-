import pandas as pd
import plotly.express as px

df = pd.read_csv("D:\deepthi projects\C107\data.csv")
mean = df.groupby("level")["attempt"].mean()
print(mean)

fig = px.scatter(mean,x=df["student_id"],y=df["level"],color=df["attempt"],size=df["attempt"])
fig.show()