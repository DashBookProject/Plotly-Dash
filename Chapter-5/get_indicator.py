import pandas as pd
from pandas_datareader import wb

df = wb.get_indicators()[['id','name']]
df = df[df.name == 'Individuals using the Internet (% of population)']
print(df)
