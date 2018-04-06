# Copyright (c) 2018 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================
"""This module runs all the ASHRAE Appendix-G extions on the idf file to make the baseline idf file"""

import click

from eppy.easyopen import easyopen

@click.command()
@click.option('--idf', help='Path to the proposed IDF file')
@click.option('--idd', default=None, help='Path to the IDD file. Optional - will find IDD')
@click.option('--baseline', default=None, help='Path to the generated baseline IDF file. Optional - Will output to stdout')


def py90dot1(idf, idd, baseline):
    """Generates the ASHRAE baseline IDF file"""
    click.echo('IDD file is  %s' % idd)
    click.echo('IDF file is  %s' % idf)
    proposedidf = easyopen(idf, idd)
    
    # - All the ASHRAE basline functions happen here
    # this is just a stub
    # so do nothing 
    # - All the ASHRAE basline functions happen here

    if baseline:
        proposedidf.saveas(baseline)
        click.echo('saved baseline file as  %s' % baseline)
    else:
        proposedidf.printidf()
    

if __name__ == '__main__':
    py90dot1()

