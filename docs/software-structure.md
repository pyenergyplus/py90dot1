### Preamble
py90dot1 will take any take any proposed Energyplus idf text file and generate a baseline ASHRAE90.1 Energyplus idf text file.

To convert a proposed model into a baseline model, the original model has to be transformed through a series of steps. Some of these steps can happen in parallel (meaning, they can happen in any sequence) and other steps occur in a particular sequence.

This is a draft of the steps needed

1. set the construction to ASHRAE materials for all surfaces based on climate zone
  1. filter surfaces as roof, wall, floor, window
  - put in appropriate baseline construction for roof, wall, floor, window.
2. resize the windows as per Appendix-G rules
3. remove all the exterior shades
4. turn off self shading in the building
5. **A** Select the baseline mechanical system based on *Table G3.1.1-3*
6. **B** remove existing mechanical system and insert baseline mechanical system
  - needs step **A**
- **C** do a sizing run
  - needs all the steps before **A**
  - needs step **B**
- insert the results of sizing run into model
  - needs step **C**

Going through all the above steps will result in a baseline model.  
