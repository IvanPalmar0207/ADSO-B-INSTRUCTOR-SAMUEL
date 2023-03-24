SELECT ProductID, ProductName, QuantityPerUnit, max(UnitPrice) as
MaxUnitPrice FROM Products;