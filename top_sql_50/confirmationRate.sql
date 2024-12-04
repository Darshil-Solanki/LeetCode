# Write your MySQL query statement below
SELECT S.user_id, ROUND(IFNULL(RES.RES, 0), 2) AS confirmation_rate FROM SIGNUPS S LEFT JOIN 

(SELECT T.USER_ID, SC.SUC / T.TOT AS RES FROM 
    (SELECT USER_ID, COUNT(*) AS TOT FROM CONFIRMATIONS GROUP BY USER_ID) T 
    JOIN
    (SELECT USER_ID, COUNT(*) as SUC FROM CONFIRMATIONS WHERE ACTION = "confirmed" GROUP BY USER_ID) SC
    ON T.USER_ID = SC.USER_ID) RES 
ON 
S.USER_ID = RES.USER_ID;

-- Better Approach
-- select s.user_id, round(avg(if(c.action="confirmed",1,0)),2) as confirmation_rate
-- from Signups as s left join Confirmations as c on s.user_id= c.user_id group by user_id;
