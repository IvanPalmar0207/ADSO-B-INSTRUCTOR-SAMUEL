SELECT OrderID, CustomerID, EmployeeID, ShipName, ShipAddress FROM
Orders WHERE EmployeeID in (SELECT EmployeeID FROM Employees 
WHERE Country='USA');