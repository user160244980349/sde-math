### README ###

##### DEPENDENCIES #####
- [SymPy](https://docs.sympy.org/latest/index.html)
- [numpy](https://numpy.org/)
- [plotly](https://plotly.com/python/)
- [PyQt5](https://pypi.org/project/PyQt5/)

##### AFTER CLONE #####
1. `pip install -r requirements.txt`
1. install sqlite3 and add it to PATH variable
1. copy `config.example.py` to `config.py` and edit paths
1. ready to run

##### RUN #####
Entry                   | Description
------------------------|------------------------------------
`main_gui.py`           | GUI application
`main_linear.py`        | console linear modeling
`main_nonlinear.py`     | console nonlinear modeling
`main_txt_store_c.py`   | console store C coefficients in txt
`main_db_store_c.py`    | console store C coefficients in db

##### TODO #####
- [x] Generation of C coefficients
- [x] Bunch of linear stuff
- [x] Euler method
    - [x] Euler with trajectories
- [x] Milstein method
    - [x] I0(i1)
    - [x] I00(i1, i2, q)
    - [x] G operators
- [x] Database routines
    - [x] Database initialization
    - [x] Database for C coefficients
    - [x] C coefficients preload
    - [x] Addition with coefficients weights
- [x] C operator
    - [x] C operator with loading of C coefficients
    - [x] Uploading coefficients that not produces in database
- [x] Strong Taylor-Ito 1.5 method
    - [x] L operator
    - [x] Recursive G
    - [x] I1(i1) {5.7}
    - [x] I000(i1, i2, i3) {5.16} without limit
    - [x] I000(i, i, i) after {5.16}
    - [x] {5.17} {5.18} in I000
- [x] Trajectory as substitution argument (thrown away) 
- [x] Beautify G2 output
- [x] `is_symbol` check is not working (thrown away) 
- [x] Clean up
- [x] Comments actualization
- [x] Update tests
- [x] Context for formulas to beat redundancy (thrown away) 
- [x] Strong Taylor-Ito 2.0 method
    - [x] Recursive L
    - [x] Referenced integrals
- [ ] Strong Taylor-Ito 2.5 method
    - [x] C coefficients with weights
    - [x] Referenced integrals
    - [ ] Review
- [ ] Strong Taylor-Ito 3.0 method
    - [ ] Referenced integrals
- [x] Stratonovich Aj and Lj, Integrals "J"
- [x] Strong Taylor-Stratonovich 1.0 method
    - [x] Referenced integrals
- [x] Strong Taylor-Stratonovich 1.5 method
    - [x] Referenced integrals
- [x] Strong Taylor-Stratonovich 2.0 method
    - [x] Referenced integrals
- [ ] Strong Taylor-Stratonovich 2.5 method
    - [x] Referenced integrals
    - [ ] Review
- [ ] Strong Taylor-Stratonovich 3.0 method
    - [ ] Referenced integrals
- [x] Optimize imports
- [x] Replace ' with "
- [x] Replace formats with f-strings
- [x] Move preload in schemes classes
- [ ] Optimize schemes where functions repeats
- [ ] Rewrite some of tests
- [ ] New Lj and Aj
- [ ] Precision calculation with q
- [ ] Replace prints with logs
- [ ] Statistical tests
- [ ] L and G expansion when subbing matrices and their symbols this understood but not tested in terms of performance
- [ ] GUI
    - [ ] Greek alphabet (optional)
    - [ ] Latex output (optional)
