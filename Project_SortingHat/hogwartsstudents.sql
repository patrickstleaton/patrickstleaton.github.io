-- MySQL dump 10.16  Distrib 10.1.21-MariaDB, for Win32 (AMD64)
--
-- Host: localhost    Database: localhost
-- ------------------------------------------------------
-- Server version	10.1.21-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `hogwartsstudents`
--

DROP TABLE IF EXISTS `hogwartsstudents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hogwartsstudents` (
  `student_id` int(50) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(35) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `house` varchar(50) DEFAULT NULL,
  `date_enrolled` date DEFAULT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hogwartsstudents`
--

LOCK TABLES `hogwartsstudents` WRITE;
/*!40000 ALTER TABLE `hogwartsstudents` DISABLE KEYS */;
INSERT INTO `hogwartsstudents` VALUES (1,'Swag','Master','Slytherin','2012-11-08'),(2,'hi','sup','Slytherin','2017-05-07'),(3,'Harry','Potter','Ravenclaw',NULL),(4,'Harry','Potter','Ravenclaw','0000-00-00'),(5,'Ron','Weasley','Hufflepuff','0000-00-00'),(6,'Bob','Rodriguez','Gryffindor','0000-00-00'),(7,'Lisa','Carter','Gryffindor','0000-00-00'),(8,'Jade','Carter','Slytherin','0000-00-00'),(9,'Sam','Gurule','Gryffindor','0000-00-00'),(10,'Albert','Gates','Hufflepuff','0000-00-00'),(11,'Sarah','Mendieta','Hufflepuff','0000-00-00'),(12,'Nicolas','Tesla','Gryffindor','0000-00-00'),(13,'The','Hulk','Ravenclaw','0000-00-00'),(14,'Angel','Mena','Ravenclaw','2017-05-11'),(15,'Nicolas ','Tesla','Gryffindor','2017-05-11'),(16,'Nicolas','Tesla','Slytherin','2017-05-11'),(17,'Richard','West','Slytherin','2017-05-11'),(18,'That','guy','Ravenclaw','2017-05-11'),(19,'Albert','Einstein','Slytherin','2017-05-11'),(20,'Kenny','White','Hufflepuff','2017-05-11'),(21,'Pedro',' ','Gryffindor','2017-05-11');
/*!40000 ALTER TABLE `hogwartsstudents` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `housedetail`
--

DROP TABLE IF EXISTS `housedetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `housedetail` (
  `house_name` varchar(20) DEFAULT NULL,
  `founder` varchar(20) DEFAULT NULL,
  `house_gem` varchar(20) DEFAULT NULL,
  `animal` varchar(20) DEFAULT NULL,
  `element` varchar(20) DEFAULT NULL,
  `ghost` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `housedetail`
--

LOCK TABLES `housedetail` WRITE;
/*!40000 ALTER TABLE `housedetail` DISABLE KEYS */;
INSERT INTO `housedetail` VALUES ('Gryffindor','Godric Gryffindor','ruby','lion','fire','Nearly-Headless Nick'),('Slytherin','Salazar Slytherin','emerald','serpent','water','Bloody Baron'),('Ravenclaw','Rowena Ravenclaw','sapphire','eagle','air','The Grey Lady'),('Hufflepuff','Helga Hufflepuff','diamond','badger','earth','Fat Friar');
/*!40000 ALTER TABLE `housedetail` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-05-11  9:08:11
