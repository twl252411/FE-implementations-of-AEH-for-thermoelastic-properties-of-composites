from abaqus import *
from abaqusConstants import *
from driverUtils import executeOnCaeStartup
import numpy as np
import itertools as it

executeOnCaeStartup()
Mdb()

#---------------------------------------------------------------------------
#
asp = 10
inc_rad = 5.0
inc_len = inc_rad * asp * 2.0
rve_size = np.array([inc_len * 2.0, inc_len * 2.0, inc_len * 2.0]) * 1.25 # 1.5
extra_t = 0.2
cae_name = f'fiber_rve_.cae'
pts, angs = np.loadtxt(f'points3d_fiber.txt', delimiter=','), np.loadtxt(f'angles3d_fiber.txt', delimiter=',')

#---------------------------------------------------------------------------
#
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=6.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.0, inc_rad))
p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p.BaseSolidExtrude(sketch=s, depth=inc_len)
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']

#---------------------------------------------------------------------------
#
a = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Part-1']
ins_lists = ()
for i in range(len(pts)):
    ins_name = f'Part-1-{i+1}'
    a.Instance(name=ins_name, part=p, dependent=OFF)
    a.translate(instanceList=(ins_name, ), vector=(0.0, 0.0, -inc_len/2.0))
    a.rotate(instanceList=(ins_name, ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(0.0, 1.0, 0.0), angle=90)

    if ivf == 10:
        a.rotate(instanceList=(ins_name, ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(0.0, 0.0, 1.0), angle=angs[i,1])
        x1, y1 = np.sin(angs[i,1]/180*np.pi), -np.cos(angs[i,1]/180*np.pi)
        a.rotate(instanceList=(ins_name, ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(x1, y1, 0.0), angle=90-angs[i,0])
    else:
        a.rotate(instanceList=(ins_name,), axisPoint=(0.0, 0.0, 0.0), axisDirection=(0.0, 0.0, 1.0), angle=angs[i, 0] / np.pi * 180)
        x1, y1 = np.sin(angs[i, 0]), -np.cos(angs[i, 0])
        a.rotate(instanceList=(ins_name,), axisPoint=(0.0, 0.0, 0.0), axisDirection=(x1, y1, 0.0), angle=90 - angs[i, 1] / np.pi * 180)

    a.translate(instanceList=(ins_name, ), vector=(pts[i,0], pts[i,1], pts[i,2]))
    ins_lists += (a.instances[ins_name], )
a.InstanceFromBooleanMerge(name='Part-New', instances=ins_lists, keepIntersections=ON, originalInstances=DELETE, domain=GEOMETRY)
a.deleteFeatures(('Part-New-1',))
mdb.models['Model-1'].parts.changeKey(fromName='Part-New', toName='Part-2')
del mdb.models['Model-1'].parts['Part-1']
#
p = mdb.models['Model-1'].parts['Part-2']
a.Instance(name='Part-2-1', part=p, dependent=OFF)
a.Instance(name='Part-2-2', part=p, dependent=OFF)

#---------------------------------------------------------------------------
#
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.rectangle(point1=(0.0, 0.0), point2=(rve_size[0],rve_size[1]))
p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p.BaseSolidExtrude(sketch=s1, depth=rve_size[2])
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
#
a = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Part-1']
a.Instance(name='Part-1-1', part=p, dependent=OFF)

#---------------------------------------------------------------------------
#
a = mdb.models['Model-1'].rootAssembly
a.InstanceFromBooleanCut(name='Part-3',instanceToBeCut=a.instances['Part-2-1'],
    cuttingInstances=(a.instances['Part-1-1'], ), originalInstances=DELETE)
a.InstanceFromBooleanCut(name='Part-4', instanceToBeCut=a.instances['Part-2-2'],
    cuttingInstances=(a.instances['Part-3-1'], ), originalInstances=DELETE)
del mdb.models['Model-1'].parts['Part-1']
del mdb.models['Model-1'].parts['Part-2']
del mdb.models['Model-1'].parts['Part-3']
a.deleteFeatures(('Part-4-1',))
mdb.models['Model-1'].parts.changeKey(fromName='Part-4', toName='Part-2')
#
p = mdb.models['Model-1'].parts['Part-2']
a.Instance(name='Part-2-1', part=p, dependent=OFF)
a.translate(instanceList=('Part-2-1', ), vector=(-rve_size[0]/2.0, -rve_size[1]/2.0, -rve_size[2]/2.0))

#---------------------------------------------------------------------------
#
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.rectangle(point1=(0.0, 0.0), point2=(rve_size[0]+extra_t,rve_size[1]+extra_t))
p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, type=DEFORMABLE_BODY)
p.BaseSolidExtrude(sketch=s1, depth=rve_size[2]+extra_t)
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
#
a = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Part-1']
a.Instance(name='Part-1-1', part=p, dependent=OFF)
a.translate(instanceList=('Part-1-1', ), vector=(-(rve_size[0]+extra_t)/2.0, -(rve_size[1]+extra_t)/2.0, -(rve_size[2]+extra_t)/2.0))

#---------------------------------------------------------------------------
#
a = mdb.models['Model-1'].rootAssembly
a.InstanceFromBooleanCut(name='Part-3', instanceToBeCut=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'],
    cuttingInstances=(a.instances['Part-2-1'], ), originalInstances=DELETE)
del mdb.models['Model-1'].parts['Part-1']
a.deleteFeatures(('Part-3-1',))
mdb.models['Model-1'].parts.changeKey(fromName='Part-3', toName='Part-1')

#---------------------------------------------------------------------------
#
a = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Part-1']
a.Instance(name='Part-1-1', part=p, dependent=OFF)
p = mdb.models['Model-1'].parts['Part-2']
a.Instance(name='Part-2-1', part=p, dependent=OFF)
a.translate(instanceList=('Part-2-1', ), vector=(-rve_size[0]/2.0, -rve_size[1]/2.0, -rve_size[2]/2.0))

#---------------------------------------------------------------------------
#
a = mdb.models['Model-1'].rootAssembly
a.InstanceFromBooleanMerge(name='Part-New', instances=(a.instances['Part-1-1'], a.instances['Part-2-1'], ),
    keepIntersections=ON, originalInstances=DELETE, domain=GEOMETRY)
a.deleteFeatures(('Part-New-1',))
del mdb.models['Model-1'].parts['Part-1']
del mdb.models['Model-1'].parts['Part-2']
mdb.models['Model-1'].parts.changeKey(fromName='Part-New', toName='Part-1')
p = mdb.models['Model-1'].parts['Part-1']
a.Instance(name='Part-1-1', part=p, dependent=OFF)

#---------------------------------------------------------------------------
#
p = mdb.models['Model-1'].parts['Part-1']
selcell = p.cells.findAt((((rve_size[0]+extra_t)/2.0, (rve_size[1]+extra_t)/2.0,(rve_size[2]+extra_t)/2.0), ))
p.Set(cells=selcell, name='Set-M-1')
volume1 = p.getMassProperties(regions=p.sets['Set-M-1'].cells)['volume']
#
incCells = p.cells[0:0]
for icell in p.cells:
    if icell.index != selcell[0].index:
        incCells += p.cells[icell.index:icell.index+1]
p.Set(cells=incCells, name='Set-M-2')
volume2 = p.getMassProperties(regions=p.sets['Set-M-2'].cells)['volume']
#
print (f'The volume fraction of particles is: {volume2/(volume2+volume1)}')

#---------------------------------------------------------------------------
#
mdb.saveAs(pathName=cae_name)













		
