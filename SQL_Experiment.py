import sqlite3

def my_function():

	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute("CREATE TABLE SurfMaster2 AS select SurfReport.ID, SurfReport.SwellSizeFt, SurfReport.SwellIntervalSec, WindInfo.WindMPH, WindDirection.WindDescription, SurfReport.AirTemp from SurfReport inner join WindInfo on SurfReport.ID = WindInfo.ID inner join WindDirection on WindInfo.ID = WindDirection.ID")
	conn.commit()
	cursor.close()
	conn.close()

my_function()

