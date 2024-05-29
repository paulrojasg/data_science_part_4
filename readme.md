# PARTE #4 - PROJECTO DE INTRODUCCIÓN A LA CIENCIA DE DATOS

## PASOS PARA EJECUTAR

1. Clonar o descargas los archivos del proyecto.

2. Crear archivo config.yaml con las credenciales correspondientes a la OLTP y OLAP.

La plantilla del archivo se encuentra a continuación:

```
OperationalDB:
    Server: <server>
    Database: <database>
    Driver: <example: ODBC Driver 17 for SQL Server>
ETLDB:
    Type: <mssql/postgres>
    Server: <server-address>
    Database: <database-name>
    User: <database-user>
    Password: <database-password>
```

3. Crear ambiente virtual.
```
python -m venv venv
```
E instalar las dependencias:
```
pip install -r requirements.txt
```

4. Ejecutar proyecto con:
```
jupyter notebook
```

5. Ejecutar cada archivo. Se recomienda seguir el orden referido en order.txt
















































