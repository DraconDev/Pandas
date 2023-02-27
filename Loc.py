
import pandas as pd

df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
                  index=['cobra', 'viper', 'sidewinder'],
                  columns=['max_speed', 'shield'])

mydict = pd.DataFrame([{'a': 1, 'b': 2, 'c': 3, 'd': 4},
                       {'a': 100, 'b': 200, 'c': 300, 'd': 400},
                       {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000}])

# test = df.loc['viper', 'shield']

# test = df.loc[:, ["max_speed", "shield"]]
# test = df.loc[:, "max_speed"]
# test = df.loc['cobra', ]
# test = mydict.loc[0]

test = df.loc[df['shield'] > 4]

print(test)
# print('\n')
print(df)
