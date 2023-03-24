SELECT ProductID,ProductName, sum(UnitPrice) as TotalUnitPrice
FROM Products GROUP by UnitPrice HAVING sum(UnitPrice) > 90;