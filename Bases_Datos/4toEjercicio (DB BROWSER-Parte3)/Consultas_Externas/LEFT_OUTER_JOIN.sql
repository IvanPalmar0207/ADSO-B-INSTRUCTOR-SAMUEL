SELECT reg.RegionID,terr.TerritoryID,terr.TerritoryDescription,
reg.RegionDescription FROM Territories as terr LEFT OUTER JOIN Regions
as reg on reg.RegionID=terr.RegionID;