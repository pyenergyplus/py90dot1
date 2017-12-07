# Copyright (c) 2017 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""Set the construction to ASHRAE materials for all surfaces based on climate zone"""


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
