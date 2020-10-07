from sklearn.ensemble import AdaBoostClassifier, AdaBoostRegressor, GradientBoostingClassifier, GradientBoostingRegressor
from sklearn.model_selection import cross_val_score
from sklearn import tree
# import xgboost

def check_cross_val_score(model, name, X_train, y_train):
    scores = {}
    model.fit(X_train, y_train)
    print(f"Model: {model}")
    mscore = model.score(X_train, y_train)
    print(f"Training set score: {mscore}")
    scores[name] = {}
    scores[name]['train_score'] = mscore
    cv_score = cross_val_score(model, X_train, y_train, cv=5).mean()
    print(f"CV score: {cv_score}")
    scores[name]['cv_score'] = cv_score

def cvs_decision_tree(X_train, y_train):
    """
    Classification - Decision Tree
    :return:
    """
    # Fit a decision tree using the default hyperparameters.
    dt_clf = tree.DecisionTreeClassifier()

    # Predict on the xtest set
    y_pred = dt_clf.fit(X_train, y_train).predict(X_train)

    # print the accuracy score.
    check_cross_val_score(dt_clf, 'dt_clf', X_train, y_train)

    return y_pred

def csv_adaboost(X_train, y_train):
    """
    # Create the AdaBoost Classifier using the default hyperparameters.
    """
    adaboost_clf = AdaBoostClassifier()

    # Train the classifier
    y_pred = adaboost_clf.fit(X_train, y_train).predict(X_train)

    check_cross_val_score(adaboost_clf, 'adaboost_clf', X_train, y_train)

    # return train prediction
    return y_pred

# Problems with the installation of xgboost
def csv_xgboost(X_train, y_train):
    """
    # Create the XGBoost Regressor
    :return:
    """
    import xgboost
    xgb_reg = xgboost.XGBRegressor()

    # Fit the Regressor
    y_pred = xgb_reg.fit(X_train, y_train).predict(X_train)

    # print accuracy
    check_cross_val_score(xgb_reg, 'xgb_reg', X_train, y_train)

    # return train prediction
    return y_pred