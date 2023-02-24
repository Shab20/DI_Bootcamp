show databases;

use hollywood;
CREATE TABLE actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
)

select * from actors;

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Matt','Damon','1970/08/10', 5);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('George','Clooney','1961/06/05', 2);

/*Instructions*/
/*1. Count how many actors are in the table.*/

select count(first_name) from actors;
+-------------------+
| count(first_name) |
+-------------------+
|                 2 |
+-------------------+
1 row in set (0.01 sec)

/*2. Try to add a new actor with some blank fields. What do you think the outcome will be ?*/

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('','','','');

ERROR 1292 (22007): Incorrect date value: '' for column 'age' at row 1