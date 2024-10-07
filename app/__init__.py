''' The application exists in a package. In Python, a sub-directory that includes a __init__.py file is considered a package, and can be imported. 
When you import a package, the __init__.py executes and defines what symbols the package exposes to the outside world.
'''

from flask import Flask

app = Flask(__name__) #creates the application object as an instance of class Flask imported from the flask package. The __name__ variable passed to the Flask class is a Python predefined variable, which is set to the name of the module in which it is used. Flask uses the location of the module passed here as a starting point when it needs to load associated resources such as template files, 

from app import routes