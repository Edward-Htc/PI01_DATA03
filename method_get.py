from fastapi import FastAPI
from ORM.data import *

app = FastAPI()

@app.on_event("startup")
def startup():
    database.connect()

@app.on_event("shutdown")
def shutdown():
    if not database.is_closed():
        database.close()

@app.get("/")
async def getMain():
    return ['/race','/qualifying','/circuits','/results','/constructors','/drivers','/lapTimes','/pitStops']

@app.get('/{tabla}')
async def getData(tabla:str):

        if tabla == 'race':
            return races()
        elif tabla == 'qualifying':
            return qualif()
        elif tabla == 'circuits':
            return circuits()
        elif tabla == 'results':
            return results()
        elif tabla == 'constructors':
            return constructors()
        elif tabla == 'drivers':
            return drivers()
        elif tabla == 'lapTimes':
            return lapTimes()
        elif tabla == 'pitStops':
            return pitStops()
    