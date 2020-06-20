# Jupyter_Notebooks_Pocket_Manual
Jupyter notebooks para consulta rapida.  
Dataviz seite: https://www.data-to-viz.com  


* Lembrete, testar DBSCAN para problemas de fraude.  
```
from sklearn.cluster import DBSCAN  
dbscan = DBSCAN()  
dbscan.fit(X)  
print(dbscan.labels_)  
```

