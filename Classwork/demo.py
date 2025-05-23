# import pandas as pd
# import seaborn as sns

# import plotly.express as px

# df = pd.read_csv(r"./datasets/auto-mpg.csv")
# values = {1: "USA", 2: "Europe", 3: "Japan"}
# df.replace({"origin" : values}, inplace=True)
# df_new = df.loc[df.horsepower.str.isdigit(), ['origin', 'mpg', 'cylinders', 'displacement','horsepower', 'weight', 'acceleration']]
# df_new.horsepower = df_new.horsepower.astype(int)



# fig = px.histogram(df_new, x = "origin", y = "mpg", histfunc="avg", color = "origin", height=300, width=500,
#                   title="Average MPG by Origin",
#                 labels={"origin": "Vehicle Origin", "mpg": "Average Miles per Gallon"})

# fig.update_layout(
#     title_font_size=12,
#     title_font_color="darkblue",
#     xaxis_title_font_size=10,
#     yaxis_title_font_size=10,
#     legend_title_text="Origin",
#     legend_title_font_color="black",
#     legend_font_size=10,
#     plot_bgcolor='white',
#     paper_bgcolor='whitesmoke'
# )
# fig.show()

import nbformat
print(nbformat.__version__)