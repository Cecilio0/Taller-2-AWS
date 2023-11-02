# Para lambda
# python3 -m venv venv
# source venv/bin/activate
# pip3 install -r requirements.txt
# 1. pip3 install -t dependencies -r requirements.txt
# 2. (cd dependencies; zip ../aws_lambda_artifact.zip -r .)
# 3. zip aws_lambda_artifact.zip -u main.py
from mangum import Mangum
from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
import psycopg2
import boto3

s3 = boto3.client('s3',
                  aws_access_key_id='',
                  aws_secret_access_key='')
 
bucket_name = ""
       
conn = psycopg2.connect(database = "",
                        user = "postgres",
                        host= '',
                        password = "",
                        port = 5432)

app=FastAPI()
handler=Mangum(app)

class Blanket(BaseModel):
    id: int
    type: str
    widthCM: int
    heightCM: int
    

@app.post("/rds/save")
async def saveBlanket(blanket: Blanket):
    cur = conn.cursor()
    cur.execute("INSERT INTO blankets (id, type, widthCM, heightCM) VALUES (%s, %s, %s, %s)", (blanket.id, blanket.type, blanket.widthCM, blanket.heightCM))
    conn.commit()
    cur.close()
    conn.close()
    return {"status": "ok"}

@app.get("/rds/get")
async def getBlankets():
    cur = conn.cursor()
    cur.execute("SELECT * FROM blankets")
    rows = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return rows

@app.post("/s3/save")
async def saveBlanket(file: UploadFile):
    s3.put_object(Bucket=bucket_name, Key=f"{file.filename}", Body=file.file.read())
    return {"status": "ok"}

@app.get("/s3/get")
async def getBlankets():
    response = s3.list_objects_v2(Bucket=bucket_name)
    return {'Length': len(response['Contents'])}

@app.get("/rds/getFilter")
async def getBlanketsFilter(type: str | None = None, widthCM: int | None = None, heightCM: int | None = None):
    queryString = "SELECT * FROM blankets"
    
    if type != None or widthCM != None or heightCM != None:
        queryBefore = False
        queryString += " WHERE "
        if type != None:
            queryString += f"type = '{type}'"
            queryBefore = True
        if widthCM != None:
            if queryBefore:
                queryString += "AND "
            queryString += f"widthcm = {widthCM}"
            queryBefore = True
        if heightCM != None:
            if queryBefore:
                queryString += "AND "
            queryString += f"heightcm = {heightCM}"
            queryBefore = True
    cur = conn.cursor()
    cur.execute(queryString)
    rows = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    if rows == ():
        return rows
    else: 
        return {"message": "No se encontro ningun elemento"}
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0" , port=8000)