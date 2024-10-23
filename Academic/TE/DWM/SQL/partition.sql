-- Create the Student table
CREATE TABLE Student (
    roll_no INT(3),
    name CHAR(20),
    marks INT(3)
);

-- Insert data into the Student table
INSERT INTO Student (roll_no, name, marks) VALUES
(554, "Soham", 90), 
(556, "Pooja", 60), 
(568, "Swaraj", 40), 
(558, "Mudassir", 70), 
(559, "Ajay", 90), 
(561, "Kamran", 30), 
(561, "Aarya", 60), 
(564, "Advait", 80);

-- Select data from the Student table
SELECT * FROM Student;

-- Range Partition
-- Create the partitioned Student_Par_values table
CREATE TABLE Student_Par_values (
    roll_no INT(3),
    name CHAR(20),
    marks INT(3)
)
PARTITION BY RANGE (marks) (
    PARTITION p1 VALUES LESS THAN (50),
    PARTITION p2 VALUES LESS THAN (70),
    PARTITION p3 VALUES LESS THAN (80),
    PARTITION p4 VALUES LESS THAN MAXVALUE
);

-- Copying the table from Student
INSERT INTO Student_Par_values SELECT * FROM Student;

-- Check each partition
SELECT * FROM Student_Par_values PARTITION (p1);
SELECT * FROM Student_Par_values PARTITION (p2);
SELECT * FROM Student_Par_values PARTITION (p3);
SELECT * FROM Student_Par_values PARTITION (p4);


-- Hash Partition
-- Create the partitioned Student_Par_hash table
CREATE TABLE Student_Par_hash (
    roll_no INT(3),
    name CHAR(20),
    marks INT(3)
)
PARTITION BY HASH (marks) PARTITIONS 4;

-- Copying the table from Student
INSERT INTO Student_Par_hash SELECT * FROM Student;

-- See which partitions are there
select partition_name from information_schema.partitions where table_name = "Student_Par_list";

-- Check each partition
SELECT * FROM Student_Par_hash PARTITION (p0);
SELECT * FROM Student_Par_hash PARTITION (p1);
SELECT * FROM Student_Par_hash PARTITION (p2);
SELECT * FROM Student_Par_hash PARTITION (p3);


-- List Partition
-- Create the partitioned Student_Par_values table
CREATE TABLE Student_Par_list (
    roll_no INT(3),
    name CHAR(20),
    marks INT(3)
)
PARTITION BY LIST (roll_no) (
    PARTITION p1 VALUES in (554, 556, 558, 559),
    PARTITION p2 VALUES in (561, 562, 564, 568)
);

-- Copying the table from Student
INSERT INTO Student_Par_list SELECT * FROM Student;

-- Check each partition
SELECT * FROM Student_Par_list PARTITION (p1);
SELECT * FROM Student_Par_list PARTITION (p2);


-- Key Partition
-- Create the partitioned Student_Par_values table
CREATE TABLE Student_Par_key (
    roll_no INT(3) PRIMARY KEY,
    name CHAR(20),
    marks INT(3)
)
PARTITION BY KEY () PARTITIONS 4;

-- Copying the table from Student
INSERT INTO Student_Par_key SELECT * FROM Student;

-- Check each partition
SELECT * FROM Student_Par_key PARTITION (p0);
SELECT * FROM Student_Par_key PARTITION (p1);
SELECT * FROM Student_Par_key PARTITION (p2);
SELECT * FROM Student_Par_key PARTITION (p3);

-- To select partition tables for each
select partition_name from information_schema.partitions where table_name = "Student_Par_values";
select partition_name from information_schema.partitions where table_name = "Student_Par_list";
select partition_name from information_schema.partitions where table_name = "Student_Par_hash";
select partition_name from information_schema.partitions where table_name = "Student_Par_key";