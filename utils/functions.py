import json
import requests

def consume_api(end_point:str,method:str, api_url:str,auth=False, recive_file=False, headers = {}, files = None,body:dict = {},type_resp = "json")->dict | None :
    """Consume an API and returns the content as a dictionary or saves it to a file

    Args:
        body (dict): body of the request
        end_point (str): end_point
        method (str): get,post,put,delete,put,patch
        api_url (str): host url
        auth (bool, optional): bearer token. Defaults to False.
        recive_file (bool, optional): if recives a file is the rute for save it. Defaults to False.
        headers (dict, optional): headers. Defaults to {}.

    Returns:
        dict | None: if is a file return none
    """         
    if auth:
        headers["Authorization"] = auth
    response = requests.request(method, api_url+end_point, headers=headers, data=body, files=files)
    
    if recive_file and response.status_code == 200:
        with open(recive_file, "wb") as file:
            file.write(response.content)
    if type_resp == "json":
        return response.json()
    return response.text