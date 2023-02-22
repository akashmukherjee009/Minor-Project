-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 21, 2022 at 08:18 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `granite`
--

-- --------------------------------------------------------

--
-- Table structure for table `technology`
--

CREATE TABLE `technology` (
  `t_id` int(11) NOT NULL,
  `t_name` varchar(50) NOT NULL,
  `t_companyname` varchar(50) NOT NULL,
  `salary` int(50) NOT NULL,
  `start` varchar(50) NOT NULL,
  `basic` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `technology`
--

INSERT INTO `technology` (`t_id`, `t_name`, `t_companyname`, `salary`, `start`, `basic`) VALUES
(1, 'react.js', 'IBM, Accenture, Dell, Capgemini', 3750000, 'https://www.w3schools.com/REACT/DEFAULT.ASP', 'JS, C, Mongo DB, C#, Python, SQL, Java, Bootstrap'),
(2, 'jQuery', 'IBM, Accenture, Capgemini, Dell', 2350000, 'https://www.w3schools.com/jquery/', 'JS, C, C#, Python, SQL, Java, HTML, CSS'),
(3, 'angular', 'IBM, Accenture, Dell, Capgemini, Wipro', 3750000, 'https://www.javatpoint.com/angular-7-tutorial', 'JS, HTML, CSS, C#, Python, SQL, Java'),
(4, 'Vue.js', 'IBM, Accenture, Dell, Capgemini, Cognizant, Tech M', 2300000, 'https://www.w3schools.com/whatis/whatis_vue.asp', 'JS, HTML, CSS, C#, Python, SQL, Java, C'),
(5, 'Express.js', 'IBM, Wipro, TCS, Accenture', 2200000, 'https://www.javatpoint.com/expressjs-tutorial', 'JS, SQL, Java, HTML, CSS'),
(6, 'ASP.NET Core', 'TCS, IBM, Mindtree, Wipro, Cognizant', 2200000, 'https://www.tutorialsteacher.com/core', 'JS, HTML, CSS, C#, Python, SQL, Java'),
(7, 'ASP.NET ', 'IBM, Dell, TCS, Accenture, Mindtree, Infosys, Capg', 37500000, 'https://www.w3schools.com/asp/default.asp', 'JS, HTML, CSS, C#, Python, SQL, Java, C'),
(8, 'Django', 'IBM, Accenture, Dell, Capgemini, Cognizant, Mainte', 3350000, 'https://www.w3schools.com/django/', 'JS, Python, Java, HTML, CSS, SQL'),
(9, 'Flask', ' Accenture, Capgemini, Dell, TCS, Tech Mahindra, C', 1900000, 'https://www.tutorialspoint.com/flask/index.htm', 'JS, Python,  HTML, CSS, SQL'),
(10, 'Angular.js', 'Infosys, TCS, Cognizant, Tech Mahindra,  Accenture', 1500000, 'https://www.w3schools.com/angular/default.asp', 'JS, HTML, CSS, C#, Python, SQL, Java'),
(11, 'Spring ', 'Cognizant, Dell, TCS, Infosys, Tech Mahindra, Well', 2300000, 'https://www.edureka.co/blog/spring-tutorial/', 'JS, HTML, CSS, C#, Python, SQL, Java, C'),
(12, 'Drupal', 'Accenture, Encora, Net Solutions, IBM, TCS, Capgem', 700000, 'https://www.tutorialspoint.com/drupal/index.htm#:~', 'JS, HTML, CSS, C#, Python, SQL, Java, C'),
(13, 'Laravel', 'Encora, Net Solutions, ValueLabs, Mantra Labs, Kot', 350000, 'https://www.tutorialspoint.com/laravel/index.htm', 'JS, HTML, CSS, C#, Python, SQL, Java, C'),
(14, 'Fast API', 'Bharati Airtel, TCS, Tech Mahindra, Mastek', 2000000, 'https://fastapi.tiangolo.com/tutorial/first-steps/', 'JS, HTML, CSS, Python, Java, C'),
(15, 'Symfony', 'Accenture, IBM', 0, 'https://www.tutorialspoint.com/symfony/index.htm', 'JS, C, HTML,CSS'),
(16, 'Svelte', 'CGI,  Mphasis', 0, 'https://developer.mozilla.org/en-US/docs/Learn/Too', 'JS, C'),
(17, 'Ruby on Rails', 'Tech Mahindra', 0, 'https://www.javatpoint.com/ruby-on-rails-tutorial', 'JS, HTML, CSS, C'),
(18, 'Gatsby', 'Intel', 0, 'https://www.gatsbyjs.com/docs/tutorial/', 'JS, HTML, CSS, Python, SQL'),
(19, 'Machine Learning', 'Accenture, IBM, Dell, Capgemini, Wipro, TCS, Tech ', 1500000, 'https://www.javatpoint.com/machine-learning', 'JS, HTML, CSS, Python'),
(20, 'Deep Learning', 'Intel, TCS, IBM, Wipro', 0, 'https://www.javatpoint.com/deep-learning', 'Python, SQL, Java, C'),
(21, 'Cybersecurity', 'Accenture, IBM, Capgemini', 0, 'https://www.w3schools.com/cybersecurity/index.php', 'JS, Python, SQL,  C'),
(22, 'Blockchain development', 'IBM, Capgemini, Infosys', 0, 'https://www.javatpoint.com/blockchain-tutorial', 'JS, Python, SQL, Java');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `technology`
--
ALTER TABLE `technology`
  ADD PRIMARY KEY (`t_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `technology`
--
ALTER TABLE `technology`
  MODIFY `t_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
