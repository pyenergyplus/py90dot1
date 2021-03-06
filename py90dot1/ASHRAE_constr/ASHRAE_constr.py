# Copyright (c) 2017-2018 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""All the ASHRAE90.1-2010 Constructions  are here in idf text format"""

def constr_importer(climatezone):
    """returns the ASHRAE consttruction in idf text for clime zone"""
    if climatezone == 'sampleclimatezone':
        AshraeConstr = AshraeSampleConstr
    elif climatezone == 'climatezone1':
        AshraeConstr = AshraeZone1Constr
    return AshraeConstr.idftxt


class AshraeSampleConstr(object):
    """idf text for ASHRAE Zone 1 Construction and Materials"""
    idftxt = """
    WindowMaterial:SimpleGlazingSystem,
        AHSRAE_Window_Material,       !- Name
        2.6,                     !- U-Factor {W/m2-K}
        0.76,                    !- Solar Heat Gain Coefficient
        0.63;                    !- Visible Transmittance

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
        AHSRAE_ConstrWindow,         ! Material layer names follow:
        AHSRAE_Zone1_Window_Material;

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

class AshraeZone1Constr(object):
    """idf text for ASHRAE Zone 1 Construction and Materials"""
    idftxt = """
    WindowMaterial:SimpleGlazingSystem,
        AHSRAE_Zone1_Window_Material,       !- Name
        2.6,                     !- U-Factor {W/m2-K}
        0.76,                    !- Solar Heat Gain Coefficient
        0.63;                    !- Visible Transmittance

    Material:NoMass,
        AHSRAE_Zone1_Roof_Material,        ! Material Name
        Rough,           ! Roughness
        0.357731    ,    ! Resistance {M**2K/W} - 0.63 in IP-units
        0.9000000    ,   ! Thermal Absorptance
        0.7500000    ,   ! Solar Absorptance
        0.7500000    ;   ! Visible Absorptance

    Material:NoMass,
        AHSRAE_Zone1_Wall_Material,        ! Material Name
        Rough,           ! Roughness
        0.704105    ,    ! Resistance {M**2K/W} - 0.124 in IP-units
        0.9000000    ,   ! Thermal Absorptance
        0.7500000    ,   ! Solar Absorptance
        0.7500000    ;   ! Visible Absorptance

    Material:NoMass,
        AHSRAE_Zone1_Floor_Material,        ! Material Name
        Rough,           ! Roughness
        1.987392    ,    ! Resistance {M**2K/W} - 0.35 in IP-units
        0.9000000    ,   ! Thermal Absorptance
        0.7500000    ,   ! Solar Absorptance
        0.7500000    ;   ! Visible Absorptance

    Construction,
        AHSRAE_Zone1_ConstrWindow,         ! Material layer names follow:
        AHSRAE_Zone1_Window_Material;

    Construction,
        AHSRAE_Zone1_ConstrRoof,         ! Material layer names follow:
        AHSRAE_Zone1_Roof_Material;

    Construction,
        AHSRAE_Zone1_ConstrWall,         ! Material layer names follow:
        AHSRAE_Zone1_Wall_Material;

    Construction,
        AHSRAE_Zone1_ConstrFloor,         ! Material layer names follow:
        AHSRAE_Zone1_Floor_Material;

    """

