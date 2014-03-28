-- Tickets
INSERT INTO tickets VALUES (1,'normal','Andre','2004-01-01 16:00:00','store_20',5);
INSERT INTO tickets VALUES (2,'normal','Bruno','2004-01-01 17:00:00','store_30',8);
INSERT INTO tickets VALUES (3,'normal','Carlos','2004-01-01 18:00:00','store_10',3);
INSERT INTO tickets VALUES (4,'premium','Daniel','2004-01-01 19:00:00','store_20',9);
INSERT INTO tickets VALUES (5,'normal','Emanuel','2004-01-01 20:00:00','store_10',1);

-- Deposits
INSERT INTO deposits VALUES (1,1,'2004-02-01 10:00:00','store_15',5,6.0);
INSERT INTO deposits VALUES (2,3,'2004-02-01 13:00:00','store_25',8,9.6);
INSERT INTO deposits VALUES (3,4,'2004-02-01 19:00:00','machine_75',4,4.8);
INSERT INTO deposits VALUES (4,2,'2004-02-01 22:00:00','machine_85',2,2.4);
INSERT INTO deposits VALUES (5,2,'2004-02-02 15:00:00','machine_85',1,1.2);
INSERT INTO deposits VALUES (6,1,'2004-02-03 11:00:00','store_35',3,3.6);
INSERT INTO deposits VALUES (7,3,'2004-02-03 11:30:00','machine_45',7,8.4);
INSERT INTO deposits VALUES (8,5,'2004-02-03 12:00:00','machine_95',11,13.2);
INSERT INTO deposits VALUES (9,1,'2004-02-05 21:00:00','store_35',5,6.0);
INSERT INTO deposits VALUES (10,1,'2004-02-06 20:00:00','machine_65',6,7.2);

-- Validations
INSERT INTO validations VALUES (1,3,'2005-01-01 7:00:00','subway_stop_5','subway_2','subway');
INSERT INTO validations VALUES (2,2,'2005-01-01 8:00:00','subway_stop_15','subway_2','subway');
INSERT INTO validations VALUES (3,3,'2005-01-01 7:30:00','subway_stop_15','subway_3','subway');
INSERT INTO validations VALUES (4,2,'2005-01-01 9:00:00','subway_stop_45','subway_5','subway');
INSERT INTO validations VALUES (5,4,'2005-01-02 10:00:01','train_stop_20','train_60','train');
INSERT INTO validations VALUES (6,3,'2005-01-01 8:00:00','bus_stop_25','bus_10','bus');
INSERT INTO validations VALUES (7,4,'2005-01-02 14:00:00','bus_stop_78','bus_7','bus');
INSERT INTO validations VALUES (8,2,'2005-01-01 11:00:00','bus_stop_50','bus_1','bus');
INSERT INTO validations VALUES (9,1,'2005-01-03 6:00:00','subway_stop_17','subway_24','subway');
INSERT INTO validations VALUES (10,3,'2005-01-01 9:00:00','bus_stop_35','bus_20','bus');
