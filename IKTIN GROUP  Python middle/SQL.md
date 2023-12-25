


SQL (базовый синтаксис)
задача по sql

Бэкапы PostgreSQL


Customers, Orders, Shippings

// Вывести пользователей, у которых 2 и более заказов
// Вывести пользователей, у которых заказы в статусе Pending
// Вывести сумму доставленных заказов


https://www.programiz.com/sql/online-compiler/

SELECT * FROM Customers;
SELECT ' ';

SELECT * FROM Orders;
SELECT ' ';

SELECT * FROM Shippings;
SELECT ' ';


-- SELECT first_name, last_name FROM Orders JOIN Customers on Orders.customer_id=Customers.customer_id group by Orders.customer_id having count(Orders.customer_id)>=2;

-- SELECT * FROM Orders JOIN Shippings on Orders.customer_id=Shippings.customer where status='Pending';

-- SELECT SUM(ALL amount) from Orders JOIN Shippings on Orders.customer_id=Shippings.customer where status='Delivered' ;


SELECT first_name, last_name, item FROM Orders JOIN Customers on Orders.customer_id=Customers.customer_id group by Orders.customer_id having count(Orders.customer_id)>=2;

  
SELECT * FROM Orders JOIN Shippings on Orders.customer_id=Shippings.customer where status='Pending';

SELECT SUM(ALL amount) from Orders JOIN Shippings on Orders.customer_id=Shippings.customer where status='Pending' ;