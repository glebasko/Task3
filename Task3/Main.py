import sys
import DatabaseModule as dbModule

databaseName = "mydb"
user = "root"
password = "admin."

tableName = "customers"
try:
    db = dbModule.connectToMySQL(user, password);

    dbModule.createDatabase(db, databaseName)
    db = dbModule.connectToDatabase(databaseName, user, password)

    tableExists = dbModule.doesTableExist(db, tableName)

    if (tableExists == False):
        dbModule.createTable(db, tableName)

    dbModule.insertCustomer(db)

    dbModule.deleteCustomer(db, 1)
    dbModule.deleteAllCustomer(db)

    dbModule.dropTable(db, tableName)
    dbModule.dropDatabase(db, databaseName)
except:
    print("Error: ", sys.exc_info())