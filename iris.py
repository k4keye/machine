import pandas
from sklearn import svm , metrics
from sklearn.model_selection import train_test_split
csv = pandas.read_csv("iris.csv")
data =csv[["sepal.length","sepal.width","petal.length","petal.width"]]
label = csv["variety"]

train_data ,test_data , train_label , test_label = train_test_split(data,label) #전체데이터와 전체 정답
clf =svm.SVC()
clf.fit(train_data , train_label) # 학습용 데이터와 정답
result = clf.predict(test_data)# 테스트용 데이터

print(result)
score = metrics.accuracy_score(result , test_label) #결과와 정답
print(score)
