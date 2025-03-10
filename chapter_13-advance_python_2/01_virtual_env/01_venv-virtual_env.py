'''
Virtual Environment
    - A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, plus several additional packages.
    - It allows you to install packages in an isolated environment, without affecting the system-wide Python installation or other virtual environments.
    - This is useful for managing dependencies and avoiding conflicts between different projects.
    - It is a good practice to create a virtual environment for each project you work on.
    
    steps to create a virtual environment:
    1. Install virtualenv package
        - pip install virtualenv
    2. Create a virtual environment
        - virtualenv venv
    3. Activate the virtual environment
        - Windows: venv\Scripts\activate
        - Linux/Mac: source venv/bin/activate
    4. Install packages in the virtual environment
        - pip install package_name
    5. Deactivate the virtual environment
        - deactivate
    6. Delete the virtual environment
        - rm -rf venv

'''

'''
    List all package installed in the virtual environment
        - pip list / pip freeze
    List all installed packages in a file 
        - pip freeze > requirements.txt
    Install all packages from a file
        - pip install -r requirements.txt

    List all virtual environments (not working)
        - lsvirtualenv
    Remove a virtual environment (not working)
        - rmvirtualenv venv
    Create a virtual environment with a specific Python version
        - virtualenv -p python3.8 venv
    Create a virtual environment with a specific Python version and packages
        - virtualenv -p python3.8 venv --packages package_name
'''

'''
commands to create a virtual environment and install packages:

    pip install virtualenv                  # install virtualenv package
    virtualenv < environment_name >         # create a virtual environment
    < environment_name >\Scripts\activate   # activate the virtual environment
    pip install < package_name >            # install packages in the virtual environment

    pip freeze                              # list all packages installed in the virtual environment
    pip freeze > requirements.txt           # save all installed packages in a file
    pip install -r requirements.txt         # install all packages from the file
    deactivate                              # deactivate the virtual environment
    rm -rf < environment_name >             # delete the virtual environment

'''