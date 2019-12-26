import pandas as pd
from string import Template

PRINT_DEBUG = False


def print_debug(val):
    if PRINT_DEBUG:
        print(val)


# ask for file name
# infile = input('Path to input file (no file extension): ') + '.json'
infile = "data/msg.json"

df = pd.read_json(infile)

# print(dataframe)
print_debug(len(df.index))
print_debug(df.columns)
# print(list(df["sender_name"]))
sender_list = list(df["sender_name"])
sender_set = set(sender_list)
sender_dict = {}

for s in sender_set:
    sender_dict[s] = sender_list.count(s)

print_debug(sender_dict)

ts_df = pd.DataFrame(data=df, columns=["timestamp_ms", "sender_name"])
print_debug(ts_df)

print_debug(">>> filter")

df_list = []
for s in sender_set:
    sdf = ts_df[ts_df.sender_name == s]
    df_list.append(sdf)

out = Template("out/out$ind.csv")
for i, d in enumerate(df_list):
    d.to_csv(out.substitute(ind=i), index=False, sep=",")

print("end")
