SELECT TerritoryID,EmployeeID FROM EmployeeTerritories WHERE TerritoryID
>= (SELECT TerritoryID FROM Territories WHERE RegionID=2);
