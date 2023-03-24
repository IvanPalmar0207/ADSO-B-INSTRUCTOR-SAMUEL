SELECT ProductID, ProductName, UnitPrice, UnitsInStock, (SELECT
 avg(ReorderLevel) FROM Products) as AVGReorderLevel FROM Products;