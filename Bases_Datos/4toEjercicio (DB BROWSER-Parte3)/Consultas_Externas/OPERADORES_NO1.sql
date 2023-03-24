  SELECT SupplierID,ProductID,ProductName FROM Products WHERE SupplierID =
  (SELECT SupplierID FROM Suppliers WHERE SupplierID=10);