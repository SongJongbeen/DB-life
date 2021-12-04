BEGIN TRANSACTION;
CREATE TABLE CLIENT(CLno INT NOT NULL, CLname CHAR(20) NOT NULL, Rname CHAR(20) NOT NULL, CLhistory INT, PRIMARY KEY(CLno));
INSERT INTO "CLIENT" VALUES(1,'설병헌','고상혁',0);
INSERT INTO "CLIENT" VALUES(2,'권강민','노은성',0);
INSERT INTO "CLIENT" VALUES(3,'안요한','오재우',0);
INSERT INTO "CLIENT" VALUES(4,'안재범','한성우',0);
INSERT INTO "CLIENT" VALUES(5,'송경모','고종석',0);
INSERT INTO "CLIENT" VALUES(6,'전광조','김수혁',0);
INSERT INTO "CLIENT" VALUES(7,'최이수','심소은',0);
INSERT INTO "CLIENT" VALUES(8,'유강민','허태기',0);
INSERT INTO "CLIENT" VALUES(9,'임현승','심상원',0);
INSERT INTO "CLIENT" VALUES(10,'한경모','유연자',0);
INSERT INTO "CLIENT" VALUES(11,'오철순','표우준',0);
INSERT INTO "CLIENT" VALUES(12,'하성한','박선민',0);
INSERT INTO "CLIENT" VALUES(13,'탁병헌','박태우',0);
INSERT INTO "CLIENT" VALUES(14,'유경구','전영웅',0);
INSERT INTO "CLIENT" VALUES(15,'손여진','천강석',0);
INSERT INTO "CLIENT" VALUES(16,'설은채','류다운',0);
INSERT INTO "CLIENT" VALUES(17,'정지해','윤으뜸',0);
INSERT INTO "CLIENT" VALUES(18,'고나영','성한결',0);
INSERT INTO "CLIENT" VALUES(19,'유혜린','김다은',0);
INSERT INTO "CLIENT" VALUES(20,'백자경','정보미',0);
CREATE TABLE CONTRACT(Cno INT, Eno INT, CLno INT, Ctype CHAR(1), Cactive INT, PRIMARY KEY(Cno));
INSERT INTO "CONTRACT" VALUES(1,5,9,'A',0);
INSERT INTO "CONTRACT" VALUES(2,5,5,'B',0);
INSERT INTO "CONTRACT" VALUES(3,6,10,'A',0);
INSERT INTO "CONTRACT" VALUES(4,6,4,'A',0);
INSERT INTO "CONTRACT" VALUES(5,4,16,'C',0);
INSERT INTO "CONTRACT" VALUES(6,4,8,'D',0);
INSERT INTO "CONTRACT" VALUES(7,7,12,'E',0);
INSERT INTO "CONTRACT" VALUES(8,3,2,'D',0);
INSERT INTO "CONTRACT" VALUES(9,15,17,'B',0);
INSERT INTO "CONTRACT" VALUES(10,14,19,'E',0);
INSERT INTO "CONTRACT" VALUES(11,20,13,'E',0);
INSERT INTO "CONTRACT" VALUES(12,19,7,'C',0);
INSERT INTO "CONTRACT" VALUES(13,19,1,'C',0);
INSERT INTO "CONTRACT" VALUES(14,16,14,'C',0);
INSERT INTO "CONTRACT" VALUES(15,18,3,'A',0);
INSERT INTO "CONTRACT" VALUES(16,1,6,'A',0);
INSERT INTO "CONTRACT" VALUES(17,1,18,'A',0);
INSERT INTO "CONTRACT" VALUES(18,1,15,'E',0);
INSERT INTO "CONTRACT" VALUES(19,1,20,'D',0);
INSERT INTO "CONTRACT" VALUES(20,2,11,'C',0);
CREATE TABLE CTYPE(Ctype CHAR(1), Premium INT, Payout INT, PRIMARY KEY(Ctype));
INSERT INTO "CTYPE" VALUES('A',46,5000);
INSERT INTO "CTYPE" VALUES('B',49,7000);
INSERT INTO "CTYPE" VALUES('C',51,7000);
INSERT INTO "CTYPE" VALUES('D',55,10000);
INSERT INTO "CTYPE" VALUES('E',61,15000);
CREATE TABLE EMPLOYEE(Eno INT NOT NULL, Ename CHAR(20) NOT NULL, Erole INT NOT NULL, Eyear INT, Ewage INT, Ebonus INT, PRIMARY KEY(Eno));
INSERT INTO "EMPLOYEE" VALUES(1,'강수혜',5,20,10100,400);
INSERT INTO "EMPLOYEE" VALUES(2,'배현희',5,19,10000,100);
INSERT INTO "EMPLOYEE" VALUES(3,'풍은주',4,18,8000,100);
INSERT INTO "EMPLOYEE" VALUES(4,'심시호',4,18,8000,200);
INSERT INTO "EMPLOYEE" VALUES(5,'유유경',3,10,6100,200);
INSERT INTO "EMPLOYEE" VALUES(6,'홍재원',2,7,5200,200);
INSERT INTO "EMPLOYEE" VALUES(7,'백시현',2,7,5200,100);
INSERT INTO "EMPLOYEE" VALUES(8,'강주영',2,7,5200,0);
INSERT INTO "EMPLOYEE" VALUES(9,'강창진',2,7,5200,0);
INSERT INTO "EMPLOYEE" VALUES(10,'박소민',1,5,4500,0);
INSERT INTO "EMPLOYEE" VALUES(11,'복우희',1,5,4500,0);
INSERT INTO "EMPLOYEE" VALUES(12,'이만호',1,5,4500,0);
INSERT INTO "EMPLOYEE" VALUES(13,'추명우',1,5,4500,0);
INSERT INTO "EMPLOYEE" VALUES(14,'송시하',0,4,4200,100);
INSERT INTO "EMPLOYEE" VALUES(15,'예정희',0,4,4200,100);
INSERT INTO "EMPLOYEE" VALUES(16,'송해빈',0,4,4200,100);
INSERT INTO "EMPLOYEE" VALUES(17,'한세빈',0,3,3300,0);
INSERT INTO "EMPLOYEE" VALUES(18,'봉세준',0,3,3300,100);
INSERT INTO "EMPLOYEE" VALUES(19,'봉재욱',0,2,3000,200);
INSERT INTO "EMPLOYEE" VALUES(20,'설은비',0,1,2800,100);
CREATE TABLE FINANCE(Fyear INT NOT NULL, Capital INT, LaborCost INT, Premium INT, Payout INT, BonusCost INT, PRIMARY KEY(Fyear));
INSERT INTO "FINANCE" VALUES(2021,1000000,106000,169000,0,2000);
COMMIT;
