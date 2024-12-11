# Write your MySQL query statement below
select p.person_name from 
(select person_name, sum(weight)over(order by turn) tot from queue
order by tot desc) p
where p.tot<=1000
limit 1

-- WITH cte AS(
-- SELECT *,
--     SUM(weight) OVER(ORDER BY turn ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS total
-- FROM Queue)

-- SELECT person_name
-- FROM cte
-- WHERE total <= 1000
-- ORDER BY total DESC
-- LIMIT 1
