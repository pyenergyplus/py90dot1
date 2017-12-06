## Collective Code Construction Contract

https://rfc.zeromq.org/spec:42/C4/

Steps for making updates to the software, based on C4 document above:

- *User*:
  - Opens an issue in issue tracker, describing problem (called issue #n)
- *Contributer*:
  - forks the repository
  - makes changes
  - commits with appropriate commit following message
    - fixed issue #n (*on first line*)
      - Problem: describe Problem
      - Solution: describe Solution
  - Make a pull request
- *Maintianer*:
  - Merge pull request into master
- *User*:
  - Closes issue #n in issue tracker
