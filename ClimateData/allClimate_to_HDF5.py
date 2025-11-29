import pandas as pd
import tables
import xmltodict


df = pd.read_csv("allClimateData.csv")
with open('allClimate_metadata.xml', 'r', encoding='utf-8') as file:
    my_xml = file.read()

metadata = xmltodict.parse(my_xml)

#add main data and variable name data
df.to_hdf("allClimate_data.h5", key="data_df", mode="w", format="table")

#attach metadata
with pd.HDFStore("allClimate_data.h5", mode="a") as s:
    storer = s.get_storer("data_df")
    for key, value in metadata.items():
        storer.attrs[key] = str(value)


#print out file structure
with tables.open_file("allClimate_data.h5", mode="r") as h5:
    print(h5) 

#print out metadata
with pd.HDFStore("allClimate_data.h5", mode="r") as s:

    storer = s.get_storer("data_df")
    attrs = storer.attrs
    
    for attr_name in dir(attrs):
        print(attr_name, getattr(attrs, attr_name))
