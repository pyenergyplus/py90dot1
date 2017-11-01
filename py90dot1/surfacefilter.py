"""filters that will filter out the walls, roof, floor, windows"""

import sys

from eppy import modeleditor
from eppy.modeleditor import IDF
iddfile = "./py90dot1/resources/iddfiles/Energy_V8_7.idd"
fname = "./py90dot1/resources/idffiles/5ZoneAirCooledWithCoupledInGradeSlab.idf"
IDF.setiddname(iddfile)
idf = IDF(fname)
allsurfaces = idf.idfobjects["BUILDINGSURFACE:DETAILED"]
surfaces = [surface for surface in allsurfaces 
    if surface.Outside_Boundary_Condition.upper() == 'Outdoors'.upper()]

# roof tilt < 45
# wall tilt >=45 and <= 135
# floor tilt > 135

roofs = [surface for surface in surfaces if surface.tilt < 45]
walls = [surface for surface in surfaces 
    if surface.tilt >= 45 and surface.tilt <= 135]
floors = [surface for surface in surfaces if surface.tilt > 135]

[surface.Outside_Boundary_Condition for surface in allsurfaces 
    if surface.Outside_Boundary_Condition.upper() == 'outdoor'.upper()]
    
[(surface.tilt, surface.Outside_Boundary_Condition) for surface in allsurfaces
    if surface.tilt == 180]    
