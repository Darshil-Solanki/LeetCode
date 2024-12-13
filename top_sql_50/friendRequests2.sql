# Write your MySQL query statement below
select t.id, sum(t.num) as num from 
((select requester_id as id, count(*) num from requestaccepted group by requester_id)
union all
(select accepter_id as id, count(*) num from requestaccepted group by accepter_id)) t group by t.id order by sum(t.num) desc limit 1

-- with cte as(select requester_id as id
-- from requestaccepted
-- union all
-- select accepter_id as id
-- from requestaccepted)
-- select id ,count(id) as num
-- from cte 
-- group by id
-- order by num desc 
-- limit 1
