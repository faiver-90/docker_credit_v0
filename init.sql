CREATE DATABASE  IF NOT EXISTS `credit` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `credit`;
-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: credit
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (3,'Managers'),(2,'Owners'),(1,'Superusers');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=769 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add Код вида деятельности',1,'add_activitycode'),(2,'Can change Код вида деятельности',1,'change_activitycode'),(3,'Can delete Код вида деятельности',1,'delete_activitycode'),(4,'Can view Код вида деятельности',1,'view_activitycode'),(5,'Can add Состояние автомобиля',2,'add_carcondition'),(6,'Can change Состояние автомобиля',2,'change_carcondition'),(7,'Can delete Состояние автомобиля',2,'delete_carcondition'),(8,'Can view Состояние автомобиля',2,'view_carcondition'),(9,'Can add Комплектация автомобиля',3,'add_carconfiguration'),(10,'Can change Комплектация автомобиля',3,'change_carconfiguration'),(11,'Can delete Комплектация автомобиля',3,'delete_carconfiguration'),(12,'Can view Комплектация автомобиля',3,'view_carconfiguration'),(13,'Can add Марка автомобиля',4,'add_carmake'),(14,'Can change Марка автомобиля',4,'change_carmake'),(15,'Can delete Марка автомобиля',4,'delete_carmake'),(16,'Can view Марка автомобиля',4,'view_carmake'),(17,'Can add Клиент',5,'add_clientpredata'),(18,'Can change Клиент',5,'change_clientpredata'),(19,'Can delete Клиент',5,'delete_clientpredata'),(20,'Can view Клиент',5,'view_clientpredata'),(21,'Can add Страна',6,'add_country'),(22,'Can change Страна',6,'change_country'),(23,'Can delete Страна',6,'delete_country'),(24,'Can view Страна',6,'view_country'),(25,'Can add Дилерский центр',7,'add_dealership'),(26,'Can change Дилерский центр',7,'change_dealership'),(27,'Can delete Дилерский центр',7,'delete_dealership'),(28,'Can view Дилерский центр',7,'view_dealership'),(29,'Can add Тип документа',8,'add_documenttype'),(30,'Can change Тип документа',8,'change_documenttype'),(31,'Can delete Тип документа',8,'delete_documenttype'),(32,'Can view Тип документа',8,'view_documenttype'),(33,'Can add Экологический класс',9,'add_ecoclass'),(34,'Can change Экологический класс',9,'change_ecoclass'),(35,'Can delete Экологический класс',9,'delete_ecoclass'),(36,'Can view Экологический класс',9,'view_ecoclass'),(37,'Can add Уровень образования',10,'add_educationlevel'),(38,'Can change Уровень образования',10,'change_educationlevel'),(39,'Can delete Уровень образования',10,'delete_educationlevel'),(40,'Can view Уровень образования',10,'view_educationlevel'),(41,'Can add Тип двигателя',11,'add_enginetype'),(42,'Can change Тип двигателя',11,'change_enginetype'),(43,'Can delete Тип двигателя',11,'delete_enginetype'),(44,'Can view Тип двигателя',11,'view_enginetype'),(45,'Can add Срок финансирования',12,'add_financingterm'),(46,'Can change Срок финансирования',12,'change_financingterm'),(47,'Can delete Срок финансирования',12,'delete_financingterm'),(48,'Can view Срок финансирования',12,'view_financingterm'),(49,'Can add Пол',13,'add_gender'),(50,'Can change Пол',13,'change_gender'),(51,'Can delete Пол',13,'delete_gender'),(52,'Can view Пол',13,'view_gender'),(53,'Can add Тип жилья',14,'add_housingtype'),(54,'Can change Тип жилья',14,'change_housingtype'),(55,'Can delete Тип жилья',14,'delete_housingtype'),(56,'Can view Тип жилья',14,'view_housingtype'),(57,'Can add Семейное положение',15,'add_maritalstatus'),(58,'Can change Семейное положение',15,'change_maritalstatus'),(59,'Can delete Семейное положение',15,'delete_maritalstatus'),(60,'Can view Семейное положение',15,'view_maritalstatus'),(61,'Can add Предложение',16,'add_offers'),(62,'Can change Предложение',16,'change_offers'),(63,'Can delete Предложение',16,'delete_offers'),(64,'Can view Предложение',16,'view_offers'),(65,'Can add Тип организации',17,'add_organizationtype'),(66,'Can change Тип организации',17,'change_organizationtype'),(67,'Can delete Тип организации',17,'delete_organizationtype'),(68,'Can view Тип организации',17,'view_organizationtype'),(69,'Can add Тип телефона',18,'add_phonetype'),(70,'Can change Тип телефона',18,'change_phonetype'),(71,'Can delete Тип телефона',18,'delete_phonetype'),(72,'Can view Тип телефона',18,'view_phonetype'),(73,'Can add Тип должности',19,'add_positiontype'),(74,'Can change Тип должности',19,'change_positiontype'),(75,'Can delete Тип должности',19,'delete_positiontype'),(76,'Can view Тип должности',19,'view_positiontype'),(77,'Can add Способ приобретения',20,'add_purchasemethod'),(78,'Can change Способ приобретения',20,'change_purchasemethod'),(79,'Can delete Способ приобретения',20,'delete_purchasemethod'),(80,'Can view Способ приобретения',20,'view_purchasemethod'),(81,'Can add Тип недвижимости',21,'add_realestatetype'),(82,'Can change Тип недвижимости',21,'change_realestatetype'),(83,'Can delete Тип недвижимости',21,'delete_realestatetype'),(84,'Can view Тип недвижимости',21,'view_realestatetype'),(85,'Can add Социальный статус',22,'add_socialstatus'),(86,'Can change Социальный статус',22,'change_socialstatus'),(87,'Can delete Социальный статус',22,'delete_socialstatus'),(88,'Can view Социальный статус',22,'view_socialstatus'),(89,'Can add Тип ПТС',23,'add_typepts'),(90,'Can change Тип ПТС',23,'change_typepts'),(91,'Can delete Тип ПТС',23,'delete_typepts'),(92,'Can view Тип ПТС',23,'view_typepts'),(93,'Can add Тип документа пользователя',24,'add_userdocumenttype'),(94,'Can change Тип документа пользователя',24,'change_userdocumenttype'),(95,'Can delete Тип документа пользователя',24,'delete_userdocumenttype'),(96,'Can view Тип документа пользователя',24,'view_userdocumenttype'),(97,'Can add Информация о машине',25,'add_carinfo'),(98,'Can change Информация о машине',25,'change_carinfo'),(99,'Can delete Информация о машине',25,'delete_carinfo'),(100,'Can view Информация о машине',25,'view_carinfo'),(101,'Can add Гражданство клиента',26,'add_citizenship'),(102,'Can change Гражданство клиента',26,'change_citizenship'),(103,'Can delete Гражданство клиента',26,'delete_citizenship'),(104,'Can view Гражданство клиента',26,'view_citizenship'),(105,'Can add Документ продажи автомобиля',27,'add_documentsaleauto'),(106,'Can change Документ продажи автомобиля',27,'change_documentsaleauto'),(107,'Can delete Документ продажи автомобиля',27,'delete_documentsaleauto'),(108,'Can view Документ продажи автомобиля',27,'view_documentsaleauto'),(109,'Can add Загруженный документ клиента',28,'add_clientuploaddocument'),(110,'Can change Загруженный документ клиента',28,'change_clientuploaddocument'),(111,'Can delete Загруженный документ клиента',28,'delete_clientuploaddocument'),(112,'Can view Загруженный документ клиента',28,'view_clientuploaddocument'),(113,'Can add Водительское удостоверение клиента',29,'add_driverlicense'),(114,'Can change Водительское удостоверение клиента',29,'change_driverlicense'),(115,'Can delete Водительское удостоверение клиента',29,'delete_driverlicense'),(116,'Can view Водительское удостоверение клиента',29,'view_driverlicense'),(117,'Can add Образование клиента',30,'add_education'),(118,'Can change Образование клиента',30,'change_education'),(119,'Can delete Образование клиента',30,'delete_education'),(120,'Can view Образование клиента',30,'view_education'),(121,'Can add Расходы клиента',31,'add_expenses'),(122,'Can change Расходы клиента',31,'change_expenses'),(123,'Can delete Расходы клиента',31,'delete_expenses'),(124,'Can view Расходы клиента',31,'view_expenses'),(125,'Can add Дополнительное страхование',32,'add_extrainsurance'),(126,'Can change Дополнительное страхование',32,'change_extrainsurance'),(127,'Can delete Дополнительное страхование',32,'delete_extrainsurance'),(128,'Can view Дополнительное страхование',32,'view_extrainsurance'),(129,'Can add Финансовая информация клиента',33,'add_financialinfo'),(130,'Can change Финансовая информация клиента',33,'change_financialinfo'),(131,'Can delete Финансовая информация клиента',33,'delete_financialinfo'),(132,'Can view Финансовая информация клиента',33,'view_financialinfo'),(133,'Can add Условия финансирования',34,'add_financingconditions'),(134,'Can change Условия финансирования',34,'change_financingconditions'),(135,'Can delete Условия финансирования',34,'delete_financingconditions'),(136,'Can view Условия финансирования',34,'view_financingconditions'),(137,'Can add Заявка',35,'add_allapplications'),(138,'Can change Заявка',35,'change_allapplications'),(139,'Can delete Заявка',35,'delete_allapplications'),(140,'Can view Заявка',35,'view_allapplications'),(141,'Can add Загранпаспорт клиента',36,'add_internationalpassport'),(142,'Can change Загранпаспорт клиента',36,'change_internationalpassport'),(143,'Can delete Загранпаспорт клиента',36,'delete_internationalpassport'),(144,'Can view Загранпаспорт клиента',36,'view_internationalpassport'),(145,'Can add Семейная информация клиента',37,'add_familyinfo'),(146,'Can change Семейная информация клиента',37,'change_familyinfo'),(147,'Can delete Семейная информация клиента',37,'delete_familyinfo'),(148,'Can view Семейная информация клиента',37,'view_familyinfo'),(149,'Can add Предложение клиента',38,'add_offersclient'),(150,'Can change Предложение клиента',38,'change_offersclient'),(151,'Can delete Предложение клиента',38,'delete_offersclient'),(152,'Can view Предложение клиента',38,'view_offersclient'),(153,'Can add Паспортные данные клиента',39,'add_passportclient'),(154,'Can change Паспортные данные клиента',39,'change_passportclient'),(155,'Can delete Паспортные данные клиента',39,'delete_passportclient'),(156,'Can view Паспортные данные клиента',39,'view_passportclient'),(157,'Can add Пенсионное свидетельство клиента',40,'add_pensioncertificate'),(158,'Can change Пенсионное свидетельство клиента',40,'change_pensioncertificate'),(159,'Can delete Пенсионное свидетельство клиента',40,'delete_pensioncertificate'),(160,'Can view Пенсионное свидетельство клиента',40,'view_pensioncertificate'),(161,'Can add Контактные данные клиента',41,'add_contactclient'),(162,'Can change Контактные данные клиента',41,'change_contactclient'),(163,'Can delete Контактные данные клиента',41,'delete_contactclient'),(164,'Can view Контактные данные клиента',41,'view_contactclient'),(165,'Can add Трудоустройство клиента',42,'add_employment'),(166,'Can change Трудоустройство клиента',42,'change_employment'),(167,'Can delete Трудоустройство клиента',42,'delete_employment'),(168,'Can view Трудоустройство клиента',42,'view_employment'),(169,'Can add Недвижимость клиента',43,'add_realestate'),(170,'Can change Недвижимость клиента',43,'change_realestate'),(171,'Can delete Недвижимость клиента',43,'delete_realestate'),(172,'Can view Недвижимость клиента',43,'view_realestate'),(173,'Can add Выбранное предложение клиента',44,'add_selectoffersclient'),(174,'Can change Выбранное предложение клиента',44,'change_selectoffersclient'),(175,'Can delete Выбранное предложение клиента',44,'delete_selectoffersclient'),(176,'Can view Выбранное предложение клиента',44,'view_selectoffersclient'),(177,'Can add Личная информация клиента',45,'add_clientinfopersonal'),(178,'Can change Личная информация клиента',45,'change_clientinfopersonal'),(179,'Can delete Личная информация клиента',45,'delete_clientinfopersonal'),(180,'Can view Личная информация клиента',45,'view_clientinfopersonal'),(181,'Can add Налоговый документ клиента',46,'add_taxdocument'),(182,'Can change Налоговый документ клиента',46,'change_taxdocument'),(183,'Can delete Налоговый документ клиента',46,'delete_taxdocument'),(184,'Can view Налоговый документ клиента',46,'view_taxdocument'),(185,'Can add Загруженный документ пользователя',47,'add_userdocument'),(186,'Can change Загруженный документ пользователя',47,'change_userdocument'),(187,'Can delete Загруженный документ пользователя',47,'delete_userdocument'),(188,'Can view Загруженный документ пользователя',47,'view_userdocument'),(189,'Can add Профиль',48,'add_userprofile'),(190,'Can change Профиль',48,'change_userprofile'),(191,'Can delete Профиль',48,'delete_userprofile'),(192,'Can view Профиль',48,'view_userprofile'),(193,'Can add Транспортное средство клиента',49,'add_vehicle'),(194,'Can change Транспортное средство клиента',49,'change_vehicle'),(195,'Can delete Транспортное средство клиента',49,'delete_vehicle'),(196,'Can view Транспортное средство клиента',49,'view_vehicle'),(197,'Can add log entry',50,'add_logentry'),(198,'Can change log entry',50,'change_logentry'),(199,'Can delete log entry',50,'delete_logentry'),(200,'Can view log entry',50,'view_logentry'),(201,'Can add permission',51,'add_permission'),(202,'Can change permission',51,'change_permission'),(203,'Can delete permission',51,'delete_permission'),(204,'Can view permission',51,'view_permission'),(205,'Can add group',52,'add_group'),(206,'Can change group',52,'change_group'),(207,'Can delete group',52,'delete_group'),(208,'Can view group',52,'view_group'),(209,'Can add user',53,'add_user'),(210,'Can change user',53,'change_user'),(211,'Can delete user',53,'delete_user'),(212,'Can view user',53,'view_user'),(213,'Can add content type',54,'add_contenttype'),(214,'Can change content type',54,'change_contenttype'),(215,'Can delete content type',54,'delete_contenttype'),(216,'Can view content type',54,'view_contenttype'),(217,'Can add session',55,'add_session'),(218,'Can change session',55,'change_session'),(219,'Can delete session',55,'delete_session'),(220,'Can view session',55,'view_session'),(221,'Can add Документ продажи автомобиля',56,'add_autosaledocument'),(222,'Can change Документ продажи автомобиля',56,'change_autosaledocument'),(223,'Can delete Документ продажи автомобиля',56,'delete_autosaledocument'),(224,'Can view Документ продажи автомобиля',56,'view_autosaledocument'),(225,'Can add Условия финансирования',57,'add_clientfinancingcondition'),(226,'Can change Условия финансирования',57,'change_clientfinancingcondition'),(227,'Can delete Условия финансирования',57,'delete_clientfinancingcondition'),(228,'Can view Условия финансирования',57,'view_clientfinancingcondition'),(229,'Can add Дополнительное страхование',58,'add_clientextrainsurance'),(230,'Can change Дополнительное страхование',58,'change_clientextrainsurance'),(231,'Can delete Дополнительное страхование',58,'delete_clientextrainsurance'),(232,'Can view Дополнительное страхование',58,'view_clientextrainsurance'),(233,'Can add Информация о машине',59,'add_clientcarinfo'),(234,'Can change Информация о машине',59,'change_clientcarinfo'),(235,'Can delete Информация о машине',59,'delete_clientcarinfo'),(236,'Can view Информация о машине',59,'view_clientcarinfo'),(237,'Can add Марка автомобиля',60,'add_carbrand'),(238,'Can change Марка автомобиля',60,'change_carbrand'),(239,'Can delete Марка автомобиля',60,'delete_carbrand'),(240,'Can view Марка автомобиля',60,'view_carbrand'),(241,'Can add Загруженный документ клиента',61,'add_clientdocument'),(242,'Can change Загруженный документ клиента',61,'change_clientdocument'),(243,'Can delete Загруженный документ клиента',61,'delete_clientdocument'),(244,'Can view Загруженный документ клиента',61,'view_clientdocument'),(245,'Can add Предложение клиента',62,'add_clientoffer'),(246,'Can change Предложение клиента',62,'change_clientoffer'),(247,'Can delete Предложение клиента',62,'delete_clientoffer'),(248,'Can view Предложение клиента',62,'view_clientoffer'),(249,'Can add Загранпаспорт клиента',63,'add_clientinternationalpassport'),(250,'Can change Загранпаспорт клиента',63,'change_clientinternationalpassport'),(251,'Can delete Загранпаспорт клиента',63,'delete_clientinternationalpassport'),(252,'Can view Загранпаспорт клиента',63,'view_clientinternationalpassport'),(253,'Can add Трудоустройство клиента',64,'add_clientemployment'),(254,'Can change Трудоустройство клиента',64,'change_clientemployment'),(255,'Can delete Трудоустройство клиента',64,'delete_clientemployment'),(256,'Can view Трудоустройство клиента',64,'view_clientemployment'),(257,'Can add Семейная информация клиента',65,'add_clientfamilyinfo'),(258,'Can change Семейная информация клиента',65,'change_clientfamilyinfo'),(259,'Can delete Семейная информация клиента',65,'delete_clientfamilyinfo'),(260,'Can view Семейная информация клиента',65,'view_clientfamilyinfo'),(261,'Can add Контактные данные клиента',66,'add_clientcontact'),(262,'Can change Контактные данные клиента',66,'change_clientcontact'),(263,'Can delete Контактные данные клиента',66,'delete_clientcontact'),(264,'Can view Контактные данные клиента',66,'view_clientcontact'),(265,'Can add Налоговый документ клиента',67,'add_clienttaxdocument'),(266,'Can change Налоговый документ клиента',67,'change_clienttaxdocument'),(267,'Can delete Налоговый документ клиента',67,'delete_clienttaxdocument'),(268,'Can view Налоговый документ клиента',67,'view_clienttaxdocument'),(269,'Can add Транспортное средство клиента',68,'add_clientvehicle'),(270,'Can change Транспортное средство клиента',68,'change_clientvehicle'),(271,'Can delete Транспортное средство клиента',68,'delete_clientvehicle'),(272,'Can view Транспортное средство клиента',68,'view_clientvehicle'),(273,'Can add Гражданство клиента',69,'add_clientcitizenship'),(274,'Can change Гражданство клиента',69,'change_clientcitizenship'),(275,'Can delete Гражданство клиента',69,'delete_clientcitizenship'),(276,'Can view Гражданство клиента',69,'view_clientcitizenship'),(277,'Can add Личная информация клиента',70,'add_clientpersonalinfo'),(278,'Can change Личная информация клиента',70,'change_clientpersonalinfo'),(279,'Can delete Личная информация клиента',70,'delete_clientpersonalinfo'),(280,'Can view Личная информация клиента',70,'view_clientpersonalinfo'),(281,'Can add Финансовая информация клиента',71,'add_clientfinancialinfo'),(282,'Can change Финансовая информация клиента',71,'change_clientfinancialinfo'),(283,'Can delete Финансовая информация клиента',71,'delete_clientfinancialinfo'),(284,'Can view Финансовая информация клиента',71,'view_clientfinancialinfo'),(285,'Can add Выбранное предложение клиента',72,'add_selectedclientoffer'),(286,'Can change Выбранное предложение клиента',72,'change_selectedclientoffer'),(287,'Can delete Выбранное предложение клиента',72,'delete_selectedclientoffer'),(288,'Can view Выбранное предложение клиента',72,'view_selectedclientoffer'),(289,'Can add Пенсионное свидетельство клиента',73,'add_clientpensioncertificate'),(290,'Can change Пенсионное свидетельство клиента',73,'change_clientpensioncertificate'),(291,'Can delete Пенсионное свидетельство клиента',73,'delete_clientpensioncertificate'),(292,'Can view Пенсионное свидетельство клиента',73,'view_clientpensioncertificate'),(293,'Can add Водительское удостоверение клиента',74,'add_clientdriverlicense'),(294,'Can change Водительское удостоверение клиента',74,'change_clientdriverlicense'),(295,'Can delete Водительское удостоверение клиента',74,'delete_clientdriverlicense'),(296,'Can view Водительское удостоверение клиента',74,'view_clientdriverlicense'),(297,'Can add Образование клиента',75,'add_clienteducation'),(298,'Can change Образование клиента',75,'change_clienteducation'),(299,'Can delete Образование клиента',75,'delete_clienteducation'),(300,'Can view Образование клиента',75,'view_clienteducation'),(301,'Can add Недвижимость клиента',76,'add_clientrealestate'),(302,'Can change Недвижимость клиента',76,'change_clientrealestate'),(303,'Can delete Недвижимость клиента',76,'delete_clientrealestate'),(304,'Can view Недвижимость клиента',76,'view_clientrealestate'),(305,'Can add Паспортные данные клиента',77,'add_clientpassport'),(306,'Can change Паспортные данные клиента',77,'change_clientpassport'),(307,'Can delete Паспортные данные клиента',77,'delete_clientpassport'),(308,'Can view Паспортные данные клиента',77,'view_clientpassport'),(309,'Can add Расходы клиента',78,'add_clientexpenses'),(310,'Can change Расходы клиента',78,'change_clientexpenses'),(311,'Can delete Расходы клиента',78,'delete_clientexpenses'),(312,'Can view Расходы клиента',78,'view_clientexpenses'),(313,'Can add blacklisted token',79,'add_blacklistedtoken'),(314,'Can change blacklisted token',79,'change_blacklistedtoken'),(315,'Can delete blacklisted token',79,'delete_blacklistedtoken'),(316,'Can view blacklisted token',79,'view_blacklistedtoken'),(317,'Can add outstanding token',80,'add_outstandingtoken'),(318,'Can change outstanding token',80,'change_outstandingtoken'),(319,'Can delete outstanding token',80,'delete_outstandingtoken'),(320,'Can view outstanding token',80,'view_outstandingtoken'),(321,'Can add Комплектация автомобиля',81,'add_carconfiguration'),(322,'Can change Комплектация автомобиля',81,'change_carconfiguration'),(323,'Can delete Комплектация автомобиля',81,'delete_carconfiguration'),(324,'Can view Комплектация автомобиля',81,'view_carconfiguration'),(325,'Can add Предложение',82,'add_offers'),(326,'Can change Предложение',82,'change_offers'),(327,'Can delete Предложение',82,'delete_offers'),(328,'Can view Предложение',82,'view_offers'),(329,'Can add Недвижимость клиента',83,'add_clientrealestate'),(330,'Can change Недвижимость клиента',83,'change_clientrealestate'),(331,'Can delete Недвижимость клиента',83,'delete_clientrealestate'),(332,'Can view Недвижимость клиента',83,'view_clientrealestate'),(333,'Can add Загранпаспорт клиента',84,'add_clientinternationalpassport'),(334,'Can change Загранпаспорт клиента',84,'change_clientinternationalpassport'),(335,'Can delete Загранпаспорт клиента',84,'delete_clientinternationalpassport'),(336,'Can view Загранпаспорт клиента',84,'view_clientinternationalpassport'),(337,'Can add Пенсионное свидетельство клиента',85,'add_clientpensioncertificate'),(338,'Can change Пенсионное свидетельство клиента',85,'change_clientpensioncertificate'),(339,'Can delete Пенсионное свидетельство клиента',85,'delete_clientpensioncertificate'),(340,'Can view Пенсионное свидетельство клиента',85,'view_clientpensioncertificate'),(341,'Can add Уровень образования',86,'add_educationlevel'),(342,'Can change Уровень образования',86,'change_educationlevel'),(343,'Can delete Уровень образования',86,'delete_educationlevel'),(344,'Can view Уровень образования',86,'view_educationlevel'),(345,'Can add Тип документа',87,'add_documenttype'),(346,'Can change Тип документа',87,'change_documenttype'),(347,'Can delete Тип документа',87,'delete_documenttype'),(348,'Can view Тип документа',87,'view_documenttype'),(349,'Can add Тип недвижимости',88,'add_realestatetype'),(350,'Can change Тип недвижимости',88,'change_realestatetype'),(351,'Can delete Тип недвижимости',88,'delete_realestatetype'),(352,'Can view Тип недвижимости',88,'view_realestatetype'),(353,'Can add Гражданство клиента',89,'add_clientcitizenship'),(354,'Can change Гражданство клиента',89,'change_clientcitizenship'),(355,'Can delete Гражданство клиента',89,'delete_clientcitizenship'),(356,'Can view Гражданство клиента',89,'view_clientcitizenship'),(357,'Can add Семейная информация клиента',90,'add_clientfamilyinfo'),(358,'Can change Семейная информация клиента',90,'change_clientfamilyinfo'),(359,'Can delete Семейная информация клиента',90,'delete_clientfamilyinfo'),(360,'Can view Семейная информация клиента',90,'view_clientfamilyinfo'),(361,'Can add Тип должности',91,'add_positiontype'),(362,'Can change Тип должности',91,'change_positiontype'),(363,'Can delete Тип должности',91,'delete_positiontype'),(364,'Can view Тип должности',91,'view_positiontype'),(365,'Can add Тип жилья',92,'add_housingtype'),(366,'Can change Тип жилья',92,'change_housingtype'),(367,'Can delete Тип жилья',92,'delete_housingtype'),(368,'Can view Тип жилья',92,'view_housingtype'),(369,'Can add Трудоустройство клиента',93,'add_clientemployment'),(370,'Can change Трудоустройство клиента',93,'change_clientemployment'),(371,'Can delete Трудоустройство клиента',93,'delete_clientemployment'),(372,'Can view Трудоустройство клиента',93,'view_clientemployment'),(373,'Can add Загруженный документ клиента',94,'add_clientdocument'),(374,'Can change Загруженный документ клиента',94,'change_clientdocument'),(375,'Can delete Загруженный документ клиента',94,'delete_clientdocument'),(376,'Can view Загруженный документ клиента',94,'view_clientdocument'),(377,'Can add Срок финансирования',95,'add_financingterm'),(378,'Can change Срок финансирования',95,'change_financingterm'),(379,'Can delete Срок финансирования',95,'delete_financingterm'),(380,'Can view Срок финансирования',95,'view_financingterm'),(381,'Can add Тип организации',96,'add_organizationtype'),(382,'Can change Тип организации',96,'change_organizationtype'),(383,'Can delete Тип организации',96,'delete_organizationtype'),(384,'Can view Тип организации',96,'view_organizationtype'),(385,'Can add Налоговый документ клиента',97,'add_clienttaxdocument'),(386,'Can change Налоговый документ клиента',97,'change_clienttaxdocument'),(387,'Can delete Налоговый документ клиента',97,'delete_clienttaxdocument'),(388,'Can view Налоговый документ клиента',97,'view_clienttaxdocument'),(389,'Can add Паспортные данные клиента',98,'add_clientpassport'),(390,'Can change Паспортные данные клиента',98,'change_clientpassport'),(391,'Can delete Паспортные данные клиента',98,'delete_clientpassport'),(392,'Can view Паспортные данные клиента',98,'view_clientpassport'),(393,'Can add Условия финансирования',99,'add_clientfinancingcondition'),(394,'Can change Условия финансирования',99,'change_clientfinancingcondition'),(395,'Can delete Условия финансирования',99,'delete_clientfinancingcondition'),(396,'Can view Условия финансирования',99,'view_clientfinancingcondition'),(397,'Can add Семейное положение',100,'add_maritalstatus'),(398,'Can change Семейное положение',100,'change_maritalstatus'),(399,'Can delete Семейное положение',100,'delete_maritalstatus'),(400,'Can view Семейное положение',100,'view_maritalstatus'),(401,'Can add Состояние автомобиля',101,'add_carcondition'),(402,'Can change Состояние автомобиля',101,'change_carcondition'),(403,'Can delete Состояние автомобиля',101,'delete_carcondition'),(404,'Can view Состояние автомобиля',101,'view_carcondition'),(405,'Can add Тип двигателя',102,'add_enginetype'),(406,'Can change Тип двигателя',102,'change_enginetype'),(407,'Can delete Тип двигателя',102,'delete_enginetype'),(408,'Can view Тип двигателя',102,'view_enginetype'),(409,'Can add Финансовая информация клиента',103,'add_clientfinancialinfo'),(410,'Can change Финансовая информация клиента',103,'change_clientfinancialinfo'),(411,'Can delete Финансовая информация клиента',103,'delete_clientfinancialinfo'),(412,'Can view Финансовая информация клиента',103,'view_clientfinancialinfo'),(413,'Can add Заявка',104,'add_allapplications'),(414,'Can change Заявка',104,'change_allapplications'),(415,'Can delete Заявка',104,'delete_allapplications'),(416,'Can view Заявка',104,'view_allapplications'),(417,'Can add Образование клиента',105,'add_clienteducation'),(418,'Can change Образование клиента',105,'change_clienteducation'),(419,'Can delete Образование клиента',105,'delete_clienteducation'),(420,'Can view Образование клиента',105,'view_clienteducation'),(421,'Can add Транспортное средство клиента',106,'add_clientvehicle'),(422,'Can change Транспортное средство клиента',106,'change_clientvehicle'),(423,'Can delete Транспортное средство клиента',106,'delete_clientvehicle'),(424,'Can view Транспортное средство клиента',106,'view_clientvehicle'),(425,'Can add Расходы клиента',107,'add_clientexpenses'),(426,'Can change Расходы клиента',107,'change_clientexpenses'),(427,'Can delete Расходы клиента',107,'delete_clientexpenses'),(428,'Can view Расходы клиента',107,'view_clientexpenses'),(429,'Can add Дополнительное страхование',108,'add_clientextrainsurance'),(430,'Can change Дополнительное страхование',108,'change_clientextrainsurance'),(431,'Can delete Дополнительное страхование',108,'delete_clientextrainsurance'),(432,'Can view Дополнительное страхование',108,'view_clientextrainsurance'),(433,'Can add Способ приобретения',109,'add_purchasemethod'),(434,'Can change Способ приобретения',109,'change_purchasemethod'),(435,'Can delete Способ приобретения',109,'delete_purchasemethod'),(436,'Can view Способ приобретения',109,'view_purchasemethod'),(437,'Can add Социальный статус',110,'add_socialstatus'),(438,'Can change Социальный статус',110,'change_socialstatus'),(439,'Can delete Социальный статус',110,'delete_socialstatus'),(440,'Can view Социальный статус',110,'view_socialstatus'),(441,'Can add Код вида деятельности',111,'add_activitycode'),(442,'Can change Код вида деятельности',111,'change_activitycode'),(443,'Can delete Код вида деятельности',111,'delete_activitycode'),(444,'Can view Код вида деятельности',111,'view_activitycode'),(445,'Can add Документ продажи автомобиля',112,'add_autosaledocument'),(446,'Can change Документ продажи автомобиля',112,'change_autosaledocument'),(447,'Can delete Документ продажи автомобиля',112,'delete_autosaledocument'),(448,'Can view Документ продажи автомобиля',112,'view_autosaledocument'),(449,'Can add Выбранное предложение клиента',113,'add_selectedclientoffer'),(450,'Can change Выбранное предложение клиента',113,'change_selectedclientoffer'),(451,'Can delete Выбранное предложение клиента',113,'delete_selectedclientoffer'),(452,'Can view Выбранное предложение клиента',113,'view_selectedclientoffer'),(453,'Can add Страна',114,'add_country'),(454,'Can change Страна',114,'change_country'),(455,'Can delete Страна',114,'delete_country'),(456,'Can view Страна',114,'view_country'),(457,'Can add Водительское удостоверение клиента',115,'add_clientdriverlicense'),(458,'Can change Водительское удостоверение клиента',115,'change_clientdriverlicense'),(459,'Can delete Водительское удостоверение клиента',115,'delete_clientdriverlicense'),(460,'Can view Водительское удостоверение клиента',115,'view_clientdriverlicense'),(461,'Can add Контактные данные клиента',116,'add_clientcontact'),(462,'Can change Контактные данные клиента',116,'change_clientcontact'),(463,'Can delete Контактные данные клиента',116,'delete_clientcontact'),(464,'Can view Контактные данные клиента',116,'view_clientcontact'),(465,'Can add Предложение клиента',117,'add_clientoffer'),(466,'Can change Предложение клиента',117,'change_clientoffer'),(467,'Can delete Предложение клиента',117,'delete_clientoffer'),(468,'Can view Предложение клиента',117,'view_clientoffer'),(469,'Can add Информация о машине',118,'add_clientcarinfo'),(470,'Can change Информация о машине',118,'change_clientcarinfo'),(471,'Can delete Информация о машине',118,'delete_clientcarinfo'),(472,'Can view Информация о машине',118,'view_clientcarinfo'),(473,'Can add Клиент',119,'add_clientpredata'),(474,'Can change Клиент',119,'change_clientpredata'),(475,'Can delete Клиент',119,'delete_clientpredata'),(476,'Can view Клиент',119,'view_clientpredata'),(477,'Can add Пол',120,'add_gender'),(478,'Can change Пол',120,'change_gender'),(479,'Can delete Пол',120,'delete_gender'),(480,'Can view Пол',120,'view_gender'),(481,'Can add Экологический класс',121,'add_ecoclass'),(482,'Can change Экологический класс',121,'change_ecoclass'),(483,'Can delete Экологический класс',121,'delete_ecoclass'),(484,'Can view Экологический класс',121,'view_ecoclass'),(485,'Can add Тип телефона',122,'add_phonetype'),(486,'Can change Тип телефона',122,'change_phonetype'),(487,'Can delete Тип телефона',122,'delete_phonetype'),(488,'Can view Тип телефона',122,'view_phonetype'),(489,'Can add Тип ПТС',123,'add_typepts'),(490,'Can change Тип ПТС',123,'change_typepts'),(491,'Can delete Тип ПТС',123,'delete_typepts'),(492,'Can view Тип ПТС',123,'view_typepts'),(493,'Can add Личная информация клиента',124,'add_clientpersonalinfo'),(494,'Can change Личная информация клиента',124,'change_clientpersonalinfo'),(495,'Can delete Личная информация клиента',124,'delete_clientpersonalinfo'),(496,'Can view Личная информация клиента',124,'view_clientpersonalinfo'),(497,'Can add Марка автомобиля',125,'add_carbrand'),(498,'Can change Марка автомобиля',125,'change_carbrand'),(499,'Can delete Марка автомобиля',125,'delete_carbrand'),(500,'Can view Марка автомобиля',125,'view_carbrand'),(501,'Can add Профиль',126,'add_userprofile'),(502,'Can change Профиль',126,'change_userprofile'),(503,'Can delete Профиль',126,'delete_userprofile'),(504,'Can view Профиль',126,'view_userprofile'),(505,'Can add Тип документа пользователя',127,'add_userdocumenttype'),(506,'Can change Тип документа пользователя',127,'change_userdocumenttype'),(507,'Can delete Тип документа пользователя',127,'delete_userdocumenttype'),(508,'Can view Тип документа пользователя',127,'view_userdocumenttype'),(509,'Can add Дилерский центр',128,'add_dealership'),(510,'Can change Дилерский центр',128,'change_dealership'),(511,'Can delete Дилерский центр',128,'delete_dealership'),(512,'Can view Дилерский центр',128,'view_dealership'),(513,'Can add Загруженный документ пользователя',129,'add_userdocument'),(514,'Can change Загруженный документ пользователя',129,'change_userdocument'),(515,'Can delete Загруженный документ пользователя',129,'delete_userdocument'),(516,'Can view Загруженный документ пользователя',129,'view_userdocument'),(517,'Can add Код вида деятельности',132,'add_activitycode'),(518,'Can change Код вида деятельности',132,'change_activitycode'),(519,'Can delete Код вида деятельности',132,'delete_activitycode'),(520,'Can view Код вида деятельности',132,'view_activitycode'),(521,'Can add Марка автомобиля',133,'add_carbrand'),(522,'Can change Марка автомобиля',133,'change_carbrand'),(523,'Can delete Марка автомобиля',133,'delete_carbrand'),(524,'Can view Марка автомобиля',133,'view_carbrand'),(525,'Can add Состояние автомобиля',134,'add_carcondition'),(526,'Can change Состояние автомобиля',134,'change_carcondition'),(527,'Can delete Состояние автомобиля',134,'delete_carcondition'),(528,'Can view Состояние автомобиля',134,'view_carcondition'),(529,'Can add Комплектация автомобиля',135,'add_carconfiguration'),(530,'Can change Комплектация автомобиля',135,'change_carconfiguration'),(531,'Can delete Комплектация автомобиля',135,'delete_carconfiguration'),(532,'Can view Комплектация автомобиля',135,'view_carconfiguration'),(533,'Can add Клиент',136,'add_clientpredata'),(534,'Can change Клиент',136,'change_clientpredata'),(535,'Can delete Клиент',136,'delete_clientpredata'),(536,'Can view Клиент',136,'view_clientpredata'),(537,'Can add Страна',137,'add_country'),(538,'Can change Страна',137,'change_country'),(539,'Can delete Страна',137,'delete_country'),(540,'Can view Страна',137,'view_country'),(541,'Can add Тип документа',138,'add_documenttype'),(542,'Can change Тип документа',138,'change_documenttype'),(543,'Can delete Тип документа',138,'delete_documenttype'),(544,'Can view Тип документа',138,'view_documenttype'),(545,'Can add Экологический класс',139,'add_ecoclass'),(546,'Can change Экологический класс',139,'change_ecoclass'),(547,'Can delete Экологический класс',139,'delete_ecoclass'),(548,'Can view Экологический класс',139,'view_ecoclass'),(549,'Can add Уровень образования',140,'add_educationlevel'),(550,'Can change Уровень образования',140,'change_educationlevel'),(551,'Can delete Уровень образования',140,'delete_educationlevel'),(552,'Can view Уровень образования',140,'view_educationlevel'),(553,'Can add Тип двигателя',141,'add_enginetype'),(554,'Can change Тип двигателя',141,'change_enginetype'),(555,'Can delete Тип двигателя',141,'delete_enginetype'),(556,'Can view Тип двигателя',141,'view_enginetype'),(557,'Can add Срок финансирования',130,'add_financingterm'),(558,'Can change Срок финансирования',130,'change_financingterm'),(559,'Can delete Срок финансирования',130,'delete_financingterm'),(560,'Can view Срок финансирования',130,'view_financingterm'),(561,'Can add Пол',142,'add_gender'),(562,'Can change Пол',142,'change_gender'),(563,'Can delete Пол',142,'delete_gender'),(564,'Can view Пол',142,'view_gender'),(565,'Can add Тип жилья',143,'add_housingtype'),(566,'Can change Тип жилья',143,'change_housingtype'),(567,'Can delete Тип жилья',143,'delete_housingtype'),(568,'Can view Тип жилья',143,'view_housingtype'),(569,'Can add Семейное положение',144,'add_maritalstatus'),(570,'Can change Семейное положение',144,'change_maritalstatus'),(571,'Can delete Семейное положение',144,'delete_maritalstatus'),(572,'Can view Семейное положение',144,'view_maritalstatus'),(573,'Can add Предложение',131,'add_offers'),(574,'Can change Предложение',131,'change_offers'),(575,'Can delete Предложение',131,'delete_offers'),(576,'Can view Предложение',131,'view_offers'),(577,'Can add Тип организации',145,'add_organizationtype'),(578,'Can change Тип организации',145,'change_organizationtype'),(579,'Can delete Тип организации',145,'delete_organizationtype'),(580,'Can view Тип организации',145,'view_organizationtype'),(581,'Can add Тип телефона',146,'add_phonetype'),(582,'Can change Тип телефона',146,'change_phonetype'),(583,'Can delete Тип телефона',146,'delete_phonetype'),(584,'Can view Тип телефона',146,'view_phonetype'),(585,'Can add Тип должности',147,'add_positiontype'),(586,'Can change Тип должности',147,'change_positiontype'),(587,'Can delete Тип должности',147,'delete_positiontype'),(588,'Can view Тип должности',147,'view_positiontype'),(589,'Can add Способ приобретения',148,'add_purchasemethod'),(590,'Can change Способ приобретения',148,'change_purchasemethod'),(591,'Can delete Способ приобретения',148,'delete_purchasemethod'),(592,'Can view Способ приобретения',148,'view_purchasemethod'),(593,'Can add Тип недвижимости',149,'add_realestatetype'),(594,'Can change Тип недвижимости',149,'change_realestatetype'),(595,'Can delete Тип недвижимости',149,'delete_realestatetype'),(596,'Can view Тип недвижимости',149,'view_realestatetype'),(597,'Can add Социальный статус',150,'add_socialstatus'),(598,'Can change Социальный статус',150,'change_socialstatus'),(599,'Can delete Социальный статус',150,'delete_socialstatus'),(600,'Can view Социальный статус',150,'view_socialstatus'),(601,'Can add Тип ПТС',151,'add_typepts'),(602,'Can change Тип ПТС',151,'change_typepts'),(603,'Can delete Тип ПТС',151,'delete_typepts'),(604,'Can view Тип ПТС',151,'view_typepts'),(605,'Can add Тип документа пользователя',152,'add_userdocumenttype'),(606,'Can change Тип документа пользователя',152,'change_userdocumenttype'),(607,'Can delete Тип документа пользователя',152,'delete_userdocumenttype'),(608,'Can view Тип документа пользователя',152,'view_userdocumenttype'),(609,'Can add Информация о машине',153,'add_clientcarinfo'),(610,'Can change Информация о машине',153,'change_clientcarinfo'),(611,'Can delete Информация о машине',153,'delete_clientcarinfo'),(612,'Can view Информация о машине',153,'view_clientcarinfo'),(613,'Can add Пенсионное свидетельство клиента',154,'add_clientpensioncertificate'),(614,'Can change Пенсионное свидетельство клиента',154,'change_clientpensioncertificate'),(615,'Can delete Пенсионное свидетельство клиента',154,'delete_clientpensioncertificate'),(616,'Can view Пенсионное свидетельство клиента',154,'view_clientpensioncertificate'),(617,'Can add Паспортные данные клиента',155,'add_clientpassport'),(618,'Can change Паспортные данные клиента',155,'change_clientpassport'),(619,'Can delete Паспортные данные клиента',155,'delete_clientpassport'),(620,'Can view Паспортные данные клиента',155,'view_clientpassport'),(621,'Can add Предложение клиента',156,'add_clientoffer'),(622,'Can change Предложение клиента',156,'change_clientoffer'),(623,'Can delete Предложение клиента',156,'delete_clientoffer'),(624,'Can view Предложение клиента',156,'view_clientoffer'),(625,'Can add Загранпаспорт клиента',157,'add_clientinternationalpassport'),(626,'Can change Загранпаспорт клиента',157,'change_clientinternationalpassport'),(627,'Can delete Загранпаспорт клиента',157,'delete_clientinternationalpassport'),(628,'Can view Загранпаспорт клиента',157,'view_clientinternationalpassport'),(629,'Can add Условия финансирования',158,'add_clientfinancingcondition'),(630,'Can change Условия финансирования',158,'change_clientfinancingcondition'),(631,'Can delete Условия финансирования',158,'delete_clientfinancingcondition'),(632,'Can view Условия финансирования',158,'view_clientfinancingcondition'),(633,'Can add Финансовая информация клиента',159,'add_clientfinancialinfo'),(634,'Can change Финансовая информация клиента',159,'change_clientfinancialinfo'),(635,'Can delete Финансовая информация клиента',159,'delete_clientfinancialinfo'),(636,'Can view Финансовая информация клиента',159,'view_clientfinancialinfo'),(637,'Can add Дополнительное страхование',160,'add_clientextrainsurance'),(638,'Can change Дополнительное страхование',160,'change_clientextrainsurance'),(639,'Can delete Дополнительное страхование',160,'delete_clientextrainsurance'),(640,'Can view Дополнительное страхование',160,'view_clientextrainsurance'),(641,'Can add Расходы клиента',161,'add_clientexpenses'),(642,'Can change Расходы клиента',161,'change_clientexpenses'),(643,'Can delete Расходы клиента',161,'delete_clientexpenses'),(644,'Can view Расходы клиента',161,'view_clientexpenses'),(645,'Can add Водительское удостоверение клиента',162,'add_clientdriverlicense'),(646,'Can change Водительское удостоверение клиента',162,'change_clientdriverlicense'),(647,'Can delete Водительское удостоверение клиента',162,'delete_clientdriverlicense'),(648,'Can view Водительское удостоверение клиента',162,'view_clientdriverlicense'),(649,'Can add Документ продажи автомобиля',163,'add_autosaledocument'),(650,'Can change Документ продажи автомобиля',163,'change_autosaledocument'),(651,'Can delete Документ продажи автомобиля',163,'delete_autosaledocument'),(652,'Can view Документ продажи автомобиля',163,'view_autosaledocument'),(653,'Can add Заявка',164,'add_allapplications'),(654,'Can change Заявка',164,'change_allapplications'),(655,'Can delete Заявка',164,'delete_allapplications'),(656,'Can view Заявка',164,'view_allapplications'),(657,'Can add Налоговый документ клиента',165,'add_clienttaxdocument'),(658,'Can change Налоговый документ клиента',165,'change_clienttaxdocument'),(659,'Can delete Налоговый документ клиента',165,'delete_clienttaxdocument'),(660,'Can view Налоговый документ клиента',165,'view_clienttaxdocument'),(661,'Can add Гражданство клиента',166,'add_clientcitizenship'),(662,'Can change Гражданство клиента',166,'change_clientcitizenship'),(663,'Can delete Гражданство клиента',166,'delete_clientcitizenship'),(664,'Can view Гражданство клиента',166,'view_clientcitizenship'),(665,'Can add Загруженный документ клиента',167,'add_clientdocument'),(666,'Can change Загруженный документ клиента',167,'change_clientdocument'),(667,'Can delete Загруженный документ клиента',167,'delete_clientdocument'),(668,'Can view Загруженный документ клиента',167,'view_clientdocument'),(669,'Can add Образование клиента',168,'add_clienteducation'),(670,'Can change Образование клиента',168,'change_clienteducation'),(671,'Can delete Образование клиента',168,'delete_clienteducation'),(672,'Can view Образование клиента',168,'view_clienteducation'),(673,'Can add Семейная информация клиента',169,'add_clientfamilyinfo'),(674,'Can change Семейная информация клиента',169,'change_clientfamilyinfo'),(675,'Can delete Семейная информация клиента',169,'delete_clientfamilyinfo'),(676,'Can view Семейная информация клиента',169,'view_clientfamilyinfo'),(677,'Can add Контактные данные клиента',170,'add_clientcontact'),(678,'Can change Контактные данные клиента',170,'change_clientcontact'),(679,'Can delete Контактные данные клиента',170,'delete_clientcontact'),(680,'Can view Контактные данные клиента',170,'view_clientcontact'),(681,'Can add Трудоустройство клиента',171,'add_clientemployment'),(682,'Can change Трудоустройство клиента',171,'change_clientemployment'),(683,'Can delete Трудоустройство клиента',171,'delete_clientemployment'),(684,'Can view Трудоустройство клиента',171,'view_clientemployment'),(685,'Can add Транспортное средство клиента',172,'add_clientvehicle'),(686,'Can change Транспортное средство клиента',172,'change_clientvehicle'),(687,'Can delete Транспортное средство клиента',172,'delete_clientvehicle'),(688,'Can view Транспортное средство клиента',172,'view_clientvehicle'),(689,'Can add Недвижимость клиента',173,'add_clientrealestate'),(690,'Can change Недвижимость клиента',173,'change_clientrealestate'),(691,'Can delete Недвижимость клиента',173,'delete_clientrealestate'),(692,'Can view Недвижимость клиента',173,'view_clientrealestate'),(693,'Can add Выбранное предложение клиента',174,'add_selectedclientoffer'),(694,'Can change Выбранное предложение клиента',174,'change_selectedclientoffer'),(695,'Can delete Выбранное предложение клиента',174,'delete_selectedclientoffer'),(696,'Can view Выбранное предложение клиента',174,'view_selectedclientoffer'),(697,'Can add Личная информация клиента',175,'add_clientpersonalinfo'),(698,'Can change Личная информация клиента',175,'change_clientpersonalinfo'),(699,'Can delete Личная информация клиента',175,'delete_clientpersonalinfo'),(700,'Can view Личная информация клиента',175,'view_clientpersonalinfo'),(701,'Can add Загруженный документ пользователя',176,'add_userdocument'),(702,'Can change Загруженный документ пользователя',176,'change_userdocument'),(703,'Can delete Загруженный документ пользователя',176,'delete_userdocument'),(704,'Can view Загруженный документ пользователя',176,'view_userdocument'),(705,'Can add log entry',177,'add_logentry'),(706,'Can change log entry',177,'change_logentry'),(707,'Can delete log entry',177,'delete_logentry'),(708,'Can view log entry',177,'view_logentry'),(709,'Can add permission',178,'add_permission'),(710,'Can change permission',178,'change_permission'),(711,'Can delete permission',178,'delete_permission'),(712,'Can view permission',178,'view_permission'),(713,'Can add group',179,'add_group'),(714,'Can change group',179,'change_group'),(715,'Can delete group',179,'delete_group'),(716,'Can view group',179,'view_group'),(717,'Can add user',180,'add_user'),(718,'Can change user',180,'change_user'),(719,'Can delete user',180,'delete_user'),(720,'Can view user',180,'view_user'),(721,'Can add content type',181,'add_contenttype'),(722,'Can change content type',181,'change_contenttype'),(723,'Can delete content type',181,'delete_contenttype'),(724,'Can view content type',181,'view_contenttype'),(725,'Can add session',182,'add_session'),(726,'Can change session',182,'change_session'),(727,'Can delete session',182,'delete_session'),(728,'Can view session',182,'view_session'),(729,'Can add Дилерский центр',183,'add_dealership'),(730,'Can change Дилерский центр',183,'change_dealership'),(731,'Can delete Дилерский центр',183,'delete_dealership'),(732,'Can view Дилерский центр',183,'view_dealership'),(733,'Can add Профиль',184,'add_userprofile'),(734,'Can change Профиль',184,'change_userprofile'),(735,'Can delete Профиль',184,'delete_userprofile'),(736,'Can view Профиль',184,'view_userprofile'),(737,'Can add Тип документа пользователя',185,'add_userdocumenttype'),(738,'Can change Тип документа пользователя',185,'change_userdocumenttype'),(739,'Can delete Тип документа пользователя',185,'delete_userdocumenttype'),(740,'Can view Тип документа пользователя',185,'view_userdocumenttype'),(741,'Can add Загруженный документ пользователя',186,'add_userdocument'),(742,'Can change Загруженный документ пользователя',186,'change_userdocument'),(743,'Can delete Загруженный документ пользователя',186,'delete_userdocument'),(744,'Can view Загруженный документ пользователя',186,'view_userdocument'),(745,'Can add crontab',187,'add_crontabschedule'),(746,'Can change crontab',187,'change_crontabschedule'),(747,'Can delete crontab',187,'delete_crontabschedule'),(748,'Can view crontab',187,'view_crontabschedule'),(749,'Can add interval',188,'add_intervalschedule'),(750,'Can change interval',188,'change_intervalschedule'),(751,'Can delete interval',188,'delete_intervalschedule'),(752,'Can view interval',188,'view_intervalschedule'),(753,'Can add periodic task',189,'add_periodictask'),(754,'Can change periodic task',189,'change_periodictask'),(755,'Can delete periodic task',189,'delete_periodictask'),(756,'Can view periodic task',189,'view_periodictask'),(757,'Can add periodic task track',190,'add_periodictasks'),(758,'Can change periodic task track',190,'change_periodictasks'),(759,'Can delete periodic task track',190,'delete_periodictasks'),(760,'Can view periodic task track',190,'view_periodictasks'),(761,'Can add solar event',191,'add_solarschedule'),(762,'Can change solar event',191,'change_solarschedule'),(763,'Can delete solar event',191,'delete_solarschedule'),(764,'Can view solar event',191,'view_solarschedule'),(765,'Can add clocked',192,'add_clockedschedule'),(766,'Can change clocked',192,'change_clockedschedule'),(767,'Can delete clocked',192,'delete_clockedschedule'),(768,'Can view clocked',192,'view_clockedschedule');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=187 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$870000$3eZoiSxyolcoCqgei5x8Lg$Hl+D5NFOH8s+/jB/adO7K1syMjDW3kIyQI6CDNGz2RA=','2024-09-17 13:46:02.397524',1,'admin','','','faiver902@gmail.com',1,1,'2024-05-29 11:47:38.000000'),(2,'pbkdf2_sha256$870000$tx6pEGIZcorDQmxYvhNhhN$vNcRtsGeBSJU/xNKb5/lt/Xbre7HVcFUIsCO9M8ygXM=','2024-09-12 11:31:20.995502',0,'owner_1','','','owner_1@mail.ru',0,1,'2024-07-23 09:56:54.000000'),(62,'pbkdf2_sha256$870000$hnHLEzUoaHiacmt3gcXdds$Nh8tm9i5ICVc3V5aqLgahqS+yIQm7i6AmXRRawDSsvg=','2024-09-12 11:36:06.718246',0,'test_user','','','test_user@gmail.com',0,1,'2024-06-30 13:37:17.000000'),(169,'pbkdf2_sha256$720000$govKmG4DBEmAFshqeX2OFs$/Fv+UClNl8RC2ntmJZism7USCqGTqvtjLGA1x4rDGKo=',NULL,0,'owner_2','','','owner_2@m.ru',0,1,'2024-08-14 14:42:26.000000'),(170,'pbkdf2_sha256$720000$0vzQBsYZC1xEQQ2VkD277X$noWGLrfxkPE8BK2Ya0HCp3fnRYTsslP8amdSlBqkRRs=',NULL,0,'owner_3','','','owner_3@n.ru',0,1,'2024-08-14 14:44:06.000000'),(178,'pbkdf2_sha256$870000$av53W2M0aCmIvvr5cZEqDX$JIlQTGaGqdPrYfZPgrtnCT55KkK1uCktOxWDS7a2m3E=','2024-09-05 13:37:29.879385',0,'user_1_1','','','fa2@mail.ru',0,1,'2024-09-05 13:33:30.734806'),(179,'pbkdf2_sha256$870000$OcK3nhUZK5fraNFI4xrryG$6nNNwSNPx/qAsJULUuEq0AETheSYmL2vc5oSTwqTWFg=','2024-09-11 16:16:50.563816',0,'user_1_2','','','fa2@mail.ru',0,1,'2024-09-05 13:39:13.905567'),(186,'pbkdf2_sha256$870000$tXAf255OQucF3ZzpmyM3aa$MNCpy6n9blTIb+/Q25O0VEAMdkKs1u+Z0ZxN1vLoFSQ=',NULL,0,'test_user2','','','test_user@gmail.com',0,1,'2024-09-12 11:30:28.698954');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (6,1,1),(3,2,2),(5,62,3),(4,169,2),(2,170,2),(7,178,3),(8,179,3),(15,186,3);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=350 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2024-07-23 08:04:29.427007','1',' ()',3,'',5,1),(2,'2024-07-23 08:07:54.697075','2',' ()',3,'',5,1),(3,'2024-07-23 08:11:28.918794','1','12',1,'[{\"added\": {}}]',12,1),(4,'2024-07-23 08:11:34.072201','2','60',1,'[{\"added\": {}}]',12,1),(5,'2024-07-23 08:14:22.795598','3',' ()',3,'',5,1),(6,'2024-07-24 16:33:59.557205','203',' ()',3,'',5,1),(7,'2024-07-24 16:33:59.566388','202',' ()',3,'',5,1),(8,'2024-07-24 16:33:59.567385','201',' ()',3,'',5,1),(9,'2024-07-24 16:33:59.569389','200',' ()',3,'',5,1),(10,'2024-07-24 16:33:59.571387','199',' ()',3,'',5,1),(11,'2024-07-24 16:33:59.573471','198',' ()',3,'',5,1),(12,'2024-07-24 16:33:59.575456','197',' ()',3,'',5,1),(13,'2024-07-24 16:33:59.577390','196',' ()',3,'',5,1),(14,'2024-07-24 16:33:59.580388','195',' ()',3,'',5,1),(15,'2024-07-24 16:33:59.582387','194',' ()',3,'',5,1),(16,'2024-07-24 16:33:59.584471','193',' ()',3,'',5,1),(17,'2024-07-24 16:33:59.587420','192',' ()',3,'',5,1),(18,'2024-07-24 16:33:59.589386','191',' ()',3,'',5,1),(19,'2024-07-24 16:33:59.591423','190',' ()',3,'',5,1),(20,'2024-07-24 16:33:59.593472','189',' ()',3,'',5,1),(21,'2024-07-24 16:33:59.595389','188',' ()',3,'',5,1),(22,'2024-07-24 16:33:59.597385','187',' ()',3,'',5,1),(23,'2024-07-24 16:33:59.599388','186',' ()',3,'',5,1),(24,'2024-07-24 16:33:59.602387','185',' ()',3,'',5,1),(25,'2024-07-24 16:33:59.604461','184',' ()',3,'',5,1),(26,'2024-07-24 16:33:59.606514','183',' ()',3,'',5,1),(27,'2024-07-24 16:33:59.608388','182',' ()',3,'',5,1),(28,'2024-07-24 16:33:59.611387','181',' ()',3,'',5,1),(29,'2024-07-24 16:33:59.613490','180',' ()',3,'',5,1),(30,'2024-07-24 16:33:59.615499','179',' ()',3,'',5,1),(31,'2024-07-24 16:33:59.618424','178',' ()',3,'',5,1),(32,'2024-07-24 16:33:59.620425','177',' ()',3,'',5,1),(33,'2024-07-24 16:33:59.622516','176',' ()',3,'',5,1),(34,'2024-07-24 16:33:59.624388','175',' ()',3,'',5,1),(35,'2024-07-24 16:33:59.627387','174',' ()',3,'',5,1),(36,'2024-07-24 16:33:59.629492','173',' ()',3,'',5,1),(37,'2024-07-24 16:33:59.631388','172',' ()',3,'',5,1),(38,'2024-07-24 16:33:59.634252','171',' ()',3,'',5,1),(39,'2024-07-24 16:33:59.636253','170',' ()',3,'',5,1),(40,'2024-07-24 16:33:59.639255','169',' ()',3,'',5,1),(41,'2024-07-24 16:33:59.641382','168',' ()',3,'',5,1),(42,'2024-07-24 16:33:59.643257','167',' ()',3,'',5,1),(43,'2024-07-24 16:33:59.645251','166',' ()',3,'',5,1),(44,'2024-07-24 16:33:59.647254','165',' ()',3,'',5,1),(45,'2024-07-24 16:33:59.650293','164',' ()',3,'',5,1),(46,'2024-07-24 16:33:59.652775','163',' ()',3,'',5,1),(47,'2024-07-24 16:33:59.654908','162',' ()',3,'',5,1),(48,'2024-07-24 16:33:59.657778','161',' ()',3,'',5,1),(49,'2024-07-24 16:33:59.659909','160',' ()',3,'',5,1),(50,'2024-07-24 16:33:59.662908','159',' ()',3,'',5,1),(51,'2024-07-24 16:33:59.665802','158',' ()',3,'',5,1),(52,'2024-07-24 16:33:59.668850','157',' ()',3,'',5,1),(53,'2024-07-24 16:33:59.671779','156',' ()',3,'',5,1),(54,'2024-07-24 16:33:59.674798','155',' ()',3,'',5,1),(55,'2024-07-24 16:33:59.677839','154',' ()',3,'',5,1),(56,'2024-07-24 16:33:59.680015','153',' ()',3,'',5,1),(57,'2024-07-24 16:33:59.683076','152',' ()',3,'',5,1),(58,'2024-07-24 16:33:59.685039','151',' ()',3,'',5,1),(59,'2024-07-24 16:33:59.688036','150',' ()',3,'',5,1),(60,'2024-07-24 16:33:59.691034','149',' ()',3,'',5,1),(61,'2024-07-24 16:33:59.693036','148',' ()',3,'',5,1),(62,'2024-07-24 16:33:59.696044','147',' ()',3,'',5,1),(63,'2024-07-24 16:33:59.699037','146',' ()',3,'',5,1),(64,'2024-07-24 16:33:59.702118','145',' ()',3,'',5,1),(65,'2024-07-24 16:33:59.705057','144',' ()',3,'',5,1),(66,'2024-07-24 16:33:59.708061','143',' ()',3,'',5,1),(67,'2024-07-24 16:33:59.710058','142',' ()',3,'',5,1),(68,'2024-07-24 16:33:59.713058','141',' ()',3,'',5,1),(69,'2024-07-24 16:33:59.716068','140',' ()',3,'',5,1),(70,'2024-07-24 16:33:59.719093','139',' ()',3,'',5,1),(71,'2024-07-24 16:33:59.721836','138',' ()',3,'',5,1),(72,'2024-07-24 16:33:59.725164','137',' ()',3,'',5,1),(73,'2024-07-24 16:33:59.728224','136',' ()',3,'',5,1),(74,'2024-07-24 16:33:59.730704','135',' ()',3,'',5,1),(75,'2024-07-24 16:33:59.733742','134',' ()',3,'',5,1),(76,'2024-07-24 16:33:59.736738','133',' ()',3,'',5,1),(77,'2024-07-24 16:33:59.739650','132',' ()',3,'',5,1),(78,'2024-07-24 16:33:59.742657','131',' ()',3,'',5,1),(79,'2024-07-24 16:33:59.745610','130',' ()',3,'',5,1),(80,'2024-07-24 16:33:59.748255','129',' ()',3,'',5,1),(81,'2024-07-24 16:33:59.751268','128',' ()',3,'',5,1),(82,'2024-07-24 16:33:59.754304','127',' ()',3,'',5,1),(83,'2024-07-24 16:33:59.757328','126',' ()',3,'',5,1),(84,'2024-07-24 16:33:59.760308','125',' ()',3,'',5,1),(85,'2024-07-24 16:33:59.763343','124',' ()',3,'',5,1),(86,'2024-07-24 16:33:59.766364','123',' ()',3,'',5,1),(87,'2024-07-24 16:33:59.769374','122',' ()',3,'',5,1),(88,'2024-07-24 16:33:59.772368','121',' ()',3,'',5,1),(89,'2024-07-24 16:33:59.774781','120',' ()',3,'',5,1),(90,'2024-07-24 16:33:59.777797','119',' ()',3,'',5,1),(91,'2024-07-24 16:33:59.779797','118',' ()',3,'',5,1),(92,'2024-07-24 16:33:59.782036','117',' ()',3,'',5,1),(93,'2024-07-24 16:33:59.785055','116',' ()',3,'',5,1),(94,'2024-07-24 16:33:59.787060','115',' ()',3,'',5,1),(95,'2024-07-24 16:33:59.790058','114',' ()',3,'',5,1),(96,'2024-07-24 16:33:59.793060','113',' ()',3,'',5,1),(97,'2024-07-24 16:33:59.796065','112',' ()',3,'',5,1),(98,'2024-07-24 16:33:59.799169','111',' ()',3,'',5,1),(99,'2024-07-24 16:33:59.803063','110',' ()',3,'',5,1),(100,'2024-07-24 16:33:59.806060','109',' ()',3,'',5,1),(101,'2024-07-24 16:33:59.809099','108',' ()',3,'',5,1),(102,'2024-07-24 16:33:59.811061','107',' ()',3,'',5,1),(103,'2024-07-24 16:33:59.814041','106',' ()',3,'',5,1),(104,'2024-07-24 16:33:59.817040','105',' ()',3,'',5,1),(105,'2024-07-24 16:33:59.820038','104',' ()',3,'',5,1),(106,'2024-07-24 16:35:07.482148','103',' ()',3,'',5,1),(107,'2024-07-24 16:35:07.490116','102',' ()',3,'',5,1),(108,'2024-07-24 16:35:07.492114','101',' ()',3,'',5,1),(109,'2024-07-24 16:35:07.494116','100',' ()',3,'',5,1),(110,'2024-07-24 16:35:07.495115','99',' ()',3,'',5,1),(111,'2024-07-24 16:35:07.497114','98',' ()',3,'',5,1),(112,'2024-07-24 16:35:07.498121','97',' ()',3,'',5,1),(113,'2024-07-24 16:35:07.500116','96',' ()',3,'',5,1),(114,'2024-07-24 16:35:07.502114','95',' ()',3,'',5,1),(115,'2024-07-24 16:35:07.503115','94',' ()',3,'',5,1),(116,'2024-07-24 16:35:07.505114','93',' ()',3,'',5,1),(117,'2024-07-24 16:35:07.506115','92',' ()',3,'',5,1),(118,'2024-07-24 16:35:07.508115','91',' ()',3,'',5,1),(119,'2024-07-24 16:35:07.510114','90',' ()',3,'',5,1),(120,'2024-07-24 16:35:07.511116','89',' ()',3,'',5,1),(121,'2024-07-24 16:35:07.513117','88',' ()',3,'',5,1),(122,'2024-07-24 16:35:07.515114','87',' ()',3,'',5,1),(123,'2024-07-24 16:35:07.516114','86',' ()',3,'',5,1),(124,'2024-07-24 16:35:07.518116','85',' ()',3,'',5,1),(125,'2024-07-24 16:35:07.520123','84',' ()',3,'',5,1),(126,'2024-07-24 16:35:07.523117','83',' ()',3,'',5,1),(127,'2024-07-24 16:35:07.524115','82',' ()',3,'',5,1),(128,'2024-07-24 16:35:07.526115','81',' ()',3,'',5,1),(129,'2024-07-24 16:35:07.528119','80',' ()',3,'',5,1),(130,'2024-07-24 16:35:07.529115','79',' ()',3,'',5,1),(131,'2024-07-24 16:35:07.531116','78',' ()',3,'',5,1),(132,'2024-07-24 16:35:07.533118','77',' ()',3,'',5,1),(133,'2024-07-24 16:35:07.534115','76',' ()',3,'',5,1),(134,'2024-07-24 16:35:07.536116','75',' ()',3,'',5,1),(135,'2024-07-24 16:35:07.537119','74',' ()',3,'',5,1),(136,'2024-07-24 16:35:07.539117','73',' ()',3,'',5,1),(137,'2024-07-24 16:35:07.540119','72',' ()',3,'',5,1),(138,'2024-07-24 16:35:07.542201','71',' ()',3,'',5,1),(139,'2024-07-24 16:35:07.544200','70',' ()',3,'',5,1),(140,'2024-07-24 16:35:07.546079','69',' ()',3,'',5,1),(141,'2024-07-24 16:35:07.548091','68',' ()',3,'',5,1),(142,'2024-07-24 16:35:07.550126','67',' ()',3,'',5,1),(143,'2024-07-24 16:35:07.552095','66',' ()',3,'',5,1),(144,'2024-07-24 16:35:07.554091','65',' ()',3,'',5,1),(145,'2024-07-24 16:35:07.556096','64',' ()',3,'',5,1),(146,'2024-07-24 16:35:07.558092','63',' ()',3,'',5,1),(147,'2024-07-24 16:35:07.560142','62',' ()',3,'',5,1),(148,'2024-07-24 16:35:07.562092','61',' ()',3,'',5,1),(149,'2024-07-24 16:35:07.563095','60',' ()',3,'',5,1),(150,'2024-07-24 16:35:07.565092','59',' ()',3,'',5,1),(151,'2024-07-24 16:35:07.566093','58',' ()',3,'',5,1),(152,'2024-07-24 16:35:07.568092','57',' ()',3,'',5,1),(153,'2024-07-24 16:35:07.570090','56',' ()',3,'',5,1),(154,'2024-07-24 16:35:07.571493','55',' ()',3,'',5,1),(155,'2024-07-24 16:35:07.573505','54',' ()',3,'',5,1),(156,'2024-07-24 16:35:07.574506','53',' ()',3,'',5,1),(157,'2024-07-24 16:35:07.576505','52',' ()',3,'',5,1),(158,'2024-07-24 16:35:07.578506','51',' ()',3,'',5,1),(159,'2024-07-24 16:35:07.580504','50',' ()',3,'',5,1),(160,'2024-07-24 16:35:07.581504','49',' ()',3,'',5,1),(161,'2024-07-24 16:35:07.583534','48',' ()',3,'',5,1),(162,'2024-07-24 16:35:07.584503','47',' ()',3,'',5,1),(163,'2024-07-24 16:35:07.586507','46',' ()',3,'',5,1),(164,'2024-07-24 16:35:07.588365','45',' ()',3,'',5,1),(165,'2024-07-24 16:35:07.589377','44',' ()',3,'',5,1),(166,'2024-07-24 16:35:07.591163','43',' ()',3,'',5,1),(167,'2024-07-24 16:35:07.593199','42',' ()',3,'',5,1),(168,'2024-07-24 16:35:07.595175','41',' ()',3,'',5,1),(169,'2024-07-24 16:35:07.596173','40',' ()',3,'',5,1),(170,'2024-07-24 16:35:07.598228','39',' ()',3,'',5,1),(171,'2024-07-24 16:35:07.600177','38',' ()',3,'',5,1),(172,'2024-07-24 16:35:07.602175','37',' ()',3,'',5,1),(173,'2024-07-24 16:35:07.604174','36',' ()',3,'',5,1),(174,'2024-07-24 16:35:07.605174','35',' ()',3,'',5,1),(175,'2024-07-24 16:35:07.607174','34',' ()',3,'',5,1),(176,'2024-07-24 16:35:07.609179','33',' ()',3,'',5,1),(177,'2024-07-24 16:35:07.611174','32',' ()',3,'',5,1),(178,'2024-07-24 16:35:07.612826','31',' ()',3,'',5,1),(179,'2024-07-24 16:35:07.613826','30',' ()',3,'',5,1),(180,'2024-07-24 16:35:07.615828','29',' ()',3,'',5,1),(181,'2024-07-24 16:35:07.616828','28',' ()',3,'',5,1),(182,'2024-07-24 16:35:07.618827','27',' ()',3,'',5,1),(183,'2024-07-24 16:35:07.620834','26',' ()',3,'',5,1),(184,'2024-07-24 16:35:07.621825','25',' ()',3,'',5,1),(185,'2024-07-24 16:35:07.623825','24',' ()',3,'',5,1),(186,'2024-07-24 16:35:07.624828','23',' ()',3,'',5,1),(187,'2024-07-24 16:35:07.626825','22',' ()',3,'',5,1),(188,'2024-07-24 16:35:07.627826','21',' ()',3,'',5,1),(189,'2024-07-24 16:35:07.629911','20',' ()',3,'',5,1),(190,'2024-07-24 16:35:07.631385','19',' ()',3,'',5,1),(191,'2024-07-24 16:35:07.632913','18',' ()',3,'',5,1),(192,'2024-07-24 16:35:07.633915','17',' ()',3,'',5,1),(193,'2024-07-24 16:35:07.635922','16',' ()',3,'',5,1),(194,'2024-07-24 16:35:07.637922','15',' ()',3,'',5,1),(195,'2024-07-24 16:35:07.638922','14',' ()',3,'',5,1),(196,'2024-07-24 16:35:07.640922','13',' ()',3,'',5,1),(197,'2024-07-24 16:35:07.642922','12',' ()',3,'',5,1),(198,'2024-07-24 16:35:07.643923','11',' ()',3,'',5,1),(199,'2024-07-24 16:35:07.645922','10',' ()',3,'',5,1),(200,'2024-07-24 16:35:07.646922','9',' ()',3,'',5,1),(201,'2024-07-24 16:35:07.648924','8',' ()',3,'',5,1),(202,'2024-07-24 16:35:07.650923','7',' ()',3,'',5,1),(203,'2024-07-24 16:35:07.652922','6',' ()',3,'',5,1),(204,'2024-07-24 16:35:07.654176','5',' ()',3,'',5,1),(205,'2024-07-24 16:35:07.656223','4',' (+7 (___) ___-__-__)',3,'',5,1),(206,'2024-08-07 07:26:33.450100','152','admin_2',3,'',53,1),(207,'2024-08-07 07:26:33.462180','153','admin_3',3,'',53,1),(208,'2024-08-07 07:26:33.466127','154','admin_4',3,'',53,1),(209,'2024-08-07 07:26:33.471181','155','admin_5',3,'',53,1),(210,'2024-08-07 07:26:33.475179','156','admin_6',3,'',53,1),(211,'2024-08-14 07:11:14.200672','204',' ()',3,'',5,1),(212,'2024-08-14 07:11:14.205704','205',' ()',3,'',5,1),(213,'2024-08-14 07:11:14.208672','206',' ()',3,'',5,1),(214,'2024-08-14 07:11:14.209706','207',' ()',3,'',5,1),(215,'2024-08-14 07:11:14.211703','208',' ()',3,'',5,1),(216,'2024-08-14 07:11:14.214672','209',' ()',3,'',5,1),(217,'2024-08-14 07:11:14.216672','210',' ()',3,'',5,1),(218,'2024-08-14 07:11:14.218672','211',' ()',3,'',5,1),(219,'2024-08-14 07:11:14.219717','212',' ()',3,'',5,1),(220,'2024-08-14 07:11:14.221671','213',' ()',3,'',5,1),(221,'2024-08-14 07:11:14.223733','214',' ()',3,'',5,1),(222,'2024-08-14 07:11:14.225672','215',' ()',3,'',5,1),(223,'2024-08-14 07:11:14.227671','216',' ()',3,'',5,1),(224,'2024-08-14 07:11:14.228707','217',' ()',3,'',5,1),(225,'2024-08-14 07:11:14.230703','218',' ()',3,'',5,1),(226,'2024-08-14 07:11:14.232733','219',' ()',3,'',5,1),(227,'2024-08-14 07:11:14.234703','220',' ()',3,'',5,1),(228,'2024-08-14 07:11:14.236672','221',' ()',3,'',5,1),(229,'2024-08-14 07:11:14.238672','222',' ()',3,'',5,1),(230,'2024-08-14 07:11:14.239712','223',' ()',3,'',5,1),(231,'2024-08-14 07:11:14.241702','224',' ()',3,'',5,1),(232,'2024-08-14 07:11:14.243704','225',' ()',3,'',5,1),(233,'2024-08-14 07:11:14.245673','226',' ()',3,'',5,1),(234,'2024-08-14 07:11:14.247672','227',' ()',3,'',5,1),(235,'2024-08-14 07:11:14.249706','228',' ()',3,'',5,1),(236,'2024-08-14 07:11:14.251694','229',' ()',3,'',5,1),(237,'2024-08-14 07:11:14.253672','230',' ()',3,'',5,1),(238,'2024-08-14 07:11:14.254672','231',' ()',3,'',5,1),(239,'2024-08-14 07:11:14.257672','232',' ()',3,'',5,1),(240,'2024-08-14 07:11:14.259672','233',' ()',3,'',5,1),(241,'2024-08-14 07:11:14.261604','234',' ()',3,'',5,1),(242,'2024-08-14 07:11:14.262602','235',' ()',3,'',5,1),(243,'2024-08-14 07:11:14.264602','236',' ()',3,'',5,1),(244,'2024-08-14 07:11:14.266607','237',' ()',3,'',5,1),(245,'2024-08-14 07:11:14.268605','238',' ()',3,'',5,1),(246,'2024-08-14 07:11:14.270602','239',' ()',3,'',5,1),(247,'2024-08-14 07:11:14.272601','240',' ()',3,'',5,1),(248,'2024-08-14 07:11:14.274656','241',' ()',3,'',5,1),(249,'2024-08-14 07:11:14.276653','242',' ()',3,'',5,1),(250,'2024-08-14 07:11:14.278132','243',' ()',3,'',5,1),(251,'2024-08-14 07:11:14.280144','244',' ()',3,'',5,1),(252,'2024-08-14 07:11:14.282180','245',' ()',3,'',5,1),(253,'2024-08-14 14:47:54.827924','31','user_1_1',3,'',53,1),(254,'2024-08-22 16:25:46.169886','256',' ()',3,'',5,1),(255,'2024-08-22 16:25:46.169886','255',' ()',3,'',5,1),(256,'2024-08-22 16:25:46.169886','254',' ()',3,'',5,1),(257,'2024-08-22 16:25:46.169886','253',' ()',3,'',5,1),(258,'2024-08-22 16:25:46.170855','252',' ()',3,'',5,1),(259,'2024-08-22 16:25:46.170855','251',' ()',3,'',5,1),(260,'2024-08-22 16:25:46.170855','250',' ()',3,'',5,1),(261,'2024-08-22 16:25:46.170855','249',' ()',3,'',5,1),(262,'2024-08-22 16:25:46.170855','248',' ()',3,'',5,1),(263,'2024-08-22 16:25:46.170855','247',' ()',3,'',5,1),(264,'2024-08-22 16:25:46.170855','246',' ()',3,'',5,1),(265,'2024-09-03 13:52:29.389747','263',' ()',3,'',5,1),(266,'2024-09-03 13:52:29.389813','262',' ()',3,'',5,1),(267,'2024-09-03 13:52:29.389848','261','робр ()',3,'',5,1),(268,'2024-09-03 13:52:29.389879','260',' ()',3,'',5,1),(269,'2024-09-03 13:52:29.389910','259',' ()',3,'',5,1),(270,'2024-09-03 13:52:29.389940','258',' ()',3,'',5,1),(271,'2024-09-03 13:52:29.389969','257',' ()',3,'',5,1),(272,'2024-09-04 11:41:36.444596','271','Заявка 271 для клиента  ()',3,'',35,1),(273,'2024-09-04 11:41:36.444684','270','Заявка 270 для клиента  ()',3,'',35,1),(274,'2024-09-04 11:41:36.444731','269','Заявка 269 для клиента  ()',3,'',35,1),(275,'2024-09-04 11:41:36.444774','268','Заявка 268 для клиента  ()',3,'',35,1),(276,'2024-09-04 11:41:36.444815','267','Заявка 267 для клиента  ()',3,'',35,1),(277,'2024-09-04 11:41:36.444857','266','Заявка 266 для клиента  ()',3,'',35,1),(278,'2024-09-04 11:41:36.444899','265','Заявка 265 для клиента  ()',3,'',35,1),(279,'2024-09-04 11:41:36.444941','264','Заявка 264 для клиента  ()',3,'',35,1),(280,'2024-09-04 11:41:46.484443','271',' ()',3,'',5,1),(281,'2024-09-04 11:41:46.484631','270',' ()',3,'',5,1),(282,'2024-09-04 11:41:46.484738','269',' ()',3,'',5,1),(283,'2024-09-04 11:41:46.484838','268',' ()',3,'',5,1),(284,'2024-09-04 11:41:46.484936','267',' ()',3,'',5,1),(285,'2024-09-04 11:41:46.485032','266',' ()',3,'',5,1),(286,'2024-09-04 11:41:46.485126','265',' ()',3,'',5,1),(287,'2024-09-04 11:41:46.485219','264',' ()',3,'',5,1),(288,'2024-09-04 11:41:46.836340','271',' ()',3,'',5,1),(289,'2024-09-04 11:41:46.836431','270',' ()',3,'',5,1),(290,'2024-09-04 11:41:46.836491','269',' ()',3,'',5,1),(291,'2024-09-04 11:41:46.836546','268',' ()',3,'',5,1),(292,'2024-09-04 11:41:46.836598','267',' ()',3,'',5,1),(293,'2024-09-04 11:41:46.836800','266',' ()',3,'',5,1),(294,'2024-09-04 11:41:46.836856','265',' ()',3,'',5,1),(295,'2024-09-04 11:41:46.837198','264',' ()',3,'',5,1),(296,'2024-09-05 13:26:17.658604','31','user_1_1',3,'',53,1),(297,'2024-09-05 13:28:32.975082','31','user_1_1',3,'',53,1),(298,'2024-09-05 13:28:43.660740','173','user_1_10',3,'',53,1),(299,'2024-09-05 13:28:43.661025','175','user_1_20',3,'',53,1),(300,'2024-09-05 13:30:00.100027','1','admin',2,'[]',53,1),(301,'2024-09-05 13:30:05.770338','1','admin',2,'[]',53,1),(302,'2024-09-05 13:30:12.380628','2','owner_1',2,'[]',53,1),(303,'2024-09-05 13:30:17.242316','169','owner_2',2,'[]',53,1),(304,'2024-09-05 13:30:21.579614','170','owner_3',2,'[]',53,1),(305,'2024-09-05 13:30:27.375279','62','test_user',2,'[]',53,1),(306,'2024-09-05 13:30:51.595838','170','owner_3',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',53,1),(307,'2024-09-05 13:30:57.847185','2','owner_1',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',53,1),(308,'2024-09-05 13:31:04.856115','169','owner_2',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',53,1),(309,'2024-09-05 13:31:14.223115','62','test_user',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',53,1),(310,'2024-09-05 13:31:20.770518','1','admin',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',53,1),(311,'2024-09-05 18:00:20.138433','1','Superusers',2,'[{\"changed\": {\"fields\": [\"Name\"]}}]',52,1),(312,'2024-09-08 07:20:22.661078','398','273 - Offer ID: 11 - Status: Ожидание решения',2,'[{\"changed\": {\"fields\": [\"Status select offer\"]}}]',72,1),(313,'2024-09-08 07:52:04.861170','400','273 - Offer ID: 10 - Status: Ожидание решения',2,'[{\"changed\": {\"fields\": [\"\\u041d\\u0430\\u0437\\u0432\\u0430\\u043d\\u0438\\u0435 \\u043f\\u0440\\u0435\\u0434\\u043b\\u043e\\u0436\\u0435\\u043d\\u0438\\u044f\", \"Status select offer\"]}}]',72,1),(314,'2024-09-08 09:13:38.758852','275',' ()',3,'',5,1),(315,'2024-09-08 09:13:38.758902','274',' ()',3,'',5,1),(316,'2024-09-08 09:13:38.758927','273',' ()',3,'',5,1),(317,'2024-09-08 09:13:38.758950','272',' ()',3,'',5,1),(318,'2024-09-09 12:45:07.428380','280',' ()',3,'',5,1),(319,'2024-09-09 12:45:07.428435','279',' ()',3,'',5,1),(320,'2024-09-09 12:45:07.428468','278',' ()',3,'',5,1),(321,'2024-09-09 12:45:07.428498','277',' ()',3,'',5,1),(322,'2024-09-09 12:45:07.428527','276',' ()',3,'',5,1),(323,'2024-09-10 11:23:20.442100','289',' ()',3,'',5,1),(324,'2024-09-10 11:23:20.442158','288',' ()',3,'',5,1),(325,'2024-09-10 11:23:20.442192','287',' ()',3,'',5,1),(326,'2024-09-10 11:23:20.442222','286',' ()',3,'',5,1),(327,'2024-09-10 11:23:20.442252','285',' ()',3,'',5,1),(328,'2024-09-10 11:23:20.442282','284',' ()',3,'',5,1),(329,'2024-09-10 11:23:20.442312','283',' ()',3,'',5,1),(330,'2024-09-10 11:23:20.442341','282',' ()',3,'',5,1),(331,'2024-09-10 11:23:20.442389','281',' ()',3,'',5,1),(332,'2024-09-16 16:53:33.987836','1','12',1,'[{\"added\": {}}]',130,1),(333,'2024-09-16 16:53:37.525461','2','60',1,'[{\"added\": {}}]',130,1),(334,'2024-09-16 17:45:44.616975','1','Название',1,'[{\"added\": {}}]',131,1),(335,'2024-09-16 17:46:02.321052','2','Название 2',1,'[{\"added\": {}}]',131,1),(336,'2024-09-16 18:08:23.189287','1','admin',1,'[{\"added\": {}}]',184,1),(337,'2024-09-16 18:09:08.171416','1','дц 1 1',1,'[{\"added\": {}}]',183,1),(338,'2024-09-16 18:09:15.013831','2','дц 1 2',1,'[{\"added\": {}}]',183,1),(339,'2024-09-16 18:09:25.802700','3','дц 2 1',1,'[{\"added\": {}}]',183,1),(340,'2024-09-16 18:09:37.209956','4','дц 22',1,'[{\"added\": {}}]',183,1),(341,'2024-09-17 08:07:46.819181','1','Водительское удостоверение',1,'[{\"added\": {}}]',138,1),(342,'2024-09-17 08:07:52.146497','2','Паспорт',1,'[{\"added\": {}}]',138,1),(343,'2024-09-17 09:20:18.420381','1','Паспорт',1,'[{\"added\": {}}]',152,1),(344,'2024-09-17 09:20:23.640361','2','Вод удост',1,'[{\"added\": {}}]',152,1),(345,'2024-09-17 09:52:53.076737','1','1',1,'[{\"added\": {}}]',185,1),(346,'2024-09-17 09:52:54.375264','2','2',1,'[{\"added\": {}}]',185,1),(347,'2024-09-17 09:52:55.372203','3','3',1,'[{\"added\": {}}]',185,1),(348,'2024-09-17 12:49:50.776416','1','celery.backend_cleanup: 0 4 * * * (m/h/dM/MY/d) Africa/Cairo',2,'[{\"changed\": {\"fields\": [\"Task (registered)\"]}}]',189,1),(349,'2024-09-17 12:50:03.297481','1','celery.backend_cleanup: 0 4 * * * (m/h/dM/MY/d) Africa/Cairo',2,'[{\"changed\": {\"fields\": [\"Task (registered)\"]}}]',189,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_beat_clockedschedule`
--

DROP TABLE IF EXISTS `django_celery_beat_clockedschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_celery_beat_clockedschedule` (
  `id` int NOT NULL AUTO_INCREMENT,
  `clocked_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_beat_clockedschedule`
--

LOCK TABLES `django_celery_beat_clockedschedule` WRITE;
/*!40000 ALTER TABLE `django_celery_beat_clockedschedule` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_celery_beat_clockedschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_beat_crontabschedule`
--

DROP TABLE IF EXISTS `django_celery_beat_crontabschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_celery_beat_crontabschedule` (
  `id` int NOT NULL AUTO_INCREMENT,
  `minute` varchar(240) NOT NULL,
  `hour` varchar(96) NOT NULL,
  `day_of_week` varchar(64) NOT NULL,
  `day_of_month` varchar(124) NOT NULL,
  `month_of_year` varchar(64) NOT NULL,
  `timezone` varchar(63) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_beat_crontabschedule`
--

LOCK TABLES `django_celery_beat_crontabschedule` WRITE;
/*!40000 ALTER TABLE `django_celery_beat_crontabschedule` DISABLE KEYS */;
INSERT INTO `django_celery_beat_crontabschedule` VALUES (3,'0','4','*','*','*','Africa/Cairo'),(4,'*','*','*','*','*','Africa/Cairo'),(5,'0','2','*','*','*','Africa/Cairo');
/*!40000 ALTER TABLE `django_celery_beat_crontabschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_beat_intervalschedule`
--

DROP TABLE IF EXISTS `django_celery_beat_intervalschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_celery_beat_intervalschedule` (
  `id` int NOT NULL AUTO_INCREMENT,
  `every` int NOT NULL,
  `period` varchar(24) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_beat_intervalschedule`
--

LOCK TABLES `django_celery_beat_intervalschedule` WRITE;
/*!40000 ALTER TABLE `django_celery_beat_intervalschedule` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_celery_beat_intervalschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_beat_periodictask`
--

DROP TABLE IF EXISTS `django_celery_beat_periodictask`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_celery_beat_periodictask` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `task` varchar(200) NOT NULL,
  `args` longtext NOT NULL,
  `kwargs` longtext NOT NULL,
  `queue` varchar(200) DEFAULT NULL,
  `exchange` varchar(200) DEFAULT NULL,
  `routing_key` varchar(200) DEFAULT NULL,
  `expires` datetime(6) DEFAULT NULL,
  `enabled` tinyint(1) NOT NULL,
  `last_run_at` datetime(6) DEFAULT NULL,
  `total_run_count` int unsigned NOT NULL,
  `date_changed` datetime(6) NOT NULL,
  `description` longtext NOT NULL,
  `crontab_id` int DEFAULT NULL,
  `interval_id` int DEFAULT NULL,
  `solar_id` int DEFAULT NULL,
  `one_off` tinyint(1) NOT NULL,
  `start_time` datetime(6) DEFAULT NULL,
  `priority` int unsigned DEFAULT NULL,
  `headers` longtext NOT NULL DEFAULT (_utf8mb3'{}'),
  `clocked_id` int DEFAULT NULL,
  `expire_seconds` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `django_celery_beat_p_crontab_id_d3cba168_fk_django_ce` (`crontab_id`),
  KEY `django_celery_beat_p_interval_id_a8ca27da_fk_django_ce` (`interval_id`),
  KEY `django_celery_beat_p_solar_id_a87ce72c_fk_django_ce` (`solar_id`),
  KEY `django_celery_beat_p_clocked_id_47a69f82_fk_django_ce` (`clocked_id`),
  CONSTRAINT `django_celery_beat_p_clocked_id_47a69f82_fk_django_ce` FOREIGN KEY (`clocked_id`) REFERENCES `django_celery_beat_clockedschedule` (`id`),
  CONSTRAINT `django_celery_beat_p_crontab_id_d3cba168_fk_django_ce` FOREIGN KEY (`crontab_id`) REFERENCES `django_celery_beat_crontabschedule` (`id`),
  CONSTRAINT `django_celery_beat_p_interval_id_a8ca27da_fk_django_ce` FOREIGN KEY (`interval_id`) REFERENCES `django_celery_beat_intervalschedule` (`id`),
  CONSTRAINT `django_celery_beat_p_solar_id_a87ce72c_fk_django_ce` FOREIGN KEY (`solar_id`) REFERENCES `django_celery_beat_solarschedule` (`id`),
  CONSTRAINT `django_celery_beat_periodictask_chk_1` CHECK ((`total_run_count` >= 0)),
  CONSTRAINT `django_celery_beat_periodictask_chk_2` CHECK ((`priority` >= 0)),
  CONSTRAINT `django_celery_beat_periodictask_chk_3` CHECK ((`expire_seconds` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_beat_periodictask`
--

LOCK TABLES `django_celery_beat_periodictask` WRITE;
/*!40000 ALTER TABLE `django_celery_beat_periodictask` DISABLE KEYS */;
INSERT INTO `django_celery_beat_periodictask` VALUES (5,'celery.backend_cleanup','celery.backend_cleanup','[]','{}',NULL,NULL,NULL,NULL,1,NULL,0,'2024-09-17 13:44:56.718030','',3,NULL,NULL,0,NULL,NULL,'{}',NULL,43200),(6,'logout_all_users','apps.questionnaire.tasks.logout_all_users','[]','{}',NULL,NULL,NULL,NULL,1,'2024-09-17 13:44:00.006734',3,'2024-09-17 13:44:56.762077','',5,NULL,NULL,0,NULL,NULL,'{}',NULL,NULL);
/*!40000 ALTER TABLE `django_celery_beat_periodictask` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_beat_periodictasks`
--

DROP TABLE IF EXISTS `django_celery_beat_periodictasks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_celery_beat_periodictasks` (
  `ident` smallint NOT NULL,
  `last_update` datetime(6) NOT NULL,
  PRIMARY KEY (`ident`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_beat_periodictasks`
--

LOCK TABLES `django_celery_beat_periodictasks` WRITE;
/*!40000 ALTER TABLE `django_celery_beat_periodictasks` DISABLE KEYS */;
INSERT INTO `django_celery_beat_periodictasks` VALUES (1,'2024-09-17 13:44:56.763987');
/*!40000 ALTER TABLE `django_celery_beat_periodictasks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_celery_beat_solarschedule`
--

DROP TABLE IF EXISTS `django_celery_beat_solarschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_celery_beat_solarschedule` (
  `id` int NOT NULL AUTO_INCREMENT,
  `event` varchar(24) NOT NULL,
  `latitude` decimal(9,6) NOT NULL,
  `longitude` decimal(9,6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_celery_beat_solar_event_latitude_longitude_ba64999a_uniq` (`event`,`latitude`,`longitude`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_celery_beat_solarschedule`
--

LOCK TABLES `django_celery_beat_solarschedule` WRITE;
/*!40000 ALTER TABLE `django_celery_beat_solarschedule` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_celery_beat_solarschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=193 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (177,'admin','logentry'),(179,'auth','group'),(178,'auth','permission'),(180,'auth','user'),(181,'contenttypes','contenttype'),(192,'django_celery_beat','clockedschedule'),(187,'django_celery_beat','crontabschedule'),(188,'django_celery_beat','intervalschedule'),(189,'django_celery_beat','periodictask'),(190,'django_celery_beat','periodictasks'),(191,'django_celery_beat','solarschedule'),(132,'questionnaire','activitycode'),(164,'questionnaire','allapplications'),(163,'questionnaire','autosaledocument'),(133,'questionnaire','carbrand'),(134,'questionnaire','carcondition'),(135,'questionnaire','carconfiguration'),(153,'questionnaire','clientcarinfo'),(166,'questionnaire','clientcitizenship'),(170,'questionnaire','clientcontact'),(167,'questionnaire','clientdocument'),(162,'questionnaire','clientdriverlicense'),(168,'questionnaire','clienteducation'),(171,'questionnaire','clientemployment'),(161,'questionnaire','clientexpenses'),(160,'questionnaire','clientextrainsurance'),(169,'questionnaire','clientfamilyinfo'),(159,'questionnaire','clientfinancialinfo'),(158,'questionnaire','clientfinancingcondition'),(157,'questionnaire','clientinternationalpassport'),(156,'questionnaire','clientoffer'),(155,'questionnaire','clientpassport'),(154,'questionnaire','clientpensioncertificate'),(175,'questionnaire','clientpersonalinfo'),(136,'questionnaire','clientpredata'),(173,'questionnaire','clientrealestate'),(165,'questionnaire','clienttaxdocument'),(172,'questionnaire','clientvehicle'),(137,'questionnaire','country'),(138,'questionnaire','documenttype'),(139,'questionnaire','ecoclass'),(140,'questionnaire','educationlevel'),(141,'questionnaire','enginetype'),(130,'questionnaire','financingterm'),(142,'questionnaire','gender'),(143,'questionnaire','housingtype'),(144,'questionnaire','maritalstatus'),(131,'questionnaire','offers'),(145,'questionnaire','organizationtype'),(146,'questionnaire','phonetype'),(147,'questionnaire','positiontype'),(148,'questionnaire','purchasemethod'),(149,'questionnaire','realestatetype'),(174,'questionnaire','selectedclientoffer'),(150,'questionnaire','socialstatus'),(151,'questionnaire','typepts'),(176,'questionnaire','userdocument'),(152,'questionnaire','userdocumenttype'),(182,'sessions','session'),(183,'users','dealership'),(186,'users','userdocument'),(185,'users','userdocumenttype'),(184,'users','userprofile');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-07-23 08:03:02.801483'),(2,'auth','0001_initial','2024-07-23 08:03:03.320010'),(3,'admin','0001_initial','2024-07-23 08:03:03.455010'),(4,'admin','0002_logentry_remove_auto_add','2024-07-23 08:03:03.471009'),(5,'admin','0003_logentry_add_action_flag_choices','2024-07-23 08:03:03.481007'),(6,'contenttypes','0002_remove_content_type_name','2024-07-23 08:03:03.589009'),(7,'auth','0002_alter_permission_name_max_length','2024-07-23 08:03:03.660007'),(8,'auth','0003_alter_user_email_max_length','2024-07-23 08:03:03.696005'),(9,'auth','0004_alter_user_username_opts','2024-07-23 08:03:03.709010'),(10,'auth','0005_alter_user_last_login_null','2024-07-23 08:03:03.775010'),(11,'auth','0006_require_contenttypes_0002','2024-07-23 08:03:03.778010'),(12,'auth','0007_alter_validators_add_error_messages','2024-07-23 08:03:03.790007'),(13,'auth','0008_alter_user_username_max_length','2024-07-23 08:03:03.888010'),(14,'auth','0009_alter_user_last_name_max_length','2024-07-23 08:03:03.940006'),(15,'auth','0010_alter_group_name_max_length','2024-07-23 08:03:03.965008'),(16,'auth','0011_update_proxy_permissions','2024-07-23 08:03:03.974005'),(17,'auth','0012_alter_user_first_name_max_length','2024-07-23 08:03:04.053005'),(18,'questionnaire','0001_initial','2024-07-23 08:03:08.233720'),(19,'sessions','0001_initial','2024-07-23 08:03:08.271402'),(20,'questionnaire','0002_carbrand_remove_carinfo_brand_car_info_and_more','2024-07-23 08:05:45.236123'),(21,'questionnaire','0003_clientoffer_delete_offersclient','2024-07-23 08:08:18.991493'),(22,'questionnaire','0004_remove_clientinfopersonal_client_and_more','2024-07-23 08:16:28.438526'),(23,'token_blacklist','0001_initial','2024-07-30 16:49:09.821129'),(24,'token_blacklist','0002_outstandingtoken_jti_hex','2024-07-30 16:49:09.850647'),(25,'token_blacklist','0003_auto_20171017_2007','2024-07-30 16:49:09.895618'),(26,'token_blacklist','0004_auto_20171017_2013','2024-07-30 16:49:09.972066'),(27,'token_blacklist','0005_remove_outstandingtoken_jti','2024-07-30 16:49:10.030591'),(28,'token_blacklist','0006_auto_20171017_2113','2024-07-30 16:49:10.056623'),(29,'token_blacklist','0007_auto_20171017_2214','2024-07-30 16:49:10.256275'),(30,'token_blacklist','0008_migrate_to_bigautofield','2024-07-30 16:49:10.459388'),(31,'token_blacklist','0010_fix_migrate_to_bigautofield','2024-07-30 16:49:10.478422'),(32,'token_blacklist','0011_linearizes_history','2024-07-30 16:49:10.480584'),(33,'token_blacklist','0012_alter_outstandingtoken_user','2024-07-30 16:49:10.494616'),(34,'questionnaire','0005_alter_userprofile_dealership_manager_and_more','2024-08-07 07:08:55.311108'),(35,'questionnaire','0006_alter_userprofile_first_name_manager_and_more','2024-08-07 11:13:49.808654'),(36,'questionnaire','0005_remove_dealership_is_active_and_more','2024-08-22 12:30:11.668878'),(37,'questionnaire','0006_a','2024-09-03 07:44:03.456518'),(38,'questionnaire','0007_delete_a','2024-09-03 07:44:03.485198'),(39,'questionnaire','0001_initial','2024-09-16 11:14:28.741992'),(40,'questionnaire','0002_remove_userprofile_active_dealership_and_more','2024-09-16 18:00:29.277411'),(41,'users','0001_initial','2024-09-16 18:07:05.690285'),(42,'questionnaire','0003_delete_userdocumenttype','2024-09-17 09:51:08.143154'),(43,'users','0002_userdocumenttype_userdocument','2024-09-17 09:51:08.431902'),(44,'django_celery_beat','0001_initial','2024-09-17 12:22:06.284983'),(45,'django_celery_beat','0002_auto_20161118_0346','2024-09-17 12:22:06.448303'),(46,'django_celery_beat','0003_auto_20161209_0049','2024-09-17 12:22:06.494487'),(47,'django_celery_beat','0004_auto_20170221_0000','2024-09-17 12:22:06.506175'),(48,'django_celery_beat','0005_add_solarschedule_events_choices','2024-09-17 12:22:06.517054'),(49,'django_celery_beat','0006_auto_20180322_0932','2024-09-17 12:22:06.662730'),(50,'django_celery_beat','0007_auto_20180521_0826','2024-09-17 12:22:06.760003'),(51,'django_celery_beat','0008_auto_20180914_1922','2024-09-17 12:22:06.819732'),(52,'django_celery_beat','0006_auto_20180210_1226','2024-09-17 12:22:06.860399'),(53,'django_celery_beat','0006_periodictask_priority','2024-09-17 12:22:06.990365'),(54,'django_celery_beat','0009_periodictask_headers','2024-09-17 12:22:07.120153'),(55,'django_celery_beat','0010_auto_20190429_0326','2024-09-17 12:22:07.478721'),(56,'django_celery_beat','0011_auto_20190508_0153','2024-09-17 12:22:07.674238'),(57,'django_celery_beat','0012_periodictask_expire_seconds','2024-09-17 12:22:07.899997'),(58,'django_celery_beat','0013_auto_20200609_0727','2024-09-17 12:22:07.931592'),(59,'django_celery_beat','0014_remove_clockedschedule_enabled','2024-09-17 12:22:07.994801'),(60,'django_celery_beat','0015_edit_solarschedule_events_choices','2024-09-17 12:22:08.014921'),(61,'django_celery_beat','0016_alter_crontabschedule_timezone','2024-09-17 12:22:08.047602'),(62,'django_celery_beat','0017_alter_crontabschedule_month_of_year','2024-09-17 12:22:08.066282'),(63,'django_celery_beat','0018_improve_crontab_helptext','2024-09-17 12:22:08.086795'),(64,'django_celery_beat','0019_alter_periodictasks_options','2024-09-17 12:22:08.097470');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('85de36nkqi2b765k9ekuwscqljwnb6re','.eJxVjMEOwiAQRP-FsyEFF1CP3v0GsuxupWogKe3J-O_SpAc9zrw381YR1yXHtckcJ1YXZdTht0tITykb4AeWe9VUyzJPSW-K3mnTt8ryuu7u30HGlvsaBiIB8uE4mADAYn0acQTLxiAZH5g9sQvAiR36nqkb4SwB0boTqc8X81k4ig:1sqYWo:Uv4FZuyfwJx47RL2f90nZuF5VNV4SxI_VK4rLjpAbrg','2024-10-01 13:46:02.406557');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_activitycode`
--

DROP TABLE IF EXISTS `questionnaire_activitycode`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_activitycode` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `code` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_activitycode`
--

LOCK TABLES `questionnaire_activitycode` WRITE;
/*!40000 ALTER TABLE `questionnaire_activitycode` DISABLE KEYS */;
/*!40000 ALTER TABLE `questionnaire_activitycode` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_allapplications`
--

DROP TABLE IF EXISTS `questionnaire_allapplications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_allapplications` (
  `id` int NOT NULL AUTO_INCREMENT,
  `status` varchar(255) DEFAULT NULL,
  `type_all_app` varchar(255) DEFAULT NULL,
  `financing` varchar(255) DEFAULT NULL,
  `manager` varchar(255) DEFAULT NULL,
  `dealership_all_app` varchar(255) DEFAULT NULL,
  `organization` varchar(255) DEFAULT NULL,
  `date_create_all_app` datetime(6) DEFAULT NULL,
  `date_changes_all_app` datetime(6) DEFAULT NULL,
  `documents_id` bigint NOT NULL,
  `car_info_id` bigint NOT NULL,
  `extra_insurance_id` bigint NOT NULL,
  `financing_conditions_id` bigint NOT NULL,
  `client_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `questionnaire_allapp_documents_id_faeec064_fk_questionn` (`documents_id`),
  KEY `questionnaire_allapp_car_info_id_2ee173f8_fk_questionn` (`car_info_id`),
  KEY `questionnaire_allapp_extra_insurance_id_c9521364_fk_questionn` (`extra_insurance_id`),
  KEY `questionnaire_allapp_financing_conditions_16a382d1_fk_questionn` (`financing_conditions_id`),
  KEY `questionnaire_allapp_client_id_f21377f2_fk_questionn` (`client_id`),
  CONSTRAINT `questionnaire_allapp_car_info_id_2ee173f8_fk_questionn` FOREIGN KEY (`car_info_id`) REFERENCES `questionnaire_clientcarinfo` (`id`),
  CONSTRAINT `questionnaire_allapp_client_id_f21377f2_fk_questionn` FOREIGN KEY (`client_id`) REFERENCES `questionnaire_clientpredata` (`id`),
  CONSTRAINT `questionnaire_allapp_documents_id_faeec064_fk_questionn` FOREIGN KEY (`documents_id`) REFERENCES `questionnaire_autosaledocument` (`id`),
  CONSTRAINT `questionnaire_allapp_extra_insurance_id_c9521364_fk_questionn` FOREIGN KEY (`extra_insurance_id`) REFERENCES `questionnaire_clientextrainsurance` (`id`),
  CONSTRAINT `questionnaire_allapp_financing_conditions_16a382d1_fk_questionn` FOREIGN KEY (`financing_conditions_id`) REFERENCES `questionnaire_clientfinancingcondition` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_allapplications`
--

LOCK TABLES `questionnaire_allapplications` WRITE;
/*!40000 ALTER TABLE `questionnaire_allapplications` DISABLE KEYS */;
INSERT INTO `questionnaire_allapplications` VALUES (1,' ','Физическое лицо','Кредит','faiver902@gmail.com','дц 1 2',NULL,'2024-09-16 12:56:07.896938','2024-09-16 12:56:07.897017',1,1,1,1,1),(2,' ','Физическое лицо','Кредит','faiver902@gmail.com','дц 2 1',NULL,'2024-09-16 18:10:50.262852','2024-09-16 18:10:50.262888',2,2,2,2,2);
/*!40000 ALTER TABLE `questionnaire_allapplications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_autosaledocument`
--

DROP TABLE IF EXISTS `questionnaire_autosaledocument`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_autosaledocument` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `pts_number_sale_auto` varchar(255) DEFAULT NULL,
  `pts_issue_sale_auto` date DEFAULT NULL,
  `pts_issued_by_sale_auto` varchar(255) DEFAULT NULL,
  `pts_name_sale_auto` varchar(255) DEFAULT NULL,
  `dcp_number_sale_auto` varchar(255) DEFAULT NULL,
  `dcp_issue_date_sale_auto` date DEFAULT NULL,
  `client_id` bigint NOT NULL,
  `pts_type_sale_auto_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `questionnaire_autosa_client_id_d743120d_fk_questionn` (`client_id`),
  KEY `questionnaire_autosa_pts_type_sale_auto_i_80d4ba22_fk_questionn` (`pts_type_sale_auto_id`),
  CONSTRAINT `questionnaire_autosa_client_id_d743120d_fk_questionn` FOREIGN KEY (`client_id`) REFERENCES `questionnaire_clientpredata` (`id`),
  CONSTRAINT `questionnaire_autosa_pts_type_sale_auto_i_80d4ba22_fk_questionn` FOREIGN KEY (`pts_type_sale_auto_id`) REFERENCES `questionnaire_typepts` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_autosaledocument`
--

LOCK TABLES `questionnaire_autosaledocument` WRITE;
/*!40000 ALTER TABLE `questionnaire_autosaledocument` DISABLE KEYS */;
INSERT INTO `questionnaire_autosaledocument` VALUES (1,NULL,NULL,NULL,NULL,'88',NULL,1,NULL),(2,NULL,NULL,NULL,NULL,NULL,NULL,2,NULL);
/*!40000 ALTER TABLE `questionnaire_autosaledocument` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_carbrand`
--

DROP TABLE IF EXISTS `questionnaire_carbrand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_carbrand` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_carbrand`
--

LOCK TABLES `questionnaire_carbrand` WRITE;
/*!40000 ALTER TABLE `questionnaire_carbrand` DISABLE KEYS */;
/*!40000 ALTER TABLE `questionnaire_carbrand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_carcondition`
--

DROP TABLE IF EXISTS `questionnaire_carcondition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_carcondition` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `condition` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `condition` (`condition`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_carcondition`
--

LOCK TABLES `questionnaire_carcondition` WRITE;
/*!40000 ALTER TABLE `questionnaire_carcondition` DISABLE KEYS */;
/*!40000 ALTER TABLE `questionnaire_carcondition` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_carconfiguration`
--

DROP TABLE IF EXISTS `questionnaire_carconfiguration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_carconfiguration` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `configuration` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `configuration` (`configuration`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_carconfiguration`
--

LOCK TABLES `questionnaire_carconfiguration` WRITE;
/*!40000 ALTER TABLE `questionnaire_carconfiguration` DISABLE KEYS */;
/*!40000 ALTER TABLE `questionnaire_carconfiguration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_clientcarinfo`
--

DROP TABLE IF EXISTS `questionnaire_clientcarinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_clientcarinfo` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `model_car_info` varchar(255) DEFAULT NULL,
  `configuration_car_info` varchar(255) DEFAULT NULL,
  `year_car_info` varchar(4) DEFAULT NULL,
  `engine_volume_car_info` decimal(10,2) DEFAULT NULL,
  `power_car_info` varchar(255) DEFAULT NULL,
  `color_car_info` varchar(255) DEFAULT NULL,
  `mileage_car_info` varchar(255) DEFAULT NULL,
  `vin_car_info` varchar(17) DEFAULT NULL,
  `car_price_car_info` varchar(255) DEFAULT NULL,
  `dealer_equipment_price_car_info` varchar(255) DEFAULT NULL,
  `price_date_car_info` datetime(6) DEFAULT NULL,
  `body_number_car_info` varchar(255) DEFAULT NULL,
  `engine_number_car_info` varchar(255) DEFAULT NULL,
  `brand_car_info_id` bigint DEFAULT NULL,
  `condition_car_info_id` bigint DEFAULT NULL,
  `client_id` bigint NOT NULL,
  `eco_class_car_info_id` bigint DEFAULT NULL,
  `engine_type_car_info_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `questionnaire_client_brand_car_info_id_9b7cd954_fk_questionn` (`brand_car_info_id`),
  KEY `questionnaire_client_condition_car_info_i_0845c2e2_fk_questionn` (`condition_car_info_id`),
  KEY `questionnaire_client_client_id_6e7ce3e9_fk_questionn` (`client_id`),
  KEY `questionnaire_client_eco_class_car_info_i_f25647a2_fk_questionn` (`eco_class_car_info_id`),
  KEY `questionnaire_client_engine_type_car_info_6a237d95_fk_questionn` (`engine_type_car_info_id`),
  CONSTRAINT `questionnaire_client_brand_car_info_id_9b7cd954_fk_questionn` FOREIGN KEY (`brand_car_info_id`) REFERENCES `questionnaire_carbrand` (`id`),
  CONSTRAINT `questionnaire_client_client_id_6e7ce3e9_fk_questionn` FOREIGN KEY (`client_id`) REFERENCES `questionnaire_clientpredata` (`id`),
  CONSTRAINT `questionnaire_client_condition_car_info_i_0845c2e2_fk_questionn` FOREIGN KEY (`condition_car_info_id`) REFERENCES `questionnaire_carcondition` (`id`),
  CONSTRAINT `questionnaire_client_eco_class_car_info_i_f25647a2_fk_questionn` FOREIGN KEY (`eco_class_car_info_id`) REFERENCES `questionnaire_ecoclass` (`id`),
  CONSTRAINT `questionnaire_client_engine_type_car_info_6a237d95_fk_questionn` FOREIGN KEY (`engine_type_car_info_id`) REFERENCES `questionnaire_enginetype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_clientcarinfo`
--

LOCK TABLES `questionnaire_clientcarinfo` WRITE;
/*!40000 ALTER TABLE `questionnaire_clientcarinfo` DISABLE KEYS */;
INSERT INTO `questionnaire_clientcarinfo` VALUES (1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,NULL,NULL),(2,'jg',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2024-09-16 18:10:50.249324',NULL,NULL,NULL,NULL,2,NULL,NULL);
/*!40000 ALTER TABLE `questionnaire_clientcarinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_clientcitizenship`
--

DROP TABLE IF EXISTS `questionnaire_clientcitizenship`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_clientcitizenship` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `russian_citizenship` tinyint(1) DEFAULT NULL,
  `residence_permit` tinyint(1) DEFAULT NULL,
  `us_citizenship` tinyint(1) DEFAULT NULL,
  `birth_place_citizenship` varchar(255) DEFAULT NULL,
  `tax_resident_foreign` tinyint(1) DEFAULT NULL,
  `tax_residence_countries` varchar(255) DEFAULT NULL,
  `foreign_inn` varchar(20) DEFAULT NULL,
  `client_id` bigint NOT NULL,
  `birth_country_client_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `questionnaire_client_client_id_9c6ade7e_fk_questionn` (`client_id`),
  KEY `questionnaire_client_birth_country_client_44681b69_fk_questionn` (`birth_country_client_id`),
  CONSTRAINT `questionnaire_client_birth_country_client_44681b69_fk_questionn` FOREIGN KEY (`birth_country_client_id`) REFERENCES `questionnaire_country` (`id`),
  CONSTRAINT `questionnaire_client_client_id_9c6ade7e_fk_questionn` FOREIGN KEY (`client_id`) REFERENCES `questionnaire_clientpredata` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_clientcitizenship`
--

LOCK TABLES `questionnaire_clientcitizenship` WRITE;
/*!40000 ALTER TABLE `questionnaire_clientcitizenship` DISABLE KEYS */;
INSERT INTO `questionnaire_clientcitizenship` VALUES (1,0,0,0,NULL,0,NULL,NULL,1,NULL);
/*!40000 ALTER TABLE `questionnaire_clientcitizenship` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_clientcontact`
--

DROP TABLE IF EXISTS `questionnaire_clientcontact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_clientcontact` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `living_address_contact` varchar(255) DEFAULT NULL,
  `living_start_date_contact` date DEFAULT NULL,
  `phone_number_contact` varchar(20) DEFAULT NULL,
  `email_contact` varchar(254) DEFAULT NULL,
  `notes_contact` longtext,
  `client_id` bigint NOT NULL,
  `housing_type_contact_id` bigint DEFAULT NULL,
  `phone_type_contact_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `questionnaire_client_client_id_9a5846c5_fk_questionn` (`client_id`),
  KEY `questionnaire_client_housing_type_contact_63b8b116_fk_questionn` (`housing_type_contact_id`),
  KEY `questionnaire_client_phone_type_contact_i_5ba3946c_fk_questionn` (`phone_type_contact_id`),
  CONSTRAINT `questionnaire_client_client_id_9a5846c5_fk_questionn` FOREIGN KEY (`client_id`) REFERENCES `questionnaire_clientpredata` (`id`),
  CONSTRAINT `questionnaire_client_housing_type_contact_63b8b116_fk_questionn` FOREIGN KEY (`housing_type_contact_id`) REFERENCES `questionnaire_housingtype` (`id`),
  CONSTRAINT `questionnaire_client_phone_type_contact_i_5ba3946c_fk_questionn` FOREIGN KEY (`phone_type_contact_id`) REFERENCES `questionnaire_phonetype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_clientcontact`
--

LOCK TABLES `questionnaire_clientcontact` WRITE;
/*!40000 ALTER TABLE `questionnaire_clientcontact` DISABLE KEYS */;
INSERT INTO `questionnaire_clientcontact` VALUES (1,NULL,NULL,NULL,NULL,'',1,NULL,NULL);
/*!40000 ALTER TABLE `questionnaire_clientcontact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_clientdocument`
--

DROP TABLE IF EXISTS `questionnaire_clientdocument`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_clientdocument` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `document_file` varchar(100) NOT NULL,
  `uploaded_at` datetime(6) NOT NULL,
  `client_id` bigint NOT NULL,
  `document_type_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `questionnaire_client_client_id_73c2f7fe_fk_questionn` (`client_id`),
  KEY `questionnaire_client_document_type_id_2fdaa6cc_fk_questionn` (`document_type_id`),
  CONSTRAINT `questionnaire_client_client_id_73c2f7fe_fk_questionn` FOREIGN KEY (`client_id`) REFERENCES `questionnaire_clientpredata` (`id`),
  CONSTRAINT `questionnaire_client_document_type_id_2fdaa6cc_fk_questionn` FOREIGN KEY (`document_type_id`) REFERENCES `questionnaire_documenttype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_clientdocument`
--

LOCK TABLES `questionnaire_clientdocument` WRITE;
/*!40000 ALTER TABLE `questionnaire_clientdocument` DISABLE KEYS */;
/*!40000 ALTER TABLE `questionnaire_clientdocument` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_clientdriverlicense`
--

DROP TABLE IF EXISTS `questionnaire_clientdriverlicense`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_clientdriverlicense` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `series_number_driver_license` varchar(20) DEFAULT NULL,
  `issue_date_driver_license` date DEFAULT NULL,
  `issued_by_driver_license` varchar(200) DEFAULT NULL,
  `experience_start_date_driver_license` date DEFAULT NULL,
  `client_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `questionnaire_client_client_id_c0d0d144_fk_questionn` (`client_id`),
  CONSTRAINT `questionnaire_client_client_id_c0d0d144_fk_questionn` FOREIGN KEY (`client_id`) REFERENCES `questionnaire_clientpredata` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_clientdriverlicense`
--

LOCK TABLES `questionnaire_clientdriverlicense` WRITE;
/*!40000 ALTER TABLE `questionnaire_clientdriverlicense` DISABLE KEYS */;
INSERT INTO `questionnaire_clientdriverlicense` VALUES (1,NULL,NULL,NULL,NULL,1);
/*!40000 ALTER TABLE `questionnaire_clientdriverlicense` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_clienteducation`
--

DROP TABLE IF EXISTS `questionnaire_clienteducation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_clienteducation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `client_id` bigint NOT NULL,
  `education_level_client_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `questionnaire_client_client_id_5858faf9_fk_questionn` (`client_id`),
  KEY `questionnaire_client_education_level_clie_401c7611_fk_questionn` (`education_level_client_id`),
  CONSTRAINT `questionnaire_client_client_id_5858faf9_fk_questionn` FOREIGN KEY (`client_id`) REFERENCES `questionnaire_clientpredata` (`id`),
  CONSTRAINT `questionnaire_client_education_level_clie_401c7611_fk_questionn` FOREIGN KEY (`education_level_client_id`) REFERENCES `questionnaire_educationlevel` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_clienteducation`
--

LOCK TABLES `questionnaire_clienteducation` WRITE;
/*!40000 ALTER TABLE `questionnaire_clienteducation` DISABLE KEYS */;
INSERT INTO `questionnaire_clienteducation` VALUES (1,1,NULL);
/*!40000 ALTER TABLE `questionnaire_clienteducation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_clientemployment`
--

DROP TABLE IF EXISTS `questionnaire_clientemployment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_clientemployment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `organization_inn` varchar(20) DEFAULT NULL,
  `organization_form` varchar(255) DEFAULT NULL,
  `organization_name` varchar(255) DEFAULT NULL,
  `position` varchar(255) DEFAULT NULL,
  `registration_address_employment` varchar(255) DEFAULT NULL,
  `phone_number_organization` varchar(20) DEFAULT NULL,
  `current_experience` varchar(255) DEFAULT NULL,
  `total_experience` varchar(255) DEFAULT NULL,
  `shift_method` tinyint(1) DEFAULT NULL,
  `official_position` tinyint(1) DEFAULT NULL,
  `activity_code_id` bigint DEFAULT NULL,
  `client_id` bigint NOT NULL,
  `organization_type_id` bigint DEFAULT NULL,
  `position_type_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `questionnaire_client_activity_code_id_f00ea417_fk_questionn` (`activity_code_id`),
  KEY `questionnaire_client_client_id_078d79d2_fk_questionn` (`client_id`),
  KEY `questionnaire_client_organization_type_id_3a9905b6_fk_questionn` (`organization_type_id`),
  KEY `questionnaire_client_position_type_id_984ca190_fk_questionn` (`position_type_id`),
  CONSTRAINT `questionnaire_client_activity_code_id_f00ea417_fk_questionn` FOREIGN KEY (`activity_code_id`) REFERENCES `questionnaire_activitycode` (`id`),
  CONSTRAINT `questionnaire_client_client_id_078d79d2_fk_questionn` FOREIGN KEY (`client_id`) REFERENCES `questionnaire_clientpredata` (`id`),
  CONSTRAINT `questionnaire_client_organization_type_id_3a9905b6_fk_questionn` FOREIGN KEY (`organization_type_id`) REFERENCES `questionnaire_organizationtype` (`id`),
  CONSTRAINT `questionnaire_client_position_type_id_984ca190_fk_questionn` FOREIGN KEY (`position_type_id`) REFERENCES `questionnaire_positiontype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_clientemployment`
--

LOCK TABLES `questionnaire_clientemployment` WRITE;
/*!40000 ALTER TABLE `questionnaire_clientemployment` DISABLE KEYS */;
INSERT INTO `questionnaire_clientemployment` VALUES (1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,NULL,1,NULL,NULL);
/*!40000 ALTER TABLE `questionnaire_clientemployment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_clientexpenses`
--

DROP TABLE IF EXISTS `questionnaire_clientexpenses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_clientexpenses` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `mandatory_payments` varchar(255) DEFAULT NULL,
  `loan_payments` varchar(255) DEFAULT NULL,
  `mortgage_payments` varchar(255) DEFAULT NULL,
  `client_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `questionnaire_client_client_id_04937131_fk_questionn` (`client_id`),
  CONSTRAINT `questionnaire_client_client_id_04937131_fk_questionn` FOREIGN KEY (`client_id`) REFERENCES `questionnaire_clientpredata` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_clientexpenses`
--

LOCK TABLES `questionnaire_clientexpenses` WRITE;
/*!40000 ALTER TABLE `questionnaire_clientexpenses` DISABLE KEYS */;
INSERT INTO `questionnaire_clientexpenses` VALUES (1,NULL,NULL,NULL,1);
/*!40000 ALTER TABLE `questionnaire_clientexpenses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_clientextrainsurance`
--

DROP TABLE IF EXISTS `questionnaire_clientextrainsurance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_clientextrainsurance` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `kasko_amount` varchar(255) DEFAULT NULL,
  `kasko_amount_include` tinyint(1) NOT NULL,
  `gap_amount` varchar(255) DEFAULT NULL,
  `gap_amount_include` tinyint(1) NOT NULL,
  `szh_amount` varchar(255) DEFAULT NULL,
  `szh_term` varchar(255) DEFAULT NULL,
  `szh_term_include` tinyint(1) NOT NULL,
  `financial_products_amount` varchar(255) DEFAULT NULL,
  `financial_products_amount_include` tinyint(1) DEFAULT NULL,
  `installment_commission_include` tinyint(1) DEFAULT NULL,
  `sms_notification_include` tinyint(1) DEFAULT NULL,
  `client_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `questionnaire_client_client_id_0ab41c32_fk_questionn` (`client_id`),
  CONSTRAINT `questionnaire_client_client_id_0ab41c32_fk_questionn` FOREIGN KEY (`client_id`) REFERENCES `questionnaire_clientpredata` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_clientextrainsurance`
--

LOCK TABLES `questionnaire_clientextrainsurance` WRITE;
/*!40000 ALTER TABLE `questionnaire_clientextrainsurance` DISABLE KEYS */;
INSERT INTO `questionnaire_clientextrainsurance` VALUES (1,NULL,0,NULL,0,NULL,NULL,0,NULL,0,0,0,1),(2,'0',0,'0',0,'0',NULL,0,NULL,0,0,0,2);
/*!40000 ALTER TABLE `questionnaire_clientextrainsurance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_clientfamilyinfo`
--

DROP TABLE IF EXISTS `questionnaire_clientfamilyinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_clientfamilyinfo` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `children_under_18` int DEFAULT NULL,
  `dependents` int DEFAULT NULL,
  `years_married` int DEFAULT NULL,
  `official_position_relative` tinyint(1) NOT NULL,
  `degree_of_kinship` varchar(255) DEFAULT NULL,
  `relative_position` varchar(255) DEFAULT NULL,
  `client_id` bigint NOT NULL,
  `marital_status_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `questionnaire_client_client_id_842bf9bf_fk_questionn` (`client_id`),
  KEY `questionnaire_client_marital_status_id_93416eaf_fk_questionn` (`marital_status_id`),
  CONSTRAINT `questionnaire_client_client_id_842bf9bf_fk_questionn` FOREIGN KEY (`client_id`) REFERENCES `questionnaire_clientpredata` (`id`),
  CONSTRAINT `questionnaire_client_marital_status_id_93416eaf_fk_questionn` FOREIGN KEY (`marital_status_id`) REFERENCES `questionnaire_maritalstatus` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_clientfamilyinfo`
--

LOCK TABLES `questionnaire_clientfamilyinfo` WRITE;
/*!40000 ALTER TABLE `questionnaire_clientfamilyinfo` DISABLE KEYS */;
INSERT INTO `questionnaire_clientfamilyinfo` VALUES (1,NULL,NULL,NULL,0,NULL,NULL,1,NULL);
/*!40000 ALTER TABLE `questionnaire_clientfamilyinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_clientfinancialinfo`
--

DROP TABLE IF EXISTS `questionnaire_clientfinancialinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_clientfinancialinfo` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `income_amount` varchar(255) DEFAULT NULL,
  `confirmed_income_amount` varchar(255) DEFAULT NULL,
  `income_proof_document` varchar(255) DEFAULT NULL,
  `income_source` varchar(255) DEFAULT NULL,
  `disposable_income` varchar(255) DEFAULT NULL,
  `spouse_income` varchar(255) DEFAULT NULL,
  `client_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `questionnaire_client_client_id_09a9e98a_fk_questionn` (`client_id`),
  CONSTRAINT `questionnaire_client_client_id_09a9e98a_fk_questionn` FOREIGN KEY (`client_id`) REFERENCES `questionnaire_clientpredata` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_clientfinancialinfo`
--

LOCK TABLES `questionnaire_clientfinancialinfo` WRITE;
/*!40000 ALTER TABLE `questionnaire_clientfinancialinfo` DISABLE KEYS */;
INSERT INTO `questionnaire_clientfinancialinfo` VALUES (1,NULL,NULL,NULL,NULL,NULL,NULL,1);
/*!40000 ALTER TABLE `questionnaire_clientfinancialinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_clientfinancingcondition`
--

DROP TABLE IF EXISTS `questionnaire_clientfinancingcondition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_clientfinancingcondition` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `initial_payment` varchar(255) DEFAULT NULL,
  `monthly_payment` varchar(255) DEFAULT NULL,
  `deferred_payment` tinyint(1) NOT NULL,
  `client_id` bigint NOT NULL,
  `financing_term_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `questionnaire_client_client_id_b9588c11_fk_questionn` (`client_id`),
  KEY `questionnaire_client_financing_term_id_2fa410e9_fk_questionn` (`financing_term_id`),
  CONSTRAINT `questionnaire_client_client_id_b9588c11_fk_questionn` FOREIGN KEY (`client_id`) REFERENCES `questionnaire_clientpredata` (`id`),
  CONSTRAINT `questionnaire_client_financing_term_id_2fa410e9_fk_questionn` FOREIGN KEY (`financing_term_id`) REFERENCES `questionnaire_financingterm` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_clientfinancingcondition`
--

LOCK TABLES `questionnaire_clientfinancingcondition` WRITE;
/*!40000 ALTER TABLE `questionnaire_clientfinancingcondition` DISABLE KEYS */;
INSERT INTO `questionnaire_clientfinancingcondition` VALUES (1,NULL,NULL,0,1,2),(2,NULL,NULL,0,2,1);
/*!40000 ALTER TABLE `questionnaire_clientfinancingcondition` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_clientinternationalpassport`
--

DROP TABLE IF EXISTS `questionnaire_clientinternationalpassport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_clientinternationalpassport` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `series_number_international_passport` varchar(20) DEFAULT NULL,
  `issue_date_international_passport` date DEFAULT NULL,
  `issued_by_international_passport` varchar(200) DEFAULT NULL,
  `client_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `questionnaire_client_client_id_f5a07052_fk_questionn` (`client_id`),
  CONSTRAINT `questionnaire_client_client_id_f5a07052_fk_questionn` FOREIGN KEY (`client_id`) REFERENCES `questionnaire_clientpredata` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_clientinternationalpassport`
--

LOCK TABLES `questionnaire_clientinternationalpassport` WRITE;
/*!40000 ALTER TABLE `questionnaire_clientinternationalpassport` DISABLE KEYS */;
INSERT INTO `questionnaire_clientinternationalpassport` VALUES (1,NULL,NULL,NULL,1);
/*!40000 ALTER TABLE `questionnaire_clientinternationalpassport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_clientoffer`
--

DROP TABLE IF EXISTS `questionnaire_clientoffer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_clientoffer` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `offer_id` int NOT NULL,
  `title_offer` varchar(255) NOT NULL,
  `name_bank_offer` varchar(255) NOT NULL,
  `term_offer` int NOT NULL,
  `stavka_offer` varchar(255) NOT NULL,
  `pay_offer` varchar(255) NOT NULL,
  `client_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `questionnaire_client_client_id_105f6361_fk_questionn` (`client_id`),
  CONSTRAINT `questionnaire_client_client_id_105f6361_fk_questionn` FOREIGN KEY (`client_id`) REFERENCES `questionnaire_clientpredata` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_clientoffer`
--

LOCK TABLES `questionnaire_clientoffer` WRITE;
/*!40000 ALTER TABLE `questionnaire_clientoffer` DISABLE KEYS */;
INSERT INTO `questionnaire_clientoffer` VALUES (6,2,'Название 2','Банк 2',60,'15','17777',1),(7,1,'Название','Банк 1',12,'12','4000',2);
/*!40000 ALTER TABLE `questionnaire_clientoffer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_clientpassport`
--

DROP TABLE IF EXISTS `questionnaire_clientpassport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_clientpassport` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `series_number_passport` varchar(20) DEFAULT NULL,
  `issue_date_passport` date DEFAULT NULL,
  `division_code_passport` varchar(10) DEFAULT NULL,
  `issued_by_passport` varchar(200) DEFAULT NULL,
  `client_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `questionnaire_client_client_id_84daa3cb_fk_questionn` (`client_id`),
  CONSTRAINT `questionnaire_client_client_id_84daa3cb_fk_questionn` FOREIGN KEY (`client_id`) REFERENCES `questionnaire_clientpredata` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_clientpassport`
--

LOCK TABLES `questionnaire_clientpassport` WRITE;
/*!40000 ALTER TABLE `questionnaire_clientpassport` DISABLE KEYS */;
INSERT INTO `questionnaire_clientpassport` VALUES (1,NULL,NULL,NULL,NULL,1);
/*!40000 ALTER TABLE `questionnaire_clientpassport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_clientpensioncertificate`
--

DROP TABLE IF EXISTS `questionnaire_clientpensioncertificate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_clientpensioncertificate` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `number_pension_sert` varchar(20) DEFAULT NULL,
  `client_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `questionnaire_client_client_id_70c1ef0a_fk_questionn` (`client_id`),
  CONSTRAINT `questionnaire_client_client_id_70c1ef0a_fk_questionn` FOREIGN KEY (`client_id`) REFERENCES `questionnaire_clientpredata` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_clientpensioncertificate`
--

LOCK TABLES `questionnaire_clientpensioncertificate` WRITE;
/*!40000 ALTER TABLE `questionnaire_clientpensioncertificate` DISABLE KEYS */;
INSERT INTO `questionnaire_clientpensioncertificate` VALUES (1,NULL,1);
/*!40000 ALTER TABLE `questionnaire_clientpensioncertificate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_clientpersonalinfo`
--

DROP TABLE IF EXISTS `questionnaire_clientpersonalinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_clientpersonalinfo` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `first_name_to_contact_client` varchar(255) DEFAULT NULL,
  `first_name_client` varchar(255) DEFAULT NULL,
  `last_name_client` varchar(255) DEFAULT NULL,
  `middle_name_client` varchar(255) DEFAULT NULL,
  `type_client` varchar(255) DEFAULT NULL,
  `product_client` varchar(255) DEFAULT NULL,
  `birth_date_client` date DEFAULT NULL,
  `registration_address_client` varchar(255) DEFAULT NULL,
  `registration_date_client` date DEFAULT NULL,
  `client_id` bigint NOT NULL,
  `gender_choice_client_id` bigint DEFAULT NULL,
  `housing_type_client_id` bigint DEFAULT NULL,
  `social_status_client_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `questionnaire_client_client_id_cbc86961_fk_questionn` (`client_id`),
  KEY `questionnaire_client_gender_choice_client_43027958_fk_questionn` (`gender_choice_client_id`),
  KEY `questionnaire_client_housing_type_client__06451592_fk_questionn` (`housing_type_client_id`),
  KEY `questionnaire_client_social_status_client_ecb44948_fk_questionn` (`social_status_client_id`),
  CONSTRAINT `questionnaire_client_client_id_cbc86961_fk_questionn` FOREIGN KEY (`client_id`) REFERENCES `questionnaire_clientpredata` (`id`),
  CONSTRAINT `questionnaire_client_gender_choice_client_43027958_fk_questionn` FOREIGN KEY (`gender_choice_client_id`) REFERENCES `questionnaire_gender` (`id`),
  CONSTRAINT `questionnaire_client_housing_type_client__06451592_fk_questionn` FOREIGN KEY (`housing_type_client_id`) REFERENCES `questionnaire_housingtype` (`id`),
  CONSTRAINT `questionnaire_client_social_status_client_ecb44948_fk_questionn` FOREIGN KEY (`social_status_client_id`) REFERENCES `questionnaire_socialstatus` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_clientpersonalinfo`
--

LOCK TABLES `questionnaire_clientpersonalinfo` WRITE;
/*!40000 ALTER TABLE `questionnaire_clientpersonalinfo` DISABLE KEYS */;
INSERT INTO `questionnaire_clientpersonalinfo` VALUES (1,'bf',NULL,NULL,NULL,'Физическое лицо','Кредит',NULL,NULL,NULL,1,NULL,NULL,NULL);
/*!40000 ALTER TABLE `questionnaire_clientpersonalinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_clientpredata`
--

DROP TABLE IF EXISTS `questionnaire_clientpredata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_clientpredata` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `first_name_to_contact_pre_client` varchar(255) DEFAULT NULL,
  `type_pre_client` varchar(255) DEFAULT NULL,
  `product_pre_client` varchar(255) DEFAULT NULL,
  `phone_number_pre_client` varchar(20) DEFAULT NULL,
  `total_loan_amount` varchar(255) DEFAULT NULL,
  `car_price_display` varchar(255) DEFAULT NULL,
  `additional_equipment_price_display` varchar(255) DEFAULT NULL,
  `partner_offers_shown` tinyint(1) NOT NULL,
  `type_phone_pre_client_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `questionnaire_client_type_phone_pre_clien_5179a528_fk_questionn` (`type_phone_pre_client_id`),
  CONSTRAINT `questionnaire_client_type_phone_pre_clien_5179a528_fk_questionn` FOREIGN KEY (`type_phone_pre_client_id`) REFERENCES `questionnaire_phonetype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_clientpredata`
--

LOCK TABLES `questionnaire_clientpredata` WRITE;
/*!40000 ALTER TABLE `questionnaire_clientpredata` DISABLE KEYS */;
INSERT INTO `questionnaire_clientpredata` VALUES (1,NULL,'Физическое лицо','Кредит',NULL,'0.00','0.00','0.00',0,NULL),(2,NULL,'Физическое лицо','Кредит',NULL,'0.00','0.00','0.00',0,NULL);
/*!40000 ALTER TABLE `questionnaire_clientpredata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_clientrealestate`
--

DROP TABLE IF EXISTS `questionnaire_clientrealestate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_clientrealestate` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `address_real_estate` varchar(255) DEFAULT NULL,
  `matches_registration_address_real_estate` tinyint(1) NOT NULL,
  `client_id` bigint NOT NULL,
  `purchase_method_real_estate_id` bigint DEFAULT NULL,
  `real_estate_type_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `questionnaire_client_client_id_1672e0e6_fk_questionn` (`client_id`),
  KEY `questionnaire_client_purchase_method_real_30d8ceeb_fk_questionn` (`purchase_method_real_estate_id`),
  KEY `questionnaire_client_real_estate_type_id_d13e42d4_fk_questionn` (`real_estate_type_id`),
  CONSTRAINT `questionnaire_client_client_id_1672e0e6_fk_questionn` FOREIGN KEY (`client_id`) REFERENCES `questionnaire_clientpredata` (`id`),
  CONSTRAINT `questionnaire_client_purchase_method_real_30d8ceeb_fk_questionn` FOREIGN KEY (`purchase_method_real_estate_id`) REFERENCES `questionnaire_purchasemethod` (`id`),
  CONSTRAINT `questionnaire_client_real_estate_type_id_d13e42d4_fk_questionn` FOREIGN KEY (`real_estate_type_id`) REFERENCES `questionnaire_realestatetype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_clientrealestate`
--

LOCK TABLES `questionnaire_clientrealestate` WRITE;
/*!40000 ALTER TABLE `questionnaire_clientrealestate` DISABLE KEYS */;
INSERT INTO `questionnaire_clientrealestate` VALUES (1,NULL,0,1,NULL,NULL);
/*!40000 ALTER TABLE `questionnaire_clientrealestate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_clienttaxdocument`
--

DROP TABLE IF EXISTS `questionnaire_clienttaxdocument`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_clienttaxdocument` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `series_number_tax_document` varchar(20) DEFAULT NULL,
  `number_tax_document` varchar(20) DEFAULT NULL,
  `client_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `questionnaire_client_client_id_3feecbe4_fk_questionn` (`client_id`),
  CONSTRAINT `questionnaire_client_client_id_3feecbe4_fk_questionn` FOREIGN KEY (`client_id`) REFERENCES `questionnaire_clientpredata` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_clienttaxdocument`
--

LOCK TABLES `questionnaire_clienttaxdocument` WRITE;
/*!40000 ALTER TABLE `questionnaire_clienttaxdocument` DISABLE KEYS */;
INSERT INTO `questionnaire_clienttaxdocument` VALUES (1,NULL,NULL,1);
/*!40000 ALTER TABLE `questionnaire_clienttaxdocument` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_clientvehicle`
--

DROP TABLE IF EXISTS `questionnaire_clientvehicle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_clientvehicle` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `brand_vehicle` varchar(255) DEFAULT NULL,
  `year_vehicle` int DEFAULT NULL,
  `model_vehicle` varchar(255) DEFAULT NULL,
  `purchase_year` int DEFAULT NULL,
  `client_id` bigint NOT NULL,
  `purchase_method_vehicle_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `questionnaire_client_client_id_754cc38c_fk_questionn` (`client_id`),
  KEY `questionnaire_client_purchase_method_vehi_535216d7_fk_questionn` (`purchase_method_vehicle_id`),
  CONSTRAINT `questionnaire_client_client_id_754cc38c_fk_questionn` FOREIGN KEY (`client_id`) REFERENCES `questionnaire_clientpredata` (`id`),
  CONSTRAINT `questionnaire_client_purchase_method_vehi_535216d7_fk_questionn` FOREIGN KEY (`purchase_method_vehicle_id`) REFERENCES `questionnaire_purchasemethod` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_clientvehicle`
--

LOCK TABLES `questionnaire_clientvehicle` WRITE;
/*!40000 ALTER TABLE `questionnaire_clientvehicle` DISABLE KEYS */;
INSERT INTO `questionnaire_clientvehicle` VALUES (1,NULL,NULL,NULL,NULL,1,NULL);
/*!40000 ALTER TABLE `questionnaire_clientvehicle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_country`
--

DROP TABLE IF EXISTS `questionnaire_country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_country` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_country`
--

LOCK TABLES `questionnaire_country` WRITE;
/*!40000 ALTER TABLE `questionnaire_country` DISABLE KEYS */;
/*!40000 ALTER TABLE `questionnaire_country` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_documenttype`
--

DROP TABLE IF EXISTS `questionnaire_documenttype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_documenttype` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `document_type` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `document_type` (`document_type`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_documenttype`
--

LOCK TABLES `questionnaire_documenttype` WRITE;
/*!40000 ALTER TABLE `questionnaire_documenttype` DISABLE KEYS */;
INSERT INTO `questionnaire_documenttype` VALUES (1,'Водительское удостоверение'),(2,'Паспорт');
/*!40000 ALTER TABLE `questionnaire_documenttype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_ecoclass`
--

DROP TABLE IF EXISTS `questionnaire_ecoclass`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_ecoclass` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_ecoclass`
--

LOCK TABLES `questionnaire_ecoclass` WRITE;
/*!40000 ALTER TABLE `questionnaire_ecoclass` DISABLE KEYS */;
/*!40000 ALTER TABLE `questionnaire_ecoclass` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_educationlevel`
--

DROP TABLE IF EXISTS `questionnaire_educationlevel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_educationlevel` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `level` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `level` (`level`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_educationlevel`
--

LOCK TABLES `questionnaire_educationlevel` WRITE;
/*!40000 ALTER TABLE `questionnaire_educationlevel` DISABLE KEYS */;
/*!40000 ALTER TABLE `questionnaire_educationlevel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_enginetype`
--

DROP TABLE IF EXISTS `questionnaire_enginetype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_enginetype` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `engine_type` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `engine_type` (`engine_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_enginetype`
--

LOCK TABLES `questionnaire_enginetype` WRITE;
/*!40000 ALTER TABLE `questionnaire_enginetype` DISABLE KEYS */;
/*!40000 ALTER TABLE `questionnaire_enginetype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_financingterm`
--

DROP TABLE IF EXISTS `questionnaire_financingterm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_financingterm` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `term` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `term` (`term`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_financingterm`
--

LOCK TABLES `questionnaire_financingterm` WRITE;
/*!40000 ALTER TABLE `questionnaire_financingterm` DISABLE KEYS */;
INSERT INTO `questionnaire_financingterm` VALUES (1,'12'),(2,'60');
/*!40000 ALTER TABLE `questionnaire_financingterm` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_gender`
--

DROP TABLE IF EXISTS `questionnaire_gender`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_gender` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `gender` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `gender` (`gender`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_gender`
--

LOCK TABLES `questionnaire_gender` WRITE;
/*!40000 ALTER TABLE `questionnaire_gender` DISABLE KEYS */;
/*!40000 ALTER TABLE `questionnaire_gender` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_housingtype`
--

DROP TABLE IF EXISTS `questionnaire_housingtype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_housingtype` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `type` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `type` (`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_housingtype`
--

LOCK TABLES `questionnaire_housingtype` WRITE;
/*!40000 ALTER TABLE `questionnaire_housingtype` DISABLE KEYS */;
/*!40000 ALTER TABLE `questionnaire_housingtype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_maritalstatus`
--

DROP TABLE IF EXISTS `questionnaire_maritalstatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_maritalstatus` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `status` (`status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_maritalstatus`
--

LOCK TABLES `questionnaire_maritalstatus` WRITE;
/*!40000 ALTER TABLE `questionnaire_maritalstatus` DISABLE KEYS */;
/*!40000 ALTER TABLE `questionnaire_maritalstatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_offers`
--

DROP TABLE IF EXISTS `questionnaire_offers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_offers` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `name_bank` varchar(255) NOT NULL,
  `term` int NOT NULL,
  `stavka` varchar(255) NOT NULL,
  `pay` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_offers`
--

LOCK TABLES `questionnaire_offers` WRITE;
/*!40000 ALTER TABLE `questionnaire_offers` DISABLE KEYS */;
INSERT INTO `questionnaire_offers` VALUES (1,'Название','Банк 1',12,'12','4000'),(2,'Название 2','Банк 2',60,'15','17777');
/*!40000 ALTER TABLE `questionnaire_offers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_organizationtype`
--

DROP TABLE IF EXISTS `questionnaire_organizationtype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_organizationtype` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `type` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `type` (`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_organizationtype`
--

LOCK TABLES `questionnaire_organizationtype` WRITE;
/*!40000 ALTER TABLE `questionnaire_organizationtype` DISABLE KEYS */;
/*!40000 ALTER TABLE `questionnaire_organizationtype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_phonetype`
--

DROP TABLE IF EXISTS `questionnaire_phonetype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_phonetype` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `phone_type` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `phone_type` (`phone_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_phonetype`
--

LOCK TABLES `questionnaire_phonetype` WRITE;
/*!40000 ALTER TABLE `questionnaire_phonetype` DISABLE KEYS */;
/*!40000 ALTER TABLE `questionnaire_phonetype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_positiontype`
--

DROP TABLE IF EXISTS `questionnaire_positiontype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_positiontype` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `type` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `type` (`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_positiontype`
--

LOCK TABLES `questionnaire_positiontype` WRITE;
/*!40000 ALTER TABLE `questionnaire_positiontype` DISABLE KEYS */;
/*!40000 ALTER TABLE `questionnaire_positiontype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_purchasemethod`
--

DROP TABLE IF EXISTS `questionnaire_purchasemethod`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_purchasemethod` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `method` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `method` (`method`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_purchasemethod`
--

LOCK TABLES `questionnaire_purchasemethod` WRITE;
/*!40000 ALTER TABLE `questionnaire_purchasemethod` DISABLE KEYS */;
/*!40000 ALTER TABLE `questionnaire_purchasemethod` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_realestatetype`
--

DROP TABLE IF EXISTS `questionnaire_realestatetype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_realestatetype` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `type` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `type` (`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_realestatetype`
--

LOCK TABLES `questionnaire_realestatetype` WRITE;
/*!40000 ALTER TABLE `questionnaire_realestatetype` DISABLE KEYS */;
/*!40000 ALTER TABLE `questionnaire_realestatetype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_selectedclientoffer`
--

DROP TABLE IF EXISTS `questionnaire_selectedclientoffer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_selectedclientoffer` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `offer_id` int DEFAULT NULL,
  `total_loan_amount_select` varchar(255) DEFAULT NULL,
  `car_price_display_select` varchar(255) DEFAULT NULL,
  `initial_payment_select` varchar(255) DEFAULT NULL,
  `term_select` varchar(255) DEFAULT NULL,
  `title_select` varchar(255) DEFAULT NULL,
  `monthly_payment_select` varchar(255) DEFAULT NULL,
  `stavka_select` varchar(255) DEFAULT NULL,
  `name_bank_select` varchar(255) DEFAULT NULL,
  `status_select_offer` varchar(255) DEFAULT NULL,
  `info_from_bank` varchar(255) DEFAULT NULL,
  `id_app_bank` varchar(255) DEFAULT NULL,
  `id_app_in_system` int DEFAULT NULL,
  `link_to_detail_from_bank` varchar(255) DEFAULT NULL,
  `client_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `questionnaire_select_client_id_5795cc21_fk_questionn` (`client_id`),
  CONSTRAINT `questionnaire_select_client_id_5795cc21_fk_questionn` FOREIGN KEY (`client_id`) REFERENCES `questionnaire_clientpredata` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_selectedclientoffer`
--

LOCK TABLES `questionnaire_selectedclientoffer` WRITE;
/*!40000 ALTER TABLE `questionnaire_selectedclientoffer` DISABLE KEYS */;
INSERT INTO `questionnaire_selectedclientoffer` VALUES (5,2,'0.00',NULL,NULL,'60','Название 2','17777','15','Банк 2','Одобрение',NULL,NULL,5,NULL,1),(6,1,'0.00',NULL,NULL,'12','Название','4000','12','Банк 1','Одобрение',NULL,NULL,6,NULL,2);
/*!40000 ALTER TABLE `questionnaire_selectedclientoffer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_socialstatus`
--

DROP TABLE IF EXISTS `questionnaire_socialstatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_socialstatus` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `status` (`status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_socialstatus`
--

LOCK TABLES `questionnaire_socialstatus` WRITE;
/*!40000 ALTER TABLE `questionnaire_socialstatus` DISABLE KEYS */;
/*!40000 ALTER TABLE `questionnaire_socialstatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_typepts`
--

DROP TABLE IF EXISTS `questionnaire_typepts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_typepts` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `pts_type` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `pts_type` (`pts_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_typepts`
--

LOCK TABLES `questionnaire_typepts` WRITE;
/*!40000 ALTER TABLE `questionnaire_typepts` DISABLE KEYS */;
/*!40000 ALTER TABLE `questionnaire_typepts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionnaire_userdocument`
--

DROP TABLE IF EXISTS `questionnaire_userdocument`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionnaire_userdocument` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `document_file` varchar(100) NOT NULL,
  `uploaded_at` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  `document_type_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `questionnaire_userdocument_user_id_7d7a2dc5_fk_auth_user_id` (`user_id`),
  KEY `questionnaire_userdo_document_type_id_a098a998_fk_questionn` (`document_type_id`),
  CONSTRAINT `questionnaire_userdocument_user_id_7d7a2dc5_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionnaire_userdocument`
--

LOCK TABLES `questionnaire_userdocument` WRITE;
/*!40000 ALTER TABLE `questionnaire_userdocument` DISABLE KEYS */;
INSERT INTO `questionnaire_userdocument` VALUES (2,'user_documents/user_1/1_Паспорт.pdf','2024-09-17 09:29:17.499257',1,1);
/*!40000 ALTER TABLE `questionnaire_userdocument` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `token_blacklist_blacklistedtoken`
--

DROP TABLE IF EXISTS `token_blacklist_blacklistedtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `token_blacklist_blacklistedtoken` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `blacklisted_at` datetime(6) NOT NULL,
  `token_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token_id` (`token_id`),
  CONSTRAINT `token_blacklist_blacklistedtoken_token_id_3cc7fe56_fk` FOREIGN KEY (`token_id`) REFERENCES `token_blacklist_outstandingtoken` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=119 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `token_blacklist_blacklistedtoken`
--

LOCK TABLES `token_blacklist_blacklistedtoken` WRITE;
/*!40000 ALTER TABLE `token_blacklist_blacklistedtoken` DISABLE KEYS */;
INSERT INTO `token_blacklist_blacklistedtoken` VALUES (1,'2024-08-04 12:56:39.044167',149),(2,'2024-08-04 13:02:03.288591',150),(3,'2024-08-04 13:05:07.068607',151),(4,'2024-08-04 13:06:01.147805',152),(5,'2024-08-04 13:06:18.864241',153),(6,'2024-08-04 13:06:19.012555',154),(7,'2024-08-04 13:06:20.023870',155),(8,'2024-08-04 13:06:21.033988',156),(9,'2024-08-04 13:06:22.035038',157),(10,'2024-08-04 13:06:23.043863',158),(11,'2024-08-04 13:06:24.039579',159),(12,'2024-08-04 13:06:25.037351',160),(13,'2024-08-04 13:06:26.008982',161),(14,'2024-08-04 13:06:27.039307',162),(15,'2024-08-04 13:06:28.018838',163),(16,'2024-08-04 13:06:29.022117',164),(17,'2024-08-04 13:06:30.036555',165),(18,'2024-08-04 13:06:31.026585',166),(19,'2024-08-04 13:06:32.046635',167),(20,'2024-08-04 13:06:33.028503',168),(21,'2024-08-04 13:06:34.039637',169),(22,'2024-08-04 13:06:35.038000',170),(23,'2024-08-04 13:06:36.030210',171),(24,'2024-08-04 13:06:37.012348',172),(25,'2024-08-04 13:06:38.009609',173),(26,'2024-08-04 13:06:39.026145',174),(27,'2024-08-04 13:06:40.035307',175),(28,'2024-08-04 13:06:41.042822',176),(29,'2024-08-04 13:06:42.030646',177),(30,'2024-08-04 13:06:43.039375',178),(31,'2024-08-04 13:06:44.032740',179),(32,'2024-08-04 13:06:45.034109',180),(33,'2024-08-04 13:06:46.016873',181),(34,'2024-08-04 13:06:47.023949',182),(35,'2024-08-04 13:06:48.026342',183),(36,'2024-08-04 13:06:49.044976',184),(37,'2024-08-04 13:06:50.011976',185),(38,'2024-08-04 13:06:51.046864',186),(39,'2024-08-04 13:06:52.019918',187),(40,'2024-08-04 13:06:53.029633',188),(41,'2024-08-04 13:06:54.020090',189),(42,'2024-08-04 13:06:55.037357',190),(43,'2024-08-04 13:06:56.017203',191),(44,'2024-08-04 13:06:57.017861',192),(45,'2024-08-04 13:06:58.030653',193),(46,'2024-08-04 13:06:59.029616',194),(47,'2024-08-04 13:07:00.042574',195),(48,'2024-08-04 13:07:01.042705',196),(49,'2024-08-04 13:07:02.038333',197),(50,'2024-08-04 13:07:03.027358',198),(51,'2024-08-04 13:07:04.032871',199),(52,'2024-08-04 13:07:05.038536',200),(53,'2024-08-04 13:07:06.025170',201),(54,'2024-08-04 13:07:07.042173',202),(55,'2024-08-04 13:07:08.030275',203),(56,'2024-08-04 13:07:09.035616',204),(57,'2024-08-04 13:07:10.031586',205),(58,'2024-08-04 13:07:11.039611',206),(59,'2024-08-04 13:07:12.015540',207),(60,'2024-08-04 13:07:13.037282',208),(61,'2024-08-04 13:07:14.036902',209),(62,'2024-08-04 13:07:15.047162',210),(63,'2024-08-04 13:07:16.011698',211),(64,'2024-08-04 13:07:17.032813',212),(65,'2024-08-04 13:07:18.027057',213),(66,'2024-08-04 13:07:19.002301',214),(67,'2024-08-04 13:07:20.039807',215),(68,'2024-08-04 13:07:21.031269',216),(69,'2024-08-04 13:07:22.022039',217),(70,'2024-08-04 13:07:23.033944',218),(71,'2024-08-04 13:07:24.031405',219),(72,'2024-08-04 13:07:25.033821',220),(73,'2024-08-04 13:07:26.018854',221),(74,'2024-08-04 13:07:27.041174',222),(75,'2024-08-04 13:07:28.033150',223),(76,'2024-08-04 13:07:29.033048',224),(77,'2024-08-04 13:07:30.040402',225),(78,'2024-08-04 13:07:31.026633',226),(79,'2024-08-04 13:07:32.040430',227),(80,'2024-08-04 13:07:33.032260',228),(81,'2024-08-04 13:07:34.037791',229),(82,'2024-08-04 13:07:35.019158',230),(83,'2024-08-04 13:07:36.017657',231),(84,'2024-08-04 13:07:37.031080',232),(85,'2024-08-04 13:07:38.027158',233),(86,'2024-08-04 13:07:39.033773',234),(87,'2024-08-04 13:07:40.031218',235),(88,'2024-08-04 13:07:41.032110',236),(89,'2024-08-04 13:07:42.043092',237),(90,'2024-08-04 13:07:43.032320',238),(91,'2024-08-04 13:07:44.043694',239),(92,'2024-08-04 13:07:45.023852',240),(93,'2024-08-04 13:07:46.032039',241),(94,'2024-08-04 13:07:47.040021',242),(95,'2024-08-04 13:07:48.030361',243),(96,'2024-08-04 13:07:49.040085',244),(97,'2024-08-04 13:07:50.035412',245),(98,'2024-08-04 13:07:51.009909',246),(99,'2024-08-04 13:07:52.028714',247),(100,'2024-08-04 13:07:53.033479',248),(101,'2024-08-04 13:07:54.043209',249),(102,'2024-08-04 13:07:55.031226',250),(103,'2024-08-04 13:07:56.036846',251),(104,'2024-08-04 13:07:57.041932',252),(105,'2024-08-04 13:07:58.032941',253),(106,'2024-08-04 13:07:59.023879',254),(107,'2024-08-04 13:08:00.054179',255),(108,'2024-08-04 13:08:01.055222',256),(109,'2024-08-04 13:08:02.032993',257),(110,'2024-08-04 13:08:03.024772',258),(111,'2024-08-04 13:08:05.402641',259),(112,'2024-08-04 13:08:59.285839',260),(113,'2024-08-05 05:49:48.254243',261),(114,'2024-08-06 08:09:36.445527',288),(115,'2024-08-06 10:51:01.389182',289),(116,'2024-08-07 05:49:29.643222',290),(117,'2024-08-07 11:05:52.646535',299);
/*!40000 ALTER TABLE `token_blacklist_blacklistedtoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `token_blacklist_outstandingtoken`
--

DROP TABLE IF EXISTS `token_blacklist_outstandingtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `token_blacklist_outstandingtoken` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `token` longtext NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `expires_at` datetime(6) NOT NULL,
  `user_id` int DEFAULT NULL,
  `jti` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token_blacklist_outstandingtoken_jti_hex_d9bdf6f7_uniq` (`jti`),
  KEY `token_blacklist_outs_user_id_83bc629a_fk_auth_user` (`user_id`),
  CONSTRAINT `token_blacklist_outs_user_id_83bc629a_fk_auth_user` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=300 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `token_blacklist_outstandingtoken`
--

LOCK TABLES `token_blacklist_outstandingtoken` WRITE;
/*!40000 ALTER TABLE `token_blacklist_outstandingtoken` DISABLE KEYS */;
INSERT INTO `token_blacklist_outstandingtoken` VALUES (1,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ0NDc4MCwiaWF0IjoxNzIyMzU4MzgwLCJqdGkiOiJhMDRiMmQwODhhZGI0MzQ4YjA3NTk3OTVkYTk1MDVkMyIsInVzZXJfaWQiOjF9.PewQrxFcjR3cNtsGtTSM7-gneqmtCXITH_FY_Dc5-DQ','2024-07-30 16:53:00.726930','2024-07-31 16:53:00.000000',1,'a04b2d088adb4348b0759795da9505d3'),(2,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ0NDc4MiwiaWF0IjoxNzIyMzU4MzgyLCJqdGkiOiI2YjRkYTUwNGViN2Y0YjM1YmNiN2QzZGM0MTZmZTdmMCIsInVzZXJfaWQiOjF9.ZYWfigVYeN_LwCxVvz2cea0j7cx1XWz4DtU8-3RJntk','2024-07-30 16:53:02.477622','2024-07-31 16:53:02.000000',1,'6b4da504eb7f4b35bcb7d3dc416fe7f0'),(3,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ0NDc4MiwiaWF0IjoxNzIyMzU4MzgyLCJqdGkiOiIyY2JlYTI0NjdjZjc0NDRjYmFlMWI3ZjZiMDE3NjY2MyIsInVzZXJfaWQiOjF9.L2VskwTDm8_F-aWLYzmcWDznU9rFdw1LrHsPOoJOrZE','2024-07-30 16:53:02.661755','2024-07-31 16:53:02.000000',1,'2cbea2467cf7444cbae1b7f6b0176663'),(4,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ0NDc4MywiaWF0IjoxNzIyMzU4MzgzLCJqdGkiOiI1MTJlZDQ1ZGY3Yzk0ZDgwODk5NjZkMGI3M2MyNDUyMiIsInVzZXJfaWQiOjF9.H95uDurHxP3NTmu9A2iK2X37yhSXPJi7P_wRjhGUVb4','2024-07-30 16:53:03.009756','2024-07-31 16:53:03.000000',1,'512ed45df7c94d8089966d0b73c24522'),(5,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ0NDk4MSwiaWF0IjoxNzIyMzU4NTgxLCJqdGkiOiJhZGQzZDg4ZWI3YzU0MTEzYmYwYjMwOTZhYWE4YjYyMyIsInVzZXJfaWQiOjF9.oT7xysK_bNdjtJaObtGcMAaWWOp-K1gOriv97WDfBDE','2024-07-30 16:56:21.306557','2024-07-31 16:56:21.000000',1,'add3d88eb7c54113bf0b3096aaa8b623'),(6,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ0NTEyOCwiaWF0IjoxNzIyMzU4NzI4LCJqdGkiOiIyNjBiZmU5YzQzMjI0MjkyOWE5ZjBkNTM2YTQ1M2FjNCIsInVzZXJfaWQiOjF9.Pzx_knPaSVLeG_t2Cy-56Wm7sH4QHr2A1Nwemmapk_E','2024-07-30 16:58:48.988730','2024-07-31 16:58:48.000000',1,'260bfe9c432242929a9f0d536a453ac4'),(7,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ0NTQzMSwiaWF0IjoxNzIyMzU5MDMxLCJqdGkiOiI0ZTcxYWU2MTI2Mzk0OTliOGI3YjE4OGE2NGE2Zjc4MSIsInVzZXJfaWQiOjF9.A5jAZDVRe-VWM0RlWCA_8WqWYPJRVIx44cC60s5zq0M','2024-07-30 17:03:51.949095','2024-07-31 17:03:51.000000',1,'4e71ae612639499b8b7b188a64a6f781'),(8,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ0NjU1MiwiaWF0IjoxNzIyMzYwMTUyLCJqdGkiOiI0YmQxZTIwMTQzNTE0OTRlYmI0NTM0ODg1N2RjNjFiMiIsInVzZXJfaWQiOjF9._ddZOEoaxEYfG8bE9ioGL8b8fQKkyiDFviqFjTPev8A','2024-07-30 17:22:32.002252','2024-07-31 17:22:32.000000',1,'4bd1e2014351494ebb45348857dc61b2'),(9,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ0NjY1NCwiaWF0IjoxNzIyMzYwMjU0LCJqdGkiOiIxMDMyMGZlOTFmMDg0MWM5OWFiMWRlM2E2ZDU2NDNkMyIsInVzZXJfaWQiOjF9.hYpeZ8Q3GdF8xCipRvn9nppHvyc4l096Aj3540Mo3j0','2024-07-30 17:24:14.975381','2024-07-31 17:24:14.000000',1,'10320fe91f0841c99ab1de3a6d5643d3'),(10,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ0Njc1OSwiaWF0IjoxNzIyMzYwMzU5LCJqdGkiOiI5M2Q0YjZmOGZjNWQ0ZWVkYWFiNjhjMTRjZjYyM2VkNiIsInVzZXJfaWQiOjF9.M3OS-DL8FgalprvUNfJQZutHiBY-l8kCvmt0LFksHWI','2024-07-30 17:25:59.144091','2024-07-31 17:25:59.000000',1,'93d4b6f8fc5d4eedaab68c14cf623ed6'),(11,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ0NjgxNSwiaWF0IjoxNzIyMzYwNDE1LCJqdGkiOiI3Mjg4OGU3ZGVkNDA0YjliYjI5Y2M2NjQyM2RmOGVlNCIsInVzZXJfaWQiOjF9.ZZsesM4ZYPhM1ifEZpInugpsPHn9o3GqgQiZDYd97Cs','2024-07-30 17:26:55.081775','2024-07-31 17:26:55.000000',1,'72888e7ded404b9bb29cc66423df8ee4'),(12,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ0Njg0NiwiaWF0IjoxNzIyMzYwNDQ2LCJqdGkiOiJjYWQ2NDFkYWUyZjg0OTNjOWUyMWYzNzYxMzk4NTI2MiIsInVzZXJfaWQiOjF9.d8CIug8LHeZRXPAOfy-ZWkmzjcNyk2Iyqai7Bv7v1lI','2024-07-30 17:27:26.771362','2024-07-31 17:27:26.000000',1,'cad641dae2f8493c9e21f37613985262'),(13,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ0NzY0NywiaWF0IjoxNzIyMzYxMjQ3LCJqdGkiOiJlYzM2MWMzZTYwNDg0MjNmYTMwZjdkMGNkYjEwYjU5OSIsInVzZXJfaWQiOjF9.YyrXMTqR6rYUoHfN-NhoIUbZHmXHH5Gf6kT4qVBCb_c','2024-07-30 17:40:47.645425','2024-07-31 17:40:47.000000',1,'ec361c3e6048423fa30f7d0cdb10b599'),(14,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ0Nzc0MSwiaWF0IjoxNzIyMzYxMzQxLCJqdGkiOiI2NjRjZjQzODZiMzM0ZjkwYjQyZDI3NGUwOTZiMGI3MSIsInVzZXJfaWQiOjF9.r7wfOb4A5oVRjzLKCUgnv68kHDtrU6FYnnuYcvtB6-Y','2024-07-30 17:42:21.706295','2024-07-31 17:42:21.000000',1,'664cf4386b334f90b42d274e096b0b71'),(15,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ0NzgwOCwiaWF0IjoxNzIyMzYxNDA4LCJqdGkiOiI4NWZmMjg1MmUxMWU0MmE5OWMwYjM4OTVhZGY2MmJmZCIsInVzZXJfaWQiOjF9.qyfhZxLKeDjJZYncyJp_QxgjKOJOK_fsrAJ2_sRL_0A','2024-07-30 17:43:28.835858','2024-07-31 17:43:28.000000',1,'85ff2852e11e42a99c0b3895adf62bfd'),(16,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ0Nzk0MCwiaWF0IjoxNzIyMzYxNTQwLCJqdGkiOiIzNTIzZTRmZjcxMGM0OTIzOTQyZmJmYWM2ODVkM2VjNCIsInVzZXJfaWQiOjF9.7diku5OS1OAfltkQ2QZbzeMkgHBWc8rdb4_IrZkdQOE','2024-07-30 17:45:40.136727','2024-07-31 17:45:40.000000',1,'3523e4ff710c4923942fbfac685d3ec4'),(17,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ0Nzk0MCwiaWF0IjoxNzIyMzYxNTQwLCJqdGkiOiJmZDM0MTc4Y2Q3NTc0OTgyYjIwNTQyY2NiYThmZDNjMCIsInVzZXJfaWQiOjF9.yO1S5Er6IM2v7vtM3mDMkm2_UD5qzBkuDdnEo0DRx-k','2024-07-30 17:45:40.346823','2024-07-31 17:45:40.000000',1,'fd34178cd7574982b20542ccba8fd3c0'),(18,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ0Nzk1NywiaWF0IjoxNzIyMzYxNTU3LCJqdGkiOiI5ZjVhZDI2NjMzNGE0NjhiODYzYWEwMTlhMTg0MWY2NyIsInVzZXJfaWQiOjF9.59_q3QoOm0Pj3_X6_qT2BFuOg0dvn0Vtxw0STIbbTqs','2024-07-30 17:45:57.274266','2024-07-31 17:45:57.000000',1,'9f5ad266334a468b863aa019a1841f67'),(19,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ0Nzk4MiwiaWF0IjoxNzIyMzYxNTgyLCJqdGkiOiIwNzk2MTBkNDVkYTQ0YjlkOGY1MWNiN2NlNGI3MjgzZCIsInVzZXJfaWQiOjF9.2lZp6nEGiHKy94P1heSLPBFkBfIhkdRo0_Zz6HiSLGU','2024-07-30 17:46:22.219114','2024-07-31 17:46:22.000000',1,'079610d45da44b9d8f51cb7ce4b7283d'),(20,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ0ODA0NiwiaWF0IjoxNzIyMzYxNjQ2LCJqdGkiOiI3OWQ5YWU5M2RlMjQ0M2U5ODI3NDAxODA3YWNmMDc2NSIsInVzZXJfaWQiOjF9.qtGnapQw1krxkMlYsgVocPX00F95-g9vxwvF6KUbYrc','2024-07-30 17:47:26.481245','2024-07-31 17:47:26.000000',1,'79d9ae93de2443e9827401807acf0765'),(21,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ0ODA4OSwiaWF0IjoxNzIyMzYxNjg5LCJqdGkiOiI5NzkwMGQ4MDY5Mjc0ZTk3OGE4YzljNDRmOTBhZmEzMSIsInVzZXJfaWQiOjF9.DREvzFQIoukjvF9wjmvANK7gmEpWeW3ZGA3RnUqb-TA','2024-07-30 17:48:09.141140','2024-07-31 17:48:09.000000',1,'97900d8069274e978a8c9c44f90afa31'),(22,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ0ODM2MywiaWF0IjoxNzIyMzYxOTYzLCJqdGkiOiJkNTAyMDM5ZjBmYTU0MThkOTc3OTRlY2IyNGY3YWIzYSIsInVzZXJfaWQiOjF9.7XZiuwCCLdOn5sjtSn9y25OWmr2wnkUiMgh562smAww','2024-07-30 17:52:43.054727','2024-07-31 17:52:43.000000',1,'d502039f0fa5418d97794ecb24f7ab3a'),(23,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ0ODQyMCwiaWF0IjoxNzIyMzYyMDIwLCJqdGkiOiJkZmUxZjc4ZGRmMjE0MmZiYjRhMGRmODczMmJhOTZhZiIsInVzZXJfaWQiOjF9.b_9Ds9jt7tEYCEJo0YiX7G1MwhF3zjX6Qe8XtoZHesg','2024-07-30 17:53:40.355252','2024-07-31 17:53:40.000000',1,'dfe1f78ddf2142fbb4a0df8732ba96af'),(24,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ0ODYzOCwiaWF0IjoxNzIyMzYyMjM4LCJqdGkiOiI5NjBjY2VmZDc2ODM0OGM2ODQzZGI5MDk3MGYzMmYxYyIsInVzZXJfaWQiOjF9.PvdXnXwP_BfeBmZtm9m5-7nIvuyCpn10FzAW3El7X74','2024-07-30 17:57:18.259254','2024-07-31 17:57:18.000000',1,'960ccefd768348c6843db90970f32f1c'),(25,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ0ODc4MCwiaWF0IjoxNzIyMzYyMzgwLCJqdGkiOiIyZmI3NWNmNDBkYzA0MTc0YTM1YWI1Y2VhZmQzZWNiNSIsInVzZXJfaWQiOjF9.20fGGL_q0RuyiJaebZepbqt7DmM7zB3RFhP7gFoio-c','2024-07-30 17:59:40.312012','2024-07-31 17:59:40.000000',1,'2fb75cf40dc04174a35ab5ceafd3ecb5'),(26,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ0ODgwMywiaWF0IjoxNzIyMzYyNDAzLCJqdGkiOiJhZmEwZTZiMWUyYjI0YzlkYmYxODlkZTlmZGRlNzk3YyIsInVzZXJfaWQiOjF9.ecbVgJDALOQE7lTTh1jMpY8L2yqRzjqNRiH0eMom2a0','2024-07-30 18:00:03.150863','2024-07-31 18:00:03.000000',1,'afa0e6b1e2b24c9dbf189de9fdde797c'),(27,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ0ODgxMiwiaWF0IjoxNzIyMzYyNDEyLCJqdGkiOiJiNDQ3ZTc1NDg1MjY0ZGFkYjc4NDA5ZTY1MDllZWI3MiIsInVzZXJfaWQiOjF9.jZevSbMhEknDxugEuyo3KFnefWZS67wtF9kU6Z4XTjA','2024-07-30 18:00:12.102313','2024-07-31 18:00:12.000000',1,'b447e75485264dadb78409e6509eeb72'),(28,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ0OTgwNywiaWF0IjoxNzIyMzYzNDA3LCJqdGkiOiI5OWQwMWE5MTY4N2M0MTVkYmY4M2NhNGJmNmI0ZmU0NSIsInVzZXJfaWQiOjF9.Tg3TSaFDtbdOF3G_X1Um2nkLRlCkG98HBmlqrZCVT7g','2024-07-30 18:16:47.584120','2024-07-31 18:16:47.000000',1,'99d01a91687c415dbf83ca4bf6b4fe45'),(29,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ0OTk1MCwiaWF0IjoxNzIyMzYzNTUwLCJqdGkiOiJiZGZhNDUzYTIyOTg0ZWU1OTg0MzM1ZmQyNGJlOGQwMCIsInVzZXJfaWQiOjF9.LdFPNY4_Cdln5jLQk7eUqiVsLYRLDidRPAwA9Ai2tCI','2024-07-30 18:19:10.744561','2024-07-31 18:19:10.000000',1,'bdfa453a22984ee5984335fd24be8d00'),(30,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ0OTk4OSwiaWF0IjoxNzIyMzYzNTg5LCJqdGkiOiIyOGQ5MjczYmE2NDE0ZTY1OTliODA0MWEwZjNmYTgyNSIsInVzZXJfaWQiOjF9.GZI7CRzG3jxAmbSOPfdeg9_rZaPxiStoAtyXLz7fdiQ','2024-07-30 18:19:49.785666','2024-07-31 18:19:49.000000',1,'28d9273ba6414e6599b8041a0f3fa825'),(31,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ1MDA0NywiaWF0IjoxNzIyMzYzNjQ3LCJqdGkiOiJkNmRmZjQyMGVjNmE0OTRjYWRmYzlmZjVlMWRmNzhiNyIsInVzZXJfaWQiOjF9.JmmNKAK9JW4jN1fE7fCuqermuSTVIqLV6M4WUDXEPFw','2024-07-30 18:20:47.421251','2024-07-31 18:20:47.000000',1,'d6dff420ec6a494cadfc9ff5e1df78b7'),(32,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ1MDE0MywiaWF0IjoxNzIyMzYzNzQzLCJqdGkiOiI3ZGUzNjJjMzIzMGQ0OTAyYTcyNjkxNzdmZTlhMTRmOCIsInVzZXJfaWQiOjF9.JiQ19pUcA7lcdfSGec09X9SDLPAm41NoUpDPAcU7gKM','2024-07-30 18:22:23.897070','2024-07-31 18:22:23.000000',1,'7de362c3230d4902a7269177fe9a14f8'),(33,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ1MDE3NywiaWF0IjoxNzIyMzYzNzc3LCJqdGkiOiJhMjQyZDZjMWRmODk0Y2E3OGE0Zjg0ZDNlYjk4OGVhMiIsInVzZXJfaWQiOjF9.os7SBT2OcYxG-gf0IjJdWOhkrooVl70EtAKjA0fUoKk','2024-07-30 18:22:57.543809','2024-07-31 18:22:57.000000',1,'a242d6c1df894ca78a4f84d3eb988ea2'),(34,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ1MDMwNCwiaWF0IjoxNzIyMzYzOTA0LCJqdGkiOiI0Y2E3YTk1ZTVhYzg0ZGMxOGY5NjU0MDE2MTI1ODVjNyIsInVzZXJfaWQiOjF9.vENLsA0CR-OQjnm2mOO_Ywqc12U10g3mIgfRw-_Eqcc','2024-07-30 18:25:04.865165','2024-07-31 18:25:04.000000',1,'4ca7a95e5ac84dc18f965401612585c7'),(35,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ1MTI1NSwiaWF0IjoxNzIyMzY0ODU1LCJqdGkiOiJiMGE4NWNlOTk4MTI0MGNhYmJiMmFmZjZlOWIxN2QzNiIsInVzZXJfaWQiOjF9.Akz--2QdGnPfJeH9POBQdEYO6Xwm0JDTQg7lJWAT4wQ','2024-07-30 18:40:55.555934','2024-07-31 18:40:55.000000',1,'b0a85ce9981240cabbb2aff6e9b17d36'),(36,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ1MTMxOCwiaWF0IjoxNzIyMzY0OTE4LCJqdGkiOiIwZjU3MGQzMjRhMmI0MWMyOGZkM2E3YWM4MzM5YzhhNyIsInVzZXJfaWQiOjF9.LGPi6eREO_mIBPJtXWamK4EYAkJgmL6rlEKKY56lFjA','2024-07-30 18:41:58.378684','2024-07-31 18:41:58.000000',1,'0f570d324a2b41c28fd3a7ac8339c8a7'),(37,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ1MTQwMiwiaWF0IjoxNzIyMzY1MDAyLCJqdGkiOiIyNTdlMTNlZTgyODg0ODAxYThjNmM2MjBjNGM2YzlmZiIsInVzZXJfaWQiOjF9.l2hYLn7UzkMnmnais5Jd0CcpiUSLR5Obgz6OacCCB6Q','2024-07-30 18:43:22.831400','2024-07-31 18:43:22.000000',1,'257e13ee82884801a8c6c620c4c6c9ff'),(38,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ1MTQ1MSwiaWF0IjoxNzIyMzY1MDUxLCJqdGkiOiJiMTExY2UzNzRmYzg0YjdiOWMzYWNkZTYyNWZjMjc3MiIsInVzZXJfaWQiOjF9.XE1gB9_iXu6mxb1MGrzLQnWQuLCJg1FDnDbbICXeSRc','2024-07-30 18:44:11.431272','2024-07-31 18:44:11.000000',1,'b111ce374fc84b7b9c3acde625fc2772'),(39,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ1MTQ2MiwiaWF0IjoxNzIyMzY1MDYyLCJqdGkiOiI0ZTM1MjVmMzY1MTk0ZThkYmRmZjgyNTJmODVkOWQ2NiIsInVzZXJfaWQiOjF9.W7H38K9hYb1FyGe81HzujWnv_gVWYe0Tfnr-fQN681s','2024-07-30 18:44:22.259138','2024-07-31 18:44:22.000000',1,'4e3525f365194e8dbdff8252f85d9d66'),(40,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ1MTU1MywiaWF0IjoxNzIyMzY1MTUzLCJqdGkiOiI1YmQwYjFiZTgzZjE0MTU1YWQyYTBmNTVhNzI2MDAzYyIsInVzZXJfaWQiOjF9.i9zcdUCE1ep3WiLXgSSjm2Hggk7-iztYjzrhk30k11I','2024-07-30 18:45:53.760259','2024-07-31 18:45:53.000000',1,'5bd0b1be83f14155ad2a0f55a726003c'),(41,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjQ1MTc5OCwiaWF0IjoxNzIyMzY1Mzk4LCJqdGkiOiI0OGFhOWRhNDQxMTk0ZjhiODg1MDRmZWY1OGMxNGUxZSIsInVzZXJfaWQiOjF9.jHGz41wB86lio82-mKHGylrOARZJWcU68cxK4RORauo','2024-07-30 18:49:58.603519','2024-07-31 18:49:58.000000',1,'48aa9da441194f8b88504fef58c14e1e'),(42,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjUyMjIzMSwiaWF0IjoxNzIyNDM1ODMxLCJqdGkiOiIzYTkzOTQ1NmZhMjI0OTc0YmI4MzRlN2UxZTQyYjE5MCIsInVzZXJfaWQiOjF9.vmYYfUjHtt9pU3K8WEJUmR5g9aSSZBqZggKt6b5mYME','2024-07-31 14:23:51.400187','2024-08-01 14:23:51.000000',1,'3a939456fa224974bb834e7e1e42b190'),(43,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjUyMjI0OCwiaWF0IjoxNzIyNDM1ODQ4LCJqdGkiOiI4M2Q4MDA0MjgxNjU0ZDBhOTljMDc1OTA1ZTJjNTFjMyIsInVzZXJfaWQiOjMxfQ.HxDB7MX_U-pCTixHbD5HKDXDxSQM1wAiD-YMrDrXZ7Q','2024-07-31 14:24:08.432679','2024-08-01 14:24:08.000000',NULL,'83d8004281654d0a99c075905e2c51c3'),(44,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc1MzkyNiwiaWF0IjoxNzIyNjY3NTI2LCJqdGkiOiI3YWI5MjFjZWEyNmE0ZjE0OWM3ZGZiZTk0YTU3OWE3ZCIsInVzZXJfaWQiOjF9.OLKS_3NpxlixOQD3F--UbXnUBrHlCdOcFyvW81h_0Zc','2024-08-03 06:45:26.491046','2024-08-04 06:45:26.000000',1,'7ab921cea26a4f149c7dfbe94a579a7d'),(45,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc1NTQ5MSwiaWF0IjoxNzIyNjY5MDkxLCJqdGkiOiI5NDU3Zjg1NzFmZDI0ODQ2OGZjMTY0NGM3ZWU2YzZlMCIsInVzZXJfaWQiOjF9.A3rOgYGifd0n4IWoY-QatmU1lytKu-1k6yyYIUzwi54','2024-08-03 07:11:31.790440','2024-08-04 07:11:31.000000',1,'9457f8571fd248468fc1644c7ee6c6e0'),(46,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc1NTk2MiwiaWF0IjoxNzIyNjY5NTYyLCJqdGkiOiIyZjAxNzEyMWEzZjQ0NGE5YTIxM2UwNDY1ZTcwMzU2MiIsInVzZXJfaWQiOjF9.CjJOw4gwZe_K9Isvn04QcKIo7LwaJPC0HXPSHea01fw','2024-08-03 07:19:22.969225','2024-08-04 07:19:22.000000',1,'2f017121a3f444a9a213e0465e703562'),(47,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc1NjA2NSwiaWF0IjoxNzIyNjY5NjY1LCJqdGkiOiJjN2ZhMTUyYzJjYmY0MGM4YjMxOThlOTQ1YTU5MmNmMyIsInVzZXJfaWQiOjF9.d-CSgAt6qzs3of7Zl_Y6lHaoClvjkvaa4CNv4FAbM1o','2024-08-03 07:21:05.188674','2024-08-04 07:21:05.000000',1,'c7fa152c2cbf40c8b3198e945a592cf3'),(48,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc1NjY2OCwiaWF0IjoxNzIyNjcwMjY4LCJqdGkiOiI3ZjA4NzkyZGVlM2M0YTA5YTA1ODhiMTk4ZmZjYzlmMiIsInVzZXJfaWQiOjF9.wcAZWl_YDeRZ68MCcy5QR_fFwt-wL8Y7wSul2D_fmU8','2024-08-03 07:31:08.900698','2024-08-04 07:31:08.000000',1,'7f08792dee3c4a09a0588b198ffcc9f2'),(49,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc1NjkyMywiaWF0IjoxNzIyNjcwNTIzLCJqdGkiOiIyYzg3ODlkMmQ2NTM0NmJkYWNlMDUwYTQ4MDQ1NmI5ZSIsInVzZXJfaWQiOjF9.IUO68g6P-7u2ECr2hJbYh0kyEfPhhh88xul_MG7H9dA','2024-08-03 07:35:23.498402','2024-08-04 07:35:23.000000',1,'2c8789d2d65346bdace050a480456b9e'),(50,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc1NzQ4OCwiaWF0IjoxNzIyNjcxMDg4LCJqdGkiOiJjMTg1OTMxNjgxZDg0NDk5YjI4YjViNDIwNTU5M2IzZSIsInVzZXJfaWQiOjF9.aTqTnIi4Iw6gIGONvkTAFrLi_XAYhQoIhVxntuqrnDc','2024-08-03 07:44:48.722949','2024-08-04 07:44:48.000000',1,'c185931681d84499b28b5b4205593b3e'),(51,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc1ODQ1NCwiaWF0IjoxNzIyNjcyMDU0LCJqdGkiOiJhNjRiZDA3NDBiOTk0NDI5OTM5ZTEwNTczNGZmYTA4OCIsInVzZXJfaWQiOjF9.yhgEfDVFVpr8aVAG6lFe6Cwwnd6IcT9NIGIJu5RI57w','2024-08-03 08:00:54.187280','2024-08-04 08:00:54.000000',1,'a64bd0740b994429939e105734ffa088'),(52,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc1OTgzNCwiaWF0IjoxNzIyNjczNDM0LCJqdGkiOiIyNTc4NzdmYjJjNzk0YjFkOGUzNTM3ZTBhODc0MmYyNiIsInVzZXJfaWQiOjF9.4GLV6Yr_jzbLdwXN4OPg1kL_wSzEc-bEyZwOJIMzRxs','2024-08-03 08:23:54.608050','2024-08-04 08:23:54.000000',1,'257877fb2c794b1d8e3537e0a8742f26'),(53,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc1OTg0NiwiaWF0IjoxNzIyNjczNDQ2LCJqdGkiOiI0N2FkMTk1NzdiMTg0M2QzODAyNjM1YWQyOWMwZTE2OSIsInVzZXJfaWQiOjF9.jaOgQJWz_pQZ1GXVc4XZW9RbyKxv-TgB9ekMGlcKjcs','2024-08-03 08:24:06.031692','2024-08-04 08:24:06.000000',1,'47ad19577b1843d3802635ad29c0e169'),(54,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc1OTg1MCwiaWF0IjoxNzIyNjczNDUwLCJqdGkiOiIwN2IxZjIwYWViMjk0YjAxOWE3ZGE0NDBlNWVlODMyOSIsInVzZXJfaWQiOjMxfQ.OlXY0m0WqdfC8OsPBc1N3dU5DxBVNlJk9rX3dsa7YvQ','2024-08-03 08:24:10.482496','2024-08-04 08:24:10.000000',NULL,'07b1f20aeb294b019a7da440e5ee8329'),(55,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2MDI1MSwiaWF0IjoxNzIyNjczODUxLCJqdGkiOiI1OTA0MmQzNzY0YjA0OWRhOWFhN2E3Y2M0NDA5YTRiZiIsInVzZXJfaWQiOjF9.wx33cI49nzgsPdKphALI85sKhIswxZA-gbms2vQGJrc','2024-08-03 08:30:51.566598','2024-08-04 08:30:51.000000',1,'59042d3764b049da9aa7a7cc4409a4bf'),(56,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2MDUwOSwiaWF0IjoxNzIyNjc0MTA5LCJqdGkiOiJmNjdhNDJjYTc0MzI0MThlYTY4NWM4YWM0NTJiODRjOSIsInVzZXJfaWQiOjF9.ivN9dFVZeVHKqy2-8YLWVdwuo6GEWkEkQlsNZPiP3mg','2024-08-03 08:35:09.772439','2024-08-04 08:35:09.000000',1,'f67a42ca7432418ea685c8ac452b84c9'),(57,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2MDUzMywiaWF0IjoxNzIyNjc0MTMzLCJqdGkiOiJiOTRkMDJkMjhhZDE0NTJjYjQwNTQ2MzMyNDczMTVhNyIsInVzZXJfaWQiOjF9.3uuePBhFOEt48YrO_ZO3-lzX1s-si00wjuQadckDQZ4','2024-08-03 08:35:33.793619','2024-08-04 08:35:33.000000',1,'b94d02d28ad1452cb4054633247315a7'),(58,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2MDcwMSwiaWF0IjoxNzIyNjc0MzAxLCJqdGkiOiJkOTgzZWZmMjE3MGU0NzQ1OTc0YzRhY2FlMWM2MmZmZSIsInVzZXJfaWQiOjF9.xARpHxNM-5DW27zlAicLRHtgYB8H9FmCcOVnvMR6ZF0','2024-08-03 08:38:21.471628','2024-08-04 08:38:21.000000',1,'d983eff2170e4745974c4acae1c62ffe'),(59,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2MDcyNCwiaWF0IjoxNzIyNjc0MzI0LCJqdGkiOiJmYzMxMjIxN2MzNzA0OWFiYWRjYjIxYjUwMmU0ODdkMyIsInVzZXJfaWQiOjF9.AbZn_xEUec4cFWUQQffAV0oSBb_UWwnLYqz1nEwn7R4','2024-08-03 08:38:44.250094','2024-08-04 08:38:44.000000',1,'fc312217c37049abadcb21b502e487d3'),(60,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2MDc4MiwiaWF0IjoxNzIyNjc0MzgyLCJqdGkiOiJiOTgyZGI0NWNiZWQ0M2RjOTYzZWIxM2M0YzVmZjQ3YiIsInVzZXJfaWQiOjF9.6t886eKnn7rOc2i1cltyXGO4MEZ50rSU42kvVq6Czps','2024-08-03 08:39:42.118474','2024-08-04 08:39:42.000000',1,'b982db45cbed43dc963eb13c4c5ff47b'),(61,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2MDc5OSwiaWF0IjoxNzIyNjc0Mzk5LCJqdGkiOiIwZDAzMzNmY2FiMDE0MjFiODM0MThkODI3ZmNhMWNmMCIsInVzZXJfaWQiOjF9.3oCngQ6HlLgVLN2yvbXjSNr8BzDta7X340PT2xwU6oY','2024-08-03 08:39:59.505467','2024-08-04 08:39:59.000000',1,'0d0333fcab01421b83418d827fca1cf0'),(62,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2MTQxOCwiaWF0IjoxNzIyNjc1MDE4LCJqdGkiOiJmNDAzMzkwMzI2MWQ0ODZhYTZhNWU0YWY0NzU4ZjExMCIsInVzZXJfaWQiOjF9.KCV_itJe-cA5UR5nvwgttFxuBU4kMavJAXXeaf8BRI4','2024-08-03 08:50:18.831312','2024-08-04 08:50:18.000000',1,'f4033903261d486aa6a5e4af4758f110'),(63,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2MTQyMywiaWF0IjoxNzIyNjc1MDIzLCJqdGkiOiI2ODYzZTM4MmI3NDE0MTIzOGYxN2UzZmNiZmI3ODA4ZiIsInVzZXJfaWQiOjF9.-9IU-XM-Udxi9h9UKuxAXfNRhvG9lw9LTC75KhShWFQ','2024-08-03 08:50:23.174988','2024-08-04 08:50:23.000000',1,'6863e382b74141238f17e3fcbfb7808f'),(64,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2MzA1OSwiaWF0IjoxNzIyNjc2NjU5LCJqdGkiOiJmN2ZmZTVlOTQ5MWE0ZmM3YThmMjBiYThkMTc1NzgxZCIsInVzZXJfaWQiOjF9.DnPo1ihHZaEIqs7UYjILJ9EfvXEdo-Uspe2_qaHoM10','2024-08-03 09:17:39.828585','2024-08-04 09:17:39.000000',1,'f7ffe5e9491a4fc7a8f20ba8d175781d'),(65,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2MzA4NSwiaWF0IjoxNzIyNjc2Njg1LCJqdGkiOiIyMDYzNmI3OTI4YjA0OTU1YmRkMWFjMTJlZGZlZTRlYSIsInVzZXJfaWQiOjF9.-CW1ZlXA05cwe7kZksGCyEJLqexcwLip5Ii9IcdiRek','2024-08-03 09:18:05.723804','2024-08-04 09:18:05.000000',1,'20636b7928b04955bdd1ac12edfee4ea'),(66,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2MzUyNCwiaWF0IjoxNzIyNjc3MTI0LCJqdGkiOiIyNjBlMDJlM2FlZjk0ZTg2YTI0OTcwMWIyMTNmZGFkMSIsInVzZXJfaWQiOjF9.8PLfmaBOmFg3s-HMguUg6Wu6aEvs6F3yPVkwGJE3xTU','2024-08-03 09:25:24.373864','2024-08-04 09:25:24.000000',1,'260e02e3aef94e86a249701b213fdad1'),(67,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2MzUyNCwiaWF0IjoxNzIyNjc3MTI0LCJqdGkiOiJhNjIwYjc2MzllOWM0Njg5OTQyOWUwNWQxODk5YWM2MiIsInVzZXJfaWQiOjF9.SqndhITeJbXLtgakCfkOICFg4ihTGLRvQ5AuosDaKM8','2024-08-03 09:25:24.772987','2024-08-04 09:25:24.000000',1,'a620b7639e9c46899429e05d1899ac62'),(68,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2NDY4MywiaWF0IjoxNzIyNjc4MjgzLCJqdGkiOiJmYWViZjNlMTM4ZTM0ZTY2YmNhYWQ2ZDM5MWRlNDI1YyIsInVzZXJfaWQiOjF9.hG43Xqz-FFj6Y5fR2sQrgUHmQQa4bNBUulYVs2dBme8','2024-08-03 09:44:43.717783','2024-08-04 09:44:43.000000',1,'faebf3e138e34e66bcaad6d391de425c'),(69,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2NDY4NSwiaWF0IjoxNzIyNjc4Mjg1LCJqdGkiOiIwMWZlNTUxNzJlZDY0NDgxODEyZGI0YjYwMmU0NjZiNCIsInVzZXJfaWQiOjF9.SDOtgR_bww1nw7VeDkgNcTWUTnzyMy2vb1lR0q0oKfM','2024-08-03 09:44:45.222152','2024-08-04 09:44:45.000000',1,'01fe55172ed64481812db4b602e466b4'),(70,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2NDY4NiwiaWF0IjoxNzIyNjc4Mjg2LCJqdGkiOiI4NmJlZjExMGM1NjA0YjZmYmM5MjA2NWY2ZmYyMjg1YyIsInVzZXJfaWQiOjF9.fdTxjXbYSnUIlZQVQGXBZYXB-e3WkZWMP-OrD7UKR_c','2024-08-03 09:44:46.857628','2024-08-04 09:44:46.000000',1,'86bef110c5604b6fbc92065f6ff2285c'),(71,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2NDY4NiwiaWF0IjoxNzIyNjc4Mjg2LCJqdGkiOiIyNWZmMDEyNWI4Y2I0Y2FjOGM0ZTBkN2NjZDc0Y2ExMSIsInVzZXJfaWQiOjF9.AvsuzzFVpfVN-icBA7mQZEWYbqBQQnj_Zs_y1vUcCps','2024-08-03 09:44:46.958594','2024-08-04 09:44:46.000000',1,'25ff0125b8cb4cac8c4e0d7ccd74ca11'),(72,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2NDY4NywiaWF0IjoxNzIyNjc4Mjg3LCJqdGkiOiI5Y2YyZWYwMjFiNTQ0MzgxYWM0MjM5NzhlYWNmZjVhMiIsInVzZXJfaWQiOjF9.h6rmx_pg_1K5iKykx9wplJ9LvAMPm3EZ_pRtT4bIYQk','2024-08-03 09:44:47.414624','2024-08-04 09:44:47.000000',1,'9cf2ef021b544381ac423978eacff5a2'),(73,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2NDY4NywiaWF0IjoxNzIyNjc4Mjg3LCJqdGkiOiIyZDdiOTdlMTEzYjQ0ZDdmOTAxYTQ0ZjRjZDg1YTg4MSIsInVzZXJfaWQiOjF9.Gdw_ecqjZy5SSyfZUVocSfpIIJnOyagR2Nmd_J3PMu8','2024-08-03 09:44:47.472671','2024-08-04 09:44:47.000000',1,'2d7b97e113b44d7f901a44f4cd85a881'),(74,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2NDcwMCwiaWF0IjoxNzIyNjc4MzAwLCJqdGkiOiI2ZTE1ODk2MzBlOWU0Mzc2ODYwNzRhZGY1NDU1MGZlZCIsInVzZXJfaWQiOjF9.8X6gebCuq-o_TMwVxYU4-advC8HmHTiyTqz9p-cZidg','2024-08-03 09:45:00.929265','2024-08-04 09:45:00.000000',1,'6e1589630e9e437686074adf54550fed'),(75,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2NDcxMSwiaWF0IjoxNzIyNjc4MzExLCJqdGkiOiI1YmY3ZWE0MzNhMzE0M2I3OTQ4ZGQyMDEzMTY5ZjQ4ZSIsInVzZXJfaWQiOjF9.7cK0nt6xPkzMzNGMDTkbAKEHKJg3rKdpsPWu325eSTM','2024-08-03 09:45:11.706693','2024-08-04 09:45:11.000000',1,'5bf7ea433a3143b7948dd2013169f48e'),(76,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2NDcxMiwiaWF0IjoxNzIyNjc4MzEyLCJqdGkiOiI4NTA3OTY5MDdlNjg0NjMyYjQxZjBiOWRlYzFmNDU4YSIsInVzZXJfaWQiOjF9.4uzet34d-piVx5ZpmsPk2iTK3i8qFO6npKjgE8pjrfo','2024-08-03 09:45:12.183676','2024-08-04 09:45:12.000000',1,'850796907e684632b41f0b9dec1f458a'),(77,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2NDcxMiwiaWF0IjoxNzIyNjc4MzEyLCJqdGkiOiJhZTBlNmE1ZjQ1MTg0M2I2YjRlNmE0YjcxODZiZmYwNCIsInVzZXJfaWQiOjF9.PbL7xiRftyUCqDami2CWOabVZIwQbNwCjmmrPn14g5s','2024-08-03 09:45:12.338908','2024-08-04 09:45:12.000000',1,'ae0e6a5f451843b6b4e6a4b7186bff04'),(78,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2NDcxOCwiaWF0IjoxNzIyNjc4MzE4LCJqdGkiOiI2ZGNlOGQ4NTg4OTI0MDY1YmI1MGQwZWFjN2FkZWFjZCIsInVzZXJfaWQiOjF9.nHnvWCZIexvV72kizIrbJsGCTvqbptmgPZdloZ5brBw','2024-08-03 09:45:18.832737','2024-08-04 09:45:18.000000',1,'6dce8d8588924065bb50d0eac7adeacd'),(79,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2NDcyMiwiaWF0IjoxNzIyNjc4MzIyLCJqdGkiOiIzMzAwNzRkNGQyYmY0MjlmOTNiN2E0MzdhNmFiMTFmMSIsInVzZXJfaWQiOjF9.sTzZ_lbSiFnoKpTR4GTn4sLjfysMVzNKwz92gcQU6mw','2024-08-03 09:45:22.529976','2024-08-04 09:45:22.000000',1,'330074d4d2bf429f93b7a437a6ab11f1'),(80,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2NDcyMiwiaWF0IjoxNzIyNjc4MzIyLCJqdGkiOiJkNzM1NzBlMDhiZTk0ZjJjOTQ4NjgxMTI2MmFjZGUyYiIsInVzZXJfaWQiOjF9.1uyrYgBJ9QBYuLXDwtevdrWYlj5ymRs2kK0vEwceDA4','2024-08-03 09:45:22.596942','2024-08-04 09:45:22.000000',1,'d73570e08be94f2c9486811262acde2b'),(81,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2NDg4MywiaWF0IjoxNzIyNjc4NDgzLCJqdGkiOiI2MWVjMjg0OTM2ZjQ0ODg0OTZlNDA1ZDBlNWIxZDhiMiIsInVzZXJfaWQiOjF9.L8K7NTN2vWmmkModpStnsIT0fl_Aq3NLGK14PA4BrOc','2024-08-03 09:48:03.283348','2024-08-04 09:48:03.000000',1,'61ec284936f4488496e405d0e5b1d8b2'),(82,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2NTAwMCwiaWF0IjoxNzIyNjc4NjAwLCJqdGkiOiJkM2ZjZWE4ODFhZDM0ZmFhYmJjYmE5NGY3YzNmYjY4NyIsInVzZXJfaWQiOjF9.XqGZzhsjwnPZHLzk9btYAW4HAcDzEUegpsMiSNuysB8','2024-08-03 09:50:00.998468','2024-08-04 09:50:00.000000',1,'d3fcea881ad34faabbcba94f7c3fb687'),(83,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2NTMyNCwiaWF0IjoxNzIyNjc4OTI0LCJqdGkiOiIwODg5OWVhMDM4ZTU0M2Q0OTlhMDJmODkyYWY0NWVmNyIsInVzZXJfaWQiOjJ9.cnKRq-ylr4-VV19QhXL446tmsZ6wI6gsoT9a2Og_eKA','2024-08-03 09:55:24.748580','2024-08-04 09:55:24.000000',2,'08899ea038e543d499a02f892af45ef7'),(84,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2NjE0OSwiaWF0IjoxNzIyNjc5NzQ5LCJqdGkiOiIxNDc0MTY4NmZlYTY0YWM0ODJjZDVjMjdkNzc2NGEzNSIsInVzZXJfaWQiOjF9.wB7jmeepEeiq0iUZAypanBhsdExpyjdTMHsINl-rOEs','2024-08-03 10:09:09.271203','2024-08-04 10:09:09.000000',1,'14741686fea64ac482cd5c27d7764a35'),(85,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2NjUxMiwiaWF0IjoxNzIyNjgwMTEyLCJqdGkiOiJiMjdiYzRjMzA3ZDc0MDAwYmMyOTMyNWQzZGYxNTQyZSIsInVzZXJfaWQiOjF9.3s8BrzSav0ibUQK57zFFY8A0j5Hj9nOuQk3beUhpM18','2024-08-03 10:15:12.399894','2024-08-04 10:15:12.000000',1,'b27bc4c307d74000bc29325d3df1542e'),(86,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2NzA3NywiaWF0IjoxNzIyNjgwNjc3LCJqdGkiOiJkNjAyZmMxYWIwMGI0MGQ2OWE0NDAzZGUxZDk0Y2Y5ZCIsInVzZXJfaWQiOjF9.LY1pM0LZZ99q8bnthWjDHgrbZhSBGXaP92OokGRH1jA','2024-08-03 10:24:37.549897','2024-08-04 10:24:37.000000',1,'d602fc1ab00b40d69a4403de1d94cf9d'),(87,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2NzA5NiwiaWF0IjoxNzIyNjgwNjk2LCJqdGkiOiI5OTczYWFmYmVmMDE0MDVjODNkMWFiZjFkZmE0OWU1MyIsInVzZXJfaWQiOjF9.voQt8gZyH3Yz28NMq1SwUUIhIfaawKLIq1caWJJxOdA','2024-08-03 10:24:56.945928','2024-08-04 10:24:56.000000',1,'9973aafbef01405c83d1abf1dfa49e53'),(88,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2NzE0MywiaWF0IjoxNzIyNjgwNzQzLCJqdGkiOiI0ZjIxMDc4OGI5ZWQ0YzZhODQ0MWZiNmY1N2MzNTUzMiIsInVzZXJfaWQiOjF9.oisx0IvckYbEHOjfipF4uvY3eY654YgVWh6IsIQoU7w','2024-08-03 10:25:43.207580','2024-08-04 10:25:43.000000',1,'4f210788b9ed4c6a8441fb6f57c35532'),(89,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2NzI0OSwiaWF0IjoxNzIyNjgwODQ5LCJqdGkiOiI1ZjViNzE3OTRiODI0ZGNlODVkNTU1NTU1MDljMTc4YyIsInVzZXJfaWQiOjF9.Ua4tkYmGmpHqofhJ_SS58jiegN2m9Z6IH_OOdXYdxF4','2024-08-03 10:27:29.194084','2024-08-04 10:27:29.000000',1,'5f5b71794b824dce85d55555509c178c'),(90,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2OTgwMCwiaWF0IjoxNzIyNjgzNDAwLCJqdGkiOiIzMWUxYTBkYmVlN2I0YzJhYWM0NmQzNjdhMzJhODMzNiIsInVzZXJfaWQiOjF9.TwOr39P_6DUmCqIqKdkX3KEifDziJyobg0IqgWK0oy0','2024-08-03 11:10:00.282973','2024-08-04 11:10:00.000000',1,'31e1a0dbee7b4c2aac46d367a32a8336'),(91,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc2OTgxOCwiaWF0IjoxNzIyNjgzNDE4LCJqdGkiOiIzODUzZGQ4Y2I4Y2U0ODI1OWE2NDdhZmQzMWRhNzNiNSIsInVzZXJfaWQiOjF9.VXLSxqlBnoIDTs-lwacOGWQ1Sx29Gcm1nT-jfq_QblA','2024-08-03 11:10:18.668560','2024-08-04 11:10:18.000000',1,'3853dd8cb8ce48259a647afd31da73b5'),(92,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc3MDA5NSwiaWF0IjoxNzIyNjgzNjk1LCJqdGkiOiIwMjkyOTcwZTM1MTQ0ZjMzYTRiYmFhNDkzYTQyYjA5NCIsInVzZXJfaWQiOjF9.VfUc0NfIHc9qbI4R1hTlIB-UkPLI555_NwOg5P8GLHY','2024-08-03 11:14:55.806319','2024-08-04 11:14:55.000000',1,'0292970e35144f33a4bbaa493a42b094'),(93,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc3MDY0OSwiaWF0IjoxNzIyNjg0MjQ5LCJqdGkiOiJlMjliYWM5ZTEwZWM0NTU5OTU0NmU3ZjE3YjFkNjNhMSIsInVzZXJfaWQiOjF9.IkT8Rf3excFIJ30rx3BmjR1rvpZWFWYD8uFhDUGqjkQ','2024-08-03 11:24:09.409363','2024-08-04 11:24:09.000000',1,'e29bac9e10ec45599546e7f17b1d63a1'),(94,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc3MDY2NiwiaWF0IjoxNzIyNjg0MjY2LCJqdGkiOiIxMDUzNTU4NjU4ZjQ0OWFjOWFmMTk4MzNhNjVmMzNmOCIsInVzZXJfaWQiOjMxfQ.JS92_JVKXRpUUHXAZagwYl7T9d48kaDAumK_-i8Btik','2024-08-03 11:24:26.414592','2024-08-04 11:24:26.000000',NULL,'1053558658f449ac9af19833a65f33f8'),(95,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc3MDg0NCwiaWF0IjoxNzIyNjg0NDQ0LCJqdGkiOiIxZjFiYjRmZjZjMDM0NGNmYWE1YjFhY2U0ZjE2MDI1MiIsInVzZXJfaWQiOjMxfQ.yEpc0yxv7DcfBAwxM-DJVN-0-Fdl5rMfoyJ_QDJucpk','2024-08-03 11:27:24.427765','2024-08-04 11:27:24.000000',NULL,'1f1bb4ff6c0344cfaa5b1ace4f160252'),(96,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc3MDg0OCwiaWF0IjoxNzIyNjg0NDQ4LCJqdGkiOiJkZmU3NWQ5YWVjYzA0ZGFiODE5ZGVhOTk1NDU2MGQ5NSIsInVzZXJfaWQiOjF9.538Q_Gm1vPtxUmHSt9mt4Uc8Ukp89GDg-giysWxbJoQ','2024-08-03 11:27:28.708485','2024-08-04 11:27:28.000000',1,'dfe75d9aecc04dab819dea9954560d95'),(97,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc3NDc2NywiaWF0IjoxNzIyNjg4MzY3LCJqdGkiOiI0ZmQzODhlNDNjNTY0N2Y0OWFjYzQ1OGUzYmE1NzI1YyIsInVzZXJfaWQiOjF9.oeUEJmw0V2W0MHNWeI1sIoHebDgAXh22TlwinAkp8pE','2024-08-03 12:32:47.166952','2024-08-04 12:32:47.000000',1,'4fd388e43c5647f49acc458e3ba5725c'),(98,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc3NjI3OCwiaWF0IjoxNzIyNjg5ODc4LCJqdGkiOiIxOGE4MGYwMWRiYzQ0MmViOGQ1ZGVkMjQxNDIwNDFlNiIsInVzZXJfaWQiOjF9.DI2z7DTDJ6R9qxPjwnEbU46yIiyHkHUi9GM7Tchl8k4','2024-08-03 12:57:58.269959','2024-08-04 12:57:58.000000',1,'18a80f01dbc442eb8d5ded24142041e6'),(99,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc4NDQ5MywiaWF0IjoxNzIyNjk4MDkzLCJqdGkiOiJiZGJhODM5M2UzYzk0MWY4YmMzZmE2MDk4YWNiMmE2MyIsInVzZXJfaWQiOjF9.AC2--PEZxoa7ZFxat4faneJLjS1YXiEYpux8l24DknI','2024-08-03 15:14:53.957726','2024-08-04 15:14:53.000000',1,'bdba8393e3c941f8bc3fa6098acb2a63'),(100,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc4ODExMSwiaWF0IjoxNzIyNzAxNzExLCJqdGkiOiJiM2I2NzI5ZWZjYjk0MGMxYmM5NDY3MmNiYWUyZWViZiIsInVzZXJfaWQiOjF9.FWIAYcXJ2_q-HFchWhj_X81bi5lvebXKpz-1nORan70','2024-08-03 16:15:11.216102','2024-08-04 16:15:11.000000',1,'b3b6729efcb940c1bc94672cbae2eebf'),(101,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc4ODY1MSwiaWF0IjoxNzIyNzAyMjUxLCJqdGkiOiI0M2RlYzc2OWY5ZTY0Njc0ODBhNjg0YWQ3YWU5OTVjZiIsInVzZXJfaWQiOjF9.XqSJHNG_iaR5TvINT_BY9V2tswtrnmbneXqVIn4apM4','2024-08-03 16:24:11.068169','2024-08-04 16:24:11.000000',1,'43dec769f9e6467480a684ad7ae995cf'),(102,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc4ODY1OCwiaWF0IjoxNzIyNzAyMjU4LCJqdGkiOiJiNWMwMGVkOTUwMmU0ZjMzOTU3YTYwYmZjZjhhNjcwNCIsInVzZXJfaWQiOjF9.ExnxVzG5puasK0HDzpauY6sYuMB__vDoA_ZJum_Ny34','2024-08-03 16:24:18.466781','2024-08-04 16:24:18.000000',1,'b5c00ed9502e4f33957a60bfcf8a6704'),(103,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc4ODcxMiwiaWF0IjoxNzIyNzAyMzEyLCJqdGkiOiIyMjZjM2I2MTliMjg0MmU2OGQ0YWYwNTQ3Yzc0NzgzOSIsInVzZXJfaWQiOjF9.1AHjIlRVNG_xFHAD0LTJATMJVYKdW7lNts3KS_P8dUY','2024-08-03 16:25:12.562464','2024-08-04 16:25:12.000000',1,'226c3b619b2842e68d4af0547c747839'),(105,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc4OTU1OCwiaWF0IjoxNzIyNzAzMTU4LCJqdGkiOiJmMTk1ZWI4OTI4ZTQ0Njg2OTExNjkyMDZjZjRjNDE5OCIsInVzZXJfaWQiOjF9.GevNeJdl5FKRd8rGKAWWAgNw_itiRGfX9UAUDkZOASk','2024-08-03 16:39:18.409355','2024-08-04 16:39:18.000000',1,'f195eb8928e4468691169206cf4c4198'),(106,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc4OTU5MCwiaWF0IjoxNzIyNzAzMTkwLCJqdGkiOiJmMjI0MGIyMjZmM2Q0OWM2YjRjYzY1OTlmNTEyNGJjNCIsInVzZXJfaWQiOjJ9.qRo-7sN8lH1-Tpy7WHrTfDSt-IWoeSZGRActmIExOxY','2024-08-03 16:39:50.432924','2024-08-04 16:39:50.000000',2,'f2240b226f3d49c6b4cc6599f5124bc4'),(108,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc4OTcwNiwiaWF0IjoxNzIyNzAzMzA2LCJqdGkiOiI5NjI0Yjg1MjVhNTY0ZDk5YTM0YzRlNDU2OWY0NmUzYSIsInVzZXJfaWQiOjJ9.F9aT6JwKCm04Pp987Jqbx-lxx3A2LcjF6-8-_EhWQDw','2024-08-03 16:41:46.041966','2024-08-04 16:41:46.000000',2,'9624b8525a564d99a34c4e4569f46e3a'),(109,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc4OTc2NSwiaWF0IjoxNzIyNzAzMzY1LCJqdGkiOiI3Mzc4ODlmN2Q5NTk0N2Y1ODNhYjFjYjM3ZWI3ODllYiIsInVzZXJfaWQiOjF9.kKdwCEitYcpjVrXx1jyEKhisLkVZLji1SCK-dXCaHVw','2024-08-03 16:42:45.756264','2024-08-04 16:42:45.000000',1,'737889f7d95947f583ab1cb37eb789eb'),(110,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc4OTgzOCwiaWF0IjoxNzIyNzAzNDM4LCJqdGkiOiIwZWMwYzBjMjAxMTk0ZGQwOGU2YWM4MzUwZmFkZWY2ZSIsInVzZXJfaWQiOjF9.CgmevQfhkusSScInIB9mFob-Hdjrp4yhRJpNOS3FIOI','2024-08-03 16:43:58.735131','2024-08-04 16:43:58.000000',1,'0ec0c0c201194dd08e6ac8350fadef6e'),(111,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc4OTg0NCwiaWF0IjoxNzIyNzAzNDQ0LCJqdGkiOiJmNzBkMGI3NjdlNTA0ZTI2YjQ1ZGNmNWZlNWE1YjNmZiIsInVzZXJfaWQiOjJ9.VT2rxxtPAMmMNX5Znv86yt_RPedY6W_BXfAno7MSlPw','2024-08-03 16:44:04.222538','2024-08-04 16:44:04.000000',2,'f70d0b767e504e26b45dcf5fe5a5b3ff'),(113,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc5MDcxNSwiaWF0IjoxNzIyNzA0MzE1LCJqdGkiOiIzMWIyMGFjZDkxZTA0MGQyYWU1OWRlNmE4Y2M1MjNkZiIsInVzZXJfaWQiOjF9.yxnRjKW2J1nzaFJkOgeX64WE8jM6vQZV0tu90IXWyv4','2024-08-03 16:58:35.324241','2024-08-04 16:58:35.000000',1,'31b20acd91e040d2ae59de6a8cc523df'),(114,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc5MTYyNywiaWF0IjoxNzIyNzA1MjI3LCJqdGkiOiI4NDE3ZWRjYzZhOWE0NzM0ODljY2U1Y2VlYWZkODMyZCIsInVzZXJfaWQiOjJ9.hhuW1VoZp5dCixd5u741gGFSXetJzT52fzShvBlAE8o','2024-08-03 17:13:47.017735','2024-08-04 17:13:47.000000',2,'8417edcc6a9a473489cce5ceeafd832d'),(115,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc5MTc1NSwiaWF0IjoxNzIyNzA1MzU1LCJqdGkiOiI3NzVmYzdiMjIxOGM0OWJiYjFhN2E1NTUzYzkxNzYzNCIsInVzZXJfaWQiOjF9.S3RQF1PNHcQwmfzQ_0K_63sHcF2z9ysYD01kKSLLjX0','2024-08-03 17:15:55.620822','2024-08-04 17:15:55.000000',1,'775fc7b2218c49bbb1a7a5553c917634'),(117,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjc5NTM1OSwiaWF0IjoxNzIyNzA4OTU5LCJqdGkiOiJkYzhiOGEwNDBmOGU0OThjYTVlZTQyNzVmNDlkN2ZiNiIsInVzZXJfaWQiOjF9.y0nC1lDsSECg0aMtnsUOxLpxIe9I6Zj3MbRKspmec88','2024-08-03 18:15:59.247045','2024-08-04 18:15:59.000000',1,'dc8b8a040f8e498ca5ee4275f49d7fb6'),(118,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg1NTMyMywiaWF0IjoxNzIyNzY4OTIzLCJqdGkiOiIwMjE2M2Q4MGQ2OWI0M2U0OTBiOWYyMzdmOTliZDlhZCIsInVzZXJfaWQiOjF9.5Uct9HS8-lpDHoKn7ESEKXBo4OHP5naW0DIQfSl_he4','2024-08-04 10:55:23.594417','2024-08-05 10:55:23.000000',1,'02163d80d69b43e490b9f237f99bd9ad'),(119,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg1NTQ0NiwiaWF0IjoxNzIyNzY5MDQ2LCJqdGkiOiI2NzU4OTkwMzZhMmI0ZWQ0ODE0ZDVhYmJiZjU2ZDc5MiIsInVzZXJfaWQiOjF9.sAA6eWZnGs6DRm5F9igrjSPETnPm03u0DiysXqLHPjA','2024-08-04 10:57:26.729594','2024-08-05 10:57:26.000000',1,'675899036a2b4ed4814d5abbbf56d792'),(120,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg1NTQ1NiwiaWF0IjoxNzIyNzY5MDU2LCJqdGkiOiJhNTc4ZTQwN2I2M2Y0YjM5YjQ5ZmZlMTcxMTk0OWQ4NCIsInVzZXJfaWQiOjF9.7m8OY3YnDm69I8EifqsJDFZ4DrnldunKhT_Ie46unbc','2024-08-04 10:57:36.419608','2024-08-05 10:57:36.000000',1,'a578e407b63f4b39b49ffe1711949d84'),(121,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg1NzI4MCwiaWF0IjoxNzIyNzcwODgwLCJqdGkiOiI0MzhlYzhmODNlOWM0M2YyOTY2YWFlMDUxMzAwZDdhNSIsInVzZXJfaWQiOjF9.csH1mD-9lTNyMebqyqC6dsFibq9oDdE_ETRH4R2_r7Y','2024-08-04 11:28:00.745479','2024-08-05 11:28:00.000000',1,'438ec8f83e9c43f2966aae051300d7a5'),(122,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg1NzI4MSwiaWF0IjoxNzIyNzcwODgxLCJqdGkiOiJhZThmNmUzNDA2M2E0MWZjOTBmNzNmODkzM2NjZTk1ZiIsInVzZXJfaWQiOjF9.BCr83PRef7_A0HynbPFjPFgg6FoUxsPo-27JEE0W07A','2024-08-04 11:28:01.336928','2024-08-05 11:28:01.000000',1,'ae8f6e34063a41fc90f73f8933cce95f'),(123,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg1NzI5OCwiaWF0IjoxNzIyNzcwODk4LCJqdGkiOiIxNTA4YzZlMjJjYmY0MmE4YjA0ZjVkNTNlN2JhY2NjMSIsInVzZXJfaWQiOjF9.nH171fu9smaFgDr4GlmFxr89GKjfHt8ShpbjE8-0qVI','2024-08-04 11:28:18.358216','2024-08-05 11:28:18.000000',1,'1508c6e22cbf42a8b04f5d53e7baccc1'),(124,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg1NzI5OCwiaWF0IjoxNzIyNzcwODk4LCJqdGkiOiI5ODUwNzM0OTE3ODU0OTM5OGFkN2M1NDE3NTU2ZDVkMiIsInVzZXJfaWQiOjF9.8RMXjN-j30KFOJRXHcLcCXzbYxUKZFc2M_kB_yj5xrY','2024-08-04 11:28:18.637528','2024-08-05 11:28:18.000000',1,'98507349178549398ad7c5417556d5d2'),(125,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg1NzMyNCwiaWF0IjoxNzIyNzcwOTI0LCJqdGkiOiI1OTMzYTcxZjNlNTI0Y2QzODM4ODljNTljNTA4MjY0NiIsInVzZXJfaWQiOjF9.NSslX-HbDsgDaN7FfNj7Z_q2yzd8LKMZAIlLRlJ4KH8','2024-08-04 11:28:44.038311','2024-08-05 11:28:44.000000',1,'5933a71f3e524cd383889c59c5082646'),(126,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg1NzM1NSwiaWF0IjoxNzIyNzcwOTU1LCJqdGkiOiJlMzA5NWYxNzg4ZDM0M2EwYTk2ZDgwYWQzMDJiZTNhOCIsInVzZXJfaWQiOjF9.5n6bdvJ0ZBA44-LWyzmtGEP4Mt-tyPJSvkP-2aeBnHs','2024-08-04 11:29:15.283153','2024-08-05 11:29:15.000000',1,'e3095f1788d343a0a96d80ad302be3a8'),(127,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg1NzM4MSwiaWF0IjoxNzIyNzcwOTgxLCJqdGkiOiI5YjJlYzMxOTNkNTk0ZjY1OTYwNjg3YzE5NTU0ZWEyNSIsInVzZXJfaWQiOjF9.5OLNFmWSUj0nGSFA7JCvW445cFlzFfnt8XRcRqLWY1k','2024-08-04 11:29:41.289315','2024-08-05 11:29:41.000000',1,'9b2ec3193d594f65960687c19554ea25'),(128,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg1NzQxOCwiaWF0IjoxNzIyNzcxMDE4LCJqdGkiOiJiYmY4YTBjY2FhZDU0MTdlYmY3OWNjNTczN2EzZWU5NyIsInVzZXJfaWQiOjF9.ItfjLqNoufhtQVGy2PDNKB7CDNHhLAc4bP7ohkr5krM','2024-08-04 11:30:18.878660','2024-08-05 11:30:18.000000',1,'bbf8a0ccaad5417ebf79cc5737a3ee97'),(129,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg1NzQ3OCwiaWF0IjoxNzIyNzcxMDc4LCJqdGkiOiJkOWJiNGJjNWU1Mzk0MGJlOTllZmYzZWE3ZTkyYjk5NyIsInVzZXJfaWQiOjF9.isb1uw5Yxaipgybt6lzd8KcgygY3WCozR3iG-IWQhpU','2024-08-04 11:31:18.135127','2024-08-05 11:31:18.000000',1,'d9bb4bc5e53940be99eff3ea7e92b997'),(130,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg1NzQ4NiwiaWF0IjoxNzIyNzcxMDg2LCJqdGkiOiIxNDYyMWFjMTE2ZjU0YTAxYWU2ZDY5YWZjOTUwOGJkYiIsInVzZXJfaWQiOjF9.CtBE5d4lB-zQEI2w_D-2ZuzpSYUhrh4Y6gnbNxDgyhw','2024-08-04 11:31:26.262272','2024-08-05 11:31:26.000000',1,'14621ac116f54a01ae6d69afc9508bdb'),(131,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg1NzU0OCwiaWF0IjoxNzIyNzcxMTQ4LCJqdGkiOiJkNDBmMGJkNmI2ZjQ0MDAzOTA0OGU2ZWI3NGQ3YmM4MSIsInVzZXJfaWQiOjF9.aMmXR3n-ns6Ke9MUhIkAnND6DfE6ZV5jclsfTw7BaiE','2024-08-04 11:32:28.742619','2024-08-05 11:32:28.000000',1,'d40f0bd6b6f440039048e6eb74d7bc81'),(132,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg1NzU4OCwiaWF0IjoxNzIyNzcxMTg4LCJqdGkiOiJjM2RkY2E1OTQ1NTc0NjA3YTUyMDI3ZDZkZGRkN2FiZCIsInVzZXJfaWQiOjF9.ChCquSYx9cMLtNWpiZl8P2I_rIILMlqoOo-tIXSXKNo','2024-08-04 11:33:08.437188','2024-08-05 11:33:08.000000',1,'c3ddca5945574607a52027d6dddd7abd'),(133,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg1NzYyMywiaWF0IjoxNzIyNzcxMjIzLCJqdGkiOiJiNTA5ZjY2Yzc0MTg0MzNlOTVmNTY1YmU2ZGUzNTJjZSIsInVzZXJfaWQiOjF9.IsnNT9KhyNIe2OtX08JBFCu4OiNlB_q_i6mrE__oA5Y','2024-08-04 11:33:43.804939','2024-08-05 11:33:43.000000',1,'b509f66c7418433e95f565be6de352ce'),(134,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg1NzY1MSwiaWF0IjoxNzIyNzcxMjUxLCJqdGkiOiI4NWVhOGEzZjg0NTc0YTk2OTkzZjdlMjE5ZjYwZjlhYiIsInVzZXJfaWQiOjF9.C3PopQlT8nMeCx_roASu8zQM9vXw4r0vNfQzhPWWX7A','2024-08-04 11:34:11.629622','2024-08-05 11:34:11.000000',1,'85ea8a3f84574a96993f7e219f60f9ab'),(135,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg1NzY4MCwiaWF0IjoxNzIyNzcxMjgwLCJqdGkiOiJiN2Y3MTBhMDFiNGY0ZTllODMwYWJiMjVkNmRhNGQ2YyIsInVzZXJfaWQiOjF9.VUtUv-teUJyzfwBE7s-ndUyG3ucnaiTJvfihvz9EJ1Q','2024-08-04 11:34:40.293204','2024-08-05 11:34:40.000000',1,'b7f710a01b4f4e9e830abb25d6da4d6c'),(136,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg1NzY4MCwiaWF0IjoxNzIyNzcxMjgwLCJqdGkiOiJhM2ZmNWYxMzkwZWE0MDE0ODY4ZjMyMzBhZDUzODBiZSIsInVzZXJfaWQiOjF9.3q6mxg1xRc3eky9uanob3-JwcjAcSszB3EKphRE4TM8','2024-08-04 11:34:40.354248','2024-08-05 11:34:40.000000',1,'a3ff5f1390ea4014868f3230ad5380be'),(137,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg1NzcwNiwiaWF0IjoxNzIyNzcxMzA2LCJqdGkiOiJmN2U2ZWYzMGVhMjM0MTgxOWI1YjVjZTMwNjViMTNiOSIsInVzZXJfaWQiOjF9.1lYyCtzWyyUxsqEeqBeZKYlvTFQOtKe-lFPIL-aUmlg','2024-08-04 11:35:06.790529','2024-08-05 11:35:06.000000',1,'f7e6ef30ea2341819b5b5ce3065b13b9'),(138,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg1NzcyMiwiaWF0IjoxNzIyNzcxMzIyLCJqdGkiOiJjMzVmYzZmMzljYTU0OWY5OTA4OGRlOTc0YWE0MDhmNSIsInVzZXJfaWQiOjF9.v1MeRqZWYo_M5qUsMZ_I7kwy4cmnC72t2-vYe-wOGaY','2024-08-04 11:35:22.679477','2024-08-05 11:35:22.000000',1,'c35fc6f39ca549f99088de974aa408f5'),(139,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MTg3NCwiaWF0IjoxNzIyNzc1NDc0LCJqdGkiOiJkMThlMDQyODdhOGQ0MzhjOWU0MjExZTIwZTAxMTFjZSIsInVzZXJfaWQiOjF9.0Bfpv3Lc9Q8objvSTpnbWDZ0t6PS0-7gIqIlop2S3lY','2024-08-04 12:44:34.044193','2024-08-05 12:44:34.000000',1,'d18e04287a8d438c9e4211e20e0111ce'),(140,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MTg3NCwiaWF0IjoxNzIyNzc1NDc0LCJqdGkiOiI4ZjBhYzIzOWViOTU0NTYyOTJiNDZiMDMzNTVkM2UzNiIsInVzZXJfaWQiOjF9.f701eNvhyP-KITG4gbmFV2M54xTt7CWC18Im5vIWPDo','2024-08-04 12:44:34.161815','2024-08-05 12:44:34.000000',1,'8f0ac239eb95456292b46b03355d3e36'),(141,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MTkyNywiaWF0IjoxNzIyNzc1NTI3LCJqdGkiOiJhMmY2ZTI1OTU2NGY0NTI1YTczYjhlMWUxNDNlODlmNCIsInVzZXJfaWQiOjF9.44sRM3n1eBLqjtilQhVo3pm2JVUOVQGM8YdlRwblkmg','2024-08-04 12:45:27.688341','2024-08-05 12:45:27.000000',1,'a2f6e259564f4525a73b8e1e143e89f4'),(142,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MjMwNiwiaWF0IjoxNzIyNzc1OTA2LCJqdGkiOiJmYWU4Y2ExZjM1MzY0YTQ3Yjk0MjgwOWFkYzI4ZjY3MiIsInVzZXJfaWQiOjF9.aAeva7mRMY3iAKTMGvTjhdYJUVrF8sUXLkxYpE74hi4','2024-08-04 12:51:46.168518','2024-08-05 12:51:46.000000',1,'fae8ca1f35364a47b942809adc28f672'),(143,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MjMwNywiaWF0IjoxNzIyNzc1OTA3LCJqdGkiOiIzYTZjYmFkNjMzN2Q0ZTgzODc1OTI2MWUzZmE2NDljNSIsInVzZXJfaWQiOjF9.J7vShzNsZBNtPInBrZioGpczKxKcHRJRYlLyzyUzfjA','2024-08-04 12:51:47.600216','2024-08-05 12:51:47.000000',1,'3a6cbad6337d4e838759261e3fa649c5'),(144,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MjMwOCwiaWF0IjoxNzIyNzc1OTA4LCJqdGkiOiJiZDRhZjA1YjNiMjM0ZjhlYmExZDY0OTc5YTU0OTFiNiIsInVzZXJfaWQiOjF9.hdw5vgw-qp_CHeoJcL7c8YgonPZxdNuC0dHuNovob4Y','2024-08-04 12:51:48.465986','2024-08-05 12:51:48.000000',1,'bd4af05b3b234f8eba1d64979a5491b6'),(145,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MjMwOCwiaWF0IjoxNzIyNzc1OTA4LCJqdGkiOiJiYTFhNmYyODMyYmI0MzQ0ODJmZDBiYTEyNDQ0Njc1ZCIsInVzZXJfaWQiOjF9.Z62-llcnXuwMUUnws7qvgBM2G68YYD2yqwLNXZb0OTw','2024-08-04 12:51:48.828029','2024-08-05 12:51:48.000000',1,'ba1a6f2832bb434482fd0ba12444675d'),(146,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MjMxOCwiaWF0IjoxNzIyNzc1OTE4LCJqdGkiOiI5M2YxYjQzNDYyODc0NmU0YjAyNjUyMzkxOGY1YWY1NCIsInVzZXJfaWQiOjF9.u5tn5OXybubcuMPU7ko8WeB06-cNwMeGGJt5Nwos8qk','2024-08-04 12:51:58.192926','2024-08-05 12:51:58.000000',1,'93f1b434628746e4b026523918f5af54'),(147,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MjMzMywiaWF0IjoxNzIyNzc1OTMzLCJqdGkiOiI5NmRlYWViOWE0OGQ0NDk1YjBhNTA5NWY4ZjZjMDJjZSIsInVzZXJfaWQiOjF9.ZoNqAZ7m4toedfk7O6ALpP40gFSgzOd3XxqNg7oMTaE','2024-08-04 12:52:13.768371','2024-08-05 12:52:13.000000',1,'96deaeb9a48d4495b0a5095f8f6c02ce'),(148,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MjQ5MiwiaWF0IjoxNzIyNzc2MDkyLCJqdGkiOiIyMjFhMTM1MDY0YmM0NzU1YTdjN2FlNjIxOWM3MDc5MSIsInVzZXJfaWQiOjF9.lE5hQbd3BwWUgPbldn5mH_4-tma9sQxpV7JrkndMyxs','2024-08-04 12:54:52.810119','2024-08-05 12:54:52.000000',1,'221a135064bc4755a7c7ae6219c70791'),(149,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MjU0NywiaWF0IjoxNzIyNzc2MTQ3LCJqdGkiOiI2ZWY3ODM4NGQ2MzI0MDUzYjRiYmFiZDBiYmM1NDM5YyIsInVzZXJfaWQiOjF9.2wT4nWtfzHStlLWvjioowViHOe2QYWWYt-w3Uh5Cohc','2024-08-04 12:55:47.694968','2024-08-05 12:55:47.000000',1,'6ef78384d6324053b4bbabd0bbc5439c'),(150,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2Mjg3MSwiaWF0IjoxNzIyNzc2NDcxLCJqdGkiOiIzMDdkODhkNjI3NDk0ZTZkYTllZWY3YmZkZTJlNzdhNSIsInVzZXJfaWQiOjF9.bu51_AoM5fTg6udswIFasV0Oj_0ddSFME6IYcNHBPVY','2024-08-04 13:01:11.059433','2024-08-05 13:01:11.000000',1,'307d88d627494e6da9eef7bfde2e77a5'),(151,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzA3MiwiaWF0IjoxNzIyNzc2NjcyLCJqdGkiOiIwZWJmOTBkOTU5OTk0NjZkODNhMjhmZWY4Yzc0MjNmYyIsInVzZXJfaWQiOjF9.E9uQgFKRvMgUGr6q_A0-7_31h9e-5hLNthLNB0HPais','2024-08-04 13:04:32.675227','2024-08-05 13:04:32.000000',1,'0ebf90d95999466d83a28fef8c7423fc'),(152,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzEwNywiaWF0IjoxNzIyNzc2NzA3LCJqdGkiOiJkODJiOWUyOTdjNTI0YTkzOTNiYmQwMGQ4OTBkODQ0MyIsInVzZXJfaWQiOjF9.acwYjI5MaTRLMoCRYXF0hirE9b6mhi1CbQ0_Mt_q14s',NULL,'2024-08-05 13:05:07.000000',NULL,'d82b9e297c524a9393bbd00d890d8443'),(153,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzE2MSwiaWF0IjoxNzIyNzc2NzYxLCJqdGkiOiJhNjEzMzhlNWE4NWI0YTI1ODY3MzQ3MmUwYWM2MGM3YiIsInVzZXJfaWQiOjF9.mGMpsGvs7PcrD6IQParaSwS0KGMJZM9Otsa9BG_qfkg',NULL,'2024-08-05 13:06:01.000000',NULL,'a61338e5a85b4a258673472e0ac60c7b'),(154,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzE3OCwiaWF0IjoxNzIyNzc2Nzc4LCJqdGkiOiJiOGRjMDM5ZjVlMzU0YzliODJmOGNjNWUwNTJjY2RmYyIsInVzZXJfaWQiOjF9.jq3zxpVday9KvbzltfP6GnvWgwEYKc7zQCt6m68totk',NULL,'2024-08-05 13:06:18.000000',NULL,'b8dc039f5e354c9b82f8cc5e052ccdfc'),(155,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzE3OCwiaWF0IjoxNzIyNzc2Nzc4LCJqdGkiOiJhNmJlNjllZDE1NzE0ZmFjOWUzMjg2OWJhY2U1MDlmMSIsInVzZXJfaWQiOjF9.i7SH776rOovNbXNIBEVx8Nj-PaI4abTIM8agAjrkNHw',NULL,'2024-08-05 13:06:18.000000',NULL,'a6be69ed15714fac9e32869bace509f1'),(156,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzE4MCwiaWF0IjoxNzIyNzc2NzgwLCJqdGkiOiJlNTU0MzlhMWNlNDg0YzU4OTE5NmRhNzE3YmE4NDE3NiIsInVzZXJfaWQiOjF9.eLdZeYpmgMgP8rbs1xxKNQRT6WBUvAfDa0FnaRx6fKQ',NULL,'2024-08-05 13:06:20.000000',NULL,'e55439a1ce484c589196da717ba84176'),(157,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzE4MSwiaWF0IjoxNzIyNzc2NzgxLCJqdGkiOiJjMzM1NTVkMmEyZTg0YTM4OGQ5MGM4NzYwZWY5ODc3NyIsInVzZXJfaWQiOjF9.ww0gWaVykv9qxxzHR57DB6jrOgxv1aIdG62hs0GlVgQ',NULL,'2024-08-05 13:06:21.000000',NULL,'c33555d2a2e84a388d90c8760ef98777'),(158,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzE4MiwiaWF0IjoxNzIyNzc2NzgyLCJqdGkiOiJlMjJmNTJlMzc4YTA0ZDc0YmQ5YWFlNTRlOTQwOTI2NyIsInVzZXJfaWQiOjF9.pKPWo3LAOLj_nDH4M0JFOkSJ1FNpCeidx3EBxuvUH50',NULL,'2024-08-05 13:06:22.000000',NULL,'e22f52e378a04d74bd9aae54e9409267'),(159,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzE4MywiaWF0IjoxNzIyNzc2NzgzLCJqdGkiOiIxMzlmMGFjNWIwN2I0MjdmOTcxMTAyMWNhZWJmMTVlYyIsInVzZXJfaWQiOjF9.5IaDLTbCRPPLddvcE4-1H8W6NYdX0D8jrrXxWfqmurc',NULL,'2024-08-05 13:06:23.000000',NULL,'139f0ac5b07b427f9711021caebf15ec'),(160,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzE4NCwiaWF0IjoxNzIyNzc2Nzg0LCJqdGkiOiJhNjgyYzdiYzg1NjE0NDQxYTQ3NDI0ZmJiMjI4Yzc2MiIsInVzZXJfaWQiOjF9.Pga6XgLGDgDv-zuxC5s1uBadaSkvoWuyw7mdNe0RB9c',NULL,'2024-08-05 13:06:24.000000',NULL,'a682c7bc85614441a47424fbb228c762'),(161,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzE4NSwiaWF0IjoxNzIyNzc2Nzg1LCJqdGkiOiJlMjg4YWI5ZmU0NGU0YjhkYjNjMDI1NmEzYTFiZWE3MiIsInVzZXJfaWQiOjF9.7rBGY2T3MEsFsx_6RcOSlZ35Qi4FFsEzXY2GLSIJzdk',NULL,'2024-08-05 13:06:25.000000',NULL,'e288ab9fe44e4b8db3c0256a3a1bea72'),(162,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzE4NiwiaWF0IjoxNzIyNzc2Nzg2LCJqdGkiOiI5ODNjN2YzZTNlNjI0NmEwYTBhZTEwMzhhMjA3OWZkYSIsInVzZXJfaWQiOjF9.fAg5zJya58tG02xyxag9P5632tyC1RHzLCPk7auRfvg',NULL,'2024-08-05 13:06:26.000000',NULL,'983c7f3e3e6246a0a0ae1038a2079fda'),(163,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzE4NywiaWF0IjoxNzIyNzc2Nzg3LCJqdGkiOiI5M2Q4YTlhZWU5YTg0YmVhYmQ0YzRiM2NiMDI5Nzc1YSIsInVzZXJfaWQiOjF9.GlQ2zDbgvOTtei6XLuNG5_ADZsRODXzAz8PHdx_HPgs',NULL,'2024-08-05 13:06:27.000000',NULL,'93d8a9aee9a84beabd4c4b3cb029775a'),(164,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzE4OCwiaWF0IjoxNzIyNzc2Nzg4LCJqdGkiOiJiNzA1YmJkNDYwMWI0MzNkOTY1NzRjZmFhZmQ3N2E2NSIsInVzZXJfaWQiOjF9.5V1o_h9lClNaZUfMfoAQ2EkAt_wMsxu19f-YZSqjsyo',NULL,'2024-08-05 13:06:28.000000',NULL,'b705bbd4601b433d96574cfaafd77a65'),(165,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzE4OSwiaWF0IjoxNzIyNzc2Nzg5LCJqdGkiOiI2NTA0Y2U5MTY1MDE0ZWUwOWRjYzQzMzU5YmUxYTYyZCIsInVzZXJfaWQiOjF9.vfLwQz2UxSYmft_iPRIz_Mm9eRNQrTNs3ZftK_rwQGg',NULL,'2024-08-05 13:06:29.000000',NULL,'6504ce9165014ee09dcc43359be1a62d'),(166,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzE5MCwiaWF0IjoxNzIyNzc2NzkwLCJqdGkiOiI2NjhkZjE1OTAzMGI0OThlODdhNjliNDI0NmE4ZWI1MSIsInVzZXJfaWQiOjF9.mT1YHtEOcdp3lPe2IaAy0CyAjSuyTLE9z7o8n7NnElA',NULL,'2024-08-05 13:06:30.000000',NULL,'668df159030b498e87a69b4246a8eb51'),(167,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzE5MSwiaWF0IjoxNzIyNzc2NzkxLCJqdGkiOiIzM2Y4YzEwMDg3M2E0YjM5OWRhOTM0MTc3NzhiYjZmYiIsInVzZXJfaWQiOjF9.Sf_yNC34k5YXYg1JDgmBzhof8Uq6ZsrvWXRVLFw2MoE',NULL,'2024-08-05 13:06:31.000000',NULL,'33f8c100873a4b399da93417778bb6fb'),(168,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzE5MiwiaWF0IjoxNzIyNzc2NzkyLCJqdGkiOiI4YmU1NzA5NDBlOTE0Yzg4OTQ2M2I0YTUyMDZjZTBhOSIsInVzZXJfaWQiOjF9.Blg_VXG6CjPW0yptSiVDeS_9atIjxejHTu2Qh8rc34o',NULL,'2024-08-05 13:06:32.000000',NULL,'8be570940e914c889463b4a5206ce0a9'),(169,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzE5MywiaWF0IjoxNzIyNzc2NzkzLCJqdGkiOiJiMjljNzUxNmJhOTg0ZGJmOWMzZDExNzg5NjgzNmE5NiIsInVzZXJfaWQiOjF9.T_jImAt28-6FeIeZq4FitgC4j_ST2hD4gpi4vDpSOoM',NULL,'2024-08-05 13:06:33.000000',NULL,'b29c7516ba984dbf9c3d117896836a96'),(170,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzE5NCwiaWF0IjoxNzIyNzc2Nzk0LCJqdGkiOiJhNGRkY2MwNGJlMzM0MGU1OTc4YTMxMDk4MGEwYTU5MCIsInVzZXJfaWQiOjF9.DZW7Q466HyYKlgs7a0E3PGjyelg8VWH2_iaOYTwrBh0',NULL,'2024-08-05 13:06:34.000000',NULL,'a4ddcc04be3340e5978a310980a0a590'),(171,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzE5NSwiaWF0IjoxNzIyNzc2Nzk1LCJqdGkiOiJjNzJiYzc2ZDJjZTc0MjBiODE0MGFkNzAzNWNkMjFkZSIsInVzZXJfaWQiOjF9.Ds5X-_WgwpMTEr7HfD_PtrG78U_HU2AJCySFDAEsQkM',NULL,'2024-08-05 13:06:35.000000',NULL,'c72bc76d2ce7420b8140ad7035cd21de'),(172,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzE5NiwiaWF0IjoxNzIyNzc2Nzk2LCJqdGkiOiI5ZDYyMDMwMjVkMzY0MzhkOGZjZTcwM2I4OGM5YzZjMSIsInVzZXJfaWQiOjF9.oa8I_HsUchDcC9MafCb2NpySgY6v2hyKJQ3OMTb_EOY',NULL,'2024-08-05 13:06:36.000000',NULL,'9d6203025d36438d8fce703b88c9c6c1'),(173,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzE5NiwiaWF0IjoxNzIyNzc2Nzk2LCJqdGkiOiJkOTU3MjMzNDRmYWI0NGVlOTQ1YTNmYTYwZjQ2OTkzNiIsInVzZXJfaWQiOjF9.dmX45iEgiBRvF45frhE7Z2WIGpWZOx1O7C1HHVea34M',NULL,'2024-08-05 13:06:36.000000',NULL,'d95723344fab44ee945a3fa60f469936'),(174,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzE5NywiaWF0IjoxNzIyNzc2Nzk3LCJqdGkiOiI3MTM5YzA4OWVkNzU0MmM3OTMwZjllNjRkMmVmMDdkMyIsInVzZXJfaWQiOjF9.07K-hZci3TSGFPsEpQpiTZhdTrtOPhmiotOjNvecsKU',NULL,'2024-08-05 13:06:37.000000',NULL,'7139c089ed7542c7930f9e64d2ef07d3'),(175,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzE5OSwiaWF0IjoxNzIyNzc2Nzk5LCJqdGkiOiJlYmE4NWI4MDgxMjk0ZGEzOTVkYjg4NWQ5YTg1ZTk0OSIsInVzZXJfaWQiOjF9.ucpDnzuQzFp1zSxkJnNSsmcZvhajSHcXySrT1YhyGVg',NULL,'2024-08-05 13:06:39.000000',NULL,'eba85b8081294da395db885d9a85e949'),(176,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIwMCwiaWF0IjoxNzIyNzc2ODAwLCJqdGkiOiJhMDE5ZDg3Mjk1OTk0ZWEwYjU0YjQyOGZlNjU3ZWQzZCIsInVzZXJfaWQiOjF9.5bcCXS_E2Ym-Dcw2RFYdYCP_Rjl2QMDpj8kncj44pKk',NULL,'2024-08-05 13:06:40.000000',NULL,'a019d87295994ea0b54b428fe657ed3d'),(177,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIwMSwiaWF0IjoxNzIyNzc2ODAxLCJqdGkiOiJkMzBhMzQ3N2M1MjA0ZjcwOWIyODk3ZWUzNzlkMWVjZCIsInVzZXJfaWQiOjF9.rmDqjtRIFAs2Gx1xg8a0v7_DagUuIe9aWtJzxNWvURU',NULL,'2024-08-05 13:06:41.000000',NULL,'d30a3477c5204f709b2897ee379d1ecd'),(178,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIwMiwiaWF0IjoxNzIyNzc2ODAyLCJqdGkiOiJhMGVhZjNmZjIzMTk0NmVkOTNmOTBkYmFkNTdiNWEwMiIsInVzZXJfaWQiOjF9.KIX0-r1wn-QWp7dIjNxLivK8eOK7wjPn-YOWnplc-co',NULL,'2024-08-05 13:06:42.000000',NULL,'a0eaf3ff231946ed93f90dbad57b5a02'),(179,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIwMywiaWF0IjoxNzIyNzc2ODAzLCJqdGkiOiI0ZjdiZTRiZWIyYzY0MGNjOWI2MzMxMDE0Y2I2YjFlYSIsInVzZXJfaWQiOjF9.a5G6FGDGsAiWX43yyBhJaVa7YOVday7q5YHvzIcwklY',NULL,'2024-08-05 13:06:43.000000',NULL,'4f7be4beb2c640cc9b6331014cb6b1ea'),(180,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIwNCwiaWF0IjoxNzIyNzc2ODA0LCJqdGkiOiIzMjE5NDJiZjYzMzM0ZjU5OTk3YTZhYTQ0NTA0ZTQ2MSIsInVzZXJfaWQiOjF9.8iTJlTlJg7gW11vMkYGD6ESdjLzzy8ZZnyKpbzns_SQ',NULL,'2024-08-05 13:06:44.000000',NULL,'321942bf63334f59997a6aa44504e461'),(181,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIwNSwiaWF0IjoxNzIyNzc2ODA1LCJqdGkiOiIyZDFjYWM0MDUwZDg0NTc4YmEyNmE5YjM2ZjFlZjc3ZCIsInVzZXJfaWQiOjF9.odGXQSCx5YVAQxdvCZGTE1PxN01pfV1H48QwZOPGq8M',NULL,'2024-08-05 13:06:45.000000',NULL,'2d1cac4050d84578ba26a9b36f1ef77d'),(182,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIwNiwiaWF0IjoxNzIyNzc2ODA2LCJqdGkiOiIyNTlhYWZiNTE3Nzk0OWI1OTFmNjliNjgwYWU5ZmRmNyIsInVzZXJfaWQiOjF9.s5_JErPXI2Xpao8Hrf4ionua_zYWPO0RAv3iy1FvFME',NULL,'2024-08-05 13:06:46.000000',NULL,'259aafb5177949b591f69b680ae9fdf7'),(183,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIwNywiaWF0IjoxNzIyNzc2ODA3LCJqdGkiOiIxMTc3OTY5N2U3ZGE0M2Q5Yjk2NWRkMGE0YmZlZTU4YiIsInVzZXJfaWQiOjF9.OMLq4YE5v7N9VoNi1076vGMOpLA9urd18twXGrd93IQ',NULL,'2024-08-05 13:06:47.000000',NULL,'11779697e7da43d9b965dd0a4bfee58b'),(184,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIwOCwiaWF0IjoxNzIyNzc2ODA4LCJqdGkiOiJhM2U1YTE4YTEwNTY0NWI4OWE2ZmU3NmIzYjNiMThmZiIsInVzZXJfaWQiOjF9.PEs-9ePqVoVWFAWlDmLdOYtuGpUQTpTPGPOOIG-4SOc',NULL,'2024-08-05 13:06:48.000000',NULL,'a3e5a18a105645b89a6fe76b3b3b18ff'),(185,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIwOSwiaWF0IjoxNzIyNzc2ODA5LCJqdGkiOiIwYzA3NzdkM2M1Zjg0MDQ0ODMwMjMzOWFmNGUyZTUyNSIsInVzZXJfaWQiOjF9.CNkUhtVn8kGAry6-ESHBj8dj7uyypUFqm_7Zp6X75Pg',NULL,'2024-08-05 13:06:49.000000',NULL,'0c0777d3c5f840448302339af4e2e525'),(186,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIwOSwiaWF0IjoxNzIyNzc2ODA5LCJqdGkiOiI3OTk5NDM3ZGY2Yjk0ZjNjYTg5NmJhM2Q0MWRiZmQxMCIsInVzZXJfaWQiOjF9.KMDwOE-OpH9v3qtHClTvNP7f2vr7PNjU3lq_HJagqHE',NULL,'2024-08-05 13:06:49.000000',NULL,'7999437df6b94f3ca896ba3d41dbfd10'),(187,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIxMSwiaWF0IjoxNzIyNzc2ODExLCJqdGkiOiJlN2RmZWMyMmRjOWU0ZDU2ODI4MTgwYjhmZDFjMmRjYyIsInVzZXJfaWQiOjF9.RWntKftt7fWTj63UB8g_khkmBGtzmfcNVMCC0AVqJJE',NULL,'2024-08-05 13:06:51.000000',NULL,'e7dfec22dc9e4d56828180b8fd1c2dcc'),(188,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIxMiwiaWF0IjoxNzIyNzc2ODEyLCJqdGkiOiI4YmQ3MDBhNjVlMzA0OTU2OWZmZmMyYTQ2ZDg5NTA3YyIsInVzZXJfaWQiOjF9.zixYhCydnme3NqMlIpzUG8AHjERnsoqQKTtKiU8LfXU',NULL,'2024-08-05 13:06:52.000000',NULL,'8bd700a65e3049569fffc2a46d89507c'),(189,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIxMywiaWF0IjoxNzIyNzc2ODEzLCJqdGkiOiI0NzQyNDRiYTAwZDk0NjkzOGMxYTY1YjEzNjMzYWNjYiIsInVzZXJfaWQiOjF9.W15o9XKxETwuDgQr2I76ux419hZz25TSMVGVzZe6yUE',NULL,'2024-08-05 13:06:53.000000',NULL,'474244ba00d946938c1a65b13633accb'),(190,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIxNCwiaWF0IjoxNzIyNzc2ODE0LCJqdGkiOiJjOTAwYThhYjZiYjc0NWFhYTQ0N2IwM2ZjZjRiYTc4NyIsInVzZXJfaWQiOjF9.24ZRNlkvyo76SREUVUXQglhGeqK_s4tG_9F_zrMkXvs',NULL,'2024-08-05 13:06:54.000000',NULL,'c900a8ab6bb745aaa447b03fcf4ba787'),(191,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIxNSwiaWF0IjoxNzIyNzc2ODE1LCJqdGkiOiJlNzg5YjlhZTE0NGM0NjE3OTI3YWFjNmJjNjRiNjA2NSIsInVzZXJfaWQiOjF9.B0ygYTS6Fs2KPi06il5XCEglcj6ox8LR3EapjMaKx5U',NULL,'2024-08-05 13:06:55.000000',NULL,'e789b9ae144c4617927aac6bc64b6065'),(192,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIxNiwiaWF0IjoxNzIyNzc2ODE2LCJqdGkiOiI0NDQ3OGQ3NjM2Y2I0MzEzOTVhYTU5ZjAyZmZmNjVkOSIsInVzZXJfaWQiOjF9.X1UAFfqvF36H1tf50bJBlRRIdtxb4Ni_qnVjg-R2ZUI',NULL,'2024-08-05 13:06:56.000000',NULL,'44478d7636cb431395aa59f02fff65d9'),(193,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIxNywiaWF0IjoxNzIyNzc2ODE3LCJqdGkiOiIxYzZhNWEzYzhiZGY0NzVmYWUyNWUzM2IzZTNjNGI2NyIsInVzZXJfaWQiOjF9.F3yVuPMM1XMGA1FLWBgNoS-9Y-bb35n4MNoQ428mynE',NULL,'2024-08-05 13:06:57.000000',NULL,'1c6a5a3c8bdf475fae25e33b3e3c4b67'),(194,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIxOCwiaWF0IjoxNzIyNzc2ODE4LCJqdGkiOiI2YTJhNzYyMTU3NjU0Nzk0YmVlYTM5ODEyOWQzMmM0YiIsInVzZXJfaWQiOjF9.J7xDADoA5yO7I9x8Q1KTCL3Q-bSuQspDtcQCgoqCWpc',NULL,'2024-08-05 13:06:58.000000',NULL,'6a2a762157654794beea398129d32c4b'),(195,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIxOSwiaWF0IjoxNzIyNzc2ODE5LCJqdGkiOiJmODE5ZDRkOTFkZTA0ZGY2YWJkNDcyYjQxNTM5YTU2NCIsInVzZXJfaWQiOjF9.SKEcatvSXgUMUCQFIR1DnVtwwD5tKKcodpdJuFTF5Gc',NULL,'2024-08-05 13:06:59.000000',NULL,'f819d4d91de04df6abd472b41539a564'),(196,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIyMCwiaWF0IjoxNzIyNzc2ODIwLCJqdGkiOiIzM2RjNjVlMGFiZWQ0MTIxYmM1ZGM4YzA5NmYwMGU1NyIsInVzZXJfaWQiOjF9.gWJBWUC2EGmD2_pmWKMAKJaipM7gIHzegORAF-B2QyM',NULL,'2024-08-05 13:07:00.000000',NULL,'33dc65e0abed4121bc5dc8c096f00e57'),(197,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIyMSwiaWF0IjoxNzIyNzc2ODIxLCJqdGkiOiJmOTQ3YTNkNTZkNzY0MDVlOTU1YWRjN2U5MjZmZDhjZiIsInVzZXJfaWQiOjF9.OD-BJXLtwaYTvEQTWanGb5R_UsTOacS1NACgP3ru3nw',NULL,'2024-08-05 13:07:01.000000',NULL,'f947a3d56d76405e955adc7e926fd8cf'),(198,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIyMiwiaWF0IjoxNzIyNzc2ODIyLCJqdGkiOiI2ZTVmNjdjYmIwNzQ0NWEyYTYyNDM3OTEzOWYzNzJkMSIsInVzZXJfaWQiOjF9.hxXM1Tu6JFmlindUx-Wm8VJUupnE-ehuZbfeAH20TRk',NULL,'2024-08-05 13:07:02.000000',NULL,'6e5f67cbb07445a2a624379139f372d1'),(199,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIyMywiaWF0IjoxNzIyNzc2ODIzLCJqdGkiOiIwYTE2NTgzZWQzY2Q0NjczODIyMjFjNWExODUxOTQwZiIsInVzZXJfaWQiOjF9.ejDZlJWWZKyna4sxGu7XnrvZvGfHmcjhrjNHGDq-myU',NULL,'2024-08-05 13:07:03.000000',NULL,'0a16583ed3cd467382221c5a1851940f'),(200,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIyNCwiaWF0IjoxNzIyNzc2ODI0LCJqdGkiOiIzMzM3ZGJjZWJkMTE0MTkxOTBhZmNiMjU2MDNhODU3NSIsInVzZXJfaWQiOjF9.Yd-sOXrf-zghuaEECF_j2BWVlMFvYH_Vi74tmau5BL8',NULL,'2024-08-05 13:07:04.000000',NULL,'3337dbcebd11419190afcb25603a8575'),(201,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIyNSwiaWF0IjoxNzIyNzc2ODI1LCJqdGkiOiI5ZmJhMWIzNDM5NTg0NzUyOTc5MThlOTg2ZDhjYjUzYiIsInVzZXJfaWQiOjF9.4QALQaC44ta4yQLw24A3F2xdmVFt5YQ3m7CStrJtdQw',NULL,'2024-08-05 13:07:05.000000',NULL,'9fba1b343958475297918e986d8cb53b'),(202,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIyNiwiaWF0IjoxNzIyNzc2ODI2LCJqdGkiOiJiN2RlMGFlOWM5MjI0NzhjYmU4OGEyN2M1NzQ4ZDIzNyIsInVzZXJfaWQiOjF9.oGzEN0MtgSNKF_VyLcvwx3eq6dJy8edUrw74y1FUbk4',NULL,'2024-08-05 13:07:06.000000',NULL,'b7de0ae9c922478cbe88a27c5748d237'),(203,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIyNywiaWF0IjoxNzIyNzc2ODI3LCJqdGkiOiJkMTdkY2MzZWJiM2Q0NzcyODU3NmUwNzJjMjcyMDdjNCIsInVzZXJfaWQiOjF9.LQNh8GP7IETUsgkZGIDICDq2rxPA5HeFmnlz2YVtQmU',NULL,'2024-08-05 13:07:07.000000',NULL,'d17dcc3ebb3d47728576e072c27207c4'),(204,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIyOCwiaWF0IjoxNzIyNzc2ODI4LCJqdGkiOiJjZWM3OTRlYzUxN2U0ZDdhOGQ2YzEyZWZjMmZhN2FiOCIsInVzZXJfaWQiOjF9.NvlyJldnp4zP3LrQOeoNL21mvO-l6mhgNjjhj99KZks',NULL,'2024-08-05 13:07:08.000000',NULL,'cec794ec517e4d7a8d6c12efc2fa7ab8'),(205,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIyOSwiaWF0IjoxNzIyNzc2ODI5LCJqdGkiOiJiMzk5YWJjZDc4NDg0MzZkYWFlNDdhNDUzNjY3NDAxNCIsInVzZXJfaWQiOjF9.hNNX1EUtIcoYn1lYWW_E8uGlafFVKuHzdWNvdNFcJbI',NULL,'2024-08-05 13:07:09.000000',NULL,'b399abcd7848436daae47a4536674014'),(206,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIzMCwiaWF0IjoxNzIyNzc2ODMwLCJqdGkiOiIxN2RhOGRlY2NlNGQ0MTYyOTYxMjRkYmRmMWU0YzUwNSIsInVzZXJfaWQiOjF9.bP1metcFHs-VUYuqGXCSl2ONvfkupbBBSPJMg1ph_FQ',NULL,'2024-08-05 13:07:10.000000',NULL,'17da8decce4d416296124dbdf1e4c505'),(207,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIzMSwiaWF0IjoxNzIyNzc2ODMxLCJqdGkiOiJmZTNlNDI2OWM2MzI0MmJhYjBkMTgwODc3ZDExMWY5ZCIsInVzZXJfaWQiOjF9.xX4fu5ftTPCj9f_ybwto77NyatzYhO5OYNjxOKttBcM',NULL,'2024-08-05 13:07:11.000000',NULL,'fe3e4269c63242bab0d180877d111f9d'),(208,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIzMSwiaWF0IjoxNzIyNzc2ODMxLCJqdGkiOiJhYjY5ZjFlMjI4NGI0NzAyODU3MjZjYWVjNmJkNWM5NyIsInVzZXJfaWQiOjF9.Xf7TUcwiG4-lMdT5Ds6rFtw3b7JqxVSKa_koAJrgZ6s',NULL,'2024-08-05 13:07:11.000000',NULL,'ab69f1e2284b470285726caec6bd5c97'),(209,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIzMywiaWF0IjoxNzIyNzc2ODMzLCJqdGkiOiJlYzVmMzJlYjBjMjk0ZDBiYjgzZWMwOGI5ODJlY2UzYiIsInVzZXJfaWQiOjF9.PBrN8OZFAukt_BZLdeR4dT1v7l5RqRc4Eqpo9GwIKjY',NULL,'2024-08-05 13:07:13.000000',NULL,'ec5f32eb0c294d0bb83ec08b982ece3b'),(210,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIzNCwiaWF0IjoxNzIyNzc2ODM0LCJqdGkiOiJhYjk5OWU5MmE1MmE0Y2I1YWUyNThmOTg0ZjVlM2UyNSIsInVzZXJfaWQiOjF9.iceen00wPVb7DxuIKLpyxb8m8gU8f_316Ry37kN7uu8',NULL,'2024-08-05 13:07:14.000000',NULL,'ab999e92a52a4cb5ae258f984f5e3e25'),(211,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIzNSwiaWF0IjoxNzIyNzc2ODM1LCJqdGkiOiI5Y2E4ZTgwNGM4ZDU0YjE4YTRhNmU4OWRiMGQ2NWFjYiIsInVzZXJfaWQiOjF9.a_SnJpMmUhl3rhD5IuF2MiaQKByt7V1x5VW1eHMbDYE',NULL,'2024-08-05 13:07:15.000000',NULL,'9ca8e804c8d54b18a4a6e89db0d65acb'),(212,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIzNSwiaWF0IjoxNzIyNzc2ODM1LCJqdGkiOiIxMmJlMWEzZDk4NzI0ZWIzYmI1NWNkYzhkMWJjMjBjYSIsInVzZXJfaWQiOjF9.onbmRy-2ELLnrM-KhbmGQdfvUeirU1K6oxzYDY0uOC0',NULL,'2024-08-05 13:07:15.000000',NULL,'12be1a3d98724eb3bb55cdc8d1bc20ca'),(213,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIzNywiaWF0IjoxNzIyNzc2ODM3LCJqdGkiOiJjNWE5MGE5Y2MwNGE0N2RlOWE3ODkwZmM2MDg2ZjU0YSIsInVzZXJfaWQiOjF9.oNH40iwAB_FmQiSW3IoDdxoYKd_Gncu356zZB1agKCY',NULL,'2024-08-05 13:07:17.000000',NULL,'c5a90a9cc04a47de9a7890fc6086f54a'),(214,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIzOCwiaWF0IjoxNzIyNzc2ODM4LCJqdGkiOiI5OWI3NzcwMTYzMmI0NThlYjg5NDE4NzcxNmFmODAyNCIsInVzZXJfaWQiOjF9.tPEIk5YRFBrpI0k2PpIHkPyZAUYfOvLrjhCk3BFMjXc',NULL,'2024-08-05 13:07:18.000000',NULL,'99b77701632b458eb894187716af8024'),(215,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzIzOCwiaWF0IjoxNzIyNzc2ODM4LCJqdGkiOiI2ZWE3N2FjZjc0MTU0MzY2YWVkNTY3NTVkNWE2OTg4ZCIsInVzZXJfaWQiOjF9.kgVfhwRY_QuRorHH3ZW241_KCVLcztghVmrBeenAA0g',NULL,'2024-08-05 13:07:18.000000',NULL,'6ea77acf74154366aed56755d5a6988d'),(216,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI0MCwiaWF0IjoxNzIyNzc2ODQwLCJqdGkiOiJkZDM5NWQ1NWM3MTc0ZjRiYjJhMWJiYmIwOTljYzAzNSIsInVzZXJfaWQiOjF9.pN5x9ZldnNsze01SIPma5K64_eMDwibNm0pq61p7DAc',NULL,'2024-08-05 13:07:20.000000',NULL,'dd395d55c7174f4bb2a1bbbb099cc035'),(217,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI0MSwiaWF0IjoxNzIyNzc2ODQxLCJqdGkiOiIxZjkyZDIwZGUxMTM0ZWRlOGM2MmVjYjBiOTMxZDViNiIsInVzZXJfaWQiOjF9.SP7Mxp00gAhmCrQJCEracxWklij2UF1nsjgXBIWnscM',NULL,'2024-08-05 13:07:21.000000',NULL,'1f92d20de1134ede8c62ecb0b931d5b6'),(218,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI0MiwiaWF0IjoxNzIyNzc2ODQyLCJqdGkiOiJjODEyMTY1YzlkODM0ZmQ0OTQ5YmQ2MjU1NmZiOGFkZSIsInVzZXJfaWQiOjF9.0CGEu_SZif4TorNkweN1FKTZkM_1_9hL-Bi5F5rTKSw',NULL,'2024-08-05 13:07:22.000000',NULL,'c812165c9d834fd4949bd62556fb8ade'),(219,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI0MywiaWF0IjoxNzIyNzc2ODQzLCJqdGkiOiJlYzgxZTk3NmZjNGM0ZDAyYmY4NmFkZGQ4OTY2YjgxZSIsInVzZXJfaWQiOjF9.URoC_rk3yIA8HxYJGt2a-lmbAAnzqdsJknpAYhW3nxU',NULL,'2024-08-05 13:07:23.000000',NULL,'ec81e976fc4c4d02bf86addd8966b81e'),(220,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI0NCwiaWF0IjoxNzIyNzc2ODQ0LCJqdGkiOiJiMzMwMzhlNzA3Mjc0ODQwYWZiZjRjOTM1NzQ3ZGVlNSIsInVzZXJfaWQiOjF9.5yecHn_ejv6z0HsvmLxCEMnbWDpR7qr5lN2COBAtaFY',NULL,'2024-08-05 13:07:24.000000',NULL,'b33038e707274840afbf4c935747dee5'),(221,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI0NSwiaWF0IjoxNzIyNzc2ODQ1LCJqdGkiOiIwNzc4OGFmOGU3NDY0YTM5OWU5ODA4MzhjZDFkNTU2MCIsInVzZXJfaWQiOjF9.ngwyj4gGWl31n05sch3jIjebecBKpYycEWsf55HtCA8',NULL,'2024-08-05 13:07:25.000000',NULL,'07788af8e7464a399e980838cd1d5560'),(222,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI0NiwiaWF0IjoxNzIyNzc2ODQ2LCJqdGkiOiI0NGIzYmI2NTkwYjU0Mzk4YTMyNTQzNjllODljYzVkNiIsInVzZXJfaWQiOjF9.FIvXDxMvG81cENuLrdaFQhrgosHeXPb0IuplYlG7P6Q',NULL,'2024-08-05 13:07:26.000000',NULL,'44b3bb6590b54398a3254369e89cc5d6'),(223,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI0NywiaWF0IjoxNzIyNzc2ODQ3LCJqdGkiOiI1NTRlZWJiZGFlNGE0YjE0YTU0ZjUwNTI2YjExYWRiOCIsInVzZXJfaWQiOjF9.A9N1bN1nN6IyifE6JxDQzamLcaqwdUTpEdvU4qR5D-U',NULL,'2024-08-05 13:07:27.000000',NULL,'554eebbdae4a4b14a54f50526b11adb8'),(224,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI0OCwiaWF0IjoxNzIyNzc2ODQ4LCJqdGkiOiI5ZDNkZGMwYjRiNzQ0NDdkYWQ1NDViYWEwNmFhMTZkMiIsInVzZXJfaWQiOjF9.71gt2ksKdFXiMwfscHouIaWcpCiJ-JXrzkGsaHvBcyI',NULL,'2024-08-05 13:07:28.000000',NULL,'9d3ddc0b4b74447dad545baa06aa16d2'),(225,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI0OSwiaWF0IjoxNzIyNzc2ODQ5LCJqdGkiOiJhM2U3NTMwOTdiNjA0MjZhYjRjZTRlOWVmNmQ2OTUxMSIsInVzZXJfaWQiOjF9.2DfOPSvLRTEdKszzOZaJv2kkuvPvuZRHxftnh3apceI',NULL,'2024-08-05 13:07:29.000000',NULL,'a3e753097b60426ab4ce4e9ef6d69511'),(226,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI1MCwiaWF0IjoxNzIyNzc2ODUwLCJqdGkiOiI4MzZkZTk5YWI5MTc0YTE5YWUwZTAyZjdlYzc0MzdjMCIsInVzZXJfaWQiOjF9.rn_C_JgXYospo52sa418ZZWtyMc7ViwxwjFX7t7KbRw',NULL,'2024-08-05 13:07:30.000000',NULL,'836de99ab9174a19ae0e02f7ec7437c0'),(227,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI1MSwiaWF0IjoxNzIyNzc2ODUxLCJqdGkiOiIyZDE0MDc0ZTZhODE0ZDNmYTQ1YjUzYmU0NTgzY2I1ZCIsInVzZXJfaWQiOjF9.quW3SzXVLE4BziJolg1Fa0bpkgLYdzlXkGQlhcI0pl0',NULL,'2024-08-05 13:07:31.000000',NULL,'2d14074e6a814d3fa45b53be4583cb5d'),(228,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI1MiwiaWF0IjoxNzIyNzc2ODUyLCJqdGkiOiI3MmUzNGMzZmEyNGE0MmQ1YWQ4OWQ2ZWRhMDNlZjkxYyIsInVzZXJfaWQiOjF9.vr_fcJtkPkAp_Jwnd2Ktf0XHyKmbD1u5H9IvACcQfYo',NULL,'2024-08-05 13:07:32.000000',NULL,'72e34c3fa24a42d5ad89d6eda03ef91c'),(229,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI1MywiaWF0IjoxNzIyNzc2ODUzLCJqdGkiOiIxZmIxYzdhMDNjNmM0YTQ3YmViMTM0ZTJhZWNhMTQzOCIsInVzZXJfaWQiOjF9.oIV3KJ8AvEnKLPxxpg0geQxTJvQuSw3_pwR2uGMGbys',NULL,'2024-08-05 13:07:33.000000',NULL,'1fb1c7a03c6c4a47beb134e2aeca1438'),(230,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI1NCwiaWF0IjoxNzIyNzc2ODU0LCJqdGkiOiJiZWY4NGUzNjA2YmM0NGVlOTkxZTVhMzhjODQ4MTU5YSIsInVzZXJfaWQiOjF9.okB4LCoJFPvqHlIlDdQIl9pMcBYURo_JPmu0PVa54FA',NULL,'2024-08-05 13:07:34.000000',NULL,'bef84e3606bc44ee991e5a38c848159a'),(231,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI1NCwiaWF0IjoxNzIyNzc2ODU0LCJqdGkiOiJlMWI4ZmI2MDEzM2U0NmQ5YWI5NjJkZTg2NWY2MjgyOCIsInVzZXJfaWQiOjF9.Rnrfa9cYzoGePEcZyBZyT1d2jgd4PCpSDijPVPEvFg4',NULL,'2024-08-05 13:07:34.000000',NULL,'e1b8fb60133e46d9ab962de865f62828'),(232,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI1NiwiaWF0IjoxNzIyNzc2ODU2LCJqdGkiOiJmNjc2NzUwNmExZjQ0NjE0YWU0ZGViOGQyOWRhNTZlZSIsInVzZXJfaWQiOjF9.fSBNKo1jrlckIDLGE1Dvtur1Y791mByuNOOgWCTsyM4',NULL,'2024-08-05 13:07:36.000000',NULL,'f6767506a1f44614ae4deb8d29da56ee'),(233,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI1NywiaWF0IjoxNzIyNzc2ODU3LCJqdGkiOiI3OTg2MGVlYjY4ZWQ0ZDg3OTU3YzFmMmE1MmQ3NTkzNiIsInVzZXJfaWQiOjF9.0cLcN1dPjKhVCuG1WJUnqqYNjVOSa8Pj0o47M5gitCA',NULL,'2024-08-05 13:07:37.000000',NULL,'79860eeb68ed4d87957c1f2a52d75936'),(234,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI1OCwiaWF0IjoxNzIyNzc2ODU4LCJqdGkiOiI3ZGFlM2IzNTFiN2E0YjQ0YjM2ZjlkNGI5NDAwNDIzOSIsInVzZXJfaWQiOjF9.zixOhClmE6mrLm3OlSF970LTAw8y-yo_Lmkj9CLwYwM',NULL,'2024-08-05 13:07:38.000000',NULL,'7dae3b351b7a4b44b36f9d4b94004239'),(235,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI1OSwiaWF0IjoxNzIyNzc2ODU5LCJqdGkiOiJiYWRlYTdlYTQxNWE0ZTBkODE4MTRiNGIwYzNkYjk4NiIsInVzZXJfaWQiOjF9.9YBhAuSXOHDZfQHtb1fnCERyfPmok-_ciVJ80UA-b54',NULL,'2024-08-05 13:07:39.000000',NULL,'badea7ea415a4e0d81814b4b0c3db986'),(236,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI2MCwiaWF0IjoxNzIyNzc2ODYwLCJqdGkiOiIwNTlmYTM2M2QyMmQ0OTVkOTcwZTA3ZDY4MzRjYjFkZiIsInVzZXJfaWQiOjF9.1FQCCfnyosahdjQt6u_yUN0qq_Q0_L5iAN8c1YDRcQ8',NULL,'2024-08-05 13:07:40.000000',NULL,'059fa363d22d495d970e07d6834cb1df'),(237,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI2MSwiaWF0IjoxNzIyNzc2ODYxLCJqdGkiOiJiMzVmMWQxNzRkNTI0Mjk0YTg1ODY3M2QzMmU0ZTZkMCIsInVzZXJfaWQiOjF9.kMT7tGbqbeN9DwxZXBXtHocC8dNZtnfFCTiNvzxvW0Q',NULL,'2024-08-05 13:07:41.000000',NULL,'b35f1d174d524294a858673d32e4e6d0'),(238,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI2MiwiaWF0IjoxNzIyNzc2ODYyLCJqdGkiOiIzNDBlMzQ0YjJmODI0MWY5OTRjODk1MzgxYTJiODJlMCIsInVzZXJfaWQiOjF9.KCXUJfNQvfSuD8XJmHPgiojaig74Ei4iDHvYpKH64LE',NULL,'2024-08-05 13:07:42.000000',NULL,'340e344b2f8241f994c895381a2b82e0'),(239,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI2MywiaWF0IjoxNzIyNzc2ODYzLCJqdGkiOiIzYTM4MDkwMzkzZWM0MjE4YjBhZTFiZTk1YTU5MDFiMCIsInVzZXJfaWQiOjF9.6pAb6ZNw0Z4EYy_VoA4Z9_LXmDvSF4UGeHddtJfOths',NULL,'2024-08-05 13:07:43.000000',NULL,'3a38090393ec4218b0ae1be95a5901b0'),(240,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI2NCwiaWF0IjoxNzIyNzc2ODY0LCJqdGkiOiJmMDNlNWY4NTUxOGM0Mjc1ODVmNTMwZGYzZmZjY2ZlMCIsInVzZXJfaWQiOjF9.Rr8D6laNXFkOJBieZwRZeKtGgkqIJ0pUXzhBQdy3b8U',NULL,'2024-08-05 13:07:44.000000',NULL,'f03e5f85518c427585f530df3ffccfe0'),(241,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI2NCwiaWF0IjoxNzIyNzc2ODY0LCJqdGkiOiI0OTBhZDEwNTQ1ZDQ0MTU2YTg1MGU3MzAyY2UwZDRhZCIsInVzZXJfaWQiOjF9.W5GBp7tTNj5PodpukqMkkvgTjlApQ4QWjGJMJLIY520',NULL,'2024-08-05 13:07:44.000000',NULL,'490ad10545d44156a850e7302ce0d4ad'),(242,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI2NiwiaWF0IjoxNzIyNzc2ODY2LCJqdGkiOiJlMGUyZDBlZjE2ZTE0NzZhOWRhNjRmZTMxNjI1M2I5OCIsInVzZXJfaWQiOjF9.MtC6GEfAHTv4cFAY8ivc-v_W4lWDBfzxiBvDEkpFlro',NULL,'2024-08-05 13:07:46.000000',NULL,'e0e2d0ef16e1476a9da64fe316253b98'),(243,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI2NywiaWF0IjoxNzIyNzc2ODY3LCJqdGkiOiJhOTM5ZDM0MDU4YmY0MTE4ODQ4MmFiNDQ4NzhjZWYyZSIsInVzZXJfaWQiOjF9.ZXsmxD1fO56_7oASBATCqtLYIND_eXnHfKTcdjT5DZg',NULL,'2024-08-05 13:07:47.000000',NULL,'a939d34058bf41188482ab44878cef2e'),(244,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI2OCwiaWF0IjoxNzIyNzc2ODY4LCJqdGkiOiI1NTFlOWIxNTljNTM0ZmE3OTgwYTU3OGRlYTMyNTUxYiIsInVzZXJfaWQiOjF9.1fXsZ3v0c2ju6mUZ3w6yYvgUI0Y396wMy1woU5yeN78',NULL,'2024-08-05 13:07:48.000000',NULL,'551e9b159c534fa7980a578dea32551b'),(245,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI2OSwiaWF0IjoxNzIyNzc2ODY5LCJqdGkiOiIyM2JkZGMyOWY5OWM0MDEwYWY0ZjYyY2IxNmY1Mzc4NyIsInVzZXJfaWQiOjF9.1MUs89tILKgDS5WnnOmECCguvQSCQXy7_JlSuj14LEw',NULL,'2024-08-05 13:07:49.000000',NULL,'23bddc29f99c4010af4f62cb16f53787'),(246,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI3MCwiaWF0IjoxNzIyNzc2ODcwLCJqdGkiOiI0YTNhZTdjMDgwOWU0YmZiOWQzN2EzOGZjNjNkMDBhZCIsInVzZXJfaWQiOjF9.0q9IttbIRw-PcG3CVl5hP_MTLLShw-TyTIVfBr8Z8J8',NULL,'2024-08-05 13:07:50.000000',NULL,'4a3ae7c0809e4bfb9d37a38fc63d00ad'),(247,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI3MCwiaWF0IjoxNzIyNzc2ODcwLCJqdGkiOiI4YTYwZTJhM2IwMzQ0YjYzYjRjZTE5Y2U0MDY5OGM5NiIsInVzZXJfaWQiOjF9.wfZ6KYkHLPPf8fiBhWQK6dYynYeQvA4QXfp6E9-wtoo',NULL,'2024-08-05 13:07:50.000000',NULL,'8a60e2a3b0344b63b4ce19ce40698c96'),(248,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI3MiwiaWF0IjoxNzIyNzc2ODcyLCJqdGkiOiI2OGUxZWIwMWExM2U0NmMxOWFhNDgyODk2NGY4MmUwNiIsInVzZXJfaWQiOjF9.Hi2rM5jmBXXnGzHsmgndTOoQ3Mm35MqLvivVIXt7Lls',NULL,'2024-08-05 13:07:52.000000',NULL,'68e1eb01a13e46c19aa4828964f82e06'),(249,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI3MywiaWF0IjoxNzIyNzc2ODczLCJqdGkiOiI2ZWY4OWIxZjJhZmU0NzI0OGUxYmEwY2NiMmE2NDAzYSIsInVzZXJfaWQiOjF9.qpzzOV3Sd9WuCpOoUpI36ThoPULqggTLrmLT1lhdBZo',NULL,'2024-08-05 13:07:53.000000',NULL,'6ef89b1f2afe47248e1ba0ccb2a6403a'),(250,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI3NCwiaWF0IjoxNzIyNzc2ODc0LCJqdGkiOiJiZTg5MzhmNTdhOWQ0Y2U4YjQ4NDQ3NDgzNDMxNDVmOCIsInVzZXJfaWQiOjF9.NsxAujunkHCLzMaPwGqJbEUM4gvmt4ElZD8FPsoma2o',NULL,'2024-08-05 13:07:54.000000',NULL,'be8938f57a9d4ce8b4844748343145f8'),(251,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI3NSwiaWF0IjoxNzIyNzc2ODc1LCJqdGkiOiIzYzZhMGJiOWZlZTk0YWM1OGFhZWNmNWQwOTc0NDljYSIsInVzZXJfaWQiOjF9.rS9hwoaVDhqtHqCKAARu1MFmhrQGxEuGOf4voNMLRZk',NULL,'2024-08-05 13:07:55.000000',NULL,'3c6a0bb9fee94ac58aaecf5d097449ca'),(252,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI3NiwiaWF0IjoxNzIyNzc2ODc2LCJqdGkiOiIzNzI2MWFmOTU2MGY0NWEwOGExY2M0YzYyNDhhZGJiMyIsInVzZXJfaWQiOjF9.7HEgdVyZvm4eGBQUx7uwgg7hYYB_f6jCln9f0xXAK2U',NULL,'2024-08-05 13:07:56.000000',NULL,'37261af9560f45a08a1cc4c6248adbb3'),(253,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI3NywiaWF0IjoxNzIyNzc2ODc3LCJqdGkiOiI1ZGNkZjdjMTE0NDA0ZjYzOTk3OGVmOTc2MmE3ZWY4MSIsInVzZXJfaWQiOjF9.hmCNYkwDo_THkAvJii04k_BfFsSnm_C1oidSigBpwmo',NULL,'2024-08-05 13:07:57.000000',NULL,'5dcdf7c114404f639978ef9762a7ef81'),(254,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI3OCwiaWF0IjoxNzIyNzc2ODc4LCJqdGkiOiJjYTU1MWNhZWZiMDI0MmUwOTU3MDU3M2Q5NmI0MTIyYyIsInVzZXJfaWQiOjF9.XtkpTTxEF3rRRRjdbNnAIEEyV9M25lssa_-tMH62o8I',NULL,'2024-08-05 13:07:58.000000',NULL,'ca551caefb0242e09570573d96b4122c'),(255,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI3OSwiaWF0IjoxNzIyNzc2ODc5LCJqdGkiOiIwMzA1OWU0MTBjZWI0MjAxYTY0ZmI5YTFlODY0ZWZlOCIsInVzZXJfaWQiOjF9.8Dkin0Ob5akvQw2MjL6hIHbCPVe6n6Z9fBmLmBLcGhA',NULL,'2024-08-05 13:07:59.000000',NULL,'03059e410ceb4201a64fb9a1e864efe8'),(256,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI4MCwiaWF0IjoxNzIyNzc2ODgwLCJqdGkiOiJkMWMwYTI1NWQwNmY0MDFmYTkzZWY1YmRmYTNiMzViNCIsInVzZXJfaWQiOjF9._GAw8yLs-wHje7hU3eIVW1y_aBmcqS6-xuztmTfL31w',NULL,'2024-08-05 13:08:00.000000',NULL,'d1c0a255d06f401fa93ef5bdfa3b35b4'),(257,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI4MSwiaWF0IjoxNzIyNzc2ODgxLCJqdGkiOiIwMjBlMmQ0ZTM5Y2Y0Y2UxOGY2OGJlNTZjODVhOGUzNCIsInVzZXJfaWQiOjF9.d6gS-NyG0a4N6USaHBe6jZ8Scx4F1CAlEmjCn1I85WY',NULL,'2024-08-05 13:08:01.000000',NULL,'020e2d4e39cf4ce18f68be56c85a8e34'),(258,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI4MiwiaWF0IjoxNzIyNzc2ODgyLCJqdGkiOiJlZDRlYjJjYmZlMTc0ZGE5YmI3MTgzOTdkMWIzMTQ2OCIsInVzZXJfaWQiOjF9.-sEmDgrJd2CaVoE2KKsB357gB5AguAGmMrRXSuvN0iI',NULL,'2024-08-05 13:08:02.000000',NULL,'ed4eb2cbfe174da9bb718397d1b31468'),(259,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI4MywiaWF0IjoxNzIyNzc2ODgzLCJqdGkiOiJmMWYwMTVlMGIwOTU0NTVjOWFiNzdmNjBmODIxZGUyZiIsInVzZXJfaWQiOjF9.RVDEeajGgDF5zqmAOa8xFnDIUy0Ob0dt40Ww1DRZtB4',NULL,'2024-08-05 13:08:03.000000',NULL,'f1f015e0b095455c9ab77f60f821de2f'),(260,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzI4OCwiaWF0IjoxNzIyNzc2ODg4LCJqdGkiOiJhYjlmMTI0M2M4ZDk0OGM0YWIxMTEyNDYyMmI4MjFjMCIsInVzZXJfaWQiOjF9.KHmN2l10ldayJWXTG6zMaea0MjcPWw89zNDayo_L65w','2024-08-04 13:08:08.559802','2024-08-05 13:08:08.000000',1,'ab9f1243c8d948c4ab11124622b821c0'),(261,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjg2MzMzOSwiaWF0IjoxNzIyNzc2OTM5LCJqdGkiOiIwYTUwN2ExNjNkMWU0OTYwOWFiZTNkMDk2NGVjYzVmMSIsInVzZXJfaWQiOjF9.mfaS960xrlRtOugZTAqVn0M3NDqM1LCwYMS7v-rJzPs',NULL,'2024-08-05 13:08:59.000000',NULL,'0a507a163d1e49609abe3d0964ecc5f1'),(262,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjkyMzU1NCwiaWF0IjoxNzIyODM3MTU0LCJqdGkiOiI4YmU4N2Y4YmE1ZmQ0ODkzYjExNTFjNTNhY2VkMGMwNiIsInVzZXJfaWQiOjF9.kxwl-Wc3NmOFg89Y2KkmgA4Ijy9wGWEd4fV90KuN48k','2024-08-05 05:52:34.166787','2024-08-06 05:52:34.000000',1,'8be87f8ba5fd4893b1151c53aced0c06'),(263,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjkyMzU4NiwiaWF0IjoxNzIyODM3MTg2LCJqdGkiOiIxYjcwZjk3N2E4YmQ0YmY3YmQ4NjU1NWFjYzQ1MTRiOSIsInVzZXJfaWQiOjF9.Cxq6i-9aA0CMD54uWjb6Zjr4RLLapHbROF1QfXadZOo','2024-08-05 05:53:06.517183','2024-08-06 05:53:06.000000',1,'1b70f977a8bd4bf7bd86555acc4514b9'),(264,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjkyMzYwNCwiaWF0IjoxNzIyODM3MjA0LCJqdGkiOiI0ZTJjYjRiOTRkYjI0OTE5OWQxMjJlZWNhZThjZDI2OCIsInVzZXJfaWQiOjF9.j9K7I-VAo-3SCYxoamE1csKAmksHtv7vxmRILHJSY3E','2024-08-05 05:53:24.974273','2024-08-06 05:53:24.000000',1,'4e2cb4b94db249199d122eecae8cd268'),(265,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjkyMzY3NCwiaWF0IjoxNzIyODM3Mjc0LCJqdGkiOiJlMGQ4YTdjZTNiNWY0Y2E2ODFjNzYxYjkyMTZjMDIwMSIsInVzZXJfaWQiOjF9.u3_i5NAmoDkPLwiwdh6SzylwPF2EjUydZYlz5-rvKls','2024-08-05 05:54:34.625324','2024-08-06 05:54:34.000000',1,'e0d8a7ce3b5f4ca681c761b9216c0201'),(267,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjkyNjM1NCwiaWF0IjoxNzIyODM5OTU0LCJqdGkiOiI0MmE0YWY1MWU0MjY0MWQyYTlmNWM0MGUyZmNmOTNiZiIsInVzZXJfaWQiOjF9.cq37Vv1S_-_7HLf0wSVBMfuBQ7gC4SLRoPXQDUTVhbA','2024-08-05 06:39:14.071901','2024-08-06 06:39:14.000000',1,'42a4af51e42641d2a9f5c40e2fcf93bf'),(268,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjkyOTU5NSwiaWF0IjoxNzIyODQzMTk1LCJqdGkiOiJmNGNjN2MzZDY0ZDc0ZjRkYTc0OGQ4YTRiYzJlNWRkMCIsInVzZXJfaWQiOjF9.K2_4g6j2JQVXIQTTi2BseOZrDeM7ae5mL16OQodcSAM','2024-08-05 07:33:15.594460','2024-08-06 07:33:15.000000',1,'f4cc7c3d64d74f4da748d8a4bc2e5dd0'),(269,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjkyOTY3NSwiaWF0IjoxNzIyODQzMjc1LCJqdGkiOiJlNTIyYmRmYjY4MTM0NzhkYTdkODQ0Yzg3Mjg0NDQzMyIsInVzZXJfaWQiOjF9.FtontUXDvC8hE-uOy0wYh-AwPUIBK8W-HyelESG17FM','2024-08-05 07:34:35.258091','2024-08-06 07:34:35.000000',1,'e522bdfb6813478da7d844c872844433'),(270,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjkzMDg5NywiaWF0IjoxNzIyODQ0NDk3LCJqdGkiOiIwY2M0NmQ1M2ZkYzE0NzE4OGRkYzI4NDAxYTZjZGExMyIsInVzZXJfaWQiOjF9.UIRi9Ek_Th_6gYJlQYkaI2m0vurnvqa2ODibwnmfWo4','2024-08-05 07:54:57.759987','2024-08-06 07:54:57.000000',1,'0cc46d53fdc147188ddc28401a6cda13'),(271,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjkzMDk1NiwiaWF0IjoxNzIyODQ0NTU2LCJqdGkiOiIxY2MyNzJhNzc2OWU0ZDQ3YmU5ZTJhMGM1YmJhYmZiMiIsInVzZXJfaWQiOjF9.N-E8BXaWy3GLUZ2iNH91zK2C5u7203VH9XyPo0fIvqc','2024-08-05 07:55:56.854133','2024-08-06 07:55:56.000000',1,'1cc272a7769e4d47be9e2a0c5bbabfb2'),(272,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjkzMTE3NSwiaWF0IjoxNzIyODQ0Nzc1LCJqdGkiOiI1MjQ2YmMyMDAzYzM0YTJiODEzNTg1Y2IyM2UyMGQyOSIsInVzZXJfaWQiOjF9.PBpw4yTk018tjYbk6QY0JQq5Y1nXFq662OkdTFepiwI','2024-08-05 07:59:35.424888','2024-08-06 07:59:35.000000',1,'5246bc2003c34a2b813585cb23e20d29'),(273,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjkzMTE4MSwiaWF0IjoxNzIyODQ0NzgxLCJqdGkiOiI5NmVjZWMzNjBkNWQ0NDJjODdmZmVkOGJiZGIxZTM0ZiIsInVzZXJfaWQiOjF9.wm8Rk6zzn5NxHo0QM5H31WPzwCJFk04CLc3Rp_EiCZk','2024-08-05 07:59:41.788400','2024-08-06 07:59:41.000000',1,'96ecec360d5d442c87ffed8bbdb1e34f'),(274,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjkzMTc1NiwiaWF0IjoxNzIyODQ1MzU2LCJqdGkiOiJiZDcxNWE5YTNjZDU0NmY2OTUyZjVjYWZhZTZkMGE4YSIsInVzZXJfaWQiOjF9.ZGhn3vWKmXUf7zTxtx9BKpRG0VkB8F2b3nGVOG3wBUE','2024-08-05 08:09:16.799466','2024-08-06 08:09:16.000000',1,'bd715a9a3cd546f6952f5cafae6d0a8a'),(275,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjkzMjI0OCwiaWF0IjoxNzIyODQ1ODQ4LCJqdGkiOiIyYTNhYzgzZmFjMjE0ZTdkOTMxMTBjZGQ3YzUyMDlhOSIsInVzZXJfaWQiOjF9._i9Kh63bjDYKVWhOfMagaf6Dy7NUDK4k3JMH8k5aEug','2024-08-05 08:17:28.638887','2024-08-06 08:17:28.000000',1,'2a3ac83fac214e7d93110cdd7c5209a9'),(276,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjkzMzA2MSwiaWF0IjoxNzIyODQ2NjYxLCJqdGkiOiJkZGYwYmE4M2EzMTY0MWRhYjJhNjM0NzQzYzI4Mzc3NyIsInVzZXJfaWQiOjF9.AgZgvBApbiWkXvlKGWIRUnBm88oWQkxdtPuv9CyFWKM','2024-08-05 08:31:01.326628','2024-08-06 08:31:01.000000',1,'ddf0ba83a31641dab2a634743c283777'),(277,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjkzMzA3MiwiaWF0IjoxNzIyODQ2NjcyLCJqdGkiOiI2Mjc2ZTc2NTk2ZDM0NGMxOTM4MGJhY2NjYzk3YTkyZiIsInVzZXJfaWQiOjF9.-wKxg8I6NAO6NTPFe7LOTkoafI8dIdmV4h9rpO5QpuE','2024-08-05 08:31:12.365575','2024-08-06 08:31:12.000000',1,'6276e76596d344c19380bacccc97a92f'),(278,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjkzMzEwNywiaWF0IjoxNzIyODQ2NzA3LCJqdGkiOiJlZjZmZTc5Yjc4ZmU0NWRkYTNmMDBhOGVhZjUxNTUzMSIsInVzZXJfaWQiOjF9.RVfA7PvSLzHJD5e6EkMsIqxl_yOiNpQdBAgcMA9GqwA','2024-08-05 08:31:47.907399','2024-08-06 08:31:47.000000',1,'ef6fe79b78fe45dda3f00a8eaf515531'),(279,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjkzMzE5OCwiaWF0IjoxNzIyODQ2Nzk4LCJqdGkiOiIwODllZWJjNTdlZDU0ZGU5ODVmNWM4ZTk0YjYzM2NkMyIsInVzZXJfaWQiOjF9.uyPI61NdUmGi6eZhRcErhKFZHSqHc4IH858OKILs63s','2024-08-05 08:33:18.668751','2024-08-06 08:33:18.000000',1,'089eebc57ed54de985f5c8e94b633cd3'),(280,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjkzNDY3MiwiaWF0IjoxNzIyODQ4MjcyLCJqdGkiOiI3MWY1NmY2MDA2NTE0NjFjOTZhMTFmMDQ3MmNlNTc1NSIsInVzZXJfaWQiOjF9.aDaI3BeFmiUghQMaPndQJ8dti9ivMBaR8DTvPakjAl0','2024-08-05 08:57:52.119978','2024-08-06 08:57:52.000000',1,'71f56f600651461c96a11f0472ce5755'),(281,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjkzNjQxMywiaWF0IjoxNzIyODUwMDEzLCJqdGkiOiI4NTVlZDFhNmE5MjE0MWI0YTU2ZDUzN2E0YWY2NmFhNiIsInVzZXJfaWQiOjF9.hz6bktvg1CSFyLU3XJ3_Tuszhw_MkuPrU1gPvb6Cyfg','2024-08-05 09:26:53.282860','2024-08-06 09:26:53.000000',1,'855ed1a6a92141b4a56d537a4af66aa6'),(282,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjkzNjQxNSwiaWF0IjoxNzIyODUwMDE1LCJqdGkiOiJkNmQ5ZDc3MjJiMDk0YjhiYmM4Mjk4MGY4M2Q4Mjc1MyIsInVzZXJfaWQiOjF9.91AkTuuUODVXgt8_ejHVtAGdi5O4qrrXxjXcgdRbODE','2024-08-05 09:26:55.265646','2024-08-06 09:26:55.000000',1,'d6d9d7722b094b8bbc82980f83d82753'),(283,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjkzNjQzMiwiaWF0IjoxNzIyODUwMDMyLCJqdGkiOiI1OWIwMDE3MjJmM2I0OWYwODg0NmY2NzIzMjNhZDZjNSIsInVzZXJfaWQiOjF9.X5Rsmu8N67CSdHuwLk_nRt-l-vGT1TEKiZP8fgtpawc','2024-08-05 09:27:12.855569','2024-08-06 09:27:12.000000',1,'59b001722f3b49f08846f672323ad6c5'),(284,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjk0MDA0NCwiaWF0IjoxNzIyODUzNjQ0LCJqdGkiOiIzNzBlZjUyMDliM2U0NjI0OWUxOTdkZDJkMDFhMTg5OCIsInVzZXJfaWQiOjF9.uNgbv9ac7frlYi5kl0p_6yul2jrs1pPAxn3_t0ngbGw','2024-08-05 10:27:24.925284','2024-08-06 10:27:24.000000',1,'370ef5209b3e46249e197dd2d01a1898'),(285,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjk0MDA2NCwiaWF0IjoxNzIyODUzNjY0LCJqdGkiOiI2YWVjY2RiZjg4ODI0ZDhkYmU4MjU3Yzk4OTYxM2Q5OCIsInVzZXJfaWQiOjF9.MrHjBMDc6UEJfKcIHnuscAlB3Ar0z0J9hFZuCvKAGZ0','2024-08-05 10:27:44.891725','2024-08-06 10:27:44.000000',1,'6aeccdbf88824d8dbe8257c989613d98'),(286,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjk1NzY5OCwiaWF0IjoxNzIyODcxMjk4LCJqdGkiOiJkNWI0MGJiZDllMTU0ZjYyOTljYWQ3ZWIwMzIyOWUxZSIsInVzZXJfaWQiOjF9.wCI8t0Knlsyj2U9u62dOZ3VyS4bxhMPIPNibAbjzz1c','2024-08-05 15:21:38.563831','2024-08-06 15:21:38.000000',1,'d5b40bbd9e154f6299cad7eb03229e1e'),(287,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMzAxNDc4OCwiaWF0IjoxNzIyOTI4Mzg4LCJqdGkiOiIwZGJjZjkzYTg5NjA0YTdkOTYwYjIwM2FlY2UxNDk1ZiIsInVzZXJfaWQiOjF9.77sUz4N0kC7ZTlWvB6HQcc1kXG-xg0r11HvjV4s269I','2024-08-06 07:13:08.527504','2024-08-07 07:13:08.000000',1,'0dbcf93a89604a7d960b203aece1495f'),(288,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMzAxNDg0OCwiaWF0IjoxNzIyOTI4NDQ4LCJqdGkiOiJhYTc3MGZlNTc0YWM0YzIzOTc5YWZjZjlhODNhZTQ3NiIsInVzZXJfaWQiOjF9.rJGMBfIxTjQWVqPEle4eycHp4W2pI3NhUqeAtN7cx6E','2024-08-06 07:14:08.540629','2024-08-07 07:14:08.000000',1,'aa770fe574ac4c23979afcf9a83ae476'),(289,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMzAxODE3NiwiaWF0IjoxNzIyOTMxNzc2LCJqdGkiOiI5NjdlMmZjOTg3NGY0YWUyYjNmOTUyYTdjZDE0MmMxMiIsInVzZXJfaWQiOjF9.uuU8RM-Y__1_yddALvF1qhCqFTY1febfheF5dzbXAF8',NULL,'2024-08-07 08:09:36.000000',NULL,'967e2fc9874f4ae2b3f952a7cd142c12'),(290,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMzA0NjAwMSwiaWF0IjoxNzIyOTU5NjAxLCJqdGkiOiJkNjU3YjE0ODc5NzY0M2I5Yjk0NWVhMDJjYTMzZTM4NCIsInVzZXJfaWQiOjF9.qMoW9G7MRWPu-65VQRKP3AEn2EPsIP06s6MFpmhtxEs','2024-08-06 15:53:21.340872','2024-08-07 15:53:21.000000',1,'d657b148797643b9b945ea02ca33e384'),(291,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMzA5NzI1MywiaWF0IjoxNzIzMDEwODUzLCJqdGkiOiI2OTU2Y2RmZTBhNDM0ODBjODFlNmRiMzlkZjFjOTBhNyIsInVzZXJfaWQiOjF9.Br_ya60Lnf9X1f9SngBA4Zt6o3-UBD7AclgwEOElKg0','2024-08-07 06:07:33.148447','2024-08-08 06:07:33.000000',1,'6956cdfe0a43480c81e6db39df1c90a7'),(293,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMzEwMTA1MywiaWF0IjoxNzIzMDE0NjUzLCJqdGkiOiIxZDk3YjMyNzMzYTA0NjA4YTVlNDNjYzgwZjFkYjQwMiIsInVzZXJfaWQiOjF9.-LpSuSGtOQiL0sNpmFNXyR9Ra9YP9oesNNB4yJl6XnM','2024-08-07 07:10:53.532330','2024-08-08 07:10:53.000000',1,'1d97b32733a04608a5e43cc80f1db402'),(295,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMzEwMTM2MiwiaWF0IjoxNzIzMDE0OTYyLCJqdGkiOiIxNTI4ODJhM2Q2NTg0OGM3OGMwYjczZTc5MmZiMmFjMSIsInVzZXJfaWQiOjF9.vVuaAw80KnBf_pbTw0rYK9fjjPIEVOsZ6d_E6xiMGMo','2024-08-07 07:16:02.730257','2024-08-08 07:16:02.000000',1,'152882a3d65848c78c0b73e792fb2ac1'),(296,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMzEwNDk5MiwiaWF0IjoxNzIzMDE4NTkyLCJqdGkiOiIwZjlhODM2ZGVkYWI0MmQ5OTM0MDFhYmU1NDYwY2E0MiIsInVzZXJfaWQiOjF9.MSX4Lc1vy_ae1X49yRZEu85tABBE1-Dyd3QcITjOzQc','2024-08-07 08:16:32.126845','2024-08-08 08:16:32.000000',1,'0f9a836dedab42d993401abe5460ca42'),(297,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMzEwNzU2NiwiaWF0IjoxNzIzMDIxMTY2LCJqdGkiOiIzYjlmMzU5YWNjNTM0ZGViYmFkOTlkMDI5ZDg4ZmUyMCIsInVzZXJfaWQiOjF9.1dn2e7h4pTYZzaPtTs2Gs4Txs5hF9RzXoiNuSQqTom4','2024-08-07 08:59:26.271646','2024-08-08 08:59:26.000000',1,'3b9f359acc534debbad99d029d88fe20'),(298,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMzEwNzY0MywiaWF0IjoxNzIzMDIxMjQzLCJqdGkiOiI3NzE3YTAxNWExNTQ0MWU0YjRmMzFjYjIxMGZkOWRmMiIsInVzZXJfaWQiOjF9.uw2Zwcrwy9lVgPJsERfiKq9TEE1evlhvI8DTbKX9zSU','2024-08-07 09:00:43.085976','2024-08-08 09:00:43.000000',1,'7717a015a15441e4b4f31cb210fd9df2'),(299,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMzEwODA0NiwiaWF0IjoxNzIzMDIxNjQ2LCJqdGkiOiJlYWIyMmQyYmIwODM0OWJmYjhmMmRmN2E2MGM2NDMwZSIsInVzZXJfaWQiOjF9.DF94Ut2Vje81b7oX7TtT-wuPziKf9j654bxetHTgfZ0','2024-08-07 09:07:26.742119','2024-08-08 09:07:26.000000',1,'eab22d2bb08349bfb8f2df7a60c6430e');
/*!40000 ALTER TABLE `token_blacklist_outstandingtoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_dealership`
--

DROP TABLE IF EXISTS `users_dealership`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_dealership` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `organisation_name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_dealership`
--

LOCK TABLES `users_dealership` WRITE;
/*!40000 ALTER TABLE `users_dealership` DISABLE KEYS */;
INSERT INTO `users_dealership` VALUES (1,'дц 1 1','Орг 1'),(2,'дц 1 2','Орг 1'),(3,'дц 2 1','Орг 2'),(4,'дц 22','Орг 2');
/*!40000 ALTER TABLE `users_dealership` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_userdocument`
--

DROP TABLE IF EXISTS `users_userdocument`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_userdocument` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `document_file` varchar(100) NOT NULL,
  `uploaded_at` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  `document_type_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `users_userdocument_user_id_f8679d64_fk_auth_user_id` (`user_id`),
  KEY `users_userdocument_document_type_id_82b6f066_fk_users_use` (`document_type_id`),
  CONSTRAINT `users_userdocument_document_type_id_82b6f066_fk_users_use` FOREIGN KEY (`document_type_id`) REFERENCES `users_userdocumenttype` (`id`),
  CONSTRAINT `users_userdocument_user_id_f8679d64_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_userdocument`
--

LOCK TABLES `users_userdocument` WRITE;
/*!40000 ALTER TABLE `users_userdocument` DISABLE KEYS */;
INSERT INTO `users_userdocument` VALUES (1,'user_documents/user_1/1_1.pdf','2024-09-17 09:53:08.955457',1,1);
/*!40000 ALTER TABLE `users_userdocument` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_userdocumenttype`
--

DROP TABLE IF EXISTS `users_userdocumenttype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_userdocumenttype` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `document_type` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `document_type` (`document_type`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_userdocumenttype`
--

LOCK TABLES `users_userdocumenttype` WRITE;
/*!40000 ALTER TABLE `users_userdocumenttype` DISABLE KEYS */;
INSERT INTO `users_userdocumenttype` VALUES (1,'1'),(2,'2'),(3,'3');
/*!40000 ALTER TABLE `users_userdocumenttype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_userprofile`
--

DROP TABLE IF EXISTS `users_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_userprofile` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `first_name_manager` varchar(30) DEFAULT NULL,
  `last_name_manager` varchar(30) DEFAULT NULL,
  `middle_name_manager` varchar(30) DEFAULT NULL,
  `organization_manager` varchar(255) DEFAULT NULL,
  `role_manager` varchar(50) NOT NULL,
  `date_of_birth_manager` date DEFAULT NULL,
  `phone_number_manager` varchar(20) DEFAULT NULL,
  `status_manager` tinyint(1) NOT NULL,
  `passport_series_manager` varchar(10) DEFAULT NULL,
  `passport_number_manager` varchar(10) DEFAULT NULL,
  `division_code_manager` varchar(7) DEFAULT NULL,
  `issued_by_manager` varchar(255) DEFAULT NULL,
  `issue_date_manager` date DEFAULT NULL,
  `active_dealership_id` bigint DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `users_userprofile_active_dealership_id_67bdc85e_fk_users_dea` (`active_dealership_id`),
  CONSTRAINT `users_userprofile_active_dealership_id_67bdc85e_fk_users_dea` FOREIGN KEY (`active_dealership_id`) REFERENCES `users_dealership` (`id`),
  CONSTRAINT `users_userprofile_user_id_87251ef1_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_userprofile`
--

LOCK TABLES `users_userprofile` WRITE;
/*!40000 ALTER TABLE `users_userprofile` DISABLE KEYS */;
INSERT INTO `users_userprofile` VALUES (1,'Имя','Фамилия','Отчество',NULL,'superuser',NULL,NULL,1,NULL,NULL,NULL,NULL,NULL,2,1);
/*!40000 ALTER TABLE `users_userprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_userprofile_dealership_manager`
--

DROP TABLE IF EXISTS `users_userprofile_dealership_manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_userprofile_dealership_manager` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `userprofile_id` bigint NOT NULL,
  `dealership_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_userprofile_dealer_userprofile_id_dealershi_8a87cf3e_uniq` (`userprofile_id`,`dealership_id`),
  KEY `users_userprofile_de_dealership_id_159b347d_fk_users_dea` (`dealership_id`),
  CONSTRAINT `users_userprofile_de_dealership_id_159b347d_fk_users_dea` FOREIGN KEY (`dealership_id`) REFERENCES `users_dealership` (`id`),
  CONSTRAINT `users_userprofile_de_userprofile_id_79510ce3_fk_users_use` FOREIGN KEY (`userprofile_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_userprofile_dealership_manager`
--

LOCK TABLES `users_userprofile_dealership_manager` WRITE;
/*!40000 ALTER TABLE `users_userprofile_dealership_manager` DISABLE KEYS */;
INSERT INTO `users_userprofile_dealership_manager` VALUES (2,1,2);
/*!40000 ALTER TABLE `users_userprofile_dealership_manager` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-17 16:48:51
