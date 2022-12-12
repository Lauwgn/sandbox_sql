SHOW DATABASES;

USE Azimut;

CREATE TABLE tracker_io (
	io varchar(255),
    referrer varchar(255),
    url varchar(255),
    tracker_version varchar(255),
    wti varchar(255),
    product_id varchar(255),
    wvi varchar(255)
    );
    
SHOW TABLES;

CREATE TABLE tracker_action(
	io varchar(255),
	action varchar(255),
	created_at datetime,
	local_created_at datetime
	);
    
SHOW TABLES;

CREATE TABLE tracker_wvi(
	wvi varchar(255),
    browser_name varchar(255),
    browser_version varchar(255),
    engine_name varchar(255),
    ip_address varchar(255),
    languages varchar(255),
    os varchar(255),
    platform varchar(255),
    fingerprint varchar(255)
    );
    
SHOW TABLES;

CREATE TABLE products(
	product_id varchar(255),
    product_ref varchar(255),
    template varchar(255),
    language varchar(255)
    );

SHOW TABLES;