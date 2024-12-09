# Write your MySQL query statement below
select product_id, first_year, quantity, price from 
(select product_id, year as first_year, rank() over(partition by product_id order by year) as rk, quantity, price from sales) s
where rk = 1;
-- select distinct s1.product_id, s1.year as first_year, s1.quantity, s1.price from sales s1 join 
-- (select product_id, year, rank() over(partition by product_id order by year) as rk from sales) s2
-- on s1.product_id = s2.product_id and s1.year = s2.year
-- where s2.rk = 1;
