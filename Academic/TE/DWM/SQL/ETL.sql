-- Create the Student table
CREATE TABLE Student (
    roll_no INT(3),
    name CHAR(20),
    marks INT(3)
);

-- Insert data into the Student table
INSERT INTO Student (roll_no, name, marks);

-- Select data from the Student table
SELECT * FROM Student;

-- to get parh of the file
SHOW VARIABLES LIKE 'secure_file_priv';

-- loading data from names.csv
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/names.csv' INTO TABLE Student FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/names.csv' INTO TABLE Student FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS (roll_no, name, @m1, @m2, @m3) SET marks = (@m1 + @m2 + @m3)/3; 