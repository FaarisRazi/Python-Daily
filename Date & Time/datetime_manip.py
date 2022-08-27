# Using Prayers.ipynb example, to be continued InshaAllah.
def time_diff(x, colname):
    
    df[colname] = df.diff().fillna(pd.Timedelta(seconds=0))
    #Or: diff().dt.seconds.fillna(0).apply(duration, 0) # duration() from my repo: Python-Daily/Date & Time/duration

#     today_prayers.loc[0, colname] = prayers_astime.iloc[::-5].diff()[-1]
#     today_prayers['until_next'] = today_prayers.until_next.apply(lambda x: str(x).split()[-1])
#     today_prayers['until_next'] = np.append(today_prayers.until_next[1:].values, 
#                                             today_prayers.loc['Fajr', 'until_next'])
#     today_prayers
