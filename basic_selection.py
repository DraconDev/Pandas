import pandas as pd

mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
          {'a': 100, 'b': 200, 'c': 300, 'd': 400},
          {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000}]

df = pd.DataFrame(mydict)


# test = df.tail(2)
# test = df.head(1)

# test = df[:1]
# test = df.describe()

# Transpose
# test = df.T
# test = df.T[0]

# Identical
# test = df['a']
# test = df.a


test = df[:]

print(test)
print('\n')
print(df)
