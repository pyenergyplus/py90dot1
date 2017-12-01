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
- **C** do a sizing run of baseline model
  - needs all the steps before **A**
  - needs step **B**
- **D** extract sizes from results of sizing run
  - needs step **C**
- Insert the results of sizing run into model
  - needs step **D**

Going through all the above steps will result in a baseline model.  
