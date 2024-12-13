# Write your MySQL query statement below
select * from (
select distinct visited_on, sum(amount) over(order by visited_on range between interval 6 day preceding and current row) as amount, round(sum(amount) over(order by visited_on range between interval 6 day preceding and current row) /7, 2) as average_amount  from customer 
) c 
where c.visited_on>=(select date_add(min(visited_on), interval 6 day) from customer)


-- select c1.end_date as visited_on, sum(amount) as amount, round(sum(amount)/7,2) as average_amount from Customer c join (select distinct c.visited_on as start_date ,c1.visited_on as end_date from Customer c join Customer c1 where c1.visited_on=DATE_ADD(c.visited_on, INTERVAL 6 DAY)) c1 where c.visited_on between c1.start_date and c1.end_date group by c1.end_date;
