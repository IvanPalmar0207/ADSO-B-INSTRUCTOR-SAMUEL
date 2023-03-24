SELECT ProductID,ProductName, sum(UnitPrice) as TotalUnitPrice
FROM Products GROUP by ProductID;