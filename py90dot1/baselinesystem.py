# Copyright (c) 2017-2018 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""Remove proposed mechanical system and insert baseline mechanical system"""

import click
from eppy.easyopen import easyopen

def baselinesystem(idf):
    """Remove proposed mechanical system and insert baseline mechanical system"""
    # stub where the actual functions have to be written
    return idf

@click.command()
@click.option('--idf', default=None, help='Path to the proposed IDF file')
@click.option('--idd', help='Path to the IDD file. Optional - will find IDD')
@click.option('--baseline', default=None, help='Path to the generated baseline IDF file. Optional - Will output to stdout')

def baselinesystem_main(idf, idd=None, baseline=None):
    """Remove proposed mechanical system and insert baseline mechanical system"""
    click.echo('IDD file is  %s' % idd)
    click.echo('IDF file is  %s' % idf)
    proposedidf = easyopen(idf, idd)

    # - window reduction happens here
    baselineidf = baselinesystem(proposedidf)
    # - window reduction happens here

    if baseline:
        baselineidf.saveas(baseline)
        click.echo('saved baseline file as  %s' % baseline)
    else:
        baselineidf.printidf()
    
if __name__ == '__main__':
    baselinesystem_main()

    