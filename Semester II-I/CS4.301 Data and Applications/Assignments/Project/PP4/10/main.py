import subprocess as sp
import pymysql
import pymysql.cursors

from urllib import request
response = request.urlopen("https://jsonplaceholder.typicode.com/users")
json_response = response.read()
import json
users = json.loads(json_response)

from pprint import pprint;
from tabulate import tabulate;

def toList(data):
    res = []
    for idx, sub in enumerate(data, start = 0):
        if idx == 0:
            res.append(list(sub.keys()))
            res.append(list(sub.values()))
        else:
            res.append(list(sub.values()))
    return res
    

#done
def insertFeedback():
    try:
        row = {}
        print("Enter a new feedback: ")
        row["title"] = input("Title: ")
        row["accountId"] = input("Account Id: ")
        row["comment"] = input("Comment: ")

        #error handling
        if len(row["comment"])>500 :
            print("Comment too long")
            return
        if len(row["title"])>40 :
            print("Title too long")
            return
        if len(row["accountId"])!=6 :
            print("Invalid accountId")
            return

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

#done
def deleteStockFromWatchlist():
    try:
        row = {}
        print("Delete a particular record from the watchlist(respecting foreign key constraints): ")
        row["serialNo"] = input("Serial No: ")
        row["accountId"] = input("Account Id: ")

        #error handling
        if len(row["accountId"])!=6 :
            print("Invalid AccountId")
            return

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

#done
def updateCurrentPrice():
    try:
        row = {}
        print("Update current price of a particular stock: ")
        row["securityCode"] = input("Security Code: ")
        row["newCurrentPrice"] =  float(input("New Current Price: "))

        if len(row["securityCode"])>10 :
            print("Invalid SecurityCode")
            return

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
#done
def retrieveAllStocks():
    try:
        row = {}
        print("Retrieve all stocks: ")

        query = "SELECT * FROM stock" 
        print(query)
        cur.execute(query)
        record = cur.fetchall()
        record1 = toList(record)
        print(tabulate(record1, headers="firstrow", tablefmt="pretty"))

        print("Operation Performed!")

    except Exception as e:
        con.rollback()
        print("Failed to do the operation")
        print(">>>>>>>>>>>>>", e)

    return

#done
def getTotalMoneyInvestedInAParticularStock():
    try:
        row = {}
        print("Retrieve the total money invested in a particular stock: ")
        row["securitycode"] = input("Security Code: ")

        if len(row["securitycode"])> 10 :
            print("Invalid Security Code")
            return

        query = "SELECT SUM(quantity*PurchasePrice) AS total_investment from transactions INNER JOIN comprisesof ON comprisesof.transactionID = transactions.transactionID WHERE comprisesof.securityCode = \'%s\';" %(row["securitycode"])
        print(query)
        cur.execute(query)
        record = cur.fetchall()
        record1 = toList(record)
        print(tabulate(record1, headers="firstrow", tablefmt="pretty"))
        con.commit()

        print("Operation Performed!")

    except Exception as e:
        con.rollback()
        print("Failed to do the operation")
        print(">>>>>>>>>>>>>", e)

    return

#done
def usernameStartsWithLetter():
    try:
        row = {}
        print("Retrieve username starting with a partcular letter: ")
        row["letter"] = input("letter: ")
        query = "SELECT username FROM users WHERE username LIKE \'{0}%\';".format(row["letter"])
        print(query)
        cur.execute(query)
        record = cur.fetchall()
        record1 = toList(record)
        print(tabulate(record1, headers="firstrow", tablefmt="pretty"))

        print("Operation Performed!")

    except Exception as e:
        con.rollback()
        print("Failed to do the operation")
        print(">>>>>>>>>>>>>", e)

    return

#done
def getTransactionWithMaxPurchasePrice():
    try:
        row = {}
        print("Retrieve transaction with max purchase price: ")

        query = "SELECT * FROM Transactions WHERE purchasePrice = (SELECT MAX(purchasePrice) FROM Transactions)"
        print(query)
        cur.execute(query)
        record = cur.fetchall()
        record1 = toList(record)
        print(tabulate(record1, headers="firstrow", tablefmt="pretty"))
        #con.commit()

        print("Operation Performed!")

    except Exception as e:
        con.rollback()
        print("Failed to do the operation")
        print(">>>>>>>>>>>>>", e)

    return

#done
def stocksWithStockPElessThanAValue():
    try:
        row = {}
        print("Retrieve stock with stockPE less than a given value: ")
        row["threshold"] = input("Threshold: ")
        query = "SELECT * FROM stock WHERE stockPE <= %s;" %(row["threshold"])
        print(query)
        cur.execute(query)
        record = cur.fetchall()
        record1 = toList(record)
        print(tabulate(record1, headers="firstrow", tablefmt="pretty"))
        
        print("Operation Performed!")

    except Exception as e:
        con.rollback()
        print("Failed to do the operation")
        print(">>>>>>>>>>>>>", e)

    return

def priceChangePositive():
    try:
        row = {}
        print("Retrieve the stocks whose price change is positive: ")

        query = "SELECT SecurityCode FROM stock WHERE currentPrice - prevClose > 0"
        print(query)
        cur.execute(query)
        record = cur.fetchall()
        record1 = toList(record)
        print(tabulate(record1, headers="firstrow", tablefmt="pretty"))
        
        print("Operation Performed!")

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
        getTotalMoneyInvestedInAParticularStock()
    elif(ch == 6):
        usernameStartsWithLetter()
    elif(ch == 7):
        getTransactionWithMaxPurchasePrice()
    elif(ch == 8):
        stocksWithStockPElessThanAValue()
    elif(ch == 9):
        priceChangePositive()
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
                              db='backup',
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
                print("4. Retrieve all stocks")
                print("5. Retrieve the total money invested in a particular stock")
                print("6. Retrieve username starting with a particular letter")
                print("7. Retrieve transaction with max purchase price")
                print("8. Retrieve stock(s) with stockPE less than a certain value")
                print("9. Retrieve the stocks whose price change is positive")
                print("10. Logout")

                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 10:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")

        