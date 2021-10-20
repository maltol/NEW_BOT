import requests
import pandas as pd

def short_report():
    df = pd.read_excel('C:\\Users\\user\\Desktop\\autotests\\lands.xlsx')
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    error_array = []
    for index, websites in df.iterrows():
        try:
            response = requests.get(websites["Name"])
            df.at[index, 'sts'] = "{}".format(response.status_code)
            if response.status_code > 200:
                error_array.append('\U0000274C' "{}".format(response.status_code) + ' ' + websites["Name"])
        except requests.ConnectionError:
            pass
    return "\n".join(error_array)