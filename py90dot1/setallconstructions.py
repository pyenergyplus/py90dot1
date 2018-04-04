# Copyright (c) 2017 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""Set the construction to ASHRAE materials for all surfaces based on climate zone"""

import io
import itertools
from eppy import idf_helpers

def surfacefilter(idf, filtertype='all'):
    """docstring for surfacefilter"""
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
    if filtertype == 'all':
        return dict(roofs=roofs, walls=walls, floors=floors)
    elif filtertype == 'roofs':
        return roofs
    elif filtertype == 'walls':
        return walls
    elif filtertype == 'floors':
        return floors

def glazingfilter(idf, filtertype='all'):
    """docstring for surfacefilter"""
    allwindows = idf.idfobjects["FENESTRATIONSURFACE:DETAILED"]
    return allwindows

def constr_importer(climatezone):
    """returns the ASHRAE consttruction in idf text for clime zone"""
    if climatezone == 'sampleclimatezone':
        from py90dot1.ASHRAE_constr.ASHRAE_constr import AshraeSampleConstr as AshraeConstr
    elif climatezone == 'climatezone1':
        from py90dot1.ASHRAE_constr.ASHRAE_constr import AshraeZone1Constr as AshraeConstr
    return AshraeConstr.idftxt

def setconstruction(idf, climatezone):
    """Put in appropriate baseline construction for roof, wall, floor, window."""
    materail_constr_txt = constr_importer(climatezone)
    IDF = idf.__class__ # sneaky way to avoid `from eppy.modeleditor import IDF`
    materail_constr_idf = IDF(io.StringIO(materail_constr_txt))

    idf_helpers.copyidfintoidf(idf, materail_constr_idf)
    constructions = idf.idfobjects['CONSTRUCTION']
    windowconstr = constructions[-4]
    roofconstr = constructions[-3]
    wallconstr = constructions[-2]
    floorconstr = constructions[-1] # the order is hard coded

    filteredsurfaces = surfacefilter(idf)
    roofs = filteredsurfaces['roofs']
    walls = filteredsurfaces['walls']
    floors = filteredsurfaces['floors']

    for roof in roofs:
        roof.Construction_Name = roofconstr.Name
    for wall in walls:
        wall.Construction_Name = wallconstr.Name
    for floor in floors:
        floor.Construction_Name = floorconstr.Name

    windows = glazingfilter(idf)
    for window in windows:
    	window.Construction_Name = windowconstr.Name
    return idf
