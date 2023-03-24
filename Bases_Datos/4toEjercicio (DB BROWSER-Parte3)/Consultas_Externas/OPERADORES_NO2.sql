SELECT RegionID, TerritoryID, TerritoryDescription FROM Territories
WHERE RegionID <> (SELECT RegionID FROM Regions WHERE RegionDescription <> 'Eastern') ORDER by RegionID;