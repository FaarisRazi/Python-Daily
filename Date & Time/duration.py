import datetime, time, pandas as pd

# Convert duration (eg; '10:30') to seconds, and vice versa
def duration(x):
    # Examples for seconds-to-duration and duration-to-seconds:
    # duration_seconds(1234)    = 0:20:34
    # duration_seconds("12:34") = 754
    
    val_err = ValueError(f'Invalid {type(x)} input, only numbers or'+
                          '\nduration-types ("1:23:4" / "0:27" / etc) allowed.')
    if isinstance(x, str):
        if x.replace('.','').isdigit():
            x = float(x)

        elif ':' in x: # Section for duration-to-seconds 
            sep_time = x.split(':')
            freqs = len(sep_time)
            tform = '%H:%M:%S'
            
            if freqs == sum(map(lambda x: x.isdigit(), sep_time)) and freqs < 4:
                if freqs-1 == 1:
                    tform = '%M:%S'
            else:
                raise val_err
            	
            pt = datetime.datetime.strptime(x,tform)

            return pt.second + pt.minute*60 + pt.hour*3600

        else:
            raise val_err

    return str(datetime.timedelta(seconds=x)) # Seconds-to-duration


# Check if pandas-Timestamp is between two Timestamps
def pd_isbetween(dt_main, dt_range = ()):
    # dt_range = tuple containing two pd-Timestamps.
    # dt_main = The main pd-Timestamp to be checked.
    # Example:
    # t1 = pd.to_datetime('Jan thursday 2015 04:00')
    # t2 = pd.to_datetime('Jan/1/2015 03:30')
    # t3 = pd.to_datetime('2015-Feb-20 05:45')
    # pd_isbetween(t1, (t2,t3)) = True

    start_dt, end_dt = min(dt_range), max(dt_range)

    if start_dt <= dt_main <= end_dt:
        return True
    return False
