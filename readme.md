### README ###

##### DEPENDENCIES #####
1. [SymPy](https://docs.sympy.org/latest/index.html)
1. [numpy](https://numpy.org/)
1. [scipy](https://www.scipy.org/)
1. [PyQt5](https://pypi.org/project/PyQt5/)
1. [plotly](https://plotly.com/python/)

##### AFTER CLONE #####
1. Do `pip install -r requirements.txt`
1. Install sqlite3 and add it to the PATH variable
1. Copy `config.example.py` to `config.py` and edit paths
1. Ready to run

##### RUN #####
Entry                   | Description
------------------------|------------------------------------
`main_gui.py`           | GUI application
`main_linear.py`        | console linear modeling
`main_nonlinear.py`     | console nonlinear modeling
`main_new_c.py`         | console store C coefficients in txt

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
- [x] Strong Taylor-Ito 2.5 method
    - [x] C coefficients with weights
    - [x] Referenced integrals
- [x] Strong Taylor-Ito 3.0 method
    - [x] Referenced integrals
- [x] Stratonovich Aj and Lj, Integrals "J"
- [x] Strong Taylor-Stratonovich 1.0 method
    - [x] Referenced integrals
- [x] Strong Taylor-Stratonovich 1.5 method
    - [x] Referenced integrals
- [x] Strong Taylor-Stratonovich 2.0 method
    - [x] Referenced integrals
- [x] Strong Taylor-Stratonovich 2.5 method
    - [x] Referenced integrals
- [x] Strong Taylor-Stratonovich 3.0 method
    - [x] Referenced integrals
- [x] Optimize imports
- [x] Replace ' with "
- [x] Replace formats with f-strings
- [x] Move preload in schemes classes
- [x] New Lj and Aj (review G and L)
- [x] L and G expansion when subbing matrices and their symbols these are 
      understood but are not tested in terms of performance
- [x] I10 and I01 with C from database
- [x] Q ordering
- [x] Replace prints with logs
- [x] Precision calculation with q
- [x] Big database of C
- [x] Store indices in file
- [x] Restore indices from file in a separate module
- [x] Fix ksi index error
- [x] Permanent DB connection
- [ ] Fix stack error
- [ ] More efficient C preload
- [ ] GUI
    - [ ] Latex
    - [ ] Main menu
    - [ ] Linear section
        - [ ] Input fields
        - [ ] Console with info
        - [ ] Calculate button
        - [ ] Add on plot window button
    - [ ] Nonlinear section
        - [ ] Input fields
        - [ ] Console with info
        - [ ] Calculate button
        - [ ] Add on plot window button
    - [ ] Plot window
        - [ ] Remove chart
- [ ] Optimize schemes where functions repeats
- [ ] Review all schemes and formulas
- [ ] Rewrite some of tests
- [ ] Statistical tests
- [ ] Rewrite approximations with indicators

##### NOTES #####
The most common solution is to use QStackedWidget and put all possible 
widgets into the stack. When selecting an item, just call setCurrentWidget 
to display the one you want.