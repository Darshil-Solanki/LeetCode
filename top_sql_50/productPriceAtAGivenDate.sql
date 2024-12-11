# Write your MySQL query statement below
select p1.product_id, p1.new_price as price from products p1 join
(select product_id, max(change_date) as latest_date from products where change_date<"2019-08-17" group by product_id) p2
on p1.product_id = p2.product_id and p1.change_date = p2.latest_date
union 
select distinct product_id, 10 as price from products group by product_id having min(change_date)>"2019-08-16"

-- WITH last_change AS (
--     SELECT 
--         product_id, 
--         MAX(change_date) AS last_change_date
--     FROM Products
--     WHERE change_date <= '2019-08-16'
--     GROUP BY product_id
-- )
-- SELECT 
--     p.product_id,
--     COALESCE(c.new_price, 10) AS price
-- FROM 
--     (SELECT DISTINCT product_id FROM Products) p
-- LEFT JOIN last_change lc ON p.product_id = lc.product_id
-- LEFT JOIN Products c 
--     ON p.product_id = c.product_id 
--     AND c.change_date = lc.last_change_date
-- ORDER BY 
--     p.product_id;
