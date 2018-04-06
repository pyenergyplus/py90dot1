# Copyright (c) 2017-2018 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""Set the construction to ASHRAE materials for all surfaces based on climate zone"""

import io
import itertools
import click

from eppy import modeleditor
from eppy.modeleditor import IDF
from eppy.easyopen import easyopen
from eppy import idf_helpers
try:
    from py90dot1.ASHRAE_constr import ASHRAE_constr
except ImportError as e:
    from ASHRAE_constr import ASHRAE_constr


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

def setconstruction(idf, climatezone):
    """Put in appropriate baseline construction for roof, wall, floor, window."""
    materail_constr_txt = ASHRAE_constr.constr_importer(climatezone)
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
    
@click.command()
@click.option('--idd', default=None, help='path to the IDD file. Optional - will find IDD')
@click.option('--idf', default=None, help='path to the proposed IDF file')
@click.option('--climatezone', default=1, help='ASHRAE climate zone')
@click.option('--baseline', default=None, help='path to the generated baseline IDF file')
def setconstruction_main(idd, idf, climatezone, baseline):
    """Set the ASHRAE constructions for the envelope"""
    click.echo('IDD file is  %s' % idd)
    click.echo('IDF file is  %s' % idf)
    click.echo('Climate Zone is  %s' % climatezone)
    climatezone = "climatezone{}".format(climatezone)
    idffname = idf # we are calling the eppy idf object as 'idf'. Avoids name clash
    
    proposedidf = easyopen(idffname, idd)
    
    # - setting of ASHRAE constructions happens here
    baselineidf = setconstruction(proposedidf, climatezone)
    # - setting of ASHRAE constructions happens here

    if baseline:
        proposedidf.saveas(baseline)
        click.echo('saved baseline file as  %s' % baseline)
    else:
        proposedidf.printidf()

if __name__ == '__main__':
    setconstruction_main()

