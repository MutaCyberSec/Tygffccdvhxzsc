import os

import pandas as pd
import numpy as np
import seaborn as sb

import matplotlib.pyplot as plt
import statsmodels.api as sm

# Load data into a DataFrame
df = pd.read_csv('output_data.csv')


data = df[df['mkt_id'] == 44]
# Define he dependent and independent variables

v = data['output_own_share']
p = data['output_comp_price']
g = data['output_own_sales']
h = data['output_own_profits']
r = data['output_X']

x = data['output_own_price']
y = data['output_own_cost']

def repor(X = x):
	X = sm.add_constant(X)

	# Fit the linear model
	model = sm.OLS(y, X).fit()

	# Get the summary of the regression
	print(model.summary())

#repor()

print(data.columns)


print(data.shape)

print(data.head())


def create_plot():
	sb.set(style="whitegrid")
	sb.lineplot(x= x, y=y, marker="o")
	plt.show()

create_plot()
