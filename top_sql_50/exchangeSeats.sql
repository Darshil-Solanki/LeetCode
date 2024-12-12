# Write your MySQL query statement below

select s2.id, s1.student from seat s1 cross join seat s2 where s1.id = case when s1.id%2=1 then s2.id-1 else s2.id+1 end
union
select s.id, s.student from (select * from seat order by id desc limit 1) s where s.id%2=1

-- SELECT IF (id < (SELECT MAX(id) FROM Seat), 
--             IF(id % 2 = 0, id - 1, id + 1), 
--             IF(id % 2 = 0, id - 1, id)
--         ) AS id, student
-- FROM Seat
-- ORDER BY id;
