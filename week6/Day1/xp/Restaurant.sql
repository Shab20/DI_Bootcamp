-- 1. What We Will Learn
-- Database, Table, Row, Column
-- Retrieve data, Add data

--  Exercise 1 : Items And Customers
-- Create a database called restaurant.
-- Add two tables:
-- items
-- customers.

-- Follow the instructions below to determine which columns and data types to add to the two tables:

CREATE TABLE items (
    ID int,
    Name varchar(255),
    Price int
);

CREATE TABLE customers (
    PersonID int,
    FirstName varchar(255),
    LastName varchar(255)
);

-- Add the following items to the items table:
-- 1 - Small Desk – 100 (ie. price)
-- 2 - Large desk – 300
-- 3 - Fan – 80

INSERT INTO items
VALUES ('1', 'Small Desk', '100');

INSERT INTO items
VALUES ('2', 'Large desk', '300');

INSERT INTO items
VALUES ('3', 'Fan', '80');

-- Add 5 new customers to the customers table:
-- 1 - Greg - Jones
-- 2 - Sandra - Jones
-- 3 - Scott - Scott
-- 4 - Trevor - Green
-- 5 - Melanie - Johnson

INSERT INTO customers
VALUES ('1', 'Greg', 'Jones');

INSERT INTO customers
VALUES ('2', 'Sandra', 'Jones');

INSERT INTO customers
VALUES ('3', 'Scott', 'Scott');

INSERT INTO customers
VALUES ('4', 'Trevor', 'Green');

INSERT INTO customers
VALUES ('5', 'Melanie', 'Johnson');

-- Use SQL to fetch the following data from the database:
-- All the items.

mysql> select * from items;
+------+------------+-------+
| ID   | Name       | Price |
+------+------------+-------+
|    1 | Small Desk |   100 |
|    2 | Large desk |   300 |
|    3 | Fan        |    80 |
+------+------------+-------+
3 rows in set (0.00 sec)

-- All the items with a price above 80 (80 not included).

mysql> select * from items where price > 80;
+------+------------+-------+
| ID   | Name       | Price |
+------+------------+-------+
|    1 | Small Desk |   100 |
|    2 | Large desk |   300 |
+------+------------+-------+
2 rows in set (0.00 sec)

-- All the items with a price below 300. (300 included)

mysql> select * from items where price <= 300;
+------+------------+-------+
| ID   | Name       | Price |
+------+------------+-------+
|    1 | Small Desk |   100 |
|    2 | Large desk |   300 |
|    3 | Fan        |    80 |
+------+------------+-------+
3 rows in set (0.00 sec)

-- All customers whose last name is ‘Smith’ (What will be your outcome?).

mysql> select * from customers where LastName = 'Smith';
Empty set (0.00 sec)

-- All customers whose last name is ‘Jones’.

mysql> select * from customers where LastName = 'Jones';
+----------+-----------+----------+
| PersonID | FirstName | LastName |
+----------+-----------+----------+
|        1 | Greg      | Jones    |
|        2 | Sandra    | Jones    |
+----------+-----------+----------+
2 rows in set (0.00 sec)

-- All customers whose firstname is not ‘Scott’.

mysql> select * from customers where FirstName != 'Scott';
+----------+-----------+----------+
| PersonID | FirstName | LastName |
+----------+-----------+----------+
|        1 | Greg      | Jones    |
|        2 | Sandra    | Jones    |
|        4 | Trevor    | Green    |
|        5 | Melanie   | Johnson  |
+----------+-----------+----------+
4 rows in set (0.00 sec)