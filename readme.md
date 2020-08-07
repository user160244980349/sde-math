# Readme #

- - - -
## Dependencies ##
* [SymPy](https://docs.sympy.org/latest/index.html)
* [numpy](https://numpy.org/)
* [plotly](https://plotly.com/python/)
* [PyQt5](https://pypi.org/project/PyQt5/)

- - - -
## After clone ##
`pip install -r requirements.txt`

- - - -
## Run ##
* main -- GUI application
* main_linear -- console linear modeling
* main_nonlinear -- console nonlinear modeling
* main_txt_store_c -- console store C coefficients in txt
* main_db_store_c -- console store C coefficients in db

- - - -
## TODO ##
- [x] Generation of C coefficients
- [x] Bunch of linear stuff
- [x] Euler method
    - [x] Euler with trajectories
- [x] Milstein method
    - [x] Io(i1)
    - [x] Ioo(i1, i2, q)
    - [x] G operators
- [x] Database routines
    - [x] Database initialization
    - [x] Database for C coefficients
    - [ ] C coefficients preload
- [x] C operator
    - [x] C operator with loading C coefficient
    - [x] Uploading coefficients that not produces in database
- [x] Strong Taylor 1.5 method
    - [x] L operator
    - [x] Recursive G
    - [x] Ii(i1) {5.7}
    - [x] Iooo(i1, i2, i3) {5.16} without limit
    - [x] Iooo(i, i, i) after {5.16}
    - [x] {5.17} {5.18} in Iooo
- [x] (impossible, needs to be vectorized) Trajectory as substitution arg
- [x] Beautify G2 output
- [x] is_symbol check is not working
- [ ] Clean up
- [ ] Comments actualization
- [ ] Context for formulas to beat redundancy
- [ ] Precision calculation with q
- [ ] Strong Taylor 2.0 method
    - [x] Recursive L
    - [ ] Referenced integrals
- [ ] Stratanovich equasions
    - [ ] Subformulas
- [ ] GUI
    - [ ] Greek alphabet
    - [ ] Latex output
