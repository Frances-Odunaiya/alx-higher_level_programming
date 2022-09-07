-- creates a table id_not_null in MySQL server
-- description id INT default value 1, name VARCHAR(256)
-- The database name will be passed as an argument of the mysql command
-- If the database exists, your script should not fail

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
