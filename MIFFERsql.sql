CREATE TABLE `dokoncenaobjednavka` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_stol` int(11) NOT NULL,
  `datumcas` datetime NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ;

CREATE TABLE `tovar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nazov` varchar(20) NOT NULL,
  `cena` decimal(5,2) NOT NULL,
  `mnozstvo` int(11) NOT NULL,
  `popis` varchar(85) DEFAULT NULL,
  `kategoria` int(11) NOT NULL
);

CREATE TABLE `objednavka` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_stol` int(11) NOT NULL,
  `id_tovar` int(11) NOT NULL,
  `stav` int(11) DEFAULT NULL,
  `datumcas` datetime NOT NULL DEFAULT current_timestamp(),
  `poznamka` varchar(150)  DEFAULT NULL,
   PRIMARY KEY (`id`),
   FOREIGN KEY (`id_tovar`) REFERENCES tovar (`id`)
);


CREATE TABLE `zamestnanec` (
  `id_zamestnanec` int(11) NOT NULL AUTO_INCREMENT,
  `prihlasovacie_meno` varchar(25)  NOT NULL,
  `heslo` varchar(15) NOT NULL,
  `meno` varchar(25)  NOT NULL,
  `priezvisko` varchar(30) NOT NULL,
  PRIMARY KEY (`id_zamestnanec`)
);


INSERT INTO `tovar` (`id`, `nazov`, `cena`, `mnozstvo`, `popis`, `kategoria`) VALUES
(1, 'Espreso', 1.50, 24, NULL, 1),
(2, 'Čierna káva', 1.70, 21, NULL, 1),
(3, 'Latte', 1.45, 24, NULL, 1),
(4, 'Capuccino', 1.35, 24, NULL, 1),
(5, 'Macchiato', 2.00, 24, NULL, 1),
(6, 'Kremeš', 3.20, 25, NULL, 3),
(7, 'Tiramisu', 2.80, 25, NULL, 3),
(8, 'Mascarpone', 2.65, 25, NULL, 3),
(9, 'Čokoládová Roláda', 4.20, 24, NULL, 3),
(10, 'Bábovka', 1.30, 25, NULL, 3),
(11, 'Coca-Cola', 0.90, 25, NULL, 2),
(12, 'Fanta', 1.20, 24, NULL, 2),
(13, 'Sprite', 0.85, 24, NULL, 2),
(14, 'Mirinda', 1.20, 26, NULL, 2),
(15, '7up', 0.80, 25, NULL, 2);
