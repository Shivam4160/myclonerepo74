from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error , r2_score
import matplotlib.pyplot as plt

diabetes = load_diabetes()
X = diabetes.data
Y = diabetes.target


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2 ,random_state=42)


model = LinearRegression()

model.fit(X_train,Y_train)
Y_pred = model.predict(X_test)

print("Actual value  :",Y_test[:5])
print("Predicted value  :",Y_pred[:5])

print("mean squared Error  :",mean_squared_error(Y_test,Y_pred))
print("r2 score  :",r2_score(Y_test,Y_pred))


plt.plot(Y_test[:20],marker = 'o',label='Actual')
plt.plot(Y_pred[:20],marker = 's',label='Predicted')


plt.title("Actual VS Predicted value(First 20 sample)")
plt.xlabel("Sample number")
plt.ylabel("Disease Progresion")
plt.legend("Actual VS Predicted value(First 20 sample)")
plt.grid(True)
plt.show()



plt.figure(figsize = (8,6))
plt.scatter(Y_test,Y_pred)

plt.plot([Y_test.min(),Y_test.max()],[Y_test.min(),Y_test.max()],'r--',linewidth = 2)

plt.title("Actual VS Predicted value(First 20 sample)")
plt.xlabel("Sample number")
plt.ylabel("Disease Progresion")
plt.grid(True)
plt.show()
















