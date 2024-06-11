from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import tree


class DecisionTree():
    def __init__(self, dataset, **kwargs) -> None:
        self.dataset = dataset
        self.test_size = kwargs.get("test_size", 0.3)
        self.random_state = kwargs.get("random_state", None)

        self.clf = DecisionTreeClassifier(**kwargs)
        self.X_train, self.X_test, self.y_train, self.y_test = self._train()
        self.y_pred = self._predict()

    def textual_description(self):
        return tree.export_text(
            self.clf,
            feature_names=self.dataset.feature_names
        )

    def _train(self):
        X, y = self.dataset.data, self.dataset.target
        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size = self.test_size,
            random_state = self.random_state,
            stratify = y
        )
        self.clf.fit(X_train, y_train)
        return X_train, X_test, y_train, y_test

    def _predict(self):
        y_pred = self.clf.predict(self.X_test)
        return y_pred

    def _get_seed(self):
        return self.random_state
