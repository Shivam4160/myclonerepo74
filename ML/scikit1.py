import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


df = pd.read_csv('E:\CS74\student_data.csv')

X = df[["Python","Java","DBMS","Maths","Attendance"]]
Y = df["RollNo"]
Names_nums = df["Name"] 
encoder = LabelEncoder()
encoded_Names_nums = encoder.fit_transform(Names_nums)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2 ,random_state=1)


print(f'total rows in ds:{len(X)}')
print(f'total rows in Trains(X_train):{len(X_train)}')
print(f'total rows in Tests(X_train):{len(X_test)}')
print("\n\n----- sample features------\n\n")
print(X_test)

