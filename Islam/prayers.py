# Prayer times from KhaleejTimes (since I'm in the UAE)

import urllib.request as ur, pandas as pd, numpy as np, os
from html_table_parser import HTMLTableParser
from datetime import datetime

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
today = datetime.today()#.strftime('%d-%m-%Y')
month_now = today.strftime('%B')

folder = 'Islam'
prayers_file = [i for i in os.listdir(folder) if '_prayers_' in i]
file_comment = f'New month - {month_now} Prayer-times loaded.'

#prayers_file = []
if prayers_file:
    prayers_file = prayers_file[0]
    file_path = folder+'/'+prayers_file
    
    # If the file is NOT based on the current month's prayer times
    if not prayers_file.endswith(month_now+'.npy'):
        os.remove(file_path) # Remove the "previous month" file.
        prayers_df = khaleej_prayers(month_now) # New month's file (also saved).
        print(file_comment + ' (and saved)')
    else:
        prayers_df = khaleej_prayers(file_path) # Load the saved file.
        print(file_comment.replace('New month','File'))
else:
    prayers_df = khaleej_prayers(month_now)
    print(file_comment + ' (and saved)')
