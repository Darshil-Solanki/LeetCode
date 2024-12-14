# Write your MySQL query statement below
select round(sum(tiv_2016), 2) as tiv_2016 from insurance i1 
join 
(select tiv_2015 from insurance
group by tiv_2015 having count(*)>1) i2 
on i1.tiv_2015 = i2.tiv_2015 
join
(select pid, concat(convert(lat, char), convert(lon, char)) as loc from insurance group by concat(convert(lat, char), convert(lon, char)) having count(*)=1) i3
on i1.pid = i3.pid

-- SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
-- FROM Insurance
-- WHERE tiv_2015 IN (
--     SELECT tiv_2015
--     FROM Insurance
--     GROUP BY tiv_2015
--     HAVING COUNT(*) > 1
-- )
-- AND (lat, lon) IN (
--     SELECT lat, lon
--     FROM Insurance
--     GROUP BY lat, lon
--     HAVING COUNT(*) = 1
-- )
