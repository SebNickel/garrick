from datetime import datetime

time_format = '%Y-%m-%d %H:%M:%S'

def get_timestamp():
    return datetime.now().strftime(time_format)

def add_half_interval(last_viewed):

    last_viewed_datetime = datetime.strptime(last_viewed, time_format) 

    interval = datetime.now() - last_viewed_datetime
    
    half_interval = interval / 2

    new_last_viewed_datetime = last_viewed_datetime + half_interval

    new_last_viewed = new_last_viewed_datetime.strftime(time_format)

    return new_last_viewed
