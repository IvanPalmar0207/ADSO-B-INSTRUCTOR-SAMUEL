SELECT pro.ProductID,cat.CategoryID,cat.CategoryName,cat.Description,
pro.ProductName,pro.QuantityPerUnit,pro.UnitsInStock FROM Products as pro
INNER JOIN Categories as cat ON cat.CategoryID=pro.CategoryID;