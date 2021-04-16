import pandas as pd
import datetime
from sqlalchemy import create_engine

df = pd.read_csv("./unzipped/FARA_All_Registrants.csv")
df = df.where(pd.notnull(df), None)  # replace all nan values to None


def format_datetime(date_str):
    if date_str:
        datetime_format = "%m/%d/%Y"
        datetime_obj = datetime.datetime.strptime(date_str, datetime_format)
        return datetime_obj
    else:
        return date_str


# convert date string to python default datetime obj
df["Registration Date"] = df["Registration Date"].apply(lambda x: format_datetime(x))
df["Termination Date"] = df["Termination Date"].apply(lambda x: format_datetime(x))

# clean-out first/end whitespaces
df["Zip"] = df["Zip"].apply(lambda x: x.strip() if x else x)
df["Address 2"] = df["Address 2"].apply(lambda x: x.strip() if x else x)

# write df on db
from conn import username, password, host, port, database
engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')
df.to_sql(name='registrants', con=engine, index=False, if_exists='replace')

if __name__ == "__main__":
    pass
