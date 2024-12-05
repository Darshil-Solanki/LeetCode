# Write your MySQL query statement below
SELECT DATE_FORMAT(TRANS_DATE, "%Y-%m") AS month, country, COUNT(*) AS trans_count, 
SUM(CASE WHEN STATE="approved" THEN 1 ELSE 0 END) AS approved_count,
SUM(AMOUNT) AS  trans_total_amount, 
SUM(CASE WHEN STATE="approved" THEN AMOUNT ELSE 0 END) AS approved_total_amount FROM TRANSACTIONS GROUP BY DATE_FORMAT(TRANS_DATE, "%Y-%m"), COUNTRY;
