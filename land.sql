-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 01, 2024 at 01:48 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `land`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add khatian', 7, 'add_khatian'),
(26, 'Can change khatian', 7, 'change_khatian'),
(27, 'Can delete khatian', 7, 'delete_khatian'),
(28, 'Can view khatian', 7, 'view_khatian'),
(29, 'Can add dag', 8, 'add_dag'),
(30, 'Can change dag', 8, 'change_dag'),
(31, 'Can delete dag', 8, 'delete_dag'),
(32, 'Can view dag', 8, 'view_dag'),
(33, 'Can add details', 9, 'add_details'),
(34, 'Can change details', 9, 'change_details'),
(35, 'Can delete details', 9, 'delete_details'),
(36, 'Can view details', 9, 'view_details'),
(37, 'Can add mortgage status', 10, 'add_mortgagestatus'),
(38, 'Can change mortgage status', 10, 'change_mortgagestatus'),
(39, 'Can delete mortgage status', 10, 'delete_mortgagestatus'),
(40, 'Can view mortgage status', 10, 'view_mortgagestatus'),
(41, 'Can add project', 11, 'add_project'),
(42, 'Can change project', 11, 'change_project'),
(43, 'Can delete project', 11, 'delete_project'),
(44, 'Can view project', 11, 'view_project');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$720000$p0GfcdlxRZ1hwb7kIQTDWA$YzH2hIbQ4ol8kxkWFrwrZGfRzQ1fccMG10SNEQ++9gQ=', '2024-10-01 10:48:13.459319', 1, 'admin', '', '', '', 1, 1, '2024-10-01 04:19:39.147457'),
(2, 'pbkdf2_sha256$720000$6dI5kVl6OsmiOSn68Qyg6d$KZ/hZRbx18d1amWRxbGCgmz8sLxUg/wirhoA0565L24=', '2024-10-01 10:50:28.544173', 0, 'gsadmin', 'General', 'Service', 'gs@radiant.com.bd', 0, 1, '2024-10-01 04:26:07.000000');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-10-01 04:26:07.920046', '2', 'gsadmin', 1, '[{\"added\": {}}]', 4, 1),
(2, '2024-10-01 04:26:46.167980', '2', 'gsadmin', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email address\"]}}]', 4, 1),
(3, '2024-10-01 07:23:18.492099', '1', 'Dhamrai Project', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"details\", \"object\": \"Deed 22 for Dhamrai Project\"}}]', 11, 1),
(4, '2024-10-01 07:23:44.512109', '1', 'Khatian for Address 1', 1, '[{\"added\": {}}]', 7, 1),
(5, '2024-10-01 07:24:19.588350', '1', 'Mortgage for City Bank', 1, '[{\"added\": {}}]', 10, 1),
(6, '2024-10-01 07:24:43.803887', '1', 'Dag for Address 1', 1, '[{\"added\": {}}]', 8, 1),
(7, '2024-10-01 10:48:38.496086', '2', 'Gazipur Project', 1, '[{\"added\": {}}]', 11, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(8, 'land_management', 'dag'),
(9, 'land_management', 'details'),
(7, 'land_management', 'khatian'),
(10, 'land_management', 'mortgagestatus'),
(11, 'land_management', 'project'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-10-01 04:19:18.066813'),
(2, 'auth', '0001_initial', '2024-10-01 04:19:18.876513'),
(3, 'admin', '0001_initial', '2024-10-01 04:19:19.040717'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-10-01 04:19:19.047716'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-10-01 04:19:19.055271'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-10-01 04:19:19.128422'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-10-01 04:19:19.200342'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-10-01 04:19:19.219020'),
(9, 'auth', '0004_alter_user_username_opts', '2024-10-01 04:19:19.226993'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-10-01 04:19:19.285717'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-10-01 04:19:19.289736'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-10-01 04:19:19.297763'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-10-01 04:19:19.314384'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-10-01 04:19:19.332064'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-10-01 04:19:19.353013'),
(16, 'auth', '0011_update_proxy_permissions', '2024-10-01 04:19:19.361175'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-10-01 04:19:19.381211'),
(18, 'sessions', '0001_initial', '2024-10-01 04:19:19.426144'),
(19, 'land_management', '0001_initial', '2024-10-01 07:15:44.829459');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('2lyt32tbmnh8ofgixwz3ojsfbiob62to', '.eJxVjEEOwiAQRe_C2hAYGdq6dN8zkIGZStVAUtqV8e7apAvd_vfef6lA25rD1mQJM6uLAnX63SKlh5Qd8J3KrepUy7rMUe-KPmjTY2V5Xg_37yBTy9-689RZcEwGWRAighMjk3UMDEgOI04W-0SOjePBmwhnkgFibxHAk3p_ANqZN4I:1svaSa:PctSi7BX8mInD9YuBG40xO6fCnrM1Lt13_BKFo556a4', '2024-10-15 10:50:28.558153');

-- --------------------------------------------------------

--
-- Table structure for table `land_management_dag`
--

CREATE TABLE `land_management_dag` (
  `id` bigint(20) NOT NULL,
  `cs` varchar(100) DEFAULT NULL,
  `sa` varchar(100) DEFAULT NULL,
  `rs` varchar(100) DEFAULT NULL,
  `bs_brs` varchar(100) DEFAULT NULL,
  `city_jorip` varchar(100) DEFAULT NULL,
  `details_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `land_management_dag`
--

INSERT INTO `land_management_dag` (`id`, `cs`, `sa`, `rs`, `bs_brs`, `city_jorip`, `details_id`) VALUES
(1, 'ss', 'qq', 'ee', 'rr', 'qw', 1);

-- --------------------------------------------------------

--
-- Table structure for table `land_management_details`
--

CREATE TABLE `land_management_details` (
  `id` bigint(20) NOT NULL,
  `sl` int(11) NOT NULL,
  `file_number` varchar(100) NOT NULL,
  `deed_number` varchar(100) NOT NULL,
  `registration_date` date NOT NULL,
  `mutation_status_number` varchar(100) DEFAULT NULL,
  `mutation_status_date` date DEFAULT NULL,
  `mutation_status_dcr` varchar(100) DEFAULT NULL,
  `last_seller` varchar(255) NOT NULL,
  `buyer` varchar(255) NOT NULL,
  `name_of_buyer` varchar(255) NOT NULL,
  `type_of_deed` varchar(100) NOT NULL,
  `land_area_in_decimal` decimal(10,2) NOT NULL,
  `deed_value` decimal(15,2) NOT NULL,
  `purchase_value` decimal(15,2) NOT NULL,
  `mouja` varchar(255) NOT NULL,
  `khajana_status` varchar(100) NOT NULL,
  `type_of_land` varchar(100) NOT NULL,
  `remarks` longtext DEFAULT NULL,
  `project_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `land_management_details`
--

INSERT INTO `land_management_details` (`id`, `sl`, `file_number`, `deed_number`, `registration_date`, `mutation_status_number`, `mutation_status_date`, `mutation_status_dcr`, `last_seller`, `buyer`, `name_of_buyer`, `type_of_deed`, `land_area_in_decimal`, `deed_value`, `purchase_value`, `mouja`, `khajana_status`, `type_of_land`, `remarks`, `project_id`) VALUES
(1, 1, '11', '22', '2024-10-07', NULL, NULL, '', 'KALAM', 'Radiant', 'Md. Nasser Shahrear Zahedee', 'Agreement', 35.00, 50000.00, 12000.00, 'Kulla', 'Paid', 'Agriculture', '', 1);

-- --------------------------------------------------------

--
-- Table structure for table `land_management_khatian`
--

CREATE TABLE `land_management_khatian` (
  `id` bigint(20) NOT NULL,
  `cs` varchar(100) DEFAULT NULL,
  `sa` varchar(100) DEFAULT NULL,
  `rs` varchar(100) DEFAULT NULL,
  `bs_brs` varchar(100) DEFAULT NULL,
  `city_jorip` varchar(100) DEFAULT NULL,
  `details_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `land_management_khatian`
--

INSERT INTO `land_management_khatian` (`id`, `cs`, `sa`, `rs`, `bs_brs`, `city_jorip`, `details_id`) VALUES
(1, 'ee', 'ew', 'ew', 'we', 'rr', 1);

-- --------------------------------------------------------

--
-- Table structure for table `land_management_mortgagestatus`
--

CREATE TABLE `land_management_mortgagestatus` (
  `id` bigint(20) NOT NULL,
  `bank_name` varchar(255) NOT NULL,
  `deed_number` varchar(100) NOT NULL,
  `mortgage_deed` varchar(100) DEFAULT NULL,
  `poa_deeds` varchar(100) DEFAULT NULL,
  `date` date NOT NULL,
  `details_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `land_management_mortgagestatus`
--

INSERT INTO `land_management_mortgagestatus` (`id`, `bank_name`, `deed_number`, `mortgage_deed`, `poa_deeds`, `date`, `details_id`) VALUES
(1, 'City Bank', '1122', 'mortgage_deeds/Deed.pdf', 'poa_deeds/Deed.pdf', '2024-10-08', 1);

-- --------------------------------------------------------

--
-- Table structure for table `land_management_project`
--

CREATE TABLE `land_management_project` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `Address` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `land_management_project`
--

INSERT INTO `land_management_project` (`id`, `name`, `Address`) VALUES
(1, 'Dhamrai Project', 'Kulla, Dhamrai, Dahaka'),
(2, 'Gazipur Project', 'Gazipur');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `land_management_dag`
--
ALTER TABLE `land_management_dag`
  ADD PRIMARY KEY (`id`),
  ADD KEY `land_management_dag_details_id_7fa9c60b_fk_land_mana` (`details_id`);

--
-- Indexes for table `land_management_details`
--
ALTER TABLE `land_management_details`
  ADD PRIMARY KEY (`id`),
  ADD KEY `land_management_deta_project_id_11555215_fk_land_mana` (`project_id`);

--
-- Indexes for table `land_management_khatian`
--
ALTER TABLE `land_management_khatian`
  ADD PRIMARY KEY (`id`),
  ADD KEY `land_management_khat_details_id_bb74e518_fk_land_mana` (`details_id`);

--
-- Indexes for table `land_management_mortgagestatus`
--
ALTER TABLE `land_management_mortgagestatus`
  ADD PRIMARY KEY (`id`),
  ADD KEY `land_management_mort_details_id_9ac2569d_fk_land_mana` (`details_id`);

--
-- Indexes for table `land_management_project`
--
ALTER TABLE `land_management_project`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `land_management_dag`
--
ALTER TABLE `land_management_dag`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `land_management_details`
--
ALTER TABLE `land_management_details`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `land_management_khatian`
--
ALTER TABLE `land_management_khatian`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `land_management_mortgagestatus`
--
ALTER TABLE `land_management_mortgagestatus`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `land_management_project`
--
ALTER TABLE `land_management_project`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `land_management_dag`
--
ALTER TABLE `land_management_dag`
  ADD CONSTRAINT `land_management_dag_details_id_7fa9c60b_fk_land_mana` FOREIGN KEY (`details_id`) REFERENCES `land_management_details` (`id`);

--
-- Constraints for table `land_management_details`
--
ALTER TABLE `land_management_details`
  ADD CONSTRAINT `land_management_deta_project_id_11555215_fk_land_mana` FOREIGN KEY (`project_id`) REFERENCES `land_management_project` (`id`);

--
-- Constraints for table `land_management_khatian`
--
ALTER TABLE `land_management_khatian`
  ADD CONSTRAINT `land_management_khat_details_id_bb74e518_fk_land_mana` FOREIGN KEY (`details_id`) REFERENCES `land_management_details` (`id`);

--
-- Constraints for table `land_management_mortgagestatus`
--
ALTER TABLE `land_management_mortgagestatus`
  ADD CONSTRAINT `land_management_mort_details_id_9ac2569d_fk_land_mana` FOREIGN KEY (`details_id`) REFERENCES `land_management_details` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
