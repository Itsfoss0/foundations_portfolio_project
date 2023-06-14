-- MySQL dump 10.19  Distrib 10.5.18-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: todoist_db
-- ------------------------------------------------------
-- Server version    10.5.18-MariaDB-0+deb11u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `app_users`
--

DROP TABLE IF EXISTS `app_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `age` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() + INTERVAL 1 DAY,
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_users`
--

LOCK TABLES `app_users` WRITE;
/*!40000 ALTER TABLE `app_users` DISABLE KEYS */;
INSERT INTO `app_users` VALUES (1,'Jane Doe','janedoe@test.net',33,'2023-05-23 11:27:59','$2b$12$NrXa2c7OiYLcCddgkNSMo.eVviALeJEEJ2NkisEzL6i75bQBNmrnC'),(2,'Alice Krugger','alicekrugger@testmail.net',54,'2023-05-23 11:35:10','$2b$12$JZJbmpJxaxTX.1gKaG9MO.KNv9LXJfneMf5EwmJZ11iv4uhbEaCEO'),(8,'Emma Davis','emmsdavis@gmail.net',12,'2023-05-23 11:53:11','$2b$12$ZA25lMnucsRXELUogSvPX.Plx1NsHXQlLk0vAAwRU4CJZM4G1vdRS'),(9,'Sherlock Holmes','holmesherlock@sher.me',45,'2023-05-23 12:34:58','$2b$12$MIEEvktczG9x4nYXsRdXne.2nt4LCinvKcNV/8a/6TMBMXr6vu6gK'),(10,'John Garret','jgarret@shield.net',23,'2023-05-23 13:53:09','$2b$12$93ec1n.6q5GfrwN4M2bXSOmhNYuE7OQr9SZFvLyLt9HPi4iK6n6TO'),(11,'Tristin Malda','tmalda@me.ent',13,'2023-05-23 14:23:49','$2b$12$pMjD0f10l2oOFQCPTieTceRbzd8bKVdG/GWNfVLpW5k6DCyhMKxlq'),(12,'Johnathan James','jamesjohnathan@gmail.com',15,'2023-05-23 14:30:37','$2b$12$fwFttXLNPdTY1.gU4EGQkO/qdlVtG5A6IdWcbnRK57BSZY3x0eItm'),(13,'Taylor Shaw','taylorswaw@bls.net',20,'2023-05-23 14:32:47','$2b$12$BYXhf0ZemgtXGyL3Q3nBnOvwsdvtE/dWlVCZas5K68a7S1p/Z8ijC'),(14,'John Doe','jdoe@user.net',13,'2023-05-23 14:41:19','$2b$12$rWWZlawOiur6Pgl1jKw2ceBW1Ba1S40WCHhKSIJQeIstdvTicwQ7K'),(15,'Jordana Star','jdonasar@bls.net',20,'2023-05-23 15:51:52','$2b$12$1Z1JdevkzCTqkyWkCDdgq.wh7AhyCJo8Td5YDvnDz/dN6N7xP6eGq'),(16,'Marrisa Wiegler','mwig@gmail.com',20,'2023-05-24 14:50:36','$2b$12$ufFC/Op90RMYQlcGrZ0QIOZrXM.SP.P0TSyNeF0HsdXy9VAwW9x0C'),(17,'Austin French','afrench@gmail.com',24,'2023-05-24 15:40:19','$2b$12$8u8XcrcfysG9Xkkc.eXDx.6SGB5JrwWp1BTd8Mr5DKxaaypGBGnYm'),(18,'Dayan Mayfar','dm@gmail.com',24,'2023-05-25 10:30:05','$2b$12$Chb9aGtRICJFZw09g5nYnuVkUDZLHMkHP9p.sMK3vBbBclxoD6od6'),(19,'Tasha Zapata','tzapata@gmail.com',24,'2023-05-25 10:33:28','$2b$12$IyerCUjB17/OP7dmHONZCeB0H6/M3UXG0W8i4fD6DU2smDFtgDs5a'),(20,'Fredrick Barnes','fbarnes@gmail.com',23,'2023-05-26 09:42:36','$2b$12$8Xl5lGwQ9A4G0YS6IquHWuPfykhBxMOaJg5.45BWf.3OgkUHe9aFm');
/*!40000 ALTER TABLE `app_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tasks`
--

DROP TABLE IF EXISTS `tasks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tasks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` text DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `fk_user_id` (`user_id`),
  CONSTRAINT `fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `app_users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tasks`
--

LOCK TABLES `tasks` WRITE;
/*!40000 ALTER TABLE `tasks` DISABLE KEYS */;
INSERT INTO `tasks` VALUES (1,'Finish report','Finish the quarterly report for the management',1,'2023-05-23 11:39:56'),(2,'Call John','Call John to discuss the upcoming meeting',1,'2023-05-23 12:05:24'),(3,'Buy groceries','Buy groceries for the weekend',2,'2023-05-23 12:10:17'),(4,'Submit expenses','Submit travel expenses for approval',2,'2023-05-23 12:23:45'),(5,'Pick up dry cleaning','Pick up the dry cleaning from the laundry',3,'2023-05-23 12:30:19'),(6,'Book flight','Book flight tickets for the vacation',4,'2023-05-23 12:35:56'),(7,'Finish presentation','Finish the presentation slides for the meeting',4,'2023-05-23 12:42:09'),(8,'Call client','Call the client to discuss the project updates',5,'2023-05-23 12:47:33'),(9,'Send reminder email','Send a reminder email to the team about the deadline',6,'2023-05-23 12:55:12'),(10,'Pay bills','Pay the utility bills before the due date',6,'2023-05-23 13:02:39'),(11,'Research topic','Research the latest trends in machine learning',7,'2023-05-23 13:08:51'),(12,'Attend webinar','Attend the webinar on cybersecurity',7,'2023-05-23 13:15:27'),(13,'Prepare agenda','Prepare the agenda for the team meeting',8,'2023-05-23 13:20:59'),(14,'Submit proposal','Submit the proposal for the new project',9,'2023-05-23 13:29:11'),(15,'Follow up with client','Follow up with the client regarding the contract',9,'2023-05-23 13:35:47'),(16,'Prepare presentation','Prepare the presentation for the sales pitch',10,'2023-05-23 13:41:59'),(17,'Update website','Update the company website with new content',11,'2023-05-23 13:48:34'),(18,'Review code','Review the code for the upcoming release',12,'2023-05-23 13:55:16'),(19,'Submit time off request','Submit a request for time off for vacation',13,'2023-05-23 14:01:39'),(20,'Attend meeting','Attend the project status meeting with the team',14,'2023-05-23 14:07:52'),(21,'Call supplier','Call the supplier to inquire about the delivery',15,'2023-05-23 14:14:34'),(22,'Send monthly report','Send the monthly report to the stakeholders',16,'2023-05-23 14:21:09'),(23,'Update inventory','Update the inventory system with new stock',17,'2023-05-23 14:27:41'),(24,'Organize files','Organize the files and folders on the computer',18,'2023-05-23 14:35:02'),(25,'Schedule meeting','Schedule a meeting with the department heads',19,'2023-05-23 14:41:19'),(26,'Prepare budget','Prepare the budget for the next fiscal year',20,'2023-05-23 14:47:43'),(27,'Plan team outing','Plan a team outing for team building',1,'2023-05-24 12:56:19'),(28,'Review contracts','Review the contracts with legal team',1,'2023-05-24 13:02:41'),(29,'Create marketing campaign','Create a marketing campaign for the new product launch',2,'2023-05-24 13:09:18'),(30,'Update social media','Update the social media profiles with new content',2,'2023-05-24 13:15:37');
/*!40000 ALTER TABLE `tasks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'todoist_db'
--

--
-- Dumping routines for database 'todoist_db'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-25 14:23:09
