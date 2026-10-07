#What are the name of the customers that are not listed on the Orders table becuase they have not place an order 

Select c.name as Customers
from Customers c

Left Join Orders o 
ON o.customerId = c.id

where o.customerId is Null; 