-- script that computes the score average of all records in the table second_table of the database hbtn_0c_0
SELECT SUM(score) DIV COUNT(*) AS average FROM second_table
