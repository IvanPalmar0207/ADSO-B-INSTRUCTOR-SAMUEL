SELECT cus.CustomerID, cus.CompanyName, cus.ContactName, cus.Phone,
ord.OrderDate, ord.ShipName, ord.ShipAddress,ord.ShipCountry
FROM Orders as ord LEFT JOIN Customers as cus
ON ord.CustomerID=cus.CustomerID ORDER by ord.ShipCountry;