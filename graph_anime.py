import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    "Year": [2020, 2020, 2021, 2021, 2022, 2022],
    "Category": ["A", "B", "A", "B", "A", "B"],
    "Value": [10, 15, 20, 25, 30, 35]
})

fig = px.bar(df, x="Category", y="Value", color="Category",
             animation_frame="Year", range_y=[0, 40])
fig.show()
