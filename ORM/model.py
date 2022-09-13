from peewee import *

database = MySQLDatabase('proyecti_henry', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'port': 3306, 'user': 'root', 'password': '2398'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Circuits(BaseModel):
    alti = FloatField(column_name='Alti', null=True)
    circuit_id = AutoField(column_name='CircuitID')
    circuit_ref = CharField(column_name='CircuitRef', null=True)
    country = CharField(column_name='Country', null=True)
    lat = FloatField(column_name='Lat', null=True)
    lng = FloatField(column_name='Lng', null=True)
    location = CharField(column_name='Location', null=True)
    name = CharField(column_name='Name', null=True)
    url = CharField(column_name='Url', null=True)

    class Meta:
        table_name = 'circuits'

class Constructors(BaseModel):
    constructor_id = AutoField(column_name='ConstructorId')
    constructor_ref = CharField(column_name='ConstructorRef', null=True)
    name = CharField(column_name='Name', null=True)
    nationality = CharField(column_name='Nationality', null=True)
    url = CharField(column_name='Url', null=True)

    class Meta:
        table_name = 'constructors'

class Drivers(BaseModel):
    code = CharField(column_name='Code', null=True)
    dob = CharField(column_name='Dob', null=True)
    driver_id = AutoField(column_name='DriverID')
    driver_ref = CharField(column_name='DriverRef', null=True)
    forename = CharField(column_name='Forename', null=True)
    nationality = CharField(column_name='Nationality', null=True)
    number = CharField(column_name='Number', null=True)
    surname = CharField(column_name='Surname', null=True)
    url = CharField(column_name='Url', null=True)

    class Meta:
        table_name = 'drivers'

class Races(BaseModel):
    circuit = ForeignKeyField(column_name='CircuitId', field='circuit_id', model=Circuits, null=True)#
    date = CharField(column_name='Date', null=True)#
    name = CharField(column_name='Name', null=True)#
    race_id = AutoField(column_name='RaceId')#
    round = IntegerField(column_name='Round', null=True)#
    time = CharField(column_name='Time', null=True)#
    url = CharField(column_name='Url', null=True)#
    year = IntegerField(column_name='Year', null=True)#

    class Meta:
        table_name = 'races'

class LapTimes(BaseModel):
    driver = ForeignKeyField(column_name='driverId', field='driver_id', model=Drivers, null=True)
    lap = IntegerField(column_name='lap', null=True)
    milliseconds = IntegerField(column_name='milliseconds', null=True)
    position = IntegerField(column_name='position', null=True)
    race = ForeignKeyField(column_name='raceId', field='race_id', model=Races, null=True)
    time = IntegerField(column_name='time', null=True)

    class Meta:
        table_name = 'lap_times'
        primary_key = False

class PitStops(BaseModel):
    driver = ForeignKeyField(column_name='DriverId', field='driver_id', model=Drivers, null=True)
    lap = IntegerField(column_name='Lap', null=True)
    miliseconds = IntegerField(column_name='Miliseconds', null=True)
    race = ForeignKeyField(column_name='RaceId', field='race_id', model=Races)
    stop = IntegerField(column_name='Stop', null=True)
    time = CharField(column_name='Time', null=True)

    class Meta:
        table_name = 'pit_stops'
        primary_key = False

class Qualifying(BaseModel):
    constructor = ForeignKeyField(column_name='ConstructorId', field='constructor_id', model=Constructors, null=True)
    driver = ForeignKeyField(column_name='DriverId', field='driver_id', model=Drivers, null=True)
    num = IntegerField(column_name='Num', null=True)
    position = IntegerField(column_name='Position', null=True)
    q1 = CharField(column_name='Q1', null=True)
    q2 = CharField(column_name='Q2', null=True)
    q3 = CharField(column_name='Q3', null=True)
    qualify_id = AutoField(column_name='QualifyId')
    race = ForeignKeyField(column_name='RaceId', field='race_id', model=Races, null=True)

    class Meta:
        table_name = 'qualifying'

class Results(BaseModel):
    constructor = ForeignKeyField(column_name='ConstructorId', field='constructor_id', model=Constructors, null=True)
    driver = ForeignKeyField(column_name='DriverId', field='driver_id', model=Drivers, null=True)
    fastest_lap = IntegerField(column_name='FastestLap', null=True)
    fastest_lap_speed = FloatField(column_name='FastestLapSpeed', null=True)
    fastest_lap_time = CharField(column_name='FastestLapTime', null=True)
    grid = IntegerField(column_name='Grid', null=True)
    laps = IntegerField(column_name='Laps', null=True)
    miliseconds = IntegerField(column_name='Miliseconds', null=True)
    number = IntegerField(column_name='Number', null=True)
    points = FloatField(column_name='Points', null=True)
    position = IntegerField(column_name='Position', null=True)
    position_order = IntegerField(column_name='PositionOrder', null=True)
    position_text = CharField(column_name='PositionText', null=True)
    race = ForeignKeyField(column_name='RaceId', field='race_id', model=Races, null=True)
    ranked = IntegerField(column_name='Ranked', null=True)
    result_id = AutoField(column_name='ResultId')
    status_id = IntegerField(column_name='StatusId', null=True)
    times = CharField(column_name='Times', null=True)

    class Meta:
        table_name = 'results'

