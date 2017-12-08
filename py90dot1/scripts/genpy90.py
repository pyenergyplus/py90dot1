"""generate a py90dot1 file"""

from eppy.modeleditor import IDF
# import py90dot1.setallconstructions as setallconstructions
import py90dot1
from py90dot1 import setallconstructions

iddfile = "/Applications/EnergyPlus-8-8-0/Energy+.idd"

if IDF.getiddname() == None:
    IDF.setiddname(iddfile)
    
idffile = "/Users/santosh/Documents/GitHub/py90dot1/py90dot1/scripts/1ZoneEvapCooler.idf"    
    
idf = IDF(idffile)

# ================

idf = setallconstructions.setconstruction(idf, 'climatezone1')
idf.saveas('ashrae.idf', lineendings='windows')







