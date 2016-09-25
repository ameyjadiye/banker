CREATE TABLE `transactions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bank` varchar(10) NOT NULL,
  `date` date NOT NULL,
  `reference` varchar(200) DEFAULT NULL,
  `value_date` date NOT NULL,
  `debit_amount` double NOT NULL,
  `credit_amount` double NOT NULL,
  `ref_number` mediumtext,
  `closing_balance` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
