def classify(x_train, y_train, x_test, y_test):
    classifier = classifier_constructor()

    classifier.fit(x_train, y_train)
    y_pred = classifier.predict(x_test, y_test)

    correct =  [y_pred == y_test]

    accuracy = sum(correct/len(correct))
    return accuracy

