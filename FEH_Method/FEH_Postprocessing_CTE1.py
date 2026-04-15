#
from odbAccess import *
import numpy as np

#----------------------------- Parameters ------------------------------
#
satin_num = 3 # 2 for plain and 3 for twill
job_name = f'Job_woven{satin_num}_FEH_cte'
if satin_num == 2:
    tmp_num, t_num, s_num = satin_num, 1, 4
else:
    tmp_num = satin_num + 1
    t_num, s_num = 1, 8
yarn_w, yarn_h, yarn_sec1, yarn_sec2, extra_t = 2.0, 0.6, 1.8, 0.4, 0.04   # 2.2 for twill, 2.29 for plain
rve_t = yarn_h + yarn_sec2 + extra_t/s_num
rve_size = np.array([tmp_num*yarn_w + extra_t, rve_t, tmp_num*yarn_w + extra_t])
savefile = f'Woven{satin_num}_Homogenized_CTE1_FEH.txt'
#
odb = openOdb(f'{job_name}_1.odb')
homo_alpha, VRVE = np.zeros((3, 3)), rve_size[0]*rve_size[1]*rve_size[2]
#
dtm = odb.rootAssembly.DatumCsysByThreePoints(name='CSYS-1', coordSysType=CARTESIAN, origin=(0.0, 0.0, 0.0),
    point1=(1.0, 0.0, 0.0), point2=(0.0, 1.0, 0.0))
Instance = odb.rootAssembly.instances['PART-1-1']
F1V = (odb.steps['Step-1'].frames[-1].fieldOutputs['E'].getTransformedField(datumCsys=dtm).
       getSubset(region=Instance, position=INTEGRATION_POINT).values)
F2V = odb.steps['Step-1'].frames[-1].fieldOutputs['IVOL'].getSubset(region=Instance, position=INTEGRATION_POINT).values
#
strain = np.array([v.data for v in F1V], dtype=float)
ivol = np.array([v.data for v in F2V], dtype=float)
avg_strain = np.sum(strain * ivol[:, None], axis=0) / VRVE
homo_alpha[0, 0], homo_alpha[1, 1], homo_alpha[2, 2] = avg_strain[0], avg_strain[1], avg_strain[2]
homo_alpha[0, 1], homo_alpha[0, 2], homo_alpha[1, 2] = avg_strain[3], avg_strain[4], avg_strain[5]
#
odb.close()
#
homo_alpha[1,0], homo_alpha[2,0], homo_alpha[2,1] = homo_alpha[0,1], homo_alpha[0,2], homo_alpha[1,2]
np.savetxt(savefile, homo_alpha, delimiter=",")
#


