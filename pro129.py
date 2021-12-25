import csv
import pandas as pd

df= pd.read_csv('dwarf_stars.csv')

df= df[df['Distance'].notna()]
df= df[df['Mass'].notna()]
df= df[df['Radius'].notna()]
df= df[df['Star_name'].notna()]

df['Mass']= df['Mass'].apply(lambda x: x.replace('$','').replace(',','')).astype(float)

df['Radius']= 0.102763*df['Radius']
df['Mass']= 0.000954588*df['Mass']

df.to_csv('unit_converted_stars.csv')
