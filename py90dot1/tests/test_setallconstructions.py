# Copyright (c) 2017 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""py.test for setallconstructions.py"""

import io
from py90dot1 import setallconstructions

from eppy.iddcurrent import iddcurrent
from eppy.modeleditor import IDF



# idd is read only once in this test
# if it has already been read from some other test, it will continue with the old reading
iddfhandle = io.StringIO(iddcurrent.iddtxt)
if IDF.getiddname() == None:
    IDF.setiddname(iddfhandle)

class IdfData(object):
    """Holds the idf data for testing"""
    idftxt = """  BuildingSurface:Detailed,
    Floor_Outdoor,  !- Name
    Floor,  !- Surface Type
    Exterior Floor,  !- Construction Name
    EE3070,  !- Zone Name
    Outdoors,  !- Outside Boundary Condition
    ,  !- Outside Boundary Condition Object
    SunExposed,  !- Sun Exposure
    WindExposed,  !- Wind Exposure
    0.0,  !- View Factor to Ground
    4,  !- Number of Vertices
    3.058004874444,  !- Vertex 1 X-coordinate {m}
    4.215508585040,  !- Vertex 1 Y-coordinate {m}
    0.000000000000,  !- Vertex 1 Z-coordinate {m}
    4.075106717408,  !- Vertex 2 X-coordinate {m}
    0.668452927027,  !- Vertex 2 Y-coordinate {m}
    0.000000000000,  !- Vertex 2 Z-coordinate {m}
    3.366677687126,  !- Vertex 3 X-coordinate {m}
    0.465314171456,  !- Vertex 3 Y-coordinate {m}
    0.000000000000,  !- Vertex 3 Z-coordinate {m}
    2.349575844161,  !- Vertex 4 X-coordinate {m}
    4.012369829469,  !- Vertex 4 Y-coordinate {m}
    0.000000000000;  !- Vertex 4 Z-coordinate {m}

  BuildingSurface:Detailed,
    South_Wall,  !- Name
    Wall,  !- Surface Type
    Exterior Wall,  !- Construction Name
    EE3070,  !- Zone Name
    Outdoors,  !- Outside Boundary Condition
    ,  !- Outside Boundary Condition Object
    SunExposed,  !- Sun Exposure
    WindExposed,  !- Wind Exposure
    ,  !- View Factor to Ground
    4,  !- Number of Vertices
    0.691465547705,  !- Vertex 1 X-coordinate {m}
    -0.301790565449,  !- Vertex 1 Y-coordinate {m}
    1.540000000000,  !- Vertex 1 Z-coordinate {m}
    0.691465547705,  !- Vertex 2 X-coordinate {m}
    -0.301790565449,  !- Vertex 2 Y-coordinate {m}
    0.000000000000,  !- Vertex 2 Z-coordinate {m}
    4.075106717408,  !- Vertex 3 X-coordinate {m}
    0.668452927027,  !- Vertex 3 Y-coordinate {m}
    0.000000000000,  !- Vertex 3 Z-coordinate {m}
    4.075106717408,  !- Vertex 4 X-coordinate {m}
    0.668452927027,  !- Vertex 4 Y-coordinate {m}
    1.540000000000;  !- Vertex 4 Z-coordinate {m}

  BuildingSurface:Detailed,
    North_Wall,  !- Name
    Wall,  !- Surface Type
    Exterior Wall,  !- Construction Name
    EE3070,  !- Zone Name
    Outdoors,  !- Outside Boundary Condition
    ,  !- Outside Boundary Condition Object
    SunExposed,  !- Sun Exposure
    WindExposed,  !- Wind Exposure
    ,  !- View Factor to Ground
    4,  !- Number of Vertices
    3.058004874444,  !- Vertex 1 X-coordinate {m}
    4.215508585040,  !- Vertex 1 Y-coordinate {m}
    1.540000000000,  !- Vertex 1 Z-coordinate {m}
    3.058004874444,  !- Vertex 2 X-coordinate {m}
    4.215508585040,  !- Vertex 2 Y-coordinate {m}
    0.000000000000,  !- Vertex 2 Z-coordinate {m}
    -0.325636295259,  !- Vertex 3 X-coordinate {m}
    3.245265092564,  !- Vertex 3 Y-coordinate {m}
    0.000000000000,  !- Vertex 3 Z-coordinate {m}
    -0.325636295259,  !- Vertex 4 X-coordinate {m}
    3.245265092564,  !- Vertex 4 Y-coordinate {m}
    1.540000000000;  !- Vertex 4 Z-coordinate {m}

  BuildingSurface:Detailed,
    Roof_Wall,  !- Name
    Roof,  !- Surface Type
    Exterior Roof,  !- Construction Name
    EE3070,  !- Zone Name
    Outdoors,  !- Outside Boundary Condition
    ,  !- Outside Boundary Condition Object
    SunExposed,  !- Sun Exposure
    WindExposed,  !- Wind Exposure
    ,  !- View Factor to Ground
    4,  !- Number of Vertices
    3.285870677237,  !- Vertex 1 X-coordinate {m}
    3.420846093121,  !- Vertex 1 Y-coordinate {m}
    2.828252313262,  !- Vertex 1 Z-coordinate {m}
    3.058004874444,  !- Vertex 2 X-coordinate {m}
    4.215508585040,  !- Vertex 2 Y-coordinate {m}
    1.540000000000,  !- Vertex 2 Z-coordinate {m}
    -0.325636295259,  !- Vertex 3 X-coordinate {m}
    3.245265092564,  !- Vertex 3 Y-coordinate {m}
    1.540000000000,  !- Vertex 3 Z-coordinate {m}
    -0.097770492466,  !- Vertex 4 X-coordinate {m}
    2.450602600646,  !- Vertex 4 Y-coordinate {m}
    2.828252313262;  !- Vertex 4 Z-coordinate {m}

  BuildingSurface:Detailed,
    East_Wall,  !- Name
    Wall,  !- Surface Type
    Exterior Wall,  !- Construction Name
    EE3070,  !- Zone Name
    Outdoors,  !- Outside Boundary Condition
    ,  !- Outside Boundary Condition Object
    SunExposed,  !- Sun Exposure
    WindExposed,  !- Wind Exposure
    ,  !- View Factor to Ground
    5,  !- Number of Vertices
    4.075106717408,  !- Vertex 1 X-coordinate {m}
    0.668452927027,  !- Vertex 1 Y-coordinate {m}
    1.540000000000,  !- Vertex 1 Z-coordinate {m}
    4.075106717408,  !- Vertex 2 X-coordinate {m}
    0.668452927027,  !- Vertex 2 Y-coordinate {m}
    0.000000000000,  !- Vertex 2 Z-coordinate {m}
    3.058004874444,  !- Vertex 3 X-coordinate {m}
    4.215508585040,  !- Vertex 3 Y-coordinate {m}
    0.000000000000,  !- Vertex 3 Z-coordinate {m}
    3.058004874444,  !- Vertex 4 X-coordinate {m}
    4.215508585040,  !- Vertex 4 Y-coordinate {m}
    1.540000000000,  !- Vertex 4 Z-coordinate {m}
    3.285870677237,  !- Vertex 5 X-coordinate {m}
    3.420846093121,  !- Vertex 5 Y-coordinate {m}
    2.828252313262;  !- Vertex 5 Z-coordinate {m}

  BuildingSurface:Detailed,
    West_Wall,  !- Name
    Wall,  !- Surface Type
    Exterior Wall,  !- Construction Name
    EE3070,  !- Zone Name
    Outdoors,  !- Outside Boundary Condition
    ,  !- Outside Boundary Condition Object
    SunExposed,  !- Sun Exposure
    WindExposed,  !- Wind Exposure
    ,  !- View Factor to Ground
    5,  !- Number of Vertices
    -0.097770492466,  !- Vertex 1 X-coordinate {m}
    2.450602600646,  !- Vertex 1 Y-coordinate {m}
    2.828252313262,  !- Vertex 1 Z-coordinate {m}
    -0.325636295259,  !- Vertex 2 X-coordinate {m}
    3.245265092564,  !- Vertex 2 Y-coordinate {m}
    1.540000000000,  !- Vertex 2 Z-coordinate {m}
    -0.325636295259,  !- Vertex 3 X-coordinate {m}
    3.245265092564,  !- Vertex 3 Y-coordinate {m}
    0.000000000000,  !- Vertex 3 Z-coordinate {m}
    0.691465547705,  !- Vertex 4 X-coordinate {m}
    -0.301790565449,  !- Vertex 4 Y-coordinate {m}
    0.000000000000,  !- Vertex 4 Z-coordinate {m}
    0.691465547705,  !- Vertex 5 X-coordinate {m}
    -0.301790565449,  !- Vertex 5 Y-coordinate {m}
    1.540000000000;  !- Vertex 5 Z-coordinate {m}

  BuildingSurface:Detailed,
    Roof_Roof,  !- Name
    Roof,  !- Surface Type
    Exterior Roof,  !- Construction Name
    EE3070,  !- Zone Name
    Outdoors,  !- Outside Boundary Condition
    ,  !- Outside Boundary Condition Object
    SunExposed,  !- Sun Exposure
    WindExposed,  !- Wind Exposure
    ,  !- View Factor to Ground
    4,  !- Number of Vertices
    -0.097770492466,  !- Vertex 1 X-coordinate {m}
    2.450602600646,  !- Vertex 1 Y-coordinate {m}
    2.828252313262,  !- Vertex 1 Z-coordinate {m}
    0.691465547705,  !- Vertex 2 X-coordinate {m}
    -0.301790565449,  !- Vertex 2 Y-coordinate {m}
    1.540000000000,  !- Vertex 2 Z-coordinate {m}
    4.075106717408,  !- Vertex 3 X-coordinate {m}
    0.668452927027,  !- Vertex 3 Y-coordinate {m}
    1.540000000000,  !- Vertex 3 Z-coordinate {m}
    3.285870677237,  !- Vertex 4 X-coordinate {m}
    3.420846093121,  !- Vertex 4 Y-coordinate {m}
    2.828252313262;  !- Vertex 4 Z-coordinate {m}

  BuildingSurface:Detailed,
    Floor_Ground,  !- Name
    Floor,  !- Surface Type
    Exterior Floor,  !- Construction Name
    EE3070,  !- Zone Name
    Ground,  !- Outside Boundary Condition
    ,  !- Outside Boundary Condition Object
    NoSun,  !- Sun Exposure
    NoWind,  !- Wind Exposure
    0.0,  !- View Factor to Ground
    4,  !- Number of Vertices
    2.349575844161,  !- Vertex 1 X-coordinate {m}
    4.012369829469,  !- Vertex 1 Y-coordinate {m}
    0.000000000000,  !- Vertex 1 Z-coordinate {m}
    3.366677687126,  !- Vertex 2 X-coordinate {m}
    0.465314171456,  !- Vertex 2 Y-coordinate {m}
    0.000000000000,  !- Vertex 2 Z-coordinate {m}
    0.691465547705,  !- Vertex 3 X-coordinate {m}
    -0.301790565449,  !- Vertex 3 Y-coordinate {m}
    0.000000000000,  !- Vertex 3 Z-coordinate {m}
    -0.325636295259,  !- Vertex 4 X-coordinate {m}
    3.245265092564,  !- Vertex 4 Y-coordinate {m}
    0.000000000000;  !- Vertex 4 Z-coordinate {m}
"""


def test_surfacefilter():
    """py.test for surfacefilter"""
    idftxt = IdfData.idftxt
    wallnames = set(['South_Wall', 'North_Wall', 'Roof_Wall', 'East_Wall', 'West_Wall'])
    floornames = set(['Floor_Outdoor'])
    roofnames = set(['Roof_Roof'])
    fhandle = io.StringIO(idftxt)
    idf = IDF(fhandle)

    result = setallconstructions.surfacefilter(idf, 'walls')
    resultnames = set([surface.Name for surface in result])
    assert resultnames == wallnames

    result = setallconstructions.surfacefilter(idf, 'floors')
    resultnames = set([surface.Name for surface in result])
    assert resultnames == floornames

    result = setallconstructions.surfacefilter(idf, 'roofs')
    resultnames = set([surface.Name for surface in result])
    assert resultnames == roofnames

    result = setallconstructions.surfacefilter(idf, 'all')
    resultnames = {key:set([val.Name for val in value]) for key, value in result.items()}
    assert resultnames == dict(roofs=roofnames, walls=wallnames, floors=floornames)

def test_setconstruction():
    """py.test for setconstruction"""
    idftxt = """  BuildingSurface:Detailed,
        Roof_Roof,  !- Name
        Roof,  !- Surface Type
        Exterior Roof,  !- Construction Name
        EE3070,  !- Zone Name
        Outdoors,  !- Outside Boundary Condition
        ,  !- Outside Boundary Condition Object
        SunExposed,  !- Sun Exposure
        WindExposed,  !- Wind Exposure
        ,  !- View Factor to Ground
        4,  !- Number of Vertices
        -0.097770492466,  !- Vertex 1 X-coordinate {m}
        2.450602600646,  !- Vertex 1 Y-coordinate {m}
        2.828252313262,  !- Vertex 1 Z-coordinate {m}
        0.691465547705,  !- Vertex 2 X-coordinate {m}
        -0.301790565449,  !- Vertex 2 Y-coordinate {m}
        1.540000000000,  !- Vertex 2 Z-coordinate {m}
        4.075106717408,  !- Vertex 3 X-coordinate {m}
        0.668452927027,  !- Vertex 3 Y-coordinate {m}
        1.540000000000,  !- Vertex 3 Z-coordinate {m}
        3.285870677237,  !- Vertex 4 X-coordinate {m}
        3.420846093121,  !- Vertex 4 Y-coordinate {m}
        2.828252313262;  !- Vertex 4 Z-coordinate {m}
    """
    idftxt = IdfData.idftxt
    fhandle = io.StringIO(idftxt)
    idf = IDF(fhandle)
    result = setallconstructions.setconstruction(idf, 'sampleclimatezone')
    expectedconstr = ['AHSRAE_ConstrFloor', 'AHSRAE_ConstrWall',
    'AHSRAE_ConstrWall', 'AHSRAE_ConstrWall', 'AHSRAE_ConstrWall',
    'AHSRAE_ConstrWall', 'AHSRAE_ConstrRoof', 'Exterior Floor']
    surfaces = idf.idfobjects['BuildingSurface:Detailed'.upper()]
    result_constrs = [surface.Construction_Name for surface in surfaces]
    assert result_constrs == expectedconstr
