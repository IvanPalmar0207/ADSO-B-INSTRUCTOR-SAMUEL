SELECT ProductID,ProductName FROM Products WHERE EXISTS (SELECT * 
FROM Suppliers WHERE Products.SupplierID=Suppliers.SupplierID);