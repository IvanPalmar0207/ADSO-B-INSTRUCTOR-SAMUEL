SELECT ProductID, sum(UnitsInStock) AS TotalUnitsInStock FROM Products GROUP by ProductID;