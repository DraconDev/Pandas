import pandas as pd

df = pd.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]],
                  index=[4, 5, 6], columns=['A', 'B', 'C'])

test = df.at[4, 'B']

print(test)
print('\n')
print(df)
