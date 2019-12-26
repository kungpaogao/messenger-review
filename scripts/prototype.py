import pandas as pd

# ask for file name
infile = input('Path to input file (including file extension): ')
outfile = input('Name of output file (excluding file extension): ') + '.csv'
limit_pre = input('Dataset size (default: 100000): ')
limit = int(limit_pre) if limit_pre else 100000

dataframe = pd.read_json(infile)

print(dataframe)
print(len(dataframe.index))
