-- MySQL dump 10.13  Distrib 8.0.31, for macos13.0 (arm64)
--
-- Host: localhost    Database: Project
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `administrator`
--

DROP TABLE IF EXISTS `administrator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administrator` (
  `username` varchar(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `accountID` int NOT NULL,
  `passwrd` varchar(20) NOT NULL,
  PRIMARY KEY (`accountID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrator`
--

LOCK TABLES `administrator` WRITE;
/*!40000 ALTER TABLE `administrator` DISABLE KEYS */;
INSERT INTO `administrator` VALUES ('phoenix','fwakes@gmail.com',1,'password'),('maylord','mlord@gmail.com',2,'ineedapassword'),('mayhem','mhem@gmail.com',3,'changeme'),('drast','dmaster@gmail.com',4,'secret'),('ImEsmerelda','esmerelda@gmail.com',5,'iamforgor');
/*!40000 ALTER TABLE `administrator` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comprisesof`
--

DROP TABLE IF EXISTS `comprisesof`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comprisesof` (
  `securityCode` varchar(10) NOT NULL,
  `transactionID` int NOT NULL,
  PRIMARY KEY (`securityCode`,`transactionID`),
  KEY `transactionID` (`transactionID`),
  CONSTRAINT `comprisesof_ibfk_1` FOREIGN KEY (`transactionID`) REFERENCES `Transactions` (`TransactionID`),
  CONSTRAINT `comprisesof_ibfk_2` FOREIGN KEY (`securityCode`) REFERENCES `stock` (`SecurityCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comprisesof`
--

LOCK TABLES `comprisesof` WRITE;
/*!40000 ALTER TABLE `comprisesof` DISABLE KEYS */;
INSERT INTO `comprisesof` VALUES ('PANAMAPET',999001),('SUZLON',999002),('LYKALABS',999003),('530419',999004),('SUULD',999005);
/*!40000 ALTER TABLE `comprisesof` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contain`
--

DROP TABLE IF EXISTS `contain`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contain` (
  `securityCode` varchar(10) NOT NULL,
  `accountID` int NOT NULL,
  `serialNo` int NOT NULL,
  PRIMARY KEY (`securityCode`,`accountID`,`serialNo`),
  KEY `accountID` (`accountID`),
  KEY `serialNo` (`serialNo`),
  CONSTRAINT `contain_ibfk_1` FOREIGN KEY (`securityCode`) REFERENCES `Stock` (`SecurityCode`),
  CONSTRAINT `contain_ibfk_2` FOREIGN KEY (`accountID`) REFERENCES `users` (`accountID`),
  CONSTRAINT `contain_ibfk_3` FOREIGN KEY (`serialNo`) REFERENCES `portfolioList` (`serialNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contain`
--

LOCK TABLES `contain` WRITE;
/*!40000 ALTER TABLE `contain` DISABLE KEYS */;
INSERT INTO `contain` VALUES ('PANAMAPET',123456,1),('LYKALABS',135246,1),('530419',246135,1),('SUULD',321654,1),('SUZLON',654321,1);
/*!40000 ALTER TABLE `contain` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Feedback`
--

DROP TABLE IF EXISTS `Feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Feedback` (
  `title` varchar(60) NOT NULL,
  `comment` varchar(500) NOT NULL,
  `accountID` int NOT NULL,
  PRIMARY KEY (`title`,`accountID`),
  KEY `accountID` (`accountID`),
  CONSTRAINT `feedback_ibfk_1` FOREIGN KEY (`accountID`) REFERENCES `users` (`accountID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Feedback`
--

LOCK TABLES `Feedback` WRITE;
/*!40000 ALTER TABLE `Feedback` DISABLE KEYS */;
INSERT INTO `Feedback` VALUES ('Features i dislike','Difficult to understand by normal users , Non-optimized functions which leads to larger time , Unresponsive UI',321654),('Features i like','Functionalities are good , Easiness ensured , Modern system , Optimized functions,  Responsive UI',123456),('Features i like','Functionalities are good , Easiness ensured , Modern system , Optimized functions,  Responsive UI',654321),('hello','yes',123456),('Lack of privacy in data ','So site should ensure more privacy of data , stuff such that last seen and companies can be kept confidential',135246),('Regarding User Interface ','User interface should be made more interactive so that it is easier for the user to unserstand and comprehend',246135);
/*!40000 ALTER TABLE `Feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `has`
--

DROP TABLE IF EXISTS `has`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `has` (
  `accountID` int NOT NULL,
  `portfolioListSerialNo` int NOT NULL,
  `watchListSerialNo` int NOT NULL,
  PRIMARY KEY (`accountID`,`portfolioListSerialNo`,`watchListSerialNo`),
  KEY `portfolioListSerialNo` (`portfolioListSerialNo`),
  CONSTRAINT `has_ibfk_1` FOREIGN KEY (`accountID`) REFERENCES `users` (`accountID`),
  CONSTRAINT `has_ibfk_2` FOREIGN KEY (`portfolioListSerialNo`) REFERENCES `portfolioList` (`serialNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `has`
--

LOCK TABLES `has` WRITE;
/*!40000 ALTER TABLE `has` DISABLE KEYS */;
INSERT INTO `has` VALUES (123456,1,1),(123456,1,2),(135246,1,1),(246135,1,1),(321654,1,1),(654321,1,1);
/*!40000 ALTER TABLE `has` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phoneNumber`
--

DROP TABLE IF EXISTS `phoneNumber`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `phoneNumber` (
  `accountID` int NOT NULL,
  `phnumber` varchar(20) NOT NULL,
  `countryCode` varchar(3) NOT NULL,
  PRIMARY KEY (`accountID`,`phnumber`,`countryCode`),
  CONSTRAINT `phonenumber_ibfk_1` FOREIGN KEY (`accountID`) REFERENCES `users` (`accountID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phoneNumber`
--

LOCK TABLES `phoneNumber` WRITE;
/*!40000 ALTER TABLE `phoneNumber` DISABLE KEYS */;
INSERT INTO `phoneNumber` VALUES (123456,'9041210193','+91'),(135246,'1234567890','+91'),(246135,'1234447890','+91'),(321654,'1234447890','+91'),(654321,'1234567894','+91');
/*!40000 ALTER TABLE `phoneNumber` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `portfolioList`
--

DROP TABLE IF EXISTS `portfolioList`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `portfolioList` (
  `serialNo` int NOT NULL,
  `securityCode` varchar(10) NOT NULL,
  `instrumentName` varchar(40) NOT NULL,
  `currentPrice` float NOT NULL,
  `TotalQuantity` int NOT NULL,
  `indexTag` tinyint(1) NOT NULL,
  `accountID` int NOT NULL,
  PRIMARY KEY (`serialNo`,`accountID`),
  KEY `accountID` (`accountID`),
  CONSTRAINT `portfoliolist_ibfk_1` FOREIGN KEY (`accountID`) REFERENCES `users` (`accountID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `portfolioList`
--

LOCK TABLES `portfolioList` WRITE;
/*!40000 ALTER TABLE `portfolioList` DISABLE KEYS */;
INSERT INTO `portfolioList` VALUES (1,'PANAMAPET','Panama Petrochem Ltd.',402,90,0,123456),(1,'LYKALABS','Lyka Labs Ltd.',135.9,100,0,135246),(1,'530419','Sumedha Fiscal Services',110.65,110,0,246135),(1,'SUULD','Suumaya Industries Ltd. ',35.55,185,0,321654),(1,'SUZLON','Suzlon Energy Ltd.',8.5,200,0,654321);
/*!40000 ALTER TABLE `portfolioList` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Stock`
--

DROP TABLE IF EXISTS `Stock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Stock` (
  `prevClose` float NOT NULL,
  `currentPrice` float NOT NULL,
  `quantity` int NOT NULL,
  `SecurityCode` varchar(10) NOT NULL,
  `marketCap` float NOT NULL,
  `High` float NOT NULL,
  `Low` float NOT NULL,
  `StockPE` float DEFAULT NULL,
  `BookValue` float NOT NULL,
  `dividendYield` float NOT NULL,
  `ROCE` float DEFAULT NULL,
  `ROE` float DEFAULT NULL,
  `faceValue` float NOT NULL,
  PRIMARY KEY (`SecurityCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Stock`
--

LOCK TABLES `Stock` WRITE;
/*!40000 ALTER TABLE `Stock` DISABLE KEYS */;
INSERT INTO `Stock` VALUES (105.4,110.65,100,'530419',88.3,188.2,22,55.44,63.6,0.9,10.4,6.23,10),(127.4,135.9,300,'LYKALABS',391,267,102,NULL,4.7,0,61.1,NULL,10),(0,0,0,'NIFTY_50',0,15183.4,18534.9,0,0,0,0,0,0),(355.35,402,1000,'PANAMAPET',2458,412.4,214.45,10.03,144,1.97,41.2,34.7,2),(33.9,35.55,950,'SUULD',200,175,31,0.42,248,1.41,88.5,120,10),(7.9,8.5,10000,'SUZLON',9928,12,5.42,3.96,-0.25,0,22.3,NULL,2);
/*!40000 ALTER TABLE `Stock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Transactions`
--

DROP TABLE IF EXISTS `Transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Transactions` (
  `PurchasePrice` float NOT NULL,
  `CurrentPrice` float NOT NULL,
  `TransactionID` int NOT NULL,
  `Quantity` int NOT NULL,
  `comments` varchar(255) DEFAULT NULL,
  `purchaseTime` timestamp NOT NULL,
  PRIMARY KEY (`TransactionID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Transactions`
--

LOCK TABLES `Transactions` WRITE;
/*!40000 ALTER TABLE `Transactions` DISABLE KEYS */;
INSERT INTO `Transactions` VALUES (124.25,402,999001,100,'Bought 100 shares of PANAMAPET','2019-01-01 04:30:00'),(12,8.5,999002,10000,'Bought 10000 shares of SUZLON','2019-02-01 04:30:00'),(127.4,135.9,999003,300,'Bought 300 shares of LYKALABS','2019-03-01 04:30:00'),(130.35,110.65,999004,100,'Bought 100 shares of 530419','2019-04-01 04:30:00'),(94,35.55,999005,950,'Bought 950 shares of SUULD','2019-05-01 04:30:00');
/*!40000 ALTER TABLE `Transactions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `username` varchar(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `accountID` int NOT NULL,
  `passwrd` varchar(20) NOT NULL,
  `FirstName` varchar(20) NOT NULL,
  `MiddleName` varchar(20) DEFAULT NULL,
  `LastName` varchar(20) NOT NULL,
  `DateOfBirth` date NOT NULL,
  `StreetName` varchar(20) NOT NULL,
  `AddressLine1` varchar(20) NOT NULL,
  `AddressLine2` varchar(20) DEFAULT NULL,
  `Pincode` varchar(20) NOT NULL,
  `parent_AccountID` int NOT NULL,
  `transactionID` int NOT NULL,
  PRIMARY KEY (`accountID`),
  KEY `transactionID` (`transactionID`),
  KEY `parent_AccountID` (`parent_AccountID`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`transactionID`) REFERENCES `Transactions` (`TransactionID`),
  CONSTRAINT `users_ibfk_2` FOREIGN KEY (`parent_AccountID`) REFERENCES `users` (`accountID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('oops_moment','prishakumar@grinder.com',123456,'hello_123','Prisha','idli','Kumar','2003-12-14','gachibowli','gachibowli','Omaxe','454565',123456,999001),('aaryans','aaryan@yahoo.com',135246,'aaryan_321','Aaryan',NULL,'Sharma','2002-08-05','gurdevNagar','gurdevNagar',NULL,'356736',654321,999003),('anushka5','anushka5@gmail.com',246135,'whchsh','Anushka',NULL,'Agrawal','2002-06-05','taylorStreet','taylorStreet','sunnyHomes','123456',135246,999004),('pratham_21','pratham@grinder.com',321654,'p_mishra10','Pratham',NULL,'Mishra','2001-10-21','AalamBagh','AalamBagh',NULL,'456532',246135,999005),('vanshika1030','vanshika@gmail.com',654321,'vard10','Vanshika',NULL,'Dhingra','2003-07-10','sarabhaNagar','sarabhaNagar',NULL,'141001',123456,999002);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `views`
--

DROP TABLE IF EXISTS `views`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `views` (
  `adminAccountID` int NOT NULL,
  `userAccountID` int NOT NULL,
  `portfolioListSerialNo` int NOT NULL,
  `watchListSerialNo` int NOT NULL,
  `feedbackTitle` varchar(60) NOT NULL,
  PRIMARY KEY (`adminAccountID`,`userAccountID`,`portfolioListSerialNo`,`watchListSerialNo`,`feedbackTitle`),
  KEY `userAccountID` (`userAccountID`),
  KEY `portfolioListSerialNo` (`portfolioListSerialNo`),
  KEY `watchListSerialNo` (`watchListSerialNo`),
  KEY `feedbackTitle` (`feedbackTitle`),
  CONSTRAINT `views_ibfk_1` FOREIGN KEY (`adminAccountID`) REFERENCES `administrator` (`accountID`),
  CONSTRAINT `views_ibfk_2` FOREIGN KEY (`userAccountID`) REFERENCES `users` (`accountID`),
  CONSTRAINT `views_ibfk_3` FOREIGN KEY (`portfolioListSerialNo`) REFERENCES `portfolioList` (`serialNo`),
  CONSTRAINT `views_ibfk_4` FOREIGN KEY (`watchListSerialNo`) REFERENCES `watchList` (`serialNo`),
  CONSTRAINT `views_ibfk_5` FOREIGN KEY (`feedbackTitle`) REFERENCES `Feedback` (`title`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `views`
--

LOCK TABLES `views` WRITE;
/*!40000 ALTER TABLE `views` DISABLE KEYS */;
INSERT INTO `views` VALUES (1,123456,1,1,'Features i like'),(2,123456,1,1,'Features i dislike'),(2,123456,1,2,'Features i dislike'),(3,135246,1,1,'Lack of Privacy in data '),(4,246135,1,1,'Regarding User Interface '),(5,321654,1,1,'Features i dislike');
/*!40000 ALTER TABLE `views` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `watchList`
--

DROP TABLE IF EXISTS `watchList`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `watchList` (
  `serialNo` int NOT NULL,
  `securityCode` varchar(10) NOT NULL,
  `instrumentName` varchar(40) NOT NULL,
  `currentPrice` float NOT NULL,
  `indexTag` tinyint(1) NOT NULL,
  `accountID` int NOT NULL,
  PRIMARY KEY (`serialNo`,`accountID`),
  KEY `accountID` (`accountID`),
  CONSTRAINT `watchlist_ibfk_1` FOREIGN KEY (`accountID`) REFERENCES `users` (`accountID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `watchList`
--

LOCK TABLES `watchList` WRITE;
/*!40000 ALTER TABLE `watchList` DISABLE KEYS */;
INSERT INTO `watchList` VALUES (1,'PANAMAPET','Panama Petrochem Ltd.',402,0,123456),(1,'LYKALABS','Lyka Labs Ltd',135.9,0,135246),(1,'530419','Sumedha Fiscal Services',110.65,0,246135),(1,'PANAMAPET','Panama Petrochem Ltd.',402,0,321654),(1,'SUZLON','Suzlon Energy Ltd',8.5,0,654321),(2,'NIFTY_50','Nifty 50',0,0,123456);
/*!40000 ALTER TABLE `watchList` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-27 18:39:37
