import requests
from requests.exceptions import HTTPError

def short_report():
    write_doc = open("lands_list.txt")
    error_array = []
    for line in write_doc:
        line = line.rstrip('\n')
        try:
            response = requests.get(line)
            if response.status_code > 200:
                error_array.append("\U0000274C" + str(response.status_code) + ' ' + line)
        except HTTPError as http_err:
            error_array.append(str(http_err))
        except Exception as err:
            error_array.append(str(err))
    return ('\n'.join(error_array))

def parsing1():
    write_doc = open("lands_list.txt")
    array_normal = []
    array_errors = []
    for line in write_doc:
        line = line.rstrip('\n')
        try:
            response = requests.get(line)
            if response.status_code == 200:
                array_normal.append("\U00002705" + str(response.status_code) + ' ' + line)
            elif response.status_code > 200:
                array_errors.append("\U0000274C" + str(response.status_code) + ' ' + line)
        except HTTPError as http_err:
            array_errors.append(str(http_err))
        except Exception as err:
            array_errors.append(str(err))
    return ("\n".join(array_normal + array_errors))