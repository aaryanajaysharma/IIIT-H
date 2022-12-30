import subprocess as sp
import pymysql
import pymysql.cursors


def insertFeedback():
    try:
        row = {}
        print("Enter a new feedback: ")
        row["title"] = input("title: ")
        row["accountId"] = input("accountId: ")
        row["comment"] = input("comment: ")

        query = "INSERT INTO FEEDBACK(title, accountID, comment) VALUES('%s', '%s', '%s')" % (
            row["title"], row["accountId"], row["comment"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def deleteStockFromWatchlist():
    try:
        row = {}
        print("Delete A particular from the watchlist: ")
        row["serialNo"] = input("serialNo: ")
        row["accountId"] = input("accountId: ")

        query = "DELETE FROM watchlist WHERE serialNo = '%s' AND accountId = '%s' " % (
                row["serialNo"], row["accountId"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Deleted From Database")

    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)

    return


def updateCurrentPrice():
    try:
        row = {}
        print("update current price of a particular stock : ")
        row["securityCode"] = input("securityCode: ")
        row["newCurrentPrice"] =  float(input("newCurrentPrice: "))

        query = "UPDATE stock SET currentPrice = %f WHERE securityCode = '%s' " % (
            row["newCurrentPrice"], row["securityCode"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Updated Database")

    except Exception as e:
        con.rollback()
        print("Failed to update the database")
        print(">>>>>>>>>>>>>", e)

    return
# pprint for json pretty print
def retrieveAllStocks():
    try:
        row = {}
        print("retrieve all stocks: ")

        query = "SELECT * FROM stock" 
        print(query)
        cur.execute(query)
        record = cur.fetchall()
        print(record)

        print("operation performed")

    except Exception as e:
        con.rollback()
        print("Failed to do the operation")
        print(">>>>>>>>>>>>>", e)

    return


def retrieveMarketCapWithPurchaseMonth():
    try:
        row = {}
        print("retrieve market value given purchase month: ")
        row["month"] = input("month: ")

        query = "SELECT currentPrice FROM Transactions WHERE purchaseTime LIKE '%s'" %(row["month"])
        print(query)
        cur.execute(query)
        record = cur.fetchall()
        print(record)
        con.commit()

        print("operation performed")

    except Exception as e:
        con.rollback()
        print("Failed to do the operation")
        print(">>>>>>>>>>>>>", e)

    return

def usernameStartsWithA():
    try:
        row = {}
        print("retrieve username starting with A: ")

        query = "SELECT username FROM users WHERE username LIKE 'A%'"
        print(query)
        cur.execute(query)
        con.commit()

        print("operation performed")

    except Exception as e:
        con.rollback()
        print("Failed to do the operation")
        print(">>>>>>>>>>>>>", e)

    return

def getTransactionWithMaxPurchasePrice():
    try:
        row = {}
        print("retrieve transaction with max purchase price: ")

        query = "SELECT * FROM Transactions WHERE purchasePrice = (SELECT MAX(purchasePrice) FROM Transactions)"
        print(query)
        cur.execute(query)
        record = cur.fetchall()
        print()
        con.commit()

        print("operation performed")

    except Exception as e:
        con.rollback()
        print("Failed to do the operation")
        print(">>>>>>>>>>>>>", e)

    return

def whichStockBetter():
    try:
        row = {}
        print("retrieve stock with min stockPE: ")

        query = "SELECT * FROM stock ORDER BY stockPE LIMIT 1"
        print(query)
        cur.execute(query)
        record = cur.fetchall()
        print(record)
        
        print("operation performed")

    except Exception as e:
        con.rollback()
        print("Failed to do the operation")
        print(">>>>>>>>>>>>>", e)

    return

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        insertFeedback()
    elif(ch == 2):
        deleteStockFromWatchlist()
    elif(ch == 3):
        updateCurrentPrice()
    elif(ch == 4):
        retrieveAllStocks()
    elif(ch == 5):
        retrieveMarketValueWithPurchaseMonth()
    elif(ch == 6):
        usernameStartsWithA()
    elif(ch == 7):
        getTransactionWithMaxPurchasePrice()
    elif(ch == 8):
        whichStockBetter()
    else:
        print("Error: Invalid Option")


while(1):
    tmp = sp.call('clear', shell=True)
    
    username = input("Username: ")
    password = input("Password: ")

    try:
        con = pymysql.connect(host='localhost',
                              port=3306,
                              user=username,
                              password=password,
                              db='Project',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)

                print("1. Insert Feedback")  
                print("2. Delete a stock from watchlist")  
                print("3. Update current price of a stock")
                print("4. Retrieve stock with a particular stockType")
                print("5. Retrieve market value of stocks purchased in a particular month")
                print("6. Retrieve username starting with A")
                print("7. Retrieve transaction with max purchase price")
                print("8. Retrieve stock with min stockPE")
                print("9. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 9:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")