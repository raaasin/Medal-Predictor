import pandas as pd
teams = pd.read_csv("teams.csv")
teams = teams[["team","country","year","athletes","age","prev_medals","medals"]]

teams= teams.dropna()

from sklearn.linear_model import LinearRegression
import pickle

reg= LinearRegression()
predictors = ["athletes","prev_medals"]
reg.fit(teams[predictors],teams["medals"])

pickle.dump(reg,open("olympic.pkl","wb"))
