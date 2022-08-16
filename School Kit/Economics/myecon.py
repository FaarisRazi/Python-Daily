# Handy functions for Economics to be added soon InshaAllah! 

# Getting the Quantatity Supplied/Demanded 
Qsd = lambda x,y,P: x + P*y # x = Units supplied/demanded at a price (y).

# Consumer Price Index (ct = current cost and c0 = base cost of market basket).
cpi = lambda ct, c0: ct/c0 * 100
