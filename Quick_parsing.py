import requests

def short_report():
    file1 = open("C:\\Users\\user\\Desktop\\autotests\\lnd.txt", "r")
    error_array = []
    for line in file1:
        response = requests.get(line)
        if response.status_code > 200:
            error_array.append("\U0000274C" + str(response.status_code) + ' ' + line)
        if Exception:
            pass
        if not line:
            break
    return ("\r".join(error_array))