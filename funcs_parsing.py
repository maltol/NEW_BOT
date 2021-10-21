import requests
import pandas as pd

def short_report():
    write_doc = open("lands_list.txt")
    error_array = []
    for line in write_doc:
        response = requests.get(line)
        print(str(response.status_code) + ' ' + line)
        # if response.status_code > 200:
        #     error_array.append("\U0000274C" + str(response.status_code) + ' ' + line)
    return ("\r".join(error_array))

def parsing1():
    df = pd.read_excel('lands.xlsx')
    pd.set_option('display.max_rows', None)
    array_normal = []
    array_errors = []
    for index, websites in df.iterrows():
        try:
            response = requests.get(websites["Name"])
            df.at[index, 'status_code'] = "{}".format(response.status_code)
            if response.status_code == 200:
                array_normal.append("\U00002705""{}".format(response.status_code) + ' ' + websites["Name"])
            elif response.status_code > 200:
                array_errors.append("\U0000274C""{}".format(response.status_code) + ' ' + websites["Name"])
        except requests.ConnectionError:
            pass
    return ("\n".join(array_normal + array_errors))