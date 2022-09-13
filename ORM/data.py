from ORM.model import *
def races():
    races = Races.select()
    data_races =[]
    for row in races.dicts():
        data_races.append(row)
    return data_races

def qualif():
    qualif = Qualifying.select()
    data_qualif =[]
    for row in qualif.dicts():
        data_qualif.append(row)
    return data_qualif

def circuits():
    circuits = Circuits.select()
    data_circuits =[]
    for row in circuits.dicts():
        data_circuits.append(row)
    return data_circuits

def results():
    results = Results.select()
    data_results =[]
    for row in results.dicts():
        data_results.append(row)
    return data_results

def constructors():
    constructors = Constructors.select()
    data_constructors =[]
    for row in constructors.dicts():
        data_constructors.append(row)
    return data_constructors

def drivers():
    drivers = Drivers.select()
    data_drivers =[]
    for row in drivers.dicts():
        data_drivers.append(row)
    return data_drivers

def lapTimes():
    lapTimes = LapTimes.select()
    data_lapTimes =[]
    for row in lapTimes.dicts():
        data_lapTimes.append(row)
    return data_lapTimes

def pitStops():
    pitStops = PitStops.select()
    data_pitStops =[]
    for row in pitStops.dicts():
        data_pitStops.append(row)
    return data_pitStops