from sklearn import svm
import matplotlib.pyplot as plt

x = [[1, 2], [2, 2], [3, 2], [4, 2], [5, 6], [6, 6], [7, 6], [8, 6]]
y = [9, 9, 9, 9, 5, 5, 5, 5]
clf = svm.SVC()
clf.fit(x, y)
print(clf.predict ([[1, 3]]))
t = input()