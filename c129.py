import pandas as pd
import csv
reading=pd.read_csv('dwarf_stars.csv')
reading1=pd.read_csv('solar_radius_mass.csv')
reading=reading.dropna()
reading['Mass']=(reading['Mass'].astype(float))
reading['Radius']=(reading['Radius'].astype(float))
reading['Radius']=reading['Radius'].multiply(0.102763)
reading['Mass']=reading['Mass'].multiply(0.000954588)
reading.to_csv("solar_radius_mass.csv")
merged=reading.merge(reading1)
merged.to_csv("final_stars.csv",index=False)
