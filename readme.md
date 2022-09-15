# PI01_DATA03 -- Huarcaya Tacas Edward
### Flujo del proceso de limpieza y creacion de la API

<img src='./img/Flujo.png'> </br>

## URL-Video
https://youtu.be/IvJY9dhEp4g
## Objetivo
Extraer la data para su posterior limpieza y normalizacion, luego mandarlo a mysql y de ahi a una API para un uso a futuro.

## Limitaciones
* La herramienta **Heroku** me arroja algunos errores que por mas que busco no encuentro, por eso mi proyecto individual es una simulacion como si la API estuviera levantada y lista para su consumo.</br>
<img src='./img/Prueba.png'> </br>

## Herramientas usadas
* Pandas
* Numpy
* Mysql
* Peewee(ORM)
* FastApi
* Uvicorn

## Guia de directorios
1. **Datasets:** Datos originales
2. **Clean:** Noteboocks que utilice para limpiar la data
3. **CleanDataSets:** Datos limpiados y enviados a MySQL
4. **MySQL:** Script Mysql. *Util para la extraccion con peewee*
5. **ORM:** Extraccion de la data alojada en Mysql
6. **ConsumirAPI:** Desde aqui es donde hago el consumo de la API **(simulacion)** y resuelvo las preguntas 

## Archivo principal
> Method_get.py : Desde aqui es donde utilizamos el metodo GET para enviar la data

## Archivos otros
* Tanto **Procfile** como **requeriments.txt** fueron creados para que **Heroku** pueda desplegar la API

### Visualizacion de las realaciones SQL
<img src='./img/ER.png'> </br>

## Ejercicios
Los ejercicios a continuacion los resolvi con pandas y con sql(Solo para comprobar), la solucion en pandas se encuentra en la carpeta **ConsumirAPI** </br>
####  1. Año con mas carreras
```SQL
select round,Year from races order by Round desc limit 1;
-- 2021
```
####  2. Piloto con mayor cantidad de primeros puestos
```SQL
select DriverId, count(PositionOrder) as cantidad from (select * from results where PositionOrder=1) Tabla 
group by DriverId order by cantidad ;
select * from drivers where DriverID = 1;
--Lewis Hamilton
```
####  3. Nombre del circuito mas recorrido
```SQL
select CircuitId,Round from races order by Round desc limit 1; -- 24
select * from circuits where CircuitID=24;
--Yas Marina Circuit
```
####  4. Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad American o British
```SQL
select DriverId,sum(Points) as puntaje from results where ConstructorId 
in (SELECT ConstructorId FROM proyecti_henry.constructors where Nationality in('American','British')) group by DriverId
order by puntaje desc; -- 18
select * from drivers where DriverID=18
--Jenson Button
``` 