# Week 10: Pandas

import pandas as pd

data = {
    "SlotID": [101, 102, 103],
    "Type": ["EV", "Regular", "EV"],
    "Status": ["Free", "Occupied", "Occupied"]
}

df = pd.DataFrame(data)
print(df.groupby("Type").count())