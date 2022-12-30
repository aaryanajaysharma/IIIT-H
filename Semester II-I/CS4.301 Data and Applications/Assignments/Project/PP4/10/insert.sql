INSERT INTO stock
    (prevClose, currentPrice, quantity, SecurityCode, marketCap, High, Low, StockPE, BookValue, dividendYield, ROCE, ROE, faceValue)
VALUES
    (355.35, 402.00, 1000, 'PANAMAPET', 2458, 412.40, 214.45, 10.03, 144, 1.97, 41.2, 34.7, 2.00),
    (7.90, 8.50, 10000, 'SUZLON', 9928, 12.0, 5.42, 3.96, -0.25, 0.00, 22.3, NULL, 2.00),
    (127.40, 135.90, 300, 'LYKALABS', 391, 267, 102, NULL, 4.70, 0.00, 61.1, NULL, 10.0),
    (105.40, 110.65, 100, '530419', 88.3, 188.20, 22.00, 55.44, 63.6, 0.90, 10.4, 6.23, 10.0),
    (33.90, 35.55, 950, 'SUULD', 200, 175, 31.0, 0.42, 248, 1.41, 88.5, 120, 10.0),
    (0, 0, 0, 'NIFTY_50', 0, 15183.40, 18534.90, 0, 0, 0, 0, 0, 0)
;

INSERT INTO transactions
    (PurchasePrice, CurrentPrice, TransactionID, Quantity, comments, purchaseTime)
VALUES
    (124.25, 402.00, 999001, 100, 'Bought 100 shares of PANAMAPET', '2019-01-01 10:00:00'),
    (12.00, 8.50, 999002, 10000, 'Bought 10000 shares of SUZLON', '2019-02-01 10:00:00'),
    (127.40, 135.90, 999003, 300, 'Bought 300 shares of LYKALABS', '2019-03-01 10:00:00'),
    (130.35, 110.65, 999004, 100, 'Bought 100 shares of 530419', '2019-04-01 10:00:00'),
    (94.00, 35.55, 999005, 950, 'Bought 950 shares of SUULD', '2019-05-01 10:00:00')
;

insert into users
    (username, email, accountID, passwrd, FirstName, MiddleName, LastName, DateOfBirth, StreetName, AddressLine1, AddressLine2, Pincode, parent_AccountID, transactionID)
values
    ('oops_moment', 'prishakumar@grinder.com', 123456, 'hello_123', 'Prisha', 'idli', 'Kumar', '2003-12-14', 'gachibowli', 'gachibowli', 'Omaxe', 454565, 123456, 999001),
    ('vanshika1030', 'vanshika@gmail.com', 654321, 'vard10', 'Vanshika', NULL, 'Dhingra', '2003-07-10', 'sarabhaNagar', 'sarabhaNagar', NULL, 141001, 123456, 999002),
    ('aaryans', 'aaryan@yahoo.com', 135246, 'aaryan_321', 'Aaryan', NULL, 'Sharma', '2002-08-5', 'gurdevNagar', 'gurdevNagar', NULL, 356736, 654321, 999003),
    ('anushka5', 'anushka5@gmail.com', 246135, 'whchsh', 'Anushka', NULL, 'Agrawal', '2002-06-5', 'taylorStreet', 'taylorStreet', 'sunnyHomes', 123456, 135246, 999004),
    ('pratham_21', 'pratham@grinder.com', 321654, 'p_mishra10', 'Pratham', NULL, 'Mishra', '2001-10-21', 'AalamBagh', 'AalamBagh', NULL, 456532, 246135, 999005)
;

-- administrator
insert into administrator
    (username, email, accountID, passwrd)
values
    ('phoenix', 'fwakes@gmail.com', 000001, 'password'),
    ('maylord', 'mlord@gmail.com', 000002, 'ineedapassword'),
    ('mayhem', 'mhem@gmail.com', 000003, 'changeme'),
    ('drast', 'dmaster@gmail.com', 000004, 'secret'),
    ('ImEsmerelda', 'esmerelda@gmail.com', 000005, 'iamforgor')
;

insert into Feedback
values
    ('Features i like', 'Functionalities are good , Easiness ensured , Modern system , Optimized functions,  Responsive UI', 123456),
    ('Features i dislike', 'Difficult to understand by normal users , Non-optimized functions which leads to larger time , Unresponsive UI', 321654),
    ( 'Regarding User Interface ', 'User interface should be made more interactive so that it is easier for the user to unserstand and comprehend', 246135),
    ('Lack of privacy in data ', 'So site should ensure more privacy of data , stuff such that last seen and companies can be kept confidential', 135246),
    ( 'Features i like', 'Functionalities are good , Easiness ensured , Modern system , Optimized functions,  Responsive UI', 654321)
;


insert into watchList
    (serialNo, securityCode, instrumentName, currentPrice, indexTag, accountID)
values
    (1, 'PANAMAPET', 'Panama Petrochem Ltd.', 402.00, 0, 123456),
    (1, 'SUZLON', 'Suzlon Energy Ltd', 8.50, 0, 654321),
    (1, 'LYKALABS', 'Lyka Labs Ltd', 135.90, 0, 135246),
    (1, '530419', 'Sumedha Fiscal Services', 110.65, 0, 246135),
    (1, 'PANAMAPET', 'Panama Petrochem Ltd.', 402.00, 0, 321654),
    (2, 'NIFTY_50', 'Nifty 50', 0, 0, 123456)
;

insert into portfolioList
values
    (1, 'PANAMAPET', 'Panama Petrochem Ltd.', 402.00, 90, 0, 123456),
    (1, 'SUZLON', 'Suzlon Energy Ltd.', 8.50, 200, 0, 654321),
    (1, 'LYKALABS', 'Lyka Labs Ltd.', 135.90, 100, 0, 135246),
    (1, '530419', 'Sumedha Fiscal Services', 110.65, 110, 0, 246135),
    (1, 'SUULD', 'Suumaya Industries Ltd. ', 35.55, 185, 0, 321654)
;

insert into contain
    (securityCode, accountID, serialNo)
values
    ('PANAMAPET', 123456, 1),
    ('SUZLON', 654321, 1),
    ('LYKALABS', 135246, 1),
    ('530419', 246135, 1),
    ('SUULD', 321654, 1)
;

insert into phoneNumber
values
    (123456, '9041210193', '+91'),
    (654321, '1234567894', '+91'),
    (135246, '1234567890', '+91'),
    (246135, '1234447890', '+91'),
    (321654, '1234447890', '+91')
;

insert into has
values
    (123456, 1, 1),
    (123456, 1, 2),
    (135246, 1, 1),
    (246135, 1, 1),
    (321654, 1, 1),
    (654321, 1, 1)
;

insert into views
values
    (000001, 123456, 1, 1, 'Features i like'),
    (000002, 123456, 1, 1, 'Features i dislike'),
    (000002, 123456, 1, 2, 'Features i dislike'),
    (000003, 135246, 1, 1, 'Lack of Privacy in data '),
    (000004, 246135, 1, 1, 'Regarding User Interface '),
    (000005, 321654, 1, 1, 'Features i dislike')
;

SElECT *
FROM stock;
SELECT *
FROM transactions;


INSERT INTO comprisesof
VALUES
    ('PANAMAPET', 999001),
    ('SUZLON', 999002),
    ('LYKALABS', 999003),
    ('530419', 999004),
    ('SUULD', 999005);
;