CREATE DATABASE Project;

DROP DATABASE Project;

USE Project;

CREATE TABLE Stock (
    prevClose float NOT NULL,
    currentPrice float NOT NULL,
    quantity int NOT NULL,
    SecurityCode VARCHAR(10) NOT NULL,
    marketCap float NOT NULL,
    High float NOT NULL,
    Low float NOT NULL,
    StockPE float,
    BookValue float NOT NULL,
    dividendYield float NOT NULL,
    ROCE float,
    ROE float,
    faceValue float NOT NULL,
    PRIMARY KEY (SecurityCode)
);

CREATE TABLE Transactions (
    PurchasePrice float NOT NULL,
    CurrentPrice float NOT NULL,
    TransactionID int NOT NULL,
    Quantity int NOT NULL,
    comments varchar(255),
    purchaseTime timestamp NOT NULL,
    PRIMARY KEY (TransactionID)
);

DROP TABLE users;
CREATE TABLE users (
    username VARCHAR(20) NOT NULL,
    email VARCHAR(40) NOT NULL,
    accountID int NOT NULL,
    passwrd VARCHAR(20) NOT NULL,
    FirstName VARCHAR(20) NOT NULL,
    MiddleName VARCHAR(20),
    LastName VARCHAR(20) NOT NULL,
    DateOfBirth DATE NOT NULL,
    StreetName VARCHAR(20) NOT NULL,
    AddressLine1 VARCHAR(20) NOT NULL,
    AddressLine2 VARCHAR(20),
    Pincode VARCHAR(20) NOT NULL,
    parent_AccountID int NOT NULL,
    transactionID int NOT NULL,
    FOREIGN KEY (transactionID) REFERENCES Transactions(transactionID),
    FOREIGN KEY (parent_AccountID) REFERENCES users(accountID),
    PRIMARY KEY (accountID)
);

DROP TABLE administrator;
CREATE TABLE administrator (
    username VARCHAR(20) NOT NULL,
    email VARCHAR(40) NOT NULL,
    accountID int NOT NULL,
    passwrd VARCHAR(20) NOT NULL,
    PRIMARY KEY (accountID)
);

CREATE TABLE Feedback (
    title VARCHAR(60) NOT NULL,
    comment VARCHAR(500) NOT NULL,
    accountID int NOT NULL,
    PRIMARY KEY (Title, accountID),
    FOREIGN KEY (accountID) REFERENCES users(accountID)
);

DROP TABLE watchList;
CREATE TABLE watchList (
    serialNo int NOT NULL,
    securityCode VARCHAR(10) NOT NULL,
    instrumentName VARCHAR(40) NOT NULL,
    currentPrice float NOT NULL,
    indexTag BOOLEAN NOT NULL,
    accountID int NOT NULL,
    PRIMARY KEY (serialNo, accountID),
    FOREIGN KEY (accountID) REFERENCES users(accountID)
);


CREATE TABLE portfolioList (
    serialNo int NOT NULL,
    securityCode VARCHAR(10) NOT NULL,
    instrumentName VARCHAR(40) NOT NULL,
    currentPrice float NOT NULL,
    TotalQuantity int NOT NULL,
    indexTag BOOLEAN NOT NULL,
    accountID int NOT NULL,
    PRIMARY KEY (serialNo, accountID),
    FOREIGN KEY (accountID) REFERENCES users(accountID)
);

CREATE TABLE contain (
    securityCode VARCHAR(10) NOT NULL,
    accountID int NOT NULL,
    serialNo int NOT NULL,
    PRIMARY KEY (securityCode, accountID, serialNo),
    FOREIGN KEY (securityCode) REFERENCES Stock(SecurityCode),
    FOREIGN KEY (accountID) REFERENCES users(accountID),
    FOREIGN KEY (serialNo) REFERENCES portfolioList(serialNo)
);

CREATE TABLE phoneNumber (
    accountID int NOT NULL,
    phnumber VARCHAR(20) NOT NULL,
    countryCode VARCHAR(3) NOT NULL,
    PRIMARY KEY (accountID, phnumber, countryCode),
    FOREIGN KEY (accountID) REFERENCES users(accountID)
);

CREATE TABLE has (
    accountID int NOT NULL,
    portfolioListSerialNo int NOT NULL,
    watchListSerialNo int NOT NULL,
    PRIMARY KEY (accountID, portfolioListSerialNo, watchListSerialNo),
    FOREIGN KEY (accountID) REFERENCES users(accountID),
    FOREIGN KEY (portfolioListSerialNo) REFERENCES portfolioList(serialNo)
);

CREATE TABLE views (
    adminAccountID int NOT NULL,
    userAccountID int NOT NULL,
    portfolioListSerialNo int NOT NULL,
    watchListSerialNo int NOT NULL,
    feedbackTitle VARCHAR(60) NOT NULL,
    PRIMARY KEY (adminAccountID, userAccountID, portfolioListSerialNo, watchListSerialNo, feedbackTitle),
    FOREIGN KEY (adminAccountID) REFERENCES administrator(accountID),
    FOREIGN KEY (userAccountID) REFERENCES users(accountID),
    FOREIGN KEY (portfolioListSerialNo) REFERENCES portfolioList(serialNo),
    FOREIGN KEY (watchListSerialNo) REFERENCES watchList(serialNo),
    FOREIGN KEY (feedbackTitle) REFERENCES Feedback(title)
);

CREATE TABLE comprisesof (
securityCode VARCHAR(10),
transactionID INT NOT NULL,
FOREIGN KEY (transactionID) REFERENCES Transactions(transactionID),
FOREIGN KEY (securityCode) REFERENCES stock(securityCode),
PRIMARY KEY (securityCode, transactionID)
);