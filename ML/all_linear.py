import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split




# predict height using age
'''

data = {'age':[6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
        'height':[100,108,115,123,130,135,140,145,150,155,160,161,168,170,172]
        }
df = pd.DataFrame(data)

X = df[['age']]
Y = df[['height']]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)

model = LinearRegression()
model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)


result = X_test.copy()
result["Actual height"] = Y_test.values
result["Predicted height"] = Y_pred

print(result)
'''



#predict percentage using standard

'''
data = {'standard':list(range(1,15)),
        'percentage':[45,50,55,58,60,62,64,67,70,72,75,77,80,82]
        }

df = pd.DataFrame(data)

X = df[['standard']]
Y = df[['percentage']]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)

model = LinearRegression()
model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)


result = X_test.copy()
result["Actual percentage"] = Y_test.values
result["Predicted percentage"] = Y_pred

print(result)

'''

#predict shoesize by height
'''
data = {'height':[110,120,130,140,150,160,170,180,190],
        'shoesize':[3,4,5,6,7,8,9,10,11]
        }
df = pd.DataFrame(data)

X = df[['height']]
Y = df[['shoesize']]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)

model = LinearRegression()
model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)


result = X_test.copy()
result["Actual shoesize"] = Y_test.values
result["Predicted shoesize"] = Y_pred

print(result)
'''


#predict saay by experience
'''
data = {'experience':[1,2,3,4,5,6,7,8,9,10],
        'salary':[20000,25000,30000,35000,40000,45000,50000,55000,60000,65000]
        }


df = pd.DataFrame(data)

X = df[['experience']]
Y = df[['salary']]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)

model = LinearRegression()
model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)


result = X_test.copy()
result["Actual salary"] = Y_test.values
result["Predicted salary"] = Y_pred

print(result)
'''

#predict score by hours
'''
data = {'hours':[1,2,3,4,5,6,7,8,9,10],
        'score':[30,40,50,55,60,65,70,75,85,95]
        }

df = pd.DataFrame(data)

X = df[['hours']]
Y = df[['score']]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)

model = LinearRegression()
model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)


result = X_test.copy()
result["Actual score"] = Y_test.values
result["Predicted score"] = Y_pred

print(result)

'''

#predict price by vehicle age
'''
data = {'vehicleage':[1,2,3,4,5,6,7,8,9,10],
        'resaleprice':[500000,450000,400000,350000,320000,300000,270000,250000,230000,200000]
        }


df = pd.DataFrame(data)

X = df[['vehicleage']]
Y = df[['resaleprice']]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)

model = LinearRegression()
model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)


result = X_test.copy()
result["Actual resaleprice"] = Y_test.values
result["Predicted resaleprice"] = Y_pred

print(result)

'''


#predict salary by experience CSV file

df = pd.read_csv('E:\CS74\ML\experience_salary.csv')

X = df[['years experience']]
Y = df[['salary']]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)

model = LinearRegression()
model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)


result = X_test.copy()
result["Actual salary"] = Y_test.values
result["Predicted salary"] = Y_pred

print(result)

