# Write your MySQL query statement below
SELECT P.PRODUCT_NAME, SUM(O.UNIT) AS UNIT FROM PRODUCTS P JOIN ORDERS O ON P.PRODUCT_ID = O.PRODUCT_ID WHERE O.ORDER_DATE >= "2020-02-01" AND O.ORDER_DATE <= "2020-02-29" GROUP BY P.PRODUCT_ID HAVING SUM(O.UNIT)>99

-- SELECT Products.product_name, SUM(Orders.unit) AS unit
-- FROM Products NATURAL JOIN Orders
-- WHERE YEAR(Orders.order_date) = 2020 AND MONTH(Orders.order_date) = 2
-- GROUP BY product_id
-- HAVING SUM(Orders.unit)>=100
