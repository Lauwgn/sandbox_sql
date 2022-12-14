SHOW DATABASES;

USE Azimut;

SHOW TABLES;

INSERT INTO products
(product_id, product_ref, template, language)
VALUES ("a", "b", "c", "d");

DELETE FROM products WHERE product_id = "a";

DELETE FROM products WHERE product_ref != "b";

DELETE FROM products;

SELECT * FROM products;

SHOW GRANTS FOR 'lau'@'localhost';