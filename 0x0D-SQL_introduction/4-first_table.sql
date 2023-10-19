-- Creates a table called first_table in the current database in your MySQL
-- first_table description: id INT, name VARCHAR(256)
-- The database name will be passed as an argument
-- If the table first_table already exists , the code should fail
-- SELECT or SHOW is not to be used

CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
