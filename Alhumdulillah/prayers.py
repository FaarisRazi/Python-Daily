import urllib.request as ur, pandas as pd, numpy as np, os
from html_table_parser import HTMLTableParser
import datetime

def webtables(url, headers=''):
    req = ur.Request(url=url,headers={'User-Agent': headers})
    f = ur.urlopen(req)
    xhtml = f.read().decode('utf-8')
    p = HTMLTableParser()
    p.feed(xhtml)
    
    return p.tables

def khaleej_prayers(name):
    # name = current month-name OR .npy file-name

    if name.endswith('.npy'): # if .npy file-name given, load this file.
        return np.load(name, allow_pickle=True).item()['df']
    
    # Else get (and save) a new prayers-table from KhaleejTimes:
    url = 'https://www.khaleejtimes.com/prayer-time-uae'
    uae_prayers_df = webtables(url, 'muslim-akhi')

    if len(uae_prayers_df) == 1:
        uae_prayers_df = uae_prayers_df[0]

    uae_prayers_df = pd.DataFrame(uae_prayers_df)
    uae_prayers_df.columns = uae_prayers_df.loc[0]
    uae_prayers_df = uae_prayers_df[1:].reset_index(drop=True)
    uae_prayers_df[name] = uae_prayers_df[name].astype(int)

    np.save(f'Islam/uae_prayers_{name}', 
            {'df':uae_prayers_df}, allow_pickle=True)
    
    return  uae_prayers_df

# ~~~~~~~~~~~~~~~~~~~~~~~~ Script ~~~~~~~~~~~~~~~~~~~~~~~~~~
today = datetime.datetime.today()#.strftime('%d-%m-%Y')
month_now = today.strftime('%B')

def prayersDF():
    folder = 'Islam'
    prayers_file = [i for i in os.listdir(folder) if '_prayers_' in i]
    file_comment = f'New month - {month_now} Prayer-times loaded.%s'

    #prayers_file = []
    if prayers_file:
        file_path = folder+'/'+prayers_file[0]

        # If the file is NOT based on the current month's prayer times
        if not file_path.endswith(month_now+'.npy'):
            os.remove(file_path) # Remove the "previous month" file.
        else:
            print(file_comment.replace('New month','File')%'')
            return khaleej_prayers(file_path) # Load the saved file.
    
    print(file_comment%' (and saved)')
    return khaleej_prayers(month_now)
        

# prayers_df = prayersDF() # Load our new/saved dataframe

# today_info = prayers_df[prayers_df[month_now] == today.day]
# today_prayers = today_info.T[4:].rename(columns={today_info.index[0]:'times'}).rename_axis('prayers')

# month_days_left = prayers_df.loc[today_info.index[0]:]

# days_left = month_days_left.shape[0]-1
# days_comment = '%d days left for '+month_now

# iqamah = {i:pd.Timedelta(minutes=j) if j else np.nan 
#           for i,j in zip(today_prayers.index, [20,0,15,15,2,15])}

# prayers_astime = pd.to_datetime(today_prayers.times, format='%I:%M %p')

# today_prayers['iqamah'] = prayers_astime.values + today_prayers.index.map(iqamah.get).values
# today_prayers['iqamah'] = today_prayers['iqamah'].dt.strftime('%I:%M %p')
