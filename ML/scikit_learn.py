from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
iris = load_iris()

X = iris.data
Y = iris.target

feature_names = iris.feature_names
target_names = iris.target_names

print("Feature names:", feature_names)
print("Target names:", target_names)
print("\nType of X is:", type(X))
print("\nFirst 5 rows of X:\n", X[:5])


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.4 ,random_state=1)

print("X_train Shape:", X_train.shape)
print("X_test Shape:", X_test.shape)
print("Y_train Shape:", y_train.shape)
print("Y_test Shape:", y_test.shape)


categorical_feature= ['cat', 'dog', 'dog', 'cat', 'bird']
encoder = LabelEncoder()
encoded_feature = encoder.fit_transform(categorical_feature)
print("Encoded feature:", encoded_feature)
























