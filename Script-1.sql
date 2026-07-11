SELECT * 
FROM Uber_Request_Data;

--Total Requests
SELECT COUNT(*) AS Total_Requests
FROM Uber_Request_Data;

--Pickup Point Wise Requests
SELECT `Pickup point`, COUNT(*) AS Total_Requests
FROM Uber_Request_Data
GROUP BY `Pickup point`;

--Status Wise Requests
SELECT Status, COUNT(*) AS Total
FROM Uber_Request_Data
GROUP BY Status;

--Driver Wise Requests
SELECT `Driver id`, COUNT(*) AS Total_Trips
FROM Uber_Request_Data
GROUP BY `Driver id`
ORDER BY Total_Trips DESC;

--Checking Time Format
SELECT "Request timestamp"
FROM Uber_Request_Data
LIMIT 10;

SELECT
SUBSTR("Request timestamp", 10, 2) AS Hour,
COUNT(*) AS Requests
FROM Uber_Request_Data
GROUP BY Hour
ORDER BY Hour;

--No. of Trips By Driver Id
SELECT "Driver id", COUNT(*) AS Total_Trips
FROM Uber_Request_Data
WHERE "Driver id" != 'NA'
GROUP BY "Driver id"
ORDER BY Total_Trips DESC;

--Top 10 Drivers
SELECT "Driver id", COUNT(*) AS Total_Trips
FROM Uber_Request_Data
WHERE "Driver id" != 'NA'
GROUP BY "Driver id"
ORDER BY Total_Trips DESC
LIMIT 10;

--Trip Completed
SELECT Status, COUNT(*) AS Total
FROM Uber_Request_Data
WHERE Status = 'trip completed'
GROUP BY Status;

--Cancellation Analysis
SELECT Status, COUNT(*) AS Total
FROM Uber_Request_Data
WHERE Status = 'Cancelled'
GROUP BY Status;

--No Cars Available
SELECT Status, COUNT(*) AS Total
FROM Uber_Request_Data
WHERE Status = 'No Cars Available'
GROUP BY Status;

--Pickup Point vs Status
SELECT
"Pickup point",
Status,
COUNT(*) AS Total
FROM Uber_Request_Data
GROUP BY "Pickup point", Status
ORDER BY "Pickup point";
