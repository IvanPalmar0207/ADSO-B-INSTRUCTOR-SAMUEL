SELECT ord.OrderID, ord.ShipName, ord.ShipAddress,em.EmployeeID
,em.FirstName,em.LastName, em.Country,cum.CustomerID,cum.CompanyName,
cum.ContactName, cum.ContactTitle FROM Orders as ord INNER JOIN
Employees as em on ord.EmployeeID=em.EmployeeID INNER JOIN 
Customers as cum on ord.CustomerID=cum.CustomerID;