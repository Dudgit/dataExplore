# !curl "https://nwis.waterdata.usgs.gov/nwis/uv/?parameterCd=00060,00065&format=rdb&site_no=01321000&period=&begin_date=20100101&end_date=20191231&siteStatus=all" > data.csv"

import pandas as pd

# The names of columns I'm going to load
names = ["Date","time_zone",'discharge',"gage_height"]

# Loading the data
df = pd.read_csv("data.csv",skiprows=32,delimiter='\t',names=names,usecols=[2,3,4,6])

def lookup(date_pd_series, format=None):
    """
    Function I found in Stackoverflow
    It seems much faster than converting normally
    This is an extremely fast approach to datetime parsing.
    For large data, the same dates are often repeated. Rather than
    re-parse these, we store all unique dates, parse them, and
    use a lookup to convert all dates.
    """
    dates = {date:pd.to_datetime(date, format=format) for date in date_pd_series.unique()}
    return date_pd_series.map(dates)
# Get rid of missing data
df.dropna(axis=0,inplace=True)

#Converting date format into pandas datetime
df['Date'] = lookup(df['Date'])