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
* `main.py``` -- GUI application
* `main_linear.py` -- console linear modeling
* `main_nonlinear.py` -- console nonlinear modeling
* `main_txt_store_c.py` -- console store C coefficients in txt
* `main_db_store_c.py` -- console store C coefficients in db

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
    - [x] C coefficients preload
    - [x] Addition with coefficients weights
- [x] C operator
    - [x] C operator with loading C coefficient
    - [x] Uploading coefficients that not produces in database
- [x] Strong Taylor-Ito 1.5 method
    - [x] L operator
    - [x] Recursive G
    - [x] Ii(i1) {5.7}
    - [x] Iooo(i1, i2, i3) {5.16} without limit
    - [x] Iooo(i, i, i) after {5.16}
    - [x] {5.17} {5.18} in Iooo
- [x] Trajectory as substitution argument (thrown away) 
- [x] Beautify G2 output
- [x] `is_symbol` check is not working (thrown away) 
- [x] Clean up
- [x] Comments actualization
- [ ] Update tests
- [x] Context for formulas to beat redundancy (thrown away) 
- [x] Strong Taylor-Ito 2.0 method
    - [x] Recursive L
    - [x] Referenced integrals
- [ ] Strong Taylor-Ito 2.5 method
    - [x] C coeficients with weights
    - [ ] Referenced integrals
- [ ] Strong Taylor-Ito 3.0 method
    - [ ] Referenced integrals
- [ ] Stratanovich A and L, Integrals "J"
- [ ] Strong Taylor-Stratonovich 1.0 method
    - [ ] Referenced integrals
- [ ] Strong Taylor-Stratonovich 1.5 method
    - [ ] Referenced integrals
- [ ] Strong Taylor-Stratonovich 2.0 method
    - [ ] Referenced integrals
- [ ] Strong Taylor-Stratonovich 2.5 method
    - [ ] Referenced integrals
- [ ] Strong Taylor-Stratonovich 3.0 method
    - [ ] Referenced integrals
- [ ] Precision calculation with q
- [ ] Statistical tests
- [ ] GUI
    - [ ] Greek alphabet (optional)
    - [ ] Latex output (optional)
