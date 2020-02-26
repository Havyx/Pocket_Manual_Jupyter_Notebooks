# Jupyter_Notebooks_Pocket_Manual
Jupyter notebooks para consulta rapida.  
Dataviz seite: https://www.data-to-viz.com  

df = pd.read_csv('creditcard.csv')  
df['Class'].value_counts()  
df['Class'].value_counts().plot(kind='bar')  
X = df.drop(['Class'], axis=1)  
y = df[['Class']]  
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.1)  

from sklearn.cluster import DBSCAN  
dbscan = DBSCAN()  
dbscan.fit(X)  
print(dbscan.labels_)  


