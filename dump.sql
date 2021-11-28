BEGIN TRANSACTION;
CREATE TABLE CLIENT(CLno INT NOT NULL, CLname CHAR(20) NOT NULL, Rname CHAR(20) NOT NULL, CLhistory INT, PRIMARY KEY(CLno));
INSERT INTO "CLIENT" VALUES(1,'������','������',0);
INSERT INTO "CLIENT" VALUES(2,'�ǰ���','������',0);
INSERT INTO "CLIENT" VALUES(3,'�ȿ���','�����',0);
INSERT INTO "CLIENT" VALUES(4,'�����','�Ѽ���',0);
INSERT INTO "CLIENT" VALUES(5,'�۰��','������',0);
INSERT INTO "CLIENT" VALUES(6,'������','�����',0);
INSERT INTO "CLIENT" VALUES(7,'���̼�','�ɼ���',0);
INSERT INTO "CLIENT" VALUES(8,'������','���±�',0);
INSERT INTO "CLIENT" VALUES(10,'�Ѱ��','������',0);
INSERT INTO "CLIENT" VALUES(11,'��ö��','ǥ����',0);
INSERT INTO "CLIENT" VALUES(12,'�ϼ���','�ڼ���',0);
INSERT INTO "CLIENT" VALUES(13,'Ź����','���¿�',0);
INSERT INTO "CLIENT" VALUES(14,'���汸','������',0);
INSERT INTO "CLIENT" VALUES(15,'�տ���','õ����',0);
INSERT INTO "CLIENT" VALUES(16,'����ä','���ٿ�',0);
INSERT INTO "CLIENT" VALUES(17,'������','������',0);
INSERT INTO "CLIENT" VALUES(18,'������','���Ѱ�',0);
INSERT INTO "CLIENT" VALUES(19,'������','�����',0);
INSERT INTO "CLIENT" VALUES(20,'���ڰ�','������',0);
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
INSERT INTO "EMPLOYEE" VALUES(1,'������',5,20,10100,400);
INSERT INTO "EMPLOYEE" VALUES(2,'������',5,19,10000,100);
INSERT INTO "EMPLOYEE" VALUES(3,'ǳ����',4,18,8000,100);
INSERT INTO "EMPLOYEE" VALUES(4,'�ɽ�ȣ',4,18,8000,200);
INSERT INTO "EMPLOYEE" VALUES(5,'������',3,10,6100,200);
INSERT INTO "EMPLOYEE" VALUES(6,'ȫ���',2,7,5200,200);
INSERT INTO "EMPLOYEE" VALUES(7,'�����',2,7,5200,100);
INSERT INTO "EMPLOYEE" VALUES(8,'���ֿ�',2,7,5200,0);
INSERT INTO "EMPLOYEE" VALUES(9,'��â��',2,7,5200,0);
INSERT INTO "EMPLOYEE" VALUES(10,'�ڼҹ�',1,5,4500,0);
INSERT INTO "EMPLOYEE" VALUES(11,'������',1,5,4500,0);
INSERT INTO "EMPLOYEE" VALUES(12,'�̸�ȣ',1,5,4500,0);
INSERT INTO "EMPLOYEE" VALUES(13,'�߸���',1,5,4500,0);
INSERT INTO "EMPLOYEE" VALUES(14,'�۽���',0,4,4200,100);
INSERT INTO "EMPLOYEE" VALUES(15,'������',0,4,4200,100);
INSERT INTO "EMPLOYEE" VALUES(16,'���غ�',0,4,4200,100);
INSERT INTO "EMPLOYEE" VALUES(17,'�Ѽ���',0,3,3300,0);
INSERT INTO "EMPLOYEE" VALUES(18,'������',0,3,3300,100);
INSERT INTO "EMPLOYEE" VALUES(19,'�����',0,2,3000,200);
INSERT INTO "EMPLOYEE" VALUES(20,'������',0,1,2800,100);
CREATE TABLE FINANCE(Fyear INT NOT NULL, Capital INT, LaborCost INT, Premium INT, Payout INT, BonusCost INT, PRIMARY KEY(Fyear));
INSERT INTO "FINANCE" VALUES(2021,1000000,106000,169000,0,2000);
COMMIT;