/*
CREATE DATABASE miffer
GO
*/
USE miffer

CREATE SCHEMA cafe
GO

CREATE TABLE tovar
(id			INT				NOT NULL AUTO_INCREMENT
,nazov			VARCHAR(20)		NOT NULL
,cena			DECIMAL(5,2)	NOT NULL
,mnozstvo		INT				NOT NULL
,popis			VARCHAR(85)		NULL
,kategoria		INT				NOT NULL
,PRIMARY KEY (id)
)
;



CREATE TABLE zamestnanec
(id_zamestnanec			INT		NOT NULL AUTO_INCREMENT
,prihlasovacie_meno		varchar(25)		NOT NULL
,heslo					varchar(15)		NOT NULL 
,PRIMARY KEY (id_zamestnanec)
)
;

CREATE TABLE objednavka
(id				INT				NOT NULL AUTO_INCREMENT
,id_stol			INT		NOT NULL
,id_tovar			INT			NOT NULL
,stav		INT				NOT NULL --0 - objednane 1 - donesene
,datumcas DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
,PRIMARY KEY (id)
,FOREIGN KEY (id_tovar) REFERENCES tovar(id)
)
;


drop table dezert
drop table drink
drop table kava

INSERT tovar (nazov, cena, mnozstvo, popis, kategoria ) VALUES ('Espreso', 1.50, 25, NULL,1)
,('Èierna káva', 1.70, 25, NULL,1)
,('Latte', 1.45, 25, NULL,1)
,('Capuccino', 1.35, 25, NULL,1)
,('Macchiato', 2, 25, NULL,1)

INSERT tovar (nazov, cena, mnozstvo, popis, kategoria ) VALUES ('Coca-Cola', 0.90, 25, NULL,2)
,('Fanta', 1.20, 25, NULL,2)
,('Sprite', 0.85, 25, NULL,2)
,('Mirinda', 1.20, 25, NULL,2)
,('7up', 0.80, 25, NULL,2)

INSERT tovar (nazov, cena, mnozstvo, popis, kategoria) VALUES ('Kremeš', 3.20, 25, NULL,3)
,('Tiramisu', 2.8, 25, NULL,3)
,('Mascarpone', 2.65, 25, NULL,3)
,('Èokoládová Roláda', 4.20, 25, NULL,3)
,('Bábovka', 1.30, 25, NULL,3)

INSERT zamestnanec (prihlasovacie_meno, heslo)	VALUES	('Michalik', 'KR4f8g')
,('Ferko','ER9of8')

SELECT * FROM tovar
SELECT * FROM zamestnanec