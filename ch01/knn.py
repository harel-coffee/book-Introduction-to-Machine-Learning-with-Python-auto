import numpy as np
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


def main():
    iris_dataset = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
            iris_dataset['data'], iris_dataset['target'], random_state=0)

    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(X_train, y_train)

    print("{:.2f}".format(knn.score(X_test, y_test)))


if __name__ == '__main__':
    main()
