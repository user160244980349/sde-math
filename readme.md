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
- [x] Milstein method
   - [x] Io(i1)
   - [x] Ioo(i1, i2, q)
   - [x] G, G2 operators
        - [x] Grad operator
- [x] Database routine
     - [x] Database initialization
     - [x] Database for C coefficients
- [x] C operator
    - [x] C operator with loading C coefficient
    - [x] Uploading coefficients that not produces in database
- [ ] Taylor 1.5 method
    - [x] L operator
    - [ ] Ii(i1) {5.7} 
    - [ ] Iooo(i1, i2, i3) {5.16} without limit
    - [ ] Iooo(i, i, i) after {5.16}
    - [ ] {5.17} {5.18} in Iooo()
- [ ] Beautify G2 output
- [ ] GUI
    - [ ] Greek alphabet
    - [ ] Latex test output
