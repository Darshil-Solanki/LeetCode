# Write your MySQL query statement below
SELECT Q1.QUERY_NAME, ROUND(AVG(RATING/POSITION), 2) AS QUALITY, ROUND((IFNULL( Q2.POOR_QUERY , 0)/COUNT(*))*100, 2) AS POOR_QUERY_PERCENTAGE FROM QUERIES Q1 
LEFT JOIN 
( SELECT QUERY_NAME, COUNT(*) AS POOR_QUERY FROM QUERIES WHERE RATING<3 GROUP BY QUERY_NAME) Q2 
ON Q1.QUERY_NAME = Q2.QUERY_NAME
WHERE Q1.QUERY_NAME IS NOT NULL
GROUP BY QUERY_NAME;

-- select query_name, round(avg(rating/position),2) as quality, 
-- coalesce(round(sum(case when rating<3 then 1 else 0 end)*100/count(*),2),0) as poor_query_percentage
-- from queries
-- where query_name is not null
-- group by query_name
