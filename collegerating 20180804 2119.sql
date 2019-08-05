-- MySQL Administrator dump 1.4
--
-- ------------------------------------------------------
-- Server version	5.0.10a-beta-nt


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


--
-- Create schema collegerating
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ collegerating;
USE collegerating;

--
-- Table structure for table `collegerating`.`add_college`
--

DROP TABLE IF EXISTS `add_college`;
CREATE TABLE `add_college` (
  `college_name` varchar(50) NOT NULL,
  `college_code` varchar(45) NOT NULL,
  `affilation` varchar(100) NOT NULL,
  PRIMARY KEY  (`college_code`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `collegerating`.`add_college`
--

/*!40000 ALTER TABLE `add_college` DISABLE KEYS */;
INSERT INTO `add_college` (`college_name`,`college_code`,`affilation`) VALUES 
 ('','','University of Lucknow'),
 ('BBDNITM','054','Dr. A.P.J. Abdul Kalam Technical University'),
 ('BBDNIIT','056','Dr. A.P.J. Abdul Kalam Technical University'),
 ('SRMCEM','122','Dr. A.P.J. Abdul Kalam Technical University'),
 ('GITM','360','Khwaja Moinuddin Chishti Urdu, Arabi Farsi University'),
 ('BBDEC','508','Dr. A.P.J. Abdul Kalam Technical University');
/*!40000 ALTER TABLE `add_college` ENABLE KEYS */;


--
-- Table structure for table `collegerating`.`adminlogin`
--

DROP TABLE IF EXISTS `adminlogin`;
CREATE TABLE `adminlogin` (
  `username` varchar(45) NOT NULL default 'admin',
  `password` varchar(45) NOT NULL default 'admin',
  PRIMARY KEY  (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `collegerating`.`adminlogin`
--

/*!40000 ALTER TABLE `adminlogin` DISABLE KEYS */;
INSERT INTO `adminlogin` (`username`,`password`) VALUES 
 ('admin','admin');
/*!40000 ALTER TABLE `adminlogin` ENABLE KEYS */;


--
-- Table structure for table `collegerating`.`college_details`
--

DROP TABLE IF EXISTS `college_details`;
CREATE TABLE `college_details` (
  `college_name` varchar(70) NOT NULL,
  `college_code` varchar(45) NOT NULL,
  `branch` varchar(45) NOT NULL,
  `fees` varchar(45) NOT NULL,
  `duration` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `collegerating`.`college_details`
--

/*!40000 ALTER TABLE `college_details` DISABLE KEYS */;
INSERT INTO `college_details` (`college_name`,`college_code`,`branch`,`fees`,`duration`) VALUES 
 ('BBDEC','508','BTech','83200','4 years'),
 ('BBDEC','508','BPharma','100000','4 years'),
 ('BBDEC','508','BJMC','50000','2 years'),
 ('BBDEC','508','BCA','100000','2 years'),
 ('BBDEC','508','BA','44444','2 years'),
 ('BBDEC','508','MA','444444444','2 years'),
 ('BBDEC','508','BSc','5555','2 years'),
 ('BBDEC','508','BDS','4444','2 years'),
 ('BBDEC','508','MCA','75','4 years'),
 ('BBDNITM','054','BTech','106000','4 years'),
 ('BBDNITM','054','BCA','12012','3 years'),
 ('BBDNITM','054','BPharma','48778','2 years'),
 ('BBDNIIT','056','BTech','120000','4 years'),
 ('BBDNIIT','056','BCA','200000','3 years'),
 ('BBDNIIT','056','BPharma','400000','4 years');
/*!40000 ALTER TABLE `college_details` ENABLE KEYS */;


--
-- Table structure for table `collegerating`.`manager`
--

DROP TABLE IF EXISTS `manager`;
CREATE TABLE `manager` (
  `Name` varchar(45) NOT NULL,
  `Email` varchar(200) NOT NULL,
  `UserId` varchar(45) NOT NULL,
  `Password` varchar(45) NOT NULL,
  PRIMARY KEY  (`UserId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `collegerating`.`manager`
--

/*!40000 ALTER TABLE `manager` DISABLE KEYS */;
INSERT INTO `manager` (`Name`,`Email`,`UserId`,`Password`) VALUES 
 ('Amritanshu Gau','amrit11@gmail.com','amrit11','amrit'),
 ('Anshuman Srivastava','1104anshuman@gmail.com','ansh1104','ansh'),
 ('Harsh Deep','harsh11@gmail.com','harsh11','harsh'),
 ('Shivam Srivastava','anshumansrivastava007@gmail.com','shivam1104','shivam');
/*!40000 ALTER TABLE `manager` ENABLE KEYS */;


--
-- Table structure for table `collegerating`.`managerprofile`
--

DROP TABLE IF EXISTS `managerprofile`;
CREATE TABLE `managerprofile` (
  `Name` varchar(45) NOT NULL,
  `UserId` varchar(45) NOT NULL,
  `Phone` varchar(45) NOT NULL,
  `DoB` varchar(45) NOT NULL,
  `Address` varchar(200) NOT NULL,
  `City` varchar(45) NOT NULL,
  `College` varchar(45) NOT NULL,
  PRIMARY KEY  (`UserId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `collegerating`.`managerprofile`
--

/*!40000 ALTER TABLE `managerprofile` DISABLE KEYS */;
INSERT INTO `managerprofile` (`Name`,`UserId`,`Phone`,`DoB`,`Address`,`City`,`College`) VALUES 
 ('Anshuman Srivastava','ansh1104','8858616072','11/04/1998','shiv coloy','Faizabad','BBDEC');
/*!40000 ALTER TABLE `managerprofile` ENABLE KEYS */;


--
-- Table structure for table `collegerating`.`overallpassratio`
--

DROP TABLE IF EXISTS `overallpassratio`;
CREATE TABLE `overallpassratio` (
  `college_code` varchar(45) NOT NULL,
  `college_name` varchar(45) NOT NULL,
  `year` varchar(45) NOT NULL,
  `passingratio` varchar(45) NOT NULL,
  PRIMARY KEY  (`college_code`,`college_name`,`year`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `collegerating`.`overallpassratio`
--

/*!40000 ALTER TABLE `overallpassratio` DISABLE KEYS */;
INSERT INTO `overallpassratio` (`college_code`,`college_name`,`year`,`passingratio`) VALUES 
 ('508','BBDEC','2013','48'),
 ('508','BBDEC','2014','37'),
 ('508','BBDEC','2015','42'),
 ('508','BBDEC','2016','56'),
 ('508','BBDEC','2017','66'),
 ('508','BBDEC','2018','43');
/*!40000 ALTER TABLE `overallpassratio` ENABLE KEYS */;


--
-- Table structure for table `collegerating`.`passratio`
--

DROP TABLE IF EXISTS `passratio`;
CREATE TABLE `passratio` (
  `college_code` varchar(45) NOT NULL,
  `college_name` varchar(45) NOT NULL,
  `branch` varchar(45) NOT NULL,
  `passed` varchar(45) default NULL,
  `year` varchar(45) NOT NULL,
  `passratio` varchar(45) default NULL,
  `Placed` varchar(45) default NULL,
  PRIMARY KEY  (`college_code`,`branch`,`year`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `collegerating`.`passratio`
--

/*!40000 ALTER TABLE `passratio` DISABLE KEYS */;
INSERT INTO `passratio` (`college_code`,`college_name`,`branch`,`passed`,`year`,`passratio`,`Placed`) VALUES 
 ('054','BBDNITM','BCA','425','2013','70','345'),
 ('054','BBDNITM','BCA','600','2014','85','450'),
 ('054','BBDNITM','BCA','531','2015','66','300'),
 ('054','BBDNITM','BCA','250','2016','62','100'),
 ('054','BBDNITM','BCA','250','2017','33','158'),
 ('054','BBDNITM','BCA','600','2018','75','452'),
 ('054','BBDNITM','BPharma','401','2013','50','333'),
 ('054','BBDNITM','BPharma','600','2014','76','525'),
 ('054','BBDNITM','BPharma','540','2015','68','500'),
 ('054','BBDNITM','BPharma','249','2016','35','100'),
 ('054','BBDNITM','BPharma','250','2017','35','123'),
 ('054','BBDNITM','BPharma','600','2018','81','213'),
 ('054','BBDNITM','BTech','400','2013','80','215'),
 ('054','BBDNITM','BTech','500','2014','97','369'),
 ('054','BBDNITM','BTech','531','2015','100','147'),
 ('054','BBDNITM','BTech','540','2016','90','536'),
 ('054','BBDNITM','BTech','249','2017','31','123'),
 ('054','BBDNITM','BTech','600','2018','66','589'),
 ('056','BBDNIIT','BCA','517','2013','97','512');
INSERT INTO `passratio` (`college_code`,`college_name`,`branch`,`passed`,`year`,`passratio`,`Placed`) VALUES 
 ('056','BBDNIIT','BCA','540','2014','96','233'),
 ('056','BBDNIIT','BCA','568','2015','97','500'),
 ('056','BBDNIIT','BCA','599','2016','98','587'),
 ('056','BBDNIIT','BCA','594','2017','94','326'),
 ('056','BBDNIIT','BCA','570','2018','87','547'),
 ('056','BBDNIIT','BPharma','526','2013','96','412'),
 ('056','BBDNIIT','BPharma','550','2014','96','356'),
 ('056','BBDNIIT','BPharma','583','2015','98','456'),
 ('056','BBDNIIT','BPharma','608','2016','99','589'),
 ('056','BBDNIIT','BPharma','581','2017','91','369'),
 ('056','BBDNIIT','BPharma','563','2018','84','235'),
 ('056','BBDNIIT','BTech','500','2013','96','250'),
 ('056','BBDNIIT','BTech','531','2014','97','365'),
 ('056','BBDNIIT','BTech','558','2015','97','500'),
 ('056','BBDNIIT','BTech','592','2016','99','590'),
 ('056','BBDNIIT','BTech','609','2017','99','600'),
 ('056','BBDNIIT','BTech','577','2018','89','570'),
 ('508','BBDEC','BA','5','2013','10','2'),
 ('508','BBDEC','BA','25','2014','49','20');
INSERT INTO `passratio` (`college_code`,`college_name`,`branch`,`passed`,`year`,`passratio`,`Placed`) VALUES 
 ('508','BBDEC','BA','322','2015','38','300'),
 ('508','BBDEC','BA','448','2016','53','440'),
 ('508','BBDEC','BA','551','2017','64','550'),
 ('508','BBDEC','BA','300','2018','30','210'),
 ('508','BBDEC','BCA','40','2013','90','30'),
 ('508','BBDEC','BCA','250','2014','62','220'),
 ('508','BBDEC','BCA','312','2015','62','300'),
 ('508','BBDEC','BCA','436','2016','72','430'),
 ('508','BBDEC','BCA','537','2017','67','530'),
 ('508','BBDEC','BCA','401','2018','47','400'),
 ('508','BBDEC','BDS','500','2013','64','423'),
 ('508','BBDEC','BDS','257','2014','42','250'),
 ('508','BBDEC','BDS','373','2015','53','370'),
 ('508','BBDEC','BDS','505','2016','64','500'),
 ('508','BBDEC','BDS','589','2017','74','580'),
 ('508','BBDEC','BDS','300','2018','33','230'),
 ('508','BBDEC','BJMC','500','2013','53','450'),
 ('508','BBDEC','BJMC','250','2014','26','200'),
 ('508','BBDEC','BJMC','304','2015','33','300'),
 ('508','BBDEC','BJMC','417','2016','47','400');
INSERT INTO `passratio` (`college_code`,`college_name`,`branch`,`passed`,`year`,`passratio`,`Placed`) VALUES 
 ('508','BBDEC','BJMC','522','2017','59','500'),
 ('508','BBDEC','BJMC','40','2018','9','23'),
 ('508','BBDEC','BPharma','20','2013','4','15'),
 ('508','BBDEC','BPharma','20','2014','5','13'),
 ('508','BBDEC','BPharma','302','2015','34','250'),
 ('508','BBDEC','BPharma','409','2016','46','350'),
 ('508','BBDEC','BPharma','522','2017','57','500'),
 ('508','BBDEC','BPharma','500','2018','54','450'),
 ('508','BBDEC','BSc','500','2013','71','456'),
 ('508','BBDEC','BSc','257','2014','36','250'),
 ('508','BBDEC','BSc','348','2015','47','340'),
 ('508','BBDEC','BSc','491','2016','64','470'),
 ('508','BBDEC','BSc','573','2017','75','500'),
 ('508','BBDEC','BSc','300','2018','38','240'),
 ('508','BBDEC','BTech','258','2013','32','126'),
 ('508','BBDEC','BTech','500','2014','59','450'),
 ('508','BBDEC','BTech','284','2015','28','280'),
 ('508','BBDEC','BTech','393','2016','45','350'),
 ('508','BBDEC','BTech','512','2017','57','500'),
 ('508','BBDEC','BTech','500','2018','100','480');
INSERT INTO `passratio` (`college_code`,`college_name`,`branch`,`passed`,`year`,`passratio`,`Placed`) VALUES 
 ('508','BBDEC','MA','500','2013','50','256'),
 ('508','BBDEC','MA','250','2014','25','245'),
 ('508','BBDEC','MA','334','2015','34','333'),
 ('508','BBDEC','MA','464','2016','48','460'),
 ('508','BBDEC','MA','560','2017','65','56'),
 ('508','BBDEC','MA','300','2018','42','22'),
 ('508','BBDEC','MCA','500','2013','55','236'),
 ('508','BBDEC','MCA','257','2014','29','250'),
 ('508','BBDEC','MCA','393','2015','46','333'),
 ('508','BBDEC','MCA','511','2016','62','500'),
 ('508','BBDEC','MCA','589','2017','72','444'),
 ('508','BBDEC','MCA','300','2018','37','124');
/*!40000 ALTER TABLE `passratio` ENABLE KEYS */;


--
-- Table structure for table `collegerating`.`surveyform`
--

DROP TABLE IF EXISTS `surveyform`;
CREATE TABLE `surveyform` (
  `College_name` varchar(45) NOT NULL,
  `College_code` varchar(45) NOT NULL,
  `Placement` int(1) unsigned default NULL,
  `Discipline` int(1) unsigned default NULL,
  `PassingRatio` int(1) unsigned default NULL,
  `Infrastructure` int(1) unsigned default NULL,
  PRIMARY KEY  (`College_name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='InnoDB free: 3072 kB';

--
-- Dumping data for table `collegerating`.`surveyform`
--

/*!40000 ALTER TABLE `surveyform` DISABLE KEYS */;
INSERT INTO `surveyform` (`College_name`,`College_code`,`Placement`,`Discipline`,`PassingRatio`,`Infrastructure`) VALUES 
 ('BBDEC','508',5,5,5,5),
 ('BBDNIIT','056',3,3,3,5),
 ('BBDNITM','054',3,2,3,3),
 ('GITM','360',1,3,2,1);
/*!40000 ALTER TABLE `surveyform` ENABLE KEYS */;


--
-- Table structure for table `collegerating`.`year_collegedetail`
--

DROP TABLE IF EXISTS `year_collegedetail`;
CREATE TABLE `year_collegedetail` (
  `college_code` varchar(45) NOT NULL,
  `college_name` varchar(45) NOT NULL,
  `Branch` varchar(45) NOT NULL,
  `total_admission` varchar(45) NOT NULL,
  `year` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `collegerating`.`year_collegedetail`
--

/*!40000 ALTER TABLE `year_collegedetail` DISABLE KEYS */;
INSERT INTO `year_collegedetail` (`college_code`,`college_name`,`Branch`,`total_admission`,`year`) VALUES 
 ('508','BBDEC','BA','49','2013'),
 ('360','GITM','BA','500','2013'),
 ('508','BBDEC','BA','51','2014'),
 ('508','BBDEC','BA','840','2015'),
 ('508','BBDEC','BA','844','2016'),
 ('508','BBDEC','BA','855','2017'),
 ('508','BBDEC','BA','981','2018'),
 ('054','BBDNITM','BCA','400','2016'),
 ('508','BBDEC','BCA','402','2014'),
 ('508','BBDEC','BCA','44','2013'),
 ('508','BBDEC','BCA','500','2015'),
 ('056','BBDNIIT','BCA','532','2013'),
 ('056','BBDNIIT','BCA','559','2014'),
 ('056','BBDNIIT','BCA','581','2015'),
 ('054','BBDNITM','BCA','600','2013'),
 ('508','BBDEC','BCA','600','2016'),
 ('056','BBDNIIT','BCA','609','2016'),
 ('056','BBDNIIT','BCA','628','2017'),
 ('056','BBDNIIT','BCA','650','2018'),
 ('054','BBDNITM','BCA','700','2014'),
 ('054','BBDNITM','BCA','750','2017'),
 ('054','BBDNITM','BCA','798','2018'),
 ('054','BBDNITM','BCA','800','2015'),
 ('508','BBDEC','BCA','800','2017'),
 ('508','BBDEC','BCA','850','2018');
INSERT INTO `year_collegedetail` (`college_code`,`college_name`,`Branch`,`total_admission`,`year`) VALUES 
 ('508','BBDEC','BDS','600','2014'),
 ('508','BBDEC','BDS','700','2015'),
 ('508','BBDEC','BDS','774','2013'),
 ('508','BBDEC','BDS','780','2016'),
 ('508','BBDEC','BDS','789','2017'),
 ('508','BBDEC','BDS','900','2018'),
 ('508','BBDEC','BJMC','402','2018'),
 ('508','BBDEC','BJMC','872','2017'),
 ('508','BBDEC','BJMC','887','2016'),
 ('508','BBDEC','BJMC','911','2015'),
 ('508','BBDEC','BJMC','926','2014'),
 ('508','BBDEC','BJMC','939','2013'),
 ('508','BBDEC','BPharma','400','2014'),
 ('508','BBDEC','BPharma','500','2013'),
 ('056','BBDNIIT','BPharma','546','2013'),
 ('056','BBDNIIT','BPharma','569','2014'),
 ('056','BBDNIIT','BPharma','592','2015'),
 ('056','BBDNIIT','BPharma','614','2016'),
 ('056','BBDNIIT','BPharma','637','2017'),
 ('056','BBDNIIT','BPharma','665','2018'),
 ('054','BBDNITM','BPharma','700','2016'),
 ('054','BBDNITM','BPharma','714','2017'),
 ('054','BBDNITM','BPharma','732','2018'),
 ('054','BBDNITM','BPharma','786','2014');
INSERT INTO `year_collegedetail` (`college_code`,`college_name`,`Branch`,`total_admission`,`year`) VALUES 
 ('054','BBDNITM','BPharma','790','2015'),
 ('054','BBDNITM','BPharma','798','2013'),
 ('508','BBDEC','BPharma','872','2015'),
 ('508','BBDEC','BPharma','886','2016'),
 ('508','BBDEC','BPharma','906','2017'),
 ('508','BBDEC','BPharma','921','2018'),
 ('508','BBDEC','BSc','700','2013'),
 ('508','BBDEC','BSc','712','2014'),
 ('508','BBDEC','BSc','735','2015'),
 ('508','BBDEC','BSc','756','2016'),
 ('508','BBDEC','BSc','759','2017'),
 ('508','BBDEC','BSc','780','2018'),
 ('508','BBDEC','BTech','1000','2015'),
 ('054','BBDNITM','BTech','500','2013'),
 ('508','BBDEC','BTech','500','2018'),
 ('054','BBDNITM','BTech','513','2014'),
 ('056','BBDNIIT','BTech','520','2013'),
 ('054','BBDNITM','BTech','531','2015'),
 ('056','BBDNIIT','BTech','546','2014'),
 ('056','BBDNIIT','BTech','573','2015'),
 ('056','BBDNIIT','BTech','597','2016'),
 ('054','BBDNITM','BTech','600','2016'),
 ('056','BBDNIIT','BTech','614','2017'),
 ('056','BBDNIIT','BTech','644','2018');
INSERT INTO `year_collegedetail` (`college_code`,`college_name`,`Branch`,`total_admission`,`year`) VALUES 
 ('508','BBDEC','BTech','800','2013'),
 ('054','BBDNITM','BTech','800','2017'),
 ('508','BBDEC','BTech','847','2014'),
 ('508','BBDEC','BTech','862','2016'),
 ('508','BBDEC','BTech','895','2017'),
 ('054','BBDNITM','BTech','900','2018'),
 ('508','BBDEC','MA','700','2018'),
 ('508','BBDEC','MA','850','2017'),
 ('508','BBDEC','MA','949','2016'),
 ('508','BBDEC','MA','969','2014'),
 ('508','BBDEC','MA','973','2015'),
 ('508','BBDEC','MA','981','2013'),
 ('508','BBDEC','MCA','807','2018'),
 ('508','BBDEC','MCA','812','2017'),
 ('508','BBDEC','MCA','823','2016'),
 ('508','BBDEC','MCA','837','2015'),
 ('508','BBDEC','MCA','866','2014'),
 ('508','BBDEC','MCA','900','2013');
/*!40000 ALTER TABLE `year_collegedetail` ENABLE KEYS */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
