import shapefile

myshp = open("t4_21s_300M.shp", "rb")
mydbf = open("t4_21s_300M.dbf", "rb")
r = shapefile.Reader(shp=myshp, dbf=mydbf)

shapes = r.shapes()

print shapes