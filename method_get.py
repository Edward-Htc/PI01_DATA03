from fastapi import FastAPI
from ORM.model import *

races = Races.select()
data_races =[]
for row in races.dicts():
    data_races.append(row)

qualif = Qualifying.select()
data_qualif =[]
for row in qualif.dicts():
    data_qualif.append(row)

circuits = Circuits.select()
data_circuits =[]
for row in circuits.dicts():
    data_circuits.append(row)

results = Results.select()
data_results =[]
for row in results.dicts():
    data_results.append(row)

constructors = Constructors.select()
data_constructors =[]
for row in constructors.dicts():
    data_constructors.append(row)

app = FastAPI()

@app.get("/race")
async def getRace():
    return data_races

@app.get("/qualifying")
async def getQualify():
    return data_qualif

@app.get("/circuits")
async def getCircuits():
    return data_circuits

@app.get("/results")
async def getResults():
    return data_results

@app.get("/constructors")
async def getConstructors():
    return data_constructors
