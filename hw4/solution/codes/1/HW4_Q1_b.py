import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import sklearn.datasets
from sklearn.metrics import accuracy_score




def sigmoid(x):
    return 1.0/(1.0 + np.exp(-x))

def sigmoid_prime(x):
    return sigmoid(x)*(1.0-sigmoid(x))

def tanh(x):
    return np.tanh(x)

def tanh_prime(x):
    return 1.0 - x**2

# layers=[X.shape[1],units,1]
class NeuralNetwork:
    def __init__(self, layers, activation='tanh'):
        if activation == 'sigmoid':
            self.activation = sigmoid
            self.activation_prime = sigmoid_prime
        elif activation == 'tanh':
            self.activation = tanh
            self.activation_prime = tanh_prime

        # Set weights
        self.weights = []
        for i in range(1, len(layers) - 1):
            r = 2 * np.random.random((layers[i - 1] + 1, layers[i] + 1)) - 1
            self.weights.append(r)

            r = 2 * np.random.random((layers[i] + 1, layers[i + 1])) - 1
            self.weights.append(r)

    def fit(self, X, y, learning_rate=0.2, epochs=100000):
        ones = np.atleast_2d(np.ones(X.shape[0]))
        X = np.concatenate((ones.T, X), axis=1)

        for k in range(epochs):
            i = np.random.randint(X.shape[0])
            a = [X[i]]

            for l in range(len(self.weights)):
                dot_value = np.dot(a[l], self.weights[l])
                activation = self.activation(dot_value)
                a.append(activation)
            # output layer
            error = y.iloc[i] - a[-1]
            deltas = [error * self.activation_prime(a[-1])]

            # we need to begin at the second to last layer
            # (a layer before the output layer)
            for l in range(len(a) - 2, 0, -1):
                deltas.append(deltas[-1].dot(self.weights[l].T) * self.activation_prime(a[l]))

            # reverse
            # [level3(output)->level2(hidden)]  => [level2(hidden)->level3(output)]
            deltas.reverse()

            # backpropagation
            # 1. Multiply its output delta and input activation
            #    to get the gradient of the weight.
            # 2. Subtract a ratio (percentage) of the gradient from the weight.
            for i in range(len(self.weights)):
                layer = np.atleast_2d(a[i])
                delta = np.atleast_2d(deltas[i])
                self.weights[i] += learning_rate * layer.T.dot(delta)

            if k % 10000 == 0: print ('epochs:', k)

    def predict(self, x):
        # print(x)
        a = np.concatenate((np.ones(1).T, np.array(x)),axis=None)
        for l in range(0, len(self.weights)):
            a = self.activation(np.dot(a, self.weights[l]))
        if a > 0.5:
            p=1
        else:
            p=0
        return p
if __name__ == '__main__':

    breast_cancer = sklearn.datasets.load_breast_cancer()

    # convert the data to pandas dataframe
    data = pd.DataFrame(breast_cancer.data, columns=breast_cancer.feature_names)
    data["class"] = breast_cancer.target
    data.head()
    data.describe()

    # perform scaling on the data.
    X = data.drop("class", axis=1)
    Y = data["class"]
    X = MinMaxScaler().fit_transform(X)
    X = pd.DataFrame(X, columns=data.drop("class", axis=1).columns)

    # train test split.
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state=1)

    nn = NeuralNetwork([X_train.shape[1],X_train.shape[1],1])
    nn.fit(X_train,Y_train)
    prediction=[]

    for i in range(X_test.shape[0]):
        prediction.append(nn.predict(X_test.iloc[i]))

    for i in prediction:
        print(i)

    # checking the accuracy of the model
    print("test accuracy")
    print(accuracy_score(prediction, Y_test))



