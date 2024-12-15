from fastapi import FastAPI, Form, File, UploadFile, HTTPException
from utils.functions import consume_api
# import httpx

VT_URL =  "https://www.virustotal.com/api/v3"


app = FastAPI()

@app.get("/")
async def main():
    return {"message":"runing ok ..."}



@app.post("/scan_file")
async def scan_file(apikey:str = Form(...), file:UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=422, detail="No file sent for scanning.")
    headers = {
            "X-Apikey": apikey,
            "accept": "application/json",
        }
    try:
        file_content = await file.read()
        file_info = (file.filename,file_content,file.content_type)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Imposible scan the file")
    vt_response = consume_api(end_point="/files", method="post",api_url=VT_URL, headers=headers, files={"file":file_info})
    if not vt_response.get("data"):
        raise HTTPException(status_code=500, detail="An error ocurred with the service")
    del headers["accept"]
    scan_data = consume_api(end_point=f"", method="get", api_url=vt_response["data"]["links"]["self"], headers=headers)
    if not scan_data.get("data"):
        raise HTTPException(status_code=500, detail="An error ocurred with the service")
    return scan_data["data"]