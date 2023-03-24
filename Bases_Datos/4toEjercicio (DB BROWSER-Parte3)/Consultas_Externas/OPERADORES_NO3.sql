SELECT CategoryID, ProductID, ProductName, QuantityPerUnit, UnitPrice
FROM Products WHERE CategoryID < (SELECT CategoryID FROM Categories 
WHERE CategoryID=5) order by CategoryID;