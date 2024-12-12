# Write your MySQL query statement below
select c1.category, c2.accounts_count
from 
(select 1 as id, "High Salary" as category from dual
union
select 2 as id, "Low Salary" as category from dual
union 
select 3 as id, "Average Salary" as category from dual
) c1 
join 
( select 1 as id, count(*) as accounts_count from accounts where income>50000 
union
select 2 as id, count(*) as accounts_count from accounts where income<20000 
union
select 3 as id, count(*) as accounts_count from accounts where income>=20000 and  income<=50000) c2 
on c1.id = c2.id


-- select category, max(accounts_count) as accounts_count
-- from
-- (select category, count(*) as accounts_count
-- from
-- (select account_id, case when income<20000 then 'Low Salary' when 20000<=income and income<=50000 then 'Average Salary' else 'High Salary' end as category
-- from Accounts) a1
-- group by category
-- union
-- select 'High Salary' as category, 0 as accounts_count
-- union
-- select 'Average Salary' as category, 0 as accounts_count
-- union
-- select 'Low Salary' as category, 0 as accounts_count) a2
-- group by category
