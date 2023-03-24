SELECT ProductID, ProductName FROM Products WHERE UnitsInStock<=
(SELECT max(UnitsOnOrder) FROM Products);