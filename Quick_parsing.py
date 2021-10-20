import requests

def short_report():
    write_doc = open("C:\\Users\\user\\Desktop\\autotests\\lnd.txt")
    error_array = []
    for line in write_doc:
        response = requests.get(line)
        if response.status_code > 200:
            error_array.append("\U0000274C" + str(response.status_code) + ' ' + line)
        if Exception:
            pass
        if not line:
            break
    return ("\r".join(error_array))