 SELECT D.NAME AS DEPARTMENT, E1.NAME AS EMPLOYEE, E1.SALARY FROM EMPLOYEE E1 JOIN 
    (SELECT DEPARTMENTID, SALARY, RANK() OVER(PARTITION BY DEPARTMENTID ORDER BY SALARY DESC) AS RK FROM EMPLOYEE GROUP BY DEPARTMENTID, SALARY ORDER BY DEPARTMENTID, SALARY DESC) E2
    ON E1.DEPARTMENTID = E2.DEPARTMENTID AND E1.SALARY = E2.SALARY
    JOIN DEPARTMENT D ON E1.DEPARTMENTID = D.ID 
    WHERE RK<4

-- SELECT 
--     res.Department,
--     res.Employee,
--     res.salary
-- FROM (
--     SELECT 
--         b.name AS Department,
--         a.name AS Employee,
--         a.salary,
--         DENSE_RANK() OVER (
--             PARTITION BY a.departmentid 
--             ORDER BY a.salary DESC
--         ) AS rnk
--     FROM employee a 
--     JOIN Department b 
--     ON  a.departmentid = b.id
-- ) res
-- WHERE res.rnk < 4;
