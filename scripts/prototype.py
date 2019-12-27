import pandas as pd
import datetime
from string import Template

PRINT_DEBUG = True


def print_debug(val):
    if PRINT_DEBUG:
        print(val)


# ask for file name
# infile = input('Path to input file (no file extension): ') + '.json'
infile = "data/msg.json"

data = pd.read_json(infile)

print_debug(len(data.index))
print_debug(data.columns)
sender_list = list(data["sender_name"])
sender_set = set(sender_list)
sender_dict = {}

for s in sender_set:
    sender_dict[s] = sender_list.count(s)

print_debug(sender_dict)

df = pd.DataFrame(data=data, columns=["timestamp_ms", "sender_name"])
print_debug(df)

print_debug(">>> filter")

df_list = []
for s in sender_set:
    sdf = df[df.sender_name == s]
    sdf.loc[:, "count"] = 1
    sdf.set_index("timestamp_ms", inplace=True)
    initials = "".join([name[0] for name in s.split(" ")])
    sdf = sdf.resample("D").agg(
        {"count": sum, "sender_name": (lambda _: initials)})
    df_list.append(sdf)

out = Template("out/out$ind.csv")
for i, d in enumerate(df_list):
    d.to_csv(out.substitute(ind=i), index=True, sep=",")

print("end")
