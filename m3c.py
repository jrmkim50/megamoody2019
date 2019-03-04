# -*- coding: utf-8 -*-
"""M3C.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qMPWIu_6A_ZWBuyd3xGCVcjpM6A0o0us

# Mathworks Math Modeling Challenge
---
*Smoking Data since 1980 fitted onto a Linear Regression*
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt   #Data visualisation libraries 
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

x = np.array([1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
2011])
y = np.array([9.9, 9.9, 9.7, 9.1, 9, 8.8, 8.6, 8.3, 8.1, 7.6, 7.4, 7.1, 6.9, 6.6, 6.6, 6.5, 6.4, 6.3, 6, 5.7, 5.4, 5.3, 5.1, 4.9, 4.7, 4.5, 4.5, 4.2, 4, 3.7 ,3.6, 3.5])
X = np.reshape(x, (32,1))
Y = np.reshape(y, (32,1))

plt.figure()

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=30, random_state=101)

model = LinearRegression()
model.fit(X_train,Y_train)
plt.scatter(X_test, Y_test)
plt.title('Distribution of Cigarette Users Since 1980')
plt.xlabel('Year')
plt.ylabel('Percentage of Population Using Cigarettes')
future = np.array([2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029])
ft = np.reshape(future, (18, 1))
predictions = model.predict(ft)
plt.scatter(ft, predictions)
plt.plot(x, model.predict(X), color = 'red')
poly.fit(X_poly, price2)
plt.show()
print(model.score(X,Y))
print('Expected Consumption of Cigarettes per Person per Day in 2018: ' + str(model.predict(np.reshape(([2018]),(1,1)))))
print('Expected Consumption of Cigarettes per Person per Day in 2019: ' + str(model.predict(np.reshape(([2019]),(1,1)))))
print('Expected Consumption of Cigarettes per Person per Day in 2029: ' + str(model.predict(np.reshape(([2029]),(1,1)))))



"""# E-cig, Rechargeables

*Rechargeable Unit Monthly Sales*
"""

years = np.array([2013, 2014, 2015, 2016])
sales = np.array([114.5, 187.2, 189.9, 236.6])
plt.scatter(years, sales)
plt.xlabel('Year')
plt.ylabel('Unit Sales')
plt.title('Vape Unit Sales')
plt.show()

import numpy as np
from scipy.optimize import curve_fit

years = np.array([2013, 2014, 2015, 2016])
sales = np.array([25.44, 17.56, 12.32, 10.43])

def fit_func(x, a, b):
  return a+b*np.log(x)

params = curve_fit(fit_func, years, sales)

[a,b] = params[0]

X = range(2013,2017)
X = np.array(X)
Y = a+b*np.log(X)

plt.plot(X, Y)
plt.scatter(years,sales)
plt.xlabel("Year")
plt.ylabel("Price")
plt.title("Price Comparison")

X = range(2013,2017)
X = np.array(X)
Y = a+b*np.log(-X)

plt.plot(X, Y)
plt.scatter(years,sales)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LassoCV
from sklearn.pipeline import make_pipeline
from scipy.optimize import curve_fit

years = np.array([2013, 2014, 2015, 2016])
sales = np.array([25.44, 17.56, 12.32, 10.43])
plt.scatter(years,sales)
plt.show()

plt2 = curve_fit(a+b*np.log(years), years, sales)

plt.plot(plt2)
[a,b] = plt[0];
X = years
Y = a + b*np.log(years)
plt.plot(X,Y)

"""#Universal Demand Curve for E-Cigarettes"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LassoCV
from sklearn.pipeline import make_pipeline
from scipy.optimize import curve_fit

import numpy as np
from scipy.optimize import curve_fit

x = np.array([4.45, 0.23, 10.50, 0.10, 8.94]) # E-cigarette sales per 1k people, per month
y = np.array([15.74, 34.12, 9.25, 22.63, 9.50])

def fit_func(x, a, b, c):
    return a*x*x + b*x+ c

params = curve_fit(fit_func, x, y)

[a, b, c] = params[0]

params

print(a,b,c)

X = range(12)
X = np.array(X)
Y = a*X*X+b*X+c

plt.plot(X,Y)
x = np.array([4.45, 0.23, 10.50, 0.10, 8.94]) # E-cigarette sales per 1k people, per month
y = np.array([15.74, 34.12, 9.25, 22.63, 9.50])
plt.scatter(x,y)
plt.ylabel("Price")
plt.xlabel("E-cigarette sales per 1k people, per month")
plt.title("E-Cigarette Sales")

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LassoCV
from sklearn.pipeline import make_pipeline
from scipy.optimize import curve_fit

#frequence of use
  #no use = 1, -28% but use -14 as weight
  #1-3 in past month = 1, 12.1%
  #1-2 times in past week = 3, 8.8%
  #3-6 times in past week = 4, 11.4%
  #Daily = 5, 37.8%
#age at first use
  #11 and under = 1, 7.3%
  #12-14 = 2, 22.3%
  #15-17 = 3, 28%
#poverty status
  #At or above poverty level = 1, 23.7%
  #Below poverty level = 2, 34.3%
#insurance coverage
  #Medicaid = 1, 38%
  #Medicare = 2, 13.8%
  #Private = 1, -10.7%
  #Uninsured = 4, 38%
#education level
  #still in school = 1, 29.5%
  #8th grade or less = 3, 21%
  #9th-11th = 2, 36.8%
  #12th grade = 1, 30.2%

import numpy as np
from scipy.optimize import curve_fit

features = np.array(range(1,5))
weight = np.array([14.5, 56.3, 71.96, 90])


plt.scatter(features,weight)
plt.xlabel("Individual Characteristic/Feature Count")
plt.ylabel("Drug Use Confidence Score")
plt.title("Drug Use Confidence Score Based on Personal Information Count")

def fit_func(x, a, b):
  return a+b*np.log(x)

params = curve_fit(fit_func, features, weight)

[a,b] = params[0]

X = range(1,5)
X = np.array(X)
Y = a+b*np.log(X)

plt.scatter(features,weight)
plt.plot(X, Y)
plt.xlabel("Individual Characteristic/Feature Count")
plt.ylabel("Drug Use Confidence Score")
plt.title("Drug Use Confidence Score Based on Personal Information Count")

print(a,b)

