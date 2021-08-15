# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.13-1 replay file
# Internal Version: 2013_05_16-07.58.56 126354
# Run by MMLAB_64 on Mon Feb 03 15:23:16 2020
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
#: Abaqus Error: 
#: This error may have occurred due to a change to the Abaqus Scripting
#: Interface. Please see the Abaqus Scripting Manual for the details of
#: these changes. Also see the "Example environment files" section of 
#: the Abaqus Site Guide for up-to-date examples of common tasks in the
#: environment file.
#: Execution of "onCaeGraphicsStartup()" in the site directory failed.
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=316.991119384766, 
    height=159.808334350586)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('Truss_prob.cae')
#: The model database "G:\Jalaj\Truss\Truss_prob.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Model-1'].parts['Truss']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=52.4305, 
    farPlane=60.7066, width=62.2927, height=28.6141, cameraPosition=(3.97535, 
    6.25393, 56.5685), cameraTarget=(3.97535, 6.25393, 0))
p = mdb.models['Model-1'].parts['Truss']
s = p.features['Wire-1'].sketch
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s)
s1 = mdb.models['Model-1'].sketches['__edit__']
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s1, upToFeature=p.features['Wire-1'], 
    filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(width=55.3538, height=25.4992, 
    cameraPosition=(3.30084, 5.19262, 62.0358), cameraTarget=(3.30084, 5.19262, 
    0))
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__edit__']
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
session.graphicsOptions.setValues(backgroundStyle=GRADIENT)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50.1874, 
    farPlane=62.9497, width=84.8785, height=38.9889, cameraPosition=(27.1669, 
    8.75998, 56.5685), cameraTarget=(27.1669, 8.75998, 0))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['Truss']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51.8854, 
    farPlane=61.2517, width=62.1297, height=28.6141, cameraPosition=(3.38796, 
    7.07053, 56.5685), cameraTarget=(3.38796, 7.07053, 0))
p = mdb.models['Model-1'].parts['Truss']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Job Job-1: Analysis Input File Processor completed successfully.
#: Job Job-1: Abaqus/Standard completed successfully.
#: Job Job-1 completed successfully. 
o3 = session.openOdb(name='G:/Jalaj/Truss/Job-1.odb')
#: Model: G:/Jalaj/Truss/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       1
#: Number of Node Sets:          1
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    deformationScaling=UNIFORM, uniformScaleFactor=1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.1745, 
    farPlane=98.8255, width=62.2926, height=28.6141, cameraPosition=(7.11124, 
    4.79775, 80), cameraTarget=(7.11124, 4.79775, 0))
p = mdb.models['Model-1'].parts['Truss']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=52.9026, 
    farPlane=60.2345, width=55.0418, height=25.3498, cameraPosition=(13.0983, 
    4.67551, 56.5685), cameraTarget=(13.0983, 4.67551, 0))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
odb = session.odbs['G:/Jalaj/Truss/Job-1.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
p = mdb.models['Model-1'].parts['Truss']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['Truss']
p.deleteMesh()
p = mdb.models['Model-1'].parts['Truss']
p.seedPart(size=1.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Truss']
p.seedPart(size=1.4, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Truss']
p.generateMesh()
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=ON, geometricRestrictions=ON, stopConditions=ON)
odb = session.odbs['G:/Jalaj/Truss/Job-1.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['Truss']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['Truss']
p.deleteMesh()
p = mdb.models['Model-1'].parts['Truss']
p.seedPart(size=0.5, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Truss']
p.generateMesh()
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Job Job-1: Analysis Input File Processor completed successfully.
#: Error in job Job-1: Too many attempts made for this increment
#: Job Job-1: Abaqus/Standard aborted due to errors.
#: Error in job Job-1: Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.
#: Job Job-1 aborted due to errors.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(name='G:/Jalaj/Truss/Job-1.odb')
#: Model: G:/Jalaj/Truss/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       1
#: Number of Node Sets:          1
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.75279e+006, 
    farPlane=9.22461e+006, width=5.48128e+006, height=2.51782e+006, 
    cameraPosition=(-373385, 367754, 7.4887e+006), cameraTarget=(-373385, 
    367754, 0))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['Truss']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
odb = session.odbs['G:/Jalaj/Truss/Job-1.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['Truss']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, loads=ON, 
    bcs=ON, predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['Truss']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
odb = session.odbs['G:/Jalaj/Truss/Job-1.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
p = mdb.models['Model-1'].parts['Truss']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['Truss']
p.deleteMesh()
p = mdb.models['Model-1'].parts['Truss']
p.seedPart(size=1.4, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Truss']
p.generateMesh()
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Job Job-1: Analysis Input File Processor completed successfully.
#: Job Job-1: Abaqus/Standard completed successfully.
#: Job Job-1 completed successfully. 
o3 = session.openOdb(name='G:/Jalaj/Truss/Job-1.odb')
#: Model: G:/Jalaj/Truss/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       1
#: Number of Node Sets:          1
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
p = mdb.models['Model-1'].parts['Truss']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['Truss']
p.deleteMesh()
p = mdb.models['Model-1'].parts['Truss']
p.seedPart(size=2.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Truss']
p.generateMesh()
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
#: Job Job-1: Analysis Input File Processor completed successfully.
#: Error in job Job-1: Time increment required is less than the minimum specified
#: Job Job-1: Abaqus/Standard aborted due to errors.
#: Error in job Job-1: Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.
#: Job Job-1 aborted due to errors.
o3 = session.openOdb(name='G:/Jalaj/Truss/Job-1.odb')
#: Model: G:/Jalaj/Truss/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       1
#: Number of Node Sets:          1
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=464614, 
    farPlane=793886, width=803860, height=369253, cameraPosition=(-12001.9, 
    46411.6, 629250), cameraTarget=(-12001.9, 46411.6, 0))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=439973, 
    farPlane=818527, width=1.17479e+006, height=539638, cameraPosition=(
    -104562, -4708.67, 629250), cameraTarget=(-104562, -4708.67, 0))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_UNDEF, CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_UNDEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.7198, 
    farPlane=98.2802, width=55.0418, height=25.2834, cameraPosition=(2.58093, 
    5.68115, 80), cameraTarget=(2.58093, 5.68115, 0))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].steps['Loading'].setValues(initialInc=1.0)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Job Job-1: Analysis Input File Processor completed successfully.
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['Truss']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
#: Job Job-1: Abaqus/Standard completed successfully.
#: Job Job-1 completed successfully. 
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(name='G:/Jalaj/Truss/Job-1.odb')
#: Model: G:/Jalaj/Truss/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       1
#: Number of Node Sets:          1
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_UNDEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_UNDEF, ))
o3 = session.openOdb(name='G:/Jalaj/Truss/Job-1.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['Truss']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
odb = session.odbs['G:/Jalaj/Truss/Job-1.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
odb = session.odbs['G:/Jalaj/Truss/Job-1.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.4767, 
    farPlane=100.523, width=96.0598, height=44.125, cameraPosition=(18.3173, 
    0.144829, 80), cameraTarget=(18.3173, 0.144829, 0))
p = mdb.models['Model-1'].parts['Truss']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['Truss']
p.deleteMesh()
p = mdb.models['Model-1'].parts['Truss']
p.seedPart(size=1.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Truss']
p.generateMesh()
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Job Job-1: Analysis Input File Processor completed successfully.
#: Job Job-1: Abaqus/Standard completed successfully.
#: Job Job-1 completed successfully. 
o3 = session.openOdb(name='G:/Jalaj/Truss/Job-1.odb')
#: Model: G:/Jalaj/Truss/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       1
#: Number of Node Sets:          1
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
odb = session.odbs['G:/Jalaj/Truss/Job-1.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_UNDEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=60.2195, 
    farPlane=99.7805, width=84.8785, height=38.9889, cameraPosition=(14.3321, 
    -0.607691, 80), cameraTarget=(14.3321, -0.607691, 0))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=52.4305, 
    farPlane=60.7066, width=62.2927, height=28.6141, cameraPosition=(4.17084, 
    5.80884, 56.5685), cameraTarget=(4.17084, 5.80884, 0))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Loading')
