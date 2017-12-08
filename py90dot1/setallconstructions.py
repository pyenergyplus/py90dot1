# Copyright (c) 2017 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""Set the construction to ASHRAE materials for all surfaces based on climate zone"""

import io

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

    Construction,
        AHSRAE_ConstrRoof,         ! Material layer names follow:
        AHSRAE_Material1;
    """
    IDF = idf.__class__ # sneaky way to avoid `from eppy.modeleditor import IDF`
    materail_constr_idf = IDF(io.StringIO(materail_constr_txt))
    constr = materail_constr_idf.idfobjects['Construction'.upper()][0]
    materials = materail_constr_idf.idfobjects['Material:NoMass'.upper()]
    # wallconstr = constr
    # floorconstr = constr
    # roofconstr = constr
    idf.copyidfobject(constr)
    for material in materials:
        idf.copyidfobject(material)
    roofs = surfacefilter(idf, 'roofs')
    for roof in roofs:
        roof.Construction_Name = constr.Name
    idf.printidf()
