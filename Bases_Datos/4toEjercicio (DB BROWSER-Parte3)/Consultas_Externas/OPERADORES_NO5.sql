SELECT OrderID, OrderDate, RequiredDate, ShippedDate, ShipName FROM
Orders WHERE CustomerID>(SELECT CustomerID FROM Customers WHERE
CompanyName='Alfreds Futterkiste');