import pyodbc

cnxn = pyodbc.connect(r'Driver=SQL Server;Server=.\SQLEXPRESS;Database=AdventureWorks2019;Trusted_Connection=yes;')
cursor = cnxn.cursor()

