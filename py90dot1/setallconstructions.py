# Copyright (c) 2017 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""Set the construction to ASHRAE materials for all surfaces based on climate zone"""

import io
import itertools

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

def setconstruction(idf, climatezone):
    """Put in appropriate baseline construction for roof, wall, floor, window."""
    materail_constr_txt = """
    Material:NoMass,
        AHSRAE_Material1,        ! Material Name
        Rough,           ! Roughness
        2.290965    ,    ! Resistance {M**2K/W}
        0.9000000    ,   ! Thermal Absorptance
        0.7500000    ,   ! Solar Absorptance
        0.7500000    ;   ! Visible Absorptance

    Material:NoMass,
        AHSRAE_Material2,        ! Material Name
        Rough,           ! Roughness
        2.290965    ,    ! Resistance {M**2K/W}
        0.9000000    ,   ! Thermal Absorptance
        0.7500000    ,   ! Solar Absorptance
        0.7500000    ;   ! Visible Absorptance

    Material:NoMass,
        AHSRAE_Material3,        ! Material Name
        Rough,           ! Roughness
        2.290965    ,    ! Resistance {M**2K/W}
        0.9000000    ,   ! Thermal Absorptance
        0.7500000    ,   ! Solar Absorptance
        0.7500000    ;   ! Visible Absorptance

    Construction,
        AHSRAE_ConstrRoof,         ! Material layer names follow:
        AHSRAE_Material1;

    Construction,
        AHSRAE_ConstrWall,         ! Material layer names follow:
        AHSRAE_Material1;

    Construction,
        AHSRAE_ConstrFloor,         ! Material layer names follow:
        AHSRAE_Material1;

    """
    IDF = idf.__class__ # sneaky way to avoid `from eppy.modeleditor import IDF`
    materail_constr_idf = IDF(io.StringIO(materail_constr_txt))

    # --- maybe add this to eppy as getidfobjectlist(idf) ---
    idfobjects = materail_constr_idf.idfobjects
    idfobjlst = [idfobjects[key] for key in idfobjects if idfobjects[key]]
    idfobjlst = itertools.chain.from_iterable(idfobjlst)
    idfobjlst = list(idfobjlst)
    # --- maybe add this to eppy as getidfobjectlist(idf) ---

    # --- maybe add this to eppy as copyidfintoidf(toidf, fromidf) ---
    for idfobj in idfobjlst:
        idf.copyidfobject(idfobj)
    # --- maybe add this to eppy as copyidfintoidf(toidf, fromidf) ---

    constructions = idf.idfobjects['CONSTRUCTION']
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
    return idf
