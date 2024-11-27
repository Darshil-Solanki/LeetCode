# Write your MySQL query statement below
SELECT E.machine_id , ROUND(AVG(E.TIMESTAMP - S.TIMESTAMP), 3) AS processing_time FROM ACTIVITY S JOIN ACTIVITY E 
ON S.MACHINE_ID = E.MACHINE_ID AND S.PROCESS_ID = E.PROCESS_ID AND S.ACTIVITY_TYPE = 'start' AND E.ACTIVITY_TYPE = 'end' 
GROUP BY E.MACHINE_ID;
