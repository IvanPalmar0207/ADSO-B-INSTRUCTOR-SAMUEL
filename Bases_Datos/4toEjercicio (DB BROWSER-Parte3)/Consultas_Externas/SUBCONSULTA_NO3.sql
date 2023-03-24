SELECT EmployeeID,OrderID,OrderDate,RequiredDate, ShippedDate, ShipName
FROM Orders WHERE EmployeeID in (SELECT EmployeeID FROM Employees WHERE EmployeeID=1);