The software-structure built on the process described in the document ./docs/appendix_g_process.md

1. `setallconstructions()` Set the construction to ASHRAE materials for all surfaces based on climate zone
  1. `surfacefilter()` **a.** Filter surfaces as roof, wall, floor, window
  - `setconstruction()` Put in appropriate baseline construction for roof, wall, floor, window.
    - needs step **a.**
2. `windowresizer()` Resize the windows as per Appendix-G rules
3. `shaderemover()` Remove all the exterior shades
4. `selfshadeoff()` Turn off self shading in the building
5. `systemselector()` **A** Select the baseline mechanical system based on *Table G3.1.1-3*
6. `baselinesystem()` **B** Remove proposed mechanical system and insert baseline mechanical system
  - needs step **A**
  - `removesystem()` Remove mechanical system
  - `insertsystem()` Insert baseline mechanical system
- `baselinerunner()` **C** do a sizing run of baseline model
  - needs all the steps before **A**
  - needs step **B**
- `extractsizing()` **D** extract sizes from results of sizing run
  - needs step **C**
- `insertsizing()` Insert the results of sizing run into model
  - needs step **D**
