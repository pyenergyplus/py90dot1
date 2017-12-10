### Preamble
py90dot1 will take any take any proposed Energyplus idf text file and generate a baseline ASHRAE90.1 Energyplus idf text file.

To convert a proposed model into a baseline model, the original model has to be transformed through a series of steps. Some of these steps can happen in parallel (meaning, they can happen in any sequence) and other steps occur in a particular sequence.

This is a draft of the steps needed

The software-structure built on the process described in the document ./docs/appendix_g_process.md

1.  Set the construction to ASHRAE materials for all surfaces based on climate zone
    1. **a.** Filter surfaces as roof, wall, floor, window
    - Put in appropriate baseline construction for roof, wall, floor, window.
        - needs step **a.**
2. Resize the windows as per Appendix-G rules
3. Remove all the exterior shades
4. Turn off self shading in the building
5. **A** Select the baseline mechanical system based on *Table G3.1.1-3*
6. **B** remove proposed mechanical system and insert baseline mechanical system
    - needs step **A**
    - Remove mechanical system
    - Insert baseline mechanical system

Going through all the above steps will result in a baseline model.

Changes Baseline as described in the Appendix-G TABLE G3.1
*Draft version with some simplifications for initial code*
1. Design Model: *No changes in Baseline Model*
2. Additions and Alterations: *No changes in Baseline Model*
3. Space Use Classification: *No changes in Baseline Model*
4. Schedules: *No changes in Baseline Model*
5. Building Envelope
    a. Orientations: All 4 orientations
    b. Opaque Assemblies: Put in the assembly for the climate zone
6. Lighting: Put in Ashrae Lighting Values
7. Thermal Blocks-HVAC Zones Designed: *No changes in Baseline Model*
8. Thermal Blocks-HVAC Zones Not Designed: *No changes in Baseline Model*
9. Thermal Blocks-MultiFamily Residential Buildings: *No changes in Baseline Model*
10. HVAC Systems: Use System selected from Table G3.1.1
11. Service Hot water: needs research
12. Receptacle and other loads: *No changes in Baseline Model*
13. Modeling limitations to Simulation Program: *No changes in Baseline Model*
14. Exterior conditions: *No changes in Baseline Model*
