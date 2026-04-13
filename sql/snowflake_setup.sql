CREATE DATABASE instacart_db;

USE DATABASE instacart_db;

CREATE SCHEMA instacart_schema;

USE SCHEMA instacart_schema;

CREATE WAREHOUSE instacart_wh
WAREHOUSE_SIZE = 'XSMALL'
AUTO_SUSPEND = 60
AUTO_RESUME = TRUE;

USE WAREHOUSE instacart_wh;