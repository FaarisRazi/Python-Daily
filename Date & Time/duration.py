import datetime, time

# Convert duration (eg; '10:30') to seconds, and vice versa
def duration_seconds(x):
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
