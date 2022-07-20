# To load a file (numpy, pandas, etc...) from a Github Repo
def get(url='', pickle=False, isdict=False):
    file = None
    
    pd_read = {'.xlsx':pd.read_excel, 
                '.json':pd.read_json,
                '.sql':pd.read_sql_query, 
                '.html':pd.read_html}
    
    if url.endswith('.npy'):
        import numpy as np
        import requests
        import io
        
        response = requests.get(url+'?raw=true')
        response.raise_for_status()
        bytesIO_obj = io.BytesIO(response.content)
        
        file = np.load(bytesIO_obj, allow_pickle = pickle)
        
        if isdict:
            file = np_file.item()
    
    elif any(map(url.endswith, pd_read)):
        print('Each pandas-file case to be coded later InshaAllah'+
              '\nReturning None for now...')
        pass
    
    return file
