import datetime, pandas as pd


# See example-file from >  Alhumdulillah/Prayers.ipynb
def time_diff(time_col, strf, until_next = True, dur=True):
    # strf = '%I:%M %p' (like "2:30 PM").
    # "until_next" format to show "duration" of one time-index until the next (per row).
    
    time_df = pd.to_datetime(time_col, format=strf)
    time_df = time_df.diff().fillna(pd.Timedelta(seconds=0))
    
    if until_next:
        time_f = time_df.iloc[::-time_df.shape[0] + 1].diff()[-1] # Time difference between the last and first rows.
        time_df = np.append(time_df[1:].values, time_f) # Re-adjust DF to show durations in "until next" row format.
    
    if dur:
        time_df = time_df.apply(lambda x: str(x).split()[-1])
        
    return time_df


#--------- Number to time, i.e. hours/days/months etc.
def dt_obj(s=0,m=0,h=0,d=0,w=0, mon=0, y=0): 
    dtref = dict(seconds=s,minutes=m,hours=h,days=d,
                 weeks=w,months=mon,years=y)
    non0_params = {k:v for k,v in dtref.items() if v > 0}
    
    return datetime.timedelta(**non0_params)


# -------- Adding date-times example:
main_date_str = pd.to_datetime('Nov 15 2022').strftime("%d-%b-%Y")

main_date = datetime.datetime.strptime(main_date_str, "%d-%b-%Y")

add_t = 8
next_date = (main_date + dt_obj(w=add_t)).strftime("%d-%b-%Y")

print(f'The date {main_date_str}, after {add_t} weeks is: {next_date}\n')
