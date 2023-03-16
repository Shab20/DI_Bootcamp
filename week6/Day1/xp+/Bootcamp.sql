-- 2. What We Will Learn
-- Database, Table, Row, Column
-- Retrieve data, Add data

-- 1. Create
-- 2. Create a database called bootcamp.
-- 3. Create a table called students.
-- 4. Add the following columns:
-- id
-- last_name
-- first_name
-- birth_date

CREATE TABLE students (
    id int AUTO_INCREMENT,
    first_name varchar (255),
    last_name varchar (255),
    birth_date date,
    PRIMARY KEY (id)
);

-- The id must be auto_incremented.
-- Make sure to choose the correct data type for each column.
-- To help, here is the data that you will have to insert. (How do we insert a date to a table?)

-- - Insert
-- 1. Insert the data seen above to the students table. Find the most efficient way to insert the data.

insert into students values (NULL,'Marc','Benichou','1998/11/02');
insert into students values (NULL,'Yoan','Cohen','2010/12/03');
insert into students values (NULL,'Lea','Benichou','1987/07/27');
insert into students values (NULL,'Amelia','Dux','1996/04/07');
insert into students values (NULL,'David','Grez','2003/06/04');
insert into students values (NULL,'Omer','Simpson','1980/10/03');

-- 2. Insert your last_name, first_name and birth_date to the students table (Take a look at the id given).

-- - Select
-- Fetch all of the data from the table.

mysql> select * from students;
+----+------------+-----------+------------+
| id | first_name | last_name | birth_date |
+----+------------+-----------+------------+
|  1 | Marc       | Benichou  | 1998-11-02 |
|  2 | Yoan       | Cohen     | 2010-12-03 |
|  3 | Lea        | Benichou  | 1987-07-27 |
|  4 | Amelia     | Dux       | 1996-04-07 |
|  5 | David      | Grez      | 2003-06-04 |
|  6 | Omer       | Simpson   | 1980-10-03 |
+----+------------+-----------+------------+
6 rows in set (0.00 sec)

-- Fetch all of the students first_names and last_names.

mysql> select first_name, last_name from students;
+------------+-----------+
| first_name | last_name |
+------------+-----------+
| Marc       | Benichou  |
| Yoan       | Cohen     |
| Lea        | Benichou  |
| Amelia     | Dux       |
| David      | Grez      |
| Omer       | Simpson   |
+------------+-----------+
6 rows in set (0.00 sec)

-- For the following questions, only fetch the first_names and last_names of the students.
-- Fetch the student which id is equal to 2.

mysql> select first_name, last_name from students where id = 2;
+------------+-----------+
| first_name | last_name |
+------------+-----------+
| Yoan       | Cohen     |
+------------+-----------+
1 row in set (0.01 sec)

-- Fetch the student whose last_name is Benichou AND first_name is Marc.

mysql> select first_name, last_name from students where last_name = 'Benichou' && first_name = 'Marc';
+------------+-----------+
| first_name | last_name |
+------------+-----------+
| Marc       | Benichou  |
+------------+-----------+
1 row in set, 1 warning (0.00 sec)

-- Fetch the students whose last_names are Benichou OR first_names are Marc.

mysql> select first_name, last_name from students where last_name = 'Benichou' or first_name = 'Marc';
+------------+-----------+
| first_name | last_name |
+------------+-----------+
| Marc       | Benichou  |
| Lea        | Benichou  |
+------------+-----------+
2 rows in set (0.00 sec)

-- Fetch the students whose first_names contain the letter a.

mysql> select first_name, last_name from students where first_name like '%a%';
+------------+-----------+
| first_name | last_name |
+------------+-----------+
| Marc       | Benichou  |
| Yoan       | Cohen     |
| Lea        | Benichou  |
| Amelia     | Dux       |
| David      | Grez      |
+------------+-----------+
5 rows in set (0.00 sec)

-- Fetch the students whose first_names start with the letter a.

mysql> select first_name, last_name from students where first_name like 'a%';
+------------+-----------+
| first_name | last_name |
+------------+-----------+
| Amelia     | Dux       |
+------------+-----------+
1 row in set (0.00 sec)

-- Fetch the students whose first_names end with the letter a.

mysql> select first_name, last_name from students where first_name like '%a';
+------------+-----------+
| first_name | last_name |
+------------+-----------+
| Lea        | Benichou  |
| Amelia     | Dux       |
+------------+-----------+
2 rows in set (0.00 sec)

-- Fetch the students whose second to last letter of their first_names are a (Example: Leah).

mysql> select first_name, last_name from students where first_name like '%a_';
+------------+-----------+
| first_name | last_name |
+------------+-----------+
| Yoan       | Cohen     |
+------------+-----------+
1 row in set (0.00 sec)

-- Fetch the students whose id’s are equal to 1 AND 3 .

mysql> select * from students where id = 1 or id = 3;
+----+------------+-----------+------------+
| id | first_name | last_name | birth_date |
+----+------------+-----------+------------+
|  1 | Marc       | Benichou  | 1998-11-02 |
|  3 | Lea        | Benichou  | 1987-07-27 |
+----+------------+-----------+------------+
2 rows in set (0.04 sec)