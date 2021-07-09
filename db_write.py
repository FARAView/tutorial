import pandas as pd
import datetime
from sqlalchemy import create_engine

df = pd.read_csv("./unzipped/exhibition_schedule.csv", encoding='utf-8')
df = df.where(pd.notnull(df), None)  # replace all nan values to None
del df['Unnamed: 6']
del df['Unnamed: 7']
del df['Unnamed: 8']
del df['Unnamed: 9']

del df['Unnamed: 6']
del df['Unnamed: 7']
del df['Unnamed: 8']
del df['Unnamed: 9']

# write df on db
from conn import username, password, host, port, database
engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')
df.to_sql(name='exhibition_schedule_sy', con=engine, index=False, if_exists='replace')

if __name__ == "__main__":
    pass
