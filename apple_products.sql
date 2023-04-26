
/*
CREATE TABLE apple_products.computers(
    comp_Id int primary key Auto_Increment,
    model_name varchar(50),
    ram int,
    ssd int,
    processor int
);



INSERT INTO apple_products.computers (model_name, ram, ssd, processor)
VALUES ('MacBook Pro', 16, 512, 7);

INSERT INTO apple_products.computers (model_name, ram, ssd, processor)
VALUES ('iMac', 8, 256, 5);

INSERT INTO apple_products.computers (model_name, ram, ssd, processor)
VALUES ('Mac Mini', 4, 128, 10);


INSERT INTO apple_products.computers (model_name, ram, ssd, processor)
VALUES ('MacBook Air', 8, 256, 10);

INSERT INTO apple_products.computers (model_name, ram, ssd, processor)
VALUES ('Mac Pro', 32, 1024, 9);

CREATE TABLE apple_products.mobiles(
    mobile_Id int primary key Auto_Increment,
    model_name varchar(50),
    ram int,
    storage int,
    processor int
);





INSERT INTO apple_products.mobiles (model_name, ram, storage, processor)
VALUES ('iPhone 13', 6, 128, 15);

INSERT INTO apple_products.mobiles (model_name, ram, storage, processor)
VALUES ('iPhone 12 Pro', 6, 256, 14);

INSERT INTO apple_products.mobiles (model_name, ram, storage, processor)
VALUES ('iPhone SE (2nd gen)', 3, 64, 13);

INSERT INTO apple_products.mobiles (model_name, ram, storage, processor)
VALUES ('iPhone 11', 4, 128, 13);

INSERT INTO apple_products.mobiles (model_name, ram, storage, processor)
VALUES ('iPhone XR', 3, 64, 12);



CREATE TABLE apple_products.accessories (
    accessory_Id int PRIMARY KEY AUTO_INCREMENT,
    name varchar(50),
    type varchar(50),
    compatibility varchar(50),
    mode varchar(50)
);



INSERT INTO apple_products.accessories (name, type, compatibility, mode)
VALUES ('AirPods Pro', 'Earbuds', 'iPhone/iPad/Mac', 'Bluetooth');


INSERT INTO apple_products.accessories (name, type, compatibility, mode)
VALUES ('Magic Mouse 2', 'Mouse', 'Mac', 'Bluetooth');

INSERT INTO apple_products.accessories (name, type, compatibility, mode)
VALUES ('Magic Keyboard with Numeric Keypad', 'Keyboard', 'Mac', 'Bluetooth');

INSERT INTO apple_products.accessories (name, type, compatibility, mode)
VALUES ('Leather Case with MagSafe for iPhone 13', 'Case', 'iPhone 13', 'MagSafe');

INSERT INTO apple_products.accessories (name, type, compatibility, mode)
VALUES ('Pro Display XDR', 'Monitor', 'Mac', '6K Retina Display');



CREATE TABLE apple_products.warranty (
    warranty_Id int PRIMARY KEY AUTO_INCREMENT,
    warranty_period int,
    warranty_price float,
    product_price float,
    product_id int
);

*/

INSERT INTO apple_products.warranty (warranty_period, warranty_price, product_price, product_id)
VALUES (12, 1000.0, 25000.0, 1);

INSERT INTO apple_products.warranty (warranty_period, warranty_price, product_price, product_id)
VALUES (18, 2000.0, 3500.0, 2);

INSERT INTO apple_products.warranty (warranty_period, warranty_price, product_price, product_id)
VALUES (24, 3000.0, 50000.0, 3);

INSERT INTO apple_products.warranty (warranty_period, warranty_price, product_price, product_id)
VALUES (28, 5000.0, 75000.0, 4);

INSERT INTO apple_products.warranty (warranty_period, warranty_price, product_price, product_id)
VALUES (24, 4000.0, 100000.0, 5);


