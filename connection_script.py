import pyodbc
import yaml
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

def connect_databases():
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)
        
        config_op = config['OperationalDB']
        server=config_op['Server']
        database=config_op['Database']
        driver=config_op['Driver']
        conn_op=f'mssql://@{server}/{database}?driver={driver}&trusted_connection=yes;'
        engine_op = create_engine(conn_op)
        db_op = engine_op.connect()
        
        
        config_etl = config['ETLDB']
        server=config_etl['Server']
        database=config_etl['Database']
        if config_etl['Type'] == 'mssql':
            driver=config_etl['Driver']
            conn_etl=f'mssql://@{server}/{database}?driver={driver}&trusted_connection=yes;'
        elif config_etl['Type'] == 'postgresql':
            user=config_etl['User']
            password=config_etl['Password']
            conn_etl=f'postgresql+psycopg2://{user}:{password}@{server}:5432/{database}'
        else:
            raise Exception('No valid target database')
        engine_etl = create_engine(conn_etl)
        db_etl = engine_etl.connect()

        return db_op, db_etl

    return None