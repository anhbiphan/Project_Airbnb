import pandas as pd


df = pd.DataFrame([(0, 'True'),(1, 'False')], columns=('value', 'Boolean') )


df.to_csv('bool_table.csv', index=False)



