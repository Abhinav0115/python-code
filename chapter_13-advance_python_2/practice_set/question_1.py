'''
Create two virtual environments, install some packages in first one. How do you create a similar environment in the second one?

'''

'''
Solution steps:
    pip install virtualenv
    virtualenv env1
    .\env1\bin\activate
    pip install pandas
    pip freeze > requirements.txt
    deactivate

    virtualenv env2
    .\env2\bin\activate
    pip install -r requirements.txt
    pip freeze
    deactivate

'''