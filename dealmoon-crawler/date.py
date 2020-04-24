import numpy as np
import pandas as pd
import datetime

tod = datetime.datetime.now()

store = 'zara'
filename = store+"-promotion.xlsx"
df = pd.read_excel(filename)

day = []
for i in range(df.shape[0]):
    s = [int (s) for s in df['date'][i].split() if s.isdigit()]
    d = datetime.timedelta(days=s[0])
    a = tod - d
    day.append(a.date())

output = pd.concat([df, pd.DataFrame(day)], axis=1)
output.columns = ['date', 'information', 'day']

new_filename = store+".xlsx"
output.to_excel(new_filename, index=None)
