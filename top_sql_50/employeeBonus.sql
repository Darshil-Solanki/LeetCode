SELECT E.name, B.bonus FROM EMPLOYEE E LEFT JOIN BONUS B 
ON E.EMPID = B.EMPID 
WHERE B.BONUS<1000 OR B.BONUS IS NULL;
