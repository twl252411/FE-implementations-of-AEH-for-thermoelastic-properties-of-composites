
import numpy as np

#----------------------------- Parameters ------------------------------
#
satin_num = 2  # 2 for plain and 3 for twill
job_name = f'Job_woven{satin_num}_AEH1_elastic'
savefile = f'Woven{satin_num}_Homogenized_Stiffness_AEH1.txt'
#
data = np.loadtxt(f'{job_name}_3.dat')
[row, col] = data.shape
estran = np.zeros((int(row / 2), 6))
#
for i in range(int(row/2)):
    estran[i,0:3], estran[i,3:6] = data[i*2+0,0:3], data[i*2+1,0:3]
#
[row1, col1] = estran.shape
block_size = int(row1 / 6)
valid_rows = block_size * 6
homo_stiff = estran[:valid_rows].reshape(6, block_size, 6).sum(axis=1).T
np.savetxt(savefile, homo_stiff, delimiter=",")
