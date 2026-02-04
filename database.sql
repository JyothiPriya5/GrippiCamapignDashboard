CREATE TABLE campaigns (
    id INTEGER PRIMARY KEY,
    name TEXT,
    status TEXT,
    clicks INTEGER,
    cost REAL,
    impressions INTEGER
);

INSERT INTO campaigns VALUES
(1,'Summer Sale','Active',150,45.99,1000),
(2,'Black Friday','Paused',320,89.50,2500),
(3,'Winter Deals','Active',210,60.25,1800),
(4,'New Launch','Active',400,120.75,5000),
(5,'Clearance','Paused',90,20.00,600),
(6,'Festive Offer','Active',275,70.10,2200),
(7,'Flash Sale','Paused',180,55.00,1500),
(8,'Referral Bonus','Active',350,95.60,3200),
(9,'Weekend Deal','Paused',140,38.75,900),
(10,'Mega Offer','Active',500,150.00,6000);
