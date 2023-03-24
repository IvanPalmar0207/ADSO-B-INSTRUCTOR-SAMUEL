SELECT EmployeeID, ShipName, ShipAddress, ShipCity, ShipRegion
FROM Orders WHERE EmployeeID <= (SELECT EmployeeID FROM Employees 
WHERE EmployeeID=9) ORDER by EmployeeID; 