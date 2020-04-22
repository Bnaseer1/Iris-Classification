from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# loading the data
url = "D:/Datasets/Iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'species']
dataset = read_csv(url, names=names, header=0)
##outputs the first 10 data
#print(dataset.head(10))
##outputs the shape of the dataset
#print(dataset.shape)
##outputs a statistical summary of the dataset, such as std, quartiles and means
#print(dataset.describe())
##outputs the amount of datasets for each species
#print(dataset.groupby('species').size())

##visualising the data
##box and whisker plots
#dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
#dataset.hist()
#scatter_matrix(dataset)
#pyplot.show()

##split-out validation dataset
array = dataset.values
X = array[:,0:4]
y = array[:,4]
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)

##Spot Check Alogirthms
#models = []
#models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
#models.append(('LDR', LinearDiscriminantAnalysis()))
#models.append(('KNN', KNeighborsClassifier()))
#models.append(('CART', DecisionTreeClassifier()))
#models.append(('NB', GaussianNB()))
#models.append(('SVM', SVC(gamma='auto')))

##evaluate each model in turn
#results = []
#names = []
#for name, model in models:
    #kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
    #cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
    #results.append(cv_results)
    #names.append(name)
    #print('%s: %f(%f)' % (name, cv_results.mean(), cv_results.std()))

##compare algorithms
#pyplot.boxplot(results, labels=names)
#pyplot.title('Algo Comparison')
#pyplot.show()

#make predictions
model = SVC(gamma='auto')
model.fit(X_train, Y_train)
predictions = model.predict(X_validation)

#evaluate
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))