from sklearn.ensemble import AdaBoostClassifier, AdaBoostRegressor, GradientBoostingClassifier, GradientBoostingRegressor
from sklearn.model_selection import cross_val_score
from sklearn import tree

def cvs_decision_tree(X_train, y_train):
    """
    Classification - Decision Tree
    :return:
    """
    # Fit a decision tree using the default hyperparameters.
    dt_clf = tree.DecisionTreeClassifier()

    # Predict on the xtest set
    y_pred = dt_clf.fit(X_train, y_train).predict(X_train)

    # return the accuracy score.
    return cross_val_score(dt_clf, X_train, y_train, cv=5).mean()

def csv_adaboost(X_train, y_train):
    """
    # Create the AdaBoost Classifier using the default hyperparameters.
    """
    adaboost_clf = AdaBoostClassifier()

    # Train the classifier
    adaboost_clf.fit(X_train, y_train).predict(X_train)

    # return accuracy
    return cross_val_score(adaboost_clf, X_train, y_train, cv=5).mean()