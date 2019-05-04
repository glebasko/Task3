import mysql.connector

def createTable(db, tableName):
    cursor = db.cursor()
    cursor.execute("CREATE TABLE " + tableName +
                   " (Id INT AUTO_INCREMENT PRIMARY KEY, FirstName VARCHAR(255), LastName VARCHAR(255))")

    print("Table '" + tableName + "'created\n")

def insertCustomer(db):
    cursor = db.cursor()

    sql = "INSERT INTO customers (FirstName, LastName) VALUES (%s, %s), (%s, %s), (%s, %s)"
    vals = (
        "Arnold", "Schwarzenegger",
        "Jean-Claude", "Van Damme",
        "Jason", "Statham")

    cursor.execute(sql, vals)
    db.commit()

    print(cursor.rowcount, "record inserted.\n")

def connectToDatabase(database, user, password):
    db = mysql.connector.connect(
        host="localhost",
        database=database,
        user=user,
        password=password
    )

    print("Connected to 'mydb' database\n")

    return db;

def doesTableExist(db, tableName):
    cursor = db.cursor()
    cursor.execute("SHOW TABLES LIKE '" + tableName + "'")

    result = cursor.fetchall()
    tableExists = result != []

    return tableExists

def deleteCustomer(db, customerId):
    sql = "DELETE FROM customers WHERE Id = " + str(customerId)

    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()

    print(cursor.rowcount, "record(s) deleted\n")

def deleteAllCustomer(db):
    sql = "DELETE FROM customers"

    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()

    print(cursor.rowcount, "record(s) deleted\n")

def dropTable(db, tableName):
    sql = "DROP TABLE " + tableName

    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()

    print("Table '" + tableName + "' was dropped\n")

def connectToMySQL(user, password):
    db = mysql.connector.connect(
        host="localhost",
        user=user,
        password=password
    )

    print("Connected to 'MySQL' server\n")

    return db;

def createDatabase(db, databaseName):
    cursor = db.cursor()

    cursor.execute("CREATE DATABASE " + databaseName)

    print("Database ", databaseName, " was created\n")

def dropDatabase(db, databaseName):
    cursor = db.cursor()

    cursor.execute("DROP DATABASE " + databaseName)

    print("Database '", databaseName, "' was dropped\n")