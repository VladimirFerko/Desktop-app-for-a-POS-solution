/*
CREATE DATABASE miffer
GO
*/
USE miffer

CREATE SCHEMA cafe
GO

CREATE TABLE cafe.kava
(id_kava			INT				IDENTITY
,nazov_kavy			VARCHAR(20)		NOT NULL
,cena_kavy			DECIMAL(2,1)	NOT NULL
,mnozstvo_kavy		INT				NOT NULL
,popis_kavy			VARCHAR(85)		NULL
,CONSTRAINT  kava_pk	PRIMARY KEY (id_kava)
)
GO

CREATE TABLE cafe.drink
(id_napoj				INT				IDENTITY
,meno_napoju			VARCHAR(20)		NOT NULL
,cena_napoju			DECIMAL			NOT NULL
,mnozstvo_napoju		INT				NOT NULL
,popis_napoju			VARCHAR(85)		NULL
,CONSTRAINT  drink_pk	PRIMARY KEY (id_napoj)
)
GO

CREATE TABLE cafe.dezert
(id_dezert				INT				IDENTITY
,meno_dezertu			VARCHAR(30)		NOT NULL
,cena_dezertu			DECIMAL			NOT NULL
,mnozstvo_dezertu		INT				NOT NULL
,popis_dezertu			VARCHAR(85)		NULL
,CONSTRAINT dezert_pk	PRIMARY KEY (id_dezert)
)
GO

CREATE TABLE cafe.zamestnanec
(id_zamestnanec			INT		IDENTITY
,prihlasovacie_meno		varchar(25)		NOT NULL
,heslo					varchar(15)		NOT NULL 
,meno					varchar(25)		NOT NULL
,priezvisko				varchar(25)		NOT NULL
)
GO


drop table cafe.dezert
drop table cafe.drink
drop table cafe.kava
drop table cafe.zamestnanec

INSERT cafe.kava (nazov_kavy, cena_kavy, mnozstvo_kavy, popis_kavy ) VALUES ('Espreso', 1.50, 25, NULL)
,('Èierna káva', 1.70, 25, NULL)
,('Latte', 1.45, 25, NULL)
,('Capuccino', 1.35, 25, NULL)
,('Macchiato', 2, 25, NULL)

INSERT cafe.drink (meno_napoju, cena_napoju, mnozstvo_napoju, popis_napoju ) VALUES ('Coca-Cola', 0.90, 25, NULL)
,('Fanta', 1.20, 25, NULL)
,('Sprite', 0.85, 25, NULL)
,('Mirinda', 1.20, 25, NULL)
,('7up', 0.80, 25, NULL)

INSERT cafe.dezert (meno_dezertu, cena_dezertu, mnozstvo_dezertu, popis_dezertu) VALUES ('Kremeš', 3.20, 25, NULL)
,('Tiramisu', 2.8, 25, NULL)
,('Mascarpone', 2.65, 25, NULL)
,('Èokoládová Roláda', 4.20, 25, NULL)
,('Bábovka', 1.30, 25, NULL)

INSERT cafe.zamestnanec (prihlasovacie_meno, heslo, meno, priezvisko)	VALUES	('Michalik', 'KR4f8g','Kristián','Michalik')
,('Ferko','ER9of8','Vladimír','Ferko')

SELECT * FROM cafe.drink
SELECT * FROM cafe.kava
SELECT * FROM cafe.dezert
SELECT * FROM cafe.zamestnanec