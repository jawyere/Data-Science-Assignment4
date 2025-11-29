from ucimlrepo import fetch_ucirepo 
import pandas as pd
import tables


iris = fetch_ucirepo(id=53) 
  
df = iris.data.features 
y = iris.data.targets 
df["Classification"] = y
metadata = iris.metadata
var_df = iris.variables

#add main data and variable name data
df.to_hdf("iris_data.h5", key="data_df", mode="w", format="table")
var_df.to_hdf("iris_data.h5", key="variables_df", mode="a",format="table")

#attach metadata
with pd.HDFStore("iris_data.h5", mode="a") as s:
    storer = s.get_storer("data_df")
    for key, value in metadata.items():
        storer.attrs[key] = str(value)


#print out file structure
with tables.open_file("iris_data.h5", mode="r") as h5:
    print(h5) 

#print out metadata
with pd.HDFStore("iris_data.h5", mode="r") as s:

    storer = s.get_storer("data_df")
    attrs = storer.attrs
    
    for attr_name in dir(attrs):
        pass#print(attr_name, getattr(attrs, attr_name))