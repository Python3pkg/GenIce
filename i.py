import numpy as np
density = 0.92     #default density


bondlen = 3      #bond threshold	 
celltype = "rect"
cell = np.array([8.20808916836691, 8.20808916836691, 3.85780190913245])

positions = np.fromstring("""
1.36796014080003 1.36796014080003 0
1.36796014080003 6.8400469466752 0
6.8400469466752 1.36796014080003 0
6.8400469466752 6.8400469466752 0
2.73600236249174 2.73600236249174 1.92890095456622
2.73600236249174 5.47200472498349 1.92890095456622
5.47200472498349 2.73600236249174 1.92890095456622
5.47200472498349 5.47200472498349 1.92890095456622
""", sep=" ")
positions = positions.reshape((positions.size//3,3))