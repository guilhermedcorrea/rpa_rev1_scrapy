from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import os
from pathlib import Path
from urllib import parse
from dotenv import load_dotenv
from os import path


load_dotenv()


"""Produção"""
sqlserveruserproducao = os.getenv('myboxmsqluser')
sqlserverpasswordproducao = os.getenv('myboxmsqlpassword')
sqlserverdatabaseproducao = os.getenv('myboxmsqldatabase')
sqlserverhostproducao = os.getenv('myboxmmsqlhost')

"""Testes"""
sqlserverusertestes = os.getenv('sqlserveruser')
sqlserverpasswordtestes = os.getenv('sqlserverpassword')
sqlserverdatabasetestes = os.getenv('sqlserverdatabase')
sqlserverhosttestes = os.getenv('sqlserverhost')



def sqlserver_get_conn_database_testes():

    connection_url = URL.create(
            "mssql+pyodbc",
            username=f"{sqlserverusertestes}",
            password=f"{sqlserverpasswordtestes}",
            host=f"{sqlserverhosttestes}",
            database=f"{sqlserverdatabasetestes}",
            query={
                "driver": "ODBC Driver 17 for SQL Server",
                "autocommit": "True",
        },
        )
      
    engine = create_engine(connection_url).execution_options(
    isolation_level="AUTOCOMMIT", future=True,fast_executemany=True)
    return engine


def sqlserver_get_conn_database_producao():

    connection_url = URL.create(
            "mssql+pyodbc",
            username=f"{user_mssql}",
            password=f"{password_mssql}",
            host=f"{host_mssql}",
            database=f"{database_mssql}",
            query={
                "driver": "ODBC Driver 17 for SQL Server",
                "autocommit": "True",
        }
        )
      
    engine = create_engine(connection_url).execution_options(
    isolation_level="AUTOCOMMIT", future=True,fast_executemany=True)
    return engine
