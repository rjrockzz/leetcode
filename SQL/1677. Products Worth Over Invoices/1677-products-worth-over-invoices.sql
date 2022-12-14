# Write your MySQL query statement below
/* 
Product
* product_id
* name

Invoice
* invoice_id
* product_id
* rest
* paid
* canceled
* refunded
*/
SELECT p.name, IFNULL(SUM(rest),0) rest, IFNULL(SUM(paid),0) paid, IFNULL(SUM(canceled),0) canceled, IFNULL(SUM(refunded),0) refunded 
FROM product p
LEFT JOIN invoice i USING(product_id)
GROUP BY p.name
ORDER BY p.name