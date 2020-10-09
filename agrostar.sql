-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 19, 2019 at 08:29 AM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.3.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `agrostar`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `e_mail_id` varchar(30) NOT NULL,
  `password` varchar(80) NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`e_mail_id`, `password`, `status`) VALUES
('dhruv8823@gmail.com', '$5$rounds=535000$KmsbiRDfFr2.bsND$x2tCsNpLCbzIalI5oS1zGT9XfUATDYWGZycNG6Ni7w/', 1);

-- --------------------------------------------------------

--
-- Table structure for table `brand`
--

CREATE TABLE `brand` (
  `brand_id` int(2) NOT NULL,
  `brand_name` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `brand`
--

INSERT INTO `brand` (`brand_id`, `brand_name`) VALUES
(1, 'pahuja'),
(2, 'V.N.R'),
(3, 'Proagro'),
(4, 'Seminis'),
(5, 'dhanuka'),
(6, 'U.P.L'),
(7, 'Indofil'),
(8, 'Highfieldag'),
(9, 'Abhay'),
(10, 'Rekkolt'),
(11, 'Parl'),
(12, 'Cammando'),
(13, 'Glediator'),
(14, 'Spraywell'),
(15, 'Tarplus');

-- --------------------------------------------------------

--
-- Table structure for table `city`
--

CREATE TABLE `city` (
  `city_id` int(2) NOT NULL,
  `state_id` int(2) NOT NULL,
  `city_name` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `city`
--

INSERT INTO `city` (`city_id`, `state_id`, `city_name`) VALUES
(1, 1, 'Agra'),
(2, 1, 'Allahabad'),
(3, 1, 'Kanpur'),
(4, 1, 'Lucknow'),
(5, 1, 'Mussoorie'),
(6, 1, 'Prayag'),
(7, 1, 'Varanasi'),
(8, 1, 'Meerut'),
(9, 2, 'Ahmedabad'),
(10, 2, 'Gandhinagar'),
(11, 2, 'Surat'),
(12, 2, 'Vadodara'),
(13, 2, 'Bardoli'),
(14, 3, 'Ludhiana'),
(15, 3, 'Amritsar'),
(16, 3, 'Patiala'),
(17, 4, 'Asansol'),
(18, 4, 'Darjeeling'),
(19, 4, 'Durgapur'),
(20, 4, 'Kolkata'),
(21, 4, 'Malda'),
(22, 4, 'Purulia'),
(23, 4, 'Siliguri'),
(24, 5, 'Banglore'),
(25, 5, 'Coorg'),
(26, 5, 'Mangalore'),
(27, 5, 'Mysore'),
(28, 5, 'Sakleshpur '),
(29, 6, 'Bhagalpur'),
(30, 6, 'Muzzaffarpur'),
(31, 6, 'Nalanda'),
(32, 7, 'Bhopal'),
(33, 7, 'Indore'),
(34, 7, 'Mundi'),
(35, 7, 'Ujjain'),
(36, 8, 'Bhimavaram'),
(37, 8, 'Guntur'),
(38, 8, 'Kakinada'),
(39, 8, 'Rajahmundry'),
(40, 8, 'Vijayawada'),
(41, 8, 'Visakhapatnam'),
(42, 8, 'Dharmavaram'),
(43, 8, 'Piduguralla'),
(44, 8, 'Tirupati'),
(45, 8, 'Madanapalli'),
(46, 9, 'Bhubaneswar'),
(47, 10, 'Chandigarh');

-- --------------------------------------------------------

--
-- Table structure for table `contact_us`
--

CREATE TABLE `contact_us` (
  `contact_id` int(2) NOT NULL,
  `name` varchar(25) NOT NULL,
  `mobile_no` bigint(10) NOT NULL,
  `question` text NOT NULL,
  `answer` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contact_us`
--

INSERT INTO `contact_us` (`contact_id`, `name`, `mobile_no`, `question`, `answer`) VALUES
(1, 'Kishanbhai', 8733884451, 'how it\'s work ', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `crop`
--

CREATE TABLE `crop` (
  `crop_id` int(2) NOT NULL,
  `crop_category_id` int(2) NOT NULL,
  `crop_image` varchar(50) NOT NULL,
  `crop_name` varchar(25) NOT NULL,
  `crop_description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `crop`
--

INSERT INTO `crop` (`crop_id`, `crop_category_id`, `crop_image`, `crop_name`, `crop_description`) VALUES
(6, 3, 'download.jpg6.jpg', 'Wheat', 'India, being the second largest producer of wheat in the world, has a high dependency on this rabi crop for its agricultural income. Wheat is a staple food among Indians, especially in the northern regions.\r\n<br>\r\n<br>\r\nWheat requires cool temperatures during its growing season in the range of about 14°c to 18°c. Rainfall of about 50 cms to 90 cms is most ideal. However, during harvesting season in the spring, wheat requires bright sunshine and slightly warmer temperatures. Uttar Pradesh is the largest wheat growing state in India closely followed by Punjab and Haryana.'),
(7, 4, 'crop7.jpg', 'Potato', 'Soil\r\nThe potato can be grown almost on any type of soil except saline and alkaline soils. Soils, which are naturally loose, offer least resistance to the enlargement of the tubers is preferred. Loamy and sandy loam soils, rich in organic matter with good drainage and aeration are most suitable for cultivation of potato crop. The soil with pH range of 5.2-6.4 is considered to be ideal.\r\n\r\nClimate\r\nPotato is a temperate climate crop, however it grows under a diverse range of climatic conditions. It is grown only under such conditions where the temperature during the growing seasons is moderately cool. The vegetative growth of the plant is best at a temperature of 24°C while tuber development is favoured at 20°C. Hence, potato is grown as a summer crop in the hills and as a winter crop in the tropical and subtropical regions. The crop can be raised up to an altitude of 3000 m above the sea level.\r\n\r\nSeason of planting\r\nPotatoes can be grown only under such conditions where the temperatures during the growing season are moderately cool. Therefore, the planting time varies from region to region. In hills of Himachal Pradesh and Uttar Pradesh, the spring crop is sown from January-February while the summer crop is sown in the month of May. In plains of Haryana, Punjab, Uttar Pradesh, Bihar and West Bengal spring crop is sown in January while the main crop in the 1st week of October. In the states of Madhya Pradesh, Maharashtra and Karnataka the kharif crop is sown by end of June while rabi crop is sown from mid of October-November.\r\n\r\n'),
(8, 4, 'f90-tomatoes-1168x657.jpg8.jpg', 'Tomato', 'Soil\r\n\r\nTomato can be grown on a wide range of soils from sandy to heavy clay. However, well-drained, sandy or red loam soils rich in organic matter with a pH range of 6.0-7.0 are considered as ideal.\r\n\r\nClimate\r\n\r\nTomato is a warm season crop. The best fruit colour and quality is obtained at a temperature range of 21-24°C. Temperatures above 32o C adversely affects the fruit set and development. The plants cannot withstand frost and high humidity. It requires a low to medium rainfall. Bright sunshine at the time of fruit set helps to develop dark red coloured fruits. Temperature below 10 oC adversely affects plant tissues thereby slowing down physiological activities.\r\n\r\nSeason of Planting\r\n\r\nSeeds are sown in June July for autumn winter crop and for spring summer crop seeds are sown in November. In the hills seed is sown in March April.'),
(9, 5, 'crop9.jpg', 'Pigeon pea', 'Soil type and Field Preparation :-\r\nIt is successfully grown in black cotton soils, well drained with a p H ranging from 7.0 - 8.5. Pigeonpea responds well to properly tilled and we ll drained seedbed. A deep ploughing with soil turning plough in fallow/waste lands, zero tillage sowing under intensive cropping system and Broad Bed Furrow/Ridge - furrow planting in low lying as well as intercropping areas is recommended. Raised Bed method of planting by dibbling at 2 inches depth with Row to Row distance 4 to 5 feet also 15 feet gap (2 pairs of Tur on bed) under intercropping of soybean under transplanting (Dharwad method/SPI), 5 X 3 and 3 X 1.5 feet spacing is recommended.\r\n\r\nClimate\r\nPigeonpea is predominantly a crop of tropical areas mainly cultivated in semi arid regions of India. Pigeonpea can be grown with a temperature ranging from 260C to 300C in the rainy season (June to October) and 170C to 220C in the post rainy (November to March) season. Pigeonpea is very sensitive to low radiation at pod development, therefore flowering during the monsoon and cloudy weather, leads to poor pod formation.'),
(10, 5, 'crop10.jpg', 'Black gram', 'Soil\r\nBlack gram can be grown on variety of soils ranging from sandy soils to heavy cotton soils. The most ideal soil is a well drained loam with pH of 6.5 to 7.8. Black gram cannot be grown on alkaline and saline soils. Land is prepared like any other kharif season pulse crop. However during summer it requires a thorough preparation to give a pulverized free from stubbles and weeds completely.\r\n\r\nClimate\r\nDuring kharif, it is cultivated throughout the country. It is best suited to rice fallows during rabi in southern and south-eastern parts of India. Blackgram needs relatively heavier soils than greengram.\r\n\r\n');

-- --------------------------------------------------------

--
-- Table structure for table `crop_category`
--

CREATE TABLE `crop_category` (
  `crop_category_id` int(2) NOT NULL,
  `crop_category_name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `crop_category`
--

INSERT INTO `crop_category` (`crop_category_id`, `crop_category_name`) VALUES
(6, 'Cash'),
(1, 'Fruit'),
(3, 'Grain'),
(2, 'Oilseed'),
(5, 'Pulses'),
(7, 'Spices'),
(4, 'Vegetable');

-- --------------------------------------------------------

--
-- Table structure for table `e_learn`
--

CREATE TABLE `e_learn` (
  `e_learn_id` int(2) NOT NULL,
  `e_learn_name` varchar(25) NOT NULL,
  `e_learn_description` text NOT NULL,
  `e_learn_img_tmb` varchar(50) NOT NULL,
  `e_learn_video` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `e_learn`
--

INSERT INTO `e_learn` (`e_learn_id`, `e_learn_name`, `e_learn_description`, `e_learn_img_tmb`, `e_learn_video`) VALUES
(1, 'new ', 'Des', 'e_learn_vid1.png', 'e_learn_vid1.webm'),
(2, 'video2', 'this is our first video', 'new_bg_AS.png2.png', 'WhatsApp_Video_2019-04-14_at_5.50.30_PM.mp42.mp4'),
(4, 'How it\'s work', 'this is information', 'wallpaper.jpg4.jpg', 'WhatsApp_Video_2019-04-14_at_5.50.40_PM.mp44.mp4');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `feedback_id` int(2) NOT NULL,
  `feedback_description` varchar(40) NOT NULL,
  `mobile_no` bigint(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `order_id` int(3) NOT NULL,
  `order_no` varchar(25) NOT NULL,
  `order_total_amt` float NOT NULL,
  `mobile_no` bigint(10) NOT NULL,
  `name` varchar(25) NOT NULL,
  `order_alt_mobile_no` bigint(10) NOT NULL,
  `city_id` int(2) NOT NULL,
  `order_delivery_address` varchar(80) NOT NULL,
  `order_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `delivery_date` date NOT NULL,
  `order_status` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`order_id`, `order_no`, `order_total_amt`, `mobile_no`, `name`, `order_alt_mobile_no`, `city_id`, `order_delivery_address`, `order_date`, `delivery_date`, `order_status`) VALUES
(14, '6jmh7pdxsj', 1560, 7043286169, 'dhruv suthar', 7043286169, 8, 'b-52,Nidhi parsk society,ahmedabad', '2019-03-25 14:23:34', '2019-03-31', 'Cancelled'),
(15, 'lwbbw83he9', 6240, 7043286169, 'dhruv suthar', 7043286169, 8, 'b-52,Nidhi parsk society,ahmedabad', '2019-03-25 14:23:34', '2019-03-31', 'Cancelled'),
(18, 'mp3ro466gq', 520, 7043286169, 'dhruv suthar', 7043286169, 8, 'b-52,Nidhi parsk society,ahmedabad', '2019-03-27 02:26:24', '2019-04-01', 'Cancelled'),
(23, 'kuodquz08k', 1040, 8733884451, 'dhruv suthar', 7043286169, 11, 'b-52,Nidhi parsk society,ahmedabad', '2019-03-28 07:43:32', '2019-04-02', 'Cancelled'),
(24, 'uth2z4nrfl', 520, 8733884451, 'dhruv suthar', 7984837820, 9, 'b-52,Nidhi parsk society,ahmedabad', '2019-03-28 07:49:57', '2019-04-02', 'Cancelled'),
(30, 'g5lev0ow87', 520, 8733884451, 'dhruv suthar', 7984837820, 9, 'b-52,Nidhi parsk society,ahmedabad', '2019-04-05 03:34:28', '2019-04-10', 'Cancelled'),
(31, 'tg4lqwdyld', 520, 8733884451, 'Ds', 7043286169, 9, 'b-52,Nidhi parsk society,ahmedabad', '2019-04-08 02:34:20', '2019-04-13', 'Ordered'),
(32, 'ibvu1lb3xi', 1560, 8733884451, 'dhruv suthar', 7984837820, 9, 'b-52,Nidhi parsk society,ahmedabad', '2019-04-08 02:34:20', '2019-04-13', 'Cancelled'),
(33, 'owntbu4i8w', 2080, 8733884451, 'Vismay', 8733884451, 1, 'ddjjd', '2019-04-08 03:05:54', '2019-04-13', 'Completed'),
(34, 'mpcli8zg92', 1040, 8733884451, 'dhruv suthar', 8733884451, 9, 'b-52,Nidhi parsk society,ahmedabad', '2019-04-11 07:35:30', '2019-04-16', 'Completed'),
(35, '2a0b7d1plk', 520, 7043286169, 'Kiranben', 7878047643, 1, 'B-52,Nidhi park,Thakkarnagar,Ahmedabad', '2019-04-12 09:02:57', '2019-04-17', 'Completed'),
(36, 'ittbe5cvrf', 520, 7043286169, 'dhruv suthar', 7979847320, 1, 'b-52,Nidhi parsk society,ahmedabad', '2019-04-14 03:59:57', '2019-04-19', 'Completed'),
(37, 'dl2i64jch5', 250, 7043286169, 'dhruv suthar', 7984837820, 1, 'b-52,Nidhi parsk society,ahmedabad', '2019-04-14 03:59:57', '2019-04-19', 'Completed'),
(38, 'irmtunxmfx', 520, 7043286169, 'dhruv suthar', 7984837820, 1, 'b-52,Nidhi parsk society,ahmedabad', '2019-04-14 03:59:57', '2019-04-19', 'Completed'),
(39, '04n0gkesce', 250, 7043286169, 'Vismay panchal', 7043286169, 1, 'b-52,Nidhi parsk society,ahmedabad', '2019-04-14 03:59:57', '2019-04-19', 'Completed'),
(40, 'g87gnarn57', 520, 7043286169, 'Vismay', 7984837820, 1, 'gbgttt', '2019-04-14 05:35:51', '2019-04-19', 'Ordered'),
(41, 'w2ub6e3f5u', 770, 7043286169, 'Jay', 7984837820, 1, 'Nidhi park Society', '2019-04-14 05:35:51', '2019-04-19', 'Ordered'),
(42, 'zckq9h2egl', 520, 7043286169, 'dhruv suthar', 7043286169, 1, 'b-52,Nidhi parsk society,ahmedabad', '2019-04-14 13:00:04', '2019-04-20', 'Ordered');

-- --------------------------------------------------------

--
-- Table structure for table `orders_details`
--

CREATE TABLE `orders_details` (
  `order_product_id` int(3) NOT NULL,
  `mobile_no` bigint(10) NOT NULL,
  `order_id` int(3) DEFAULT NULL,
  `product_id` int(3) NOT NULL,
  `quantity` int(3) NOT NULL,
  `is_ordered` int(1) NOT NULL DEFAULT '0',
  `is_cancelled` int(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `orders_details`
--

INSERT INTO `orders_details` (`order_product_id`, `mobile_no`, `order_id`, `product_id`, `quantity`, `is_ordered`, `is_cancelled`) VALUES
(9, 7043286169, 14, 6, 3, 1, 1),
(10, 7043286169, 15, 6, 12, 1, 1),
(14, 7043286169, 18, 6, 1, 1, 1),
(19, 8733884451, 23, 6, 2, 1, 1),
(20, 8733884451, 24, 6, 1, 1, 1),
(25, 8733884451, 30, 7, 1, 1, 1),
(26, 8733884451, 31, 7, 1, 1, 0),
(27, 8733884451, 32, 7, 2, 1, 1),
(28, 8733884451, 32, 6, 1, 1, 1),
(29, 8733884451, 33, 6, 2, 1, 1),
(30, 8733884451, 33, 7, 2, 1, 1),
(31, 8733884451, 34, 6, 2, 1, 0),
(32, 7043286169, 35, 6, 1, 1, 0),
(35, 7043286169, 36, 7, 1, 1, 0),
(36, 7043286169, 37, 8, 1, 1, 0),
(37, 7043286169, 38, 7, 1, 1, 0),
(38, 7043286169, 39, 8, 1, 1, 0),
(39, 7043286169, 40, 6, 1, 1, 0),
(40, 7043286169, 41, 6, 1, 1, 0),
(41, 7043286169, 41, 8, 1, 1, 0),
(42, 7043286169, 42, 7, 1, 1, 0),
(43, 7043286169, NULL, 6, 3, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `payment_id` int(2) NOT NULL,
  `order_id` int(3) NOT NULL,
  `transaction_id` varchar(40) DEFAULT NULL,
  `payment_method` varchar(25) NOT NULL,
  `payment_date` date DEFAULT NULL,
  `payment_status` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`payment_id`, `order_id`, `transaction_id`, `payment_method`, `payment_date`, `payment_status`) VALUES
(8, 14, NULL, 'Cash On Delivery', NULL, 'Cancelled'),
(9, 15, NULL, 'Cash On Delivery', NULL, 'Cancelled'),
(12, 18, NULL, 'Cash On Delivery', NULL, 'Cancelled'),
(17, 23, NULL, 'Cash On Delivery', NULL, 'Cancelled'),
(18, 24, NULL, 'Cash On Delivery', NULL, 'Cancelled'),
(19, 30, '20190405111212800110168855000386269', 'Debit / ATM Card', '2019-04-05', 'Cancelled'),
(20, 31, NULL, 'Cash On Delivery', NULL, 'Pending'),
(21, 32, NULL, 'Cash On Delivery', NULL, 'Cancelled'),
(22, 33, NULL, 'Cash On Delivery', NULL, 'Paid'),
(23, 34, NULL, 'Cash On Delivery', NULL, 'Paid'),
(24, 35, NULL, 'Cash On Delivery', NULL, 'Paid'),
(25, 36, NULL, 'Cash On Delivery', NULL, 'Paid'),
(26, 37, NULL, 'Cash On Delivery', NULL, 'Paid'),
(27, 38, NULL, 'Cash On Delivery', NULL, 'Paid'),
(28, 39, NULL, 'Cash On Delivery', NULL, 'Paid'),
(29, 40, '20190414111212800110168548200399579', 'Debit / ATM Card', '2019-04-14', 'Paid'),
(30, 41, NULL, 'Cash On Delivery', NULL, 'Pending'),
(31, 42, NULL, 'Cash On Delivery', NULL, 'Pending');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `product_id` int(3) NOT NULL,
  `product_category_id` int(2) NOT NULL,
  `crop_related` varchar(50) DEFAULT NULL,
  `product_brand_id` int(2) NOT NULL,
  `product_img` varchar(50) NOT NULL,
  `product_name` varchar(50) NOT NULL,
  `product_stock` int(3) NOT NULL,
  `product_price` float NOT NULL,
  `product_description` varchar(400) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`product_id`, `product_category_id`, `crop_related`, `product_brand_id`, `product_img`, `product_name`, `product_stock`, `product_price`, `product_description`) VALUES
(6, 4, 'fjfj', 1, 'tarplus_seet.png6.png', 'talpatri', 8, 520, 'djdjfj'),
(7, 4, 'None', 9, 'commando_rechargeble_torch.png7.png', 'Cammando torch', -1, 520, 'commando Torch'),
(8, 2, 'crop1,crop2,crop3`', 2, 'the_return_of_native_rice_variety.jpg8.jpg', 'Highfiled power gel', 12, 250, 'this is des');

-- --------------------------------------------------------

--
-- Table structure for table `product_category`
--

CREATE TABLE `product_category` (
  `product_category_id` int(2) NOT NULL,
  `product_category_name` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `product_category`
--

INSERT INTO `product_category` (`product_category_id`, `product_category_name`) VALUES
(1, 'Seed'),
(2, 'Crop Protection'),
(3, 'Crop Nutrition'),
(4, 'Farm Machinery');

-- --------------------------------------------------------

--
-- Table structure for table `product_review`
--

CREATE TABLE `product_review` (
  `review_id` int(3) NOT NULL,
  `product_id` int(3) NOT NULL,
  `rating` int(1) NOT NULL,
  `mobile_no` bigint(10) NOT NULL,
  `review_description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `product_review`
--

INSERT INTO `product_review` (`review_id`, `product_id`, `rating`, `mobile_no`, `review_description`) VALUES
(1, 6, 4, 8733884451, 'this is a best product'),
(2, 6, 2, 8733884451, 'this is a worst product '),
(3, 6, 4, 7043286169, 'Dhruv'),
(4, 6, 5, 7043286169, 'this'),
(5, 6, 5, 7043286169, 'thisisiis');

-- --------------------------------------------------------

--
-- Table structure for table `research_info`
--

CREATE TABLE `research_info` (
  `topic_id` int(3) NOT NULL,
  `topic_name` varchar(50) NOT NULL,
  `topic_description` text NOT NULL,
  `topic_img` varchar(50) NOT NULL,
  `topic_video` varchar(50) DEFAULT NULL,
  `mobile_no` bigint(10) NOT NULL,
  `topic_upload_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `research_info`
--

INSERT INTO `research_info` (`topic_id`, `topic_name`, `topic_description`, `topic_img`, `topic_video`, `mobile_no`, `topic_upload_date`) VALUES
(1, 'name', 'des', 'topic1.jpg', 'topic1.webm', 7043286169, '2019-03-27 02:57:33'),
(2, 'Related Wheat', 'Now a days crop price is increased', 'topic2.jpg', NULL, 7043286169, '2019-04-14 06:46:55'),
(3, 'top', 'jhjh', 'topic3.png', NULL, 7043286169, '2019-04-17 00:27:41');

-- --------------------------------------------------------

--
-- Table structure for table `state`
--

CREATE TABLE `state` (
  `state_id` int(2) NOT NULL,
  `state_name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `state`
--

INSERT INTO `state` (`state_id`, `state_name`) VALUES
(8, 'Andhra Pradesh'),
(23, 'Arunachal Pradesh'),
(14, 'Assam'),
(6, 'Bihar'),
(10, 'Chandigarh'),
(25, 'Chhattishgarh'),
(21, 'Delhi'),
(2, 'Gujarat'),
(22, 'Haryana'),
(24, 'Himachal Pradesh'),
(17, 'Jammu-Kashmir'),
(12, 'Jharkhand'),
(5, 'Karnataka'),
(18, 'Kerala'),
(7, 'Madhya Pradesh'),
(19, 'Maharastra'),
(13, 'Meghalaya'),
(9, 'Odisha'),
(3, 'Punjab'),
(16, 'Rajasthan'),
(11, 'Tamil Nadu'),
(15, 'Telangana'),
(1, 'Uttar Pradesh'),
(20, 'Uttarakhand'),
(4, 'West Bengal');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_mobile_no` bigint(10) NOT NULL,
  `user_type` varchar(25) NOT NULL,
  `user_profile` varchar(50) NOT NULL,
  `user_full_name` varchar(25) NOT NULL,
  `user_password` varchar(80) NOT NULL,
  `user_city_id` int(2) NOT NULL,
  `user_address` varchar(80) NOT NULL,
  `user_reg_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `user_status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_mobile_no`, `user_type`, `user_profile`, `user_full_name`, `user_password`, `user_city_id`, `user_address`, `user_reg_date`, `user_status`) VALUES
(7043286169, 'Agriculture Scientist', 'u_p7043286169.png', 'dhruv s', '$5$rounds=535000$8rsuj7ph5GmamR8S$jboulAbAo/5cjJDg51ZcP5ndp4jcSpSE0LBbpjm9g06', 8, 'b-52,Nidhi parsk society,ahmedabad', '2019-03-20 12:05:00', 0),
(7984837820, 'Farmer', 'Farmer.jpg', 'dhruv suthar', '$5$rounds=535000$hSKwXC.aLGkwJkBD$3Vfo0S2G0NazS4cJj0NeWNUTeVGik9xpF1cmmGgMKE0', 8, 'b-52,Nidhi parsk society,ahmedabad', '2019-04-14 03:44:43', 0),
(8733884451, 'Farmer', 'bg.jpg8733884451.jpg', 'Govind Suthar', '$5$rounds=535000$Duy3H3kSpt8xcdnl$pwjPu.uIdDEDvBfSPTlRirqy1NIshFJpwlMxx91K3e8', 9, 'b-52,Nidhi parsk society,ahmedabad', '2019-03-25 16:51:30', 0);

-- --------------------------------------------------------

--
-- Table structure for table `user_wishlist`
--

CREATE TABLE `user_wishlist` (
  `wishlist_id` int(3) NOT NULL,
  `mobile_no` bigint(10) NOT NULL,
  `product_id` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_wishlist`
--

INSERT INTO `user_wishlist` (`wishlist_id`, `mobile_no`, `product_id`) VALUES
(9, 7043286169, 6),
(10, 8733884451, 8),
(11, 8733884451, 7);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`e_mail_id`);

--
-- Indexes for table `brand`
--
ALTER TABLE `brand`
  ADD PRIMARY KEY (`brand_id`);

--
-- Indexes for table `city`
--
ALTER TABLE `city`
  ADD PRIMARY KEY (`city_id`),
  ADD UNIQUE KEY `city_name` (`city_name`),
  ADD KEY `state_id` (`state_id`);

--
-- Indexes for table `contact_us`
--
ALTER TABLE `contact_us`
  ADD PRIMARY KEY (`contact_id`);

--
-- Indexes for table `crop`
--
ALTER TABLE `crop`
  ADD PRIMARY KEY (`crop_id`),
  ADD UNIQUE KEY `crop_name` (`crop_name`),
  ADD KEY `crop_category_id` (`crop_category_id`);

--
-- Indexes for table `crop_category`
--
ALTER TABLE `crop_category`
  ADD PRIMARY KEY (`crop_category_id`),
  ADD UNIQUE KEY `crop_category_name` (`crop_category_name`);

--
-- Indexes for table `e_learn`
--
ALTER TABLE `e_learn`
  ADD PRIMARY KEY (`e_learn_id`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`feedback_id`),
  ADD UNIQUE KEY `mobile_no` (`mobile_no`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`order_id`),
  ADD KEY `city_id` (`city_id`),
  ADD KEY `mobile_no` (`mobile_no`);

--
-- Indexes for table `orders_details`
--
ALTER TABLE `orders_details`
  ADD PRIMARY KEY (`order_product_id`),
  ADD KEY `orders_details_ibfk_3` (`mobile_no`),
  ADD KEY `orders_details_ibfk_2` (`product_id`),
  ADD KEY `orders_details_ibfk_4` (`order_id`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`payment_id`),
  ADD KEY `payment_ibfk_1` (`order_id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`product_id`),
  ADD KEY `product_brand_id` (`product_brand_id`),
  ADD KEY `product_category_id` (`product_category_id`);

--
-- Indexes for table `product_category`
--
ALTER TABLE `product_category`
  ADD PRIMARY KEY (`product_category_id`);

--
-- Indexes for table `product_review`
--
ALTER TABLE `product_review`
  ADD PRIMARY KEY (`review_id`),
  ADD KEY `mobile_no` (`mobile_no`),
  ADD KEY `product_id` (`product_id`);

--
-- Indexes for table `research_info`
--
ALTER TABLE `research_info`
  ADD PRIMARY KEY (`topic_id`),
  ADD KEY `research_info_ibfk_1` (`mobile_no`);

--
-- Indexes for table `state`
--
ALTER TABLE `state`
  ADD PRIMARY KEY (`state_id`),
  ADD UNIQUE KEY `state_name` (`state_name`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_mobile_no`),
  ADD UNIQUE KEY `user_password` (`user_password`),
  ADD KEY `user_city_id` (`user_city_id`);

--
-- Indexes for table `user_wishlist`
--
ALTER TABLE `user_wishlist`
  ADD PRIMARY KEY (`wishlist_id`),
  ADD KEY `mobile_no` (`mobile_no`),
  ADD KEY `product_id` (`product_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `brand`
--
ALTER TABLE `brand`
  MODIFY `brand_id` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `city`
--
ALTER TABLE `city`
  MODIFY `city_id` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;

--
-- AUTO_INCREMENT for table `contact_us`
--
ALTER TABLE `contact_us`
  MODIFY `contact_id` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `crop`
--
ALTER TABLE `crop`
  MODIFY `crop_id` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `crop_category`
--
ALTER TABLE `crop_category`
  MODIFY `crop_category_id` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `e_learn`
--
ALTER TABLE `e_learn`
  MODIFY `e_learn_id` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `feedback_id` int(2) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `order_id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT for table `orders_details`
--
ALTER TABLE `orders_details`
  MODIFY `order_product_id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;

--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `payment_id` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `product_id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `product_category`
--
ALTER TABLE `product_category`
  MODIFY `product_category_id` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `product_review`
--
ALTER TABLE `product_review`
  MODIFY `review_id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `research_info`
--
ALTER TABLE `research_info`
  MODIFY `topic_id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `state`
--
ALTER TABLE `state`
  MODIFY `state_id` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `user_wishlist`
--
ALTER TABLE `user_wishlist`
  MODIFY `wishlist_id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `city`
--
ALTER TABLE `city`
  ADD CONSTRAINT `city_ibfk_1` FOREIGN KEY (`state_id`) REFERENCES `state` (`state_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `crop`
--
ALTER TABLE `crop`
  ADD CONSTRAINT `crop_ibfk_1` FOREIGN KEY (`crop_category_id`) REFERENCES `crop_category` (`crop_category_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `feedback`
--
ALTER TABLE `feedback`
  ADD CONSTRAINT `feedback_ibfk_1` FOREIGN KEY (`mobile_no`) REFERENCES `users` (`user_mobile_no`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`city_id`) REFERENCES `city` (`city_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`mobile_no`) REFERENCES `users` (`user_mobile_no`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `orders_details`
--
ALTER TABLE `orders_details`
  ADD CONSTRAINT `orders_details_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `orders_details_ibfk_3` FOREIGN KEY (`mobile_no`) REFERENCES `users` (`user_mobile_no`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `orders_details_ibfk_4` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `payment`
--
ALTER TABLE `payment`
  ADD CONSTRAINT `payment_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `products`
--
ALTER TABLE `products`
  ADD CONSTRAINT `products_ibfk_2` FOREIGN KEY (`product_brand_id`) REFERENCES `brand` (`brand_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `products_ibfk_3` FOREIGN KEY (`product_category_id`) REFERENCES `product_category` (`product_category_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `product_review`
--
ALTER TABLE `product_review`
  ADD CONSTRAINT `product_review_ibfk_1` FOREIGN KEY (`mobile_no`) REFERENCES `users` (`user_mobile_no`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `product_review_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`);

--
-- Constraints for table `research_info`
--
ALTER TABLE `research_info`
  ADD CONSTRAINT `research_info_ibfk_1` FOREIGN KEY (`mobile_no`) REFERENCES `users` (`user_mobile_no`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`user_city_id`) REFERENCES `city` (`city_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `user_wishlist`
--
ALTER TABLE `user_wishlist`
  ADD CONSTRAINT `user_wishlist_ibfk_1` FOREIGN KEY (`mobile_no`) REFERENCES `users` (`user_mobile_no`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `user_wishlist_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
