# Known Limitations

These are documented as the coding proceeds. We doing a quick pass at writing the software. Compromises are made as we write it, and the compromises are documented here. At a later date they will be fixed

 #### 2017-12-07

 - ASHRAE constructions are only put into surfaces that are `BUILDINGSURFACE:DETAILED`
 - other type of surfaces are ignored
 - Surfaces that have `Outside Boundary Condition = Ground` are ignored. This question has been raised in `./docs/ashrae_questions.md`
