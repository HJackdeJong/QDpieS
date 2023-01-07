import os
import pandas as pd
import json

def load_data(path, identity='.json'):
    """
    load all matched files in one folder and concat them together.
    """
    files = os.listdir(path)
    df = pd.DataFrame()
    for file in files[:]:
        if identity in file:
            data = json.load(open(path + file)) 
            temp_df = pd.DataFrame(data)
            df = pd.concat([df, temp_df])
    return df

PATH = "C:\\Users\\kalel\\OneDrive\\Desktop\\"  # write your PATH there
df = load_data(PATH, identity='.json')

# convert int to datetime
df.loc[:,"TIMESTAMP"]=pd.to_datetime(df['TIMESTAMP'], unit='ms')
# sort by the timestamp
df.sort_values('TIMESTAMP', inplace=True)
df.head()