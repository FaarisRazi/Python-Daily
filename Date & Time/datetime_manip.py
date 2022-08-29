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
