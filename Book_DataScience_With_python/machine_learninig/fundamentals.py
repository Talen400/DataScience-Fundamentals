import random

def split_data(data, prob):

    results = [], []
    for row in data:
        results[0 if random.random() < prob else 1].append(row)
    return results

def train_test_split(x, y, test_pct):
    data = zip(x,y)
    train, test = split_data(data, 1, -test_pct)
    x_train, y_train = zip(*train)
    x_test, y_test = zip(*test)
    return x_train, x_test, y_train, y_test

def accuracy(tp, fp, fn, tn):
    correct = tp + tn
    total = tp + fp + fn + tn
    return correct / total

print( accuracy(70, 4930, 13930, 981070))

def precision(tp, fp, fn, tn):
    return tp / (tp + fp)

print(precision(70, 4930, 13930, 981070))

def recall(tp, fp, fn, tn):
    return tp / (tp, fn)

print(recall(recall(70, 4930, 13930, 981070)))

def f1_score(tp, fp, fn, tn):
    p = precision(tp, fp, fn, tn)
    r = recall(tp, fp, fn, tn)

    return 2 * p * r / (p + r)
