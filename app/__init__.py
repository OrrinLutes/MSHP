import os
from flask import Flask


# test_config is a configuration populated with values to make launching easy.
# pass it in during testing
def create_app(test_config=None):
    
    myApp = Flask(__name__, instance_relative_config=True)
    
<<<<<<< HEAD
    #SECRET_KEY is to keep nasty hackers from doing dum stuff.
    myApp.config['SECRET_KEY'] = 'comicSansBeepBoopBoopPotato'
    #DATABASE is path of our database
    myApp.config.from_mapping(SECRET_KEY="dev", DATABASE = os.path.join(myApp.instance_path, "CarDB.sqlite"))

=======
    # SECRET_KEY is to keep nasty hackers from doing dum stuff.
    # DATABASE is path of our database
    myApp.config.from_mapping(SECRET_KEY="dev", DATABASE=os.path.join(myApp.instance_path, "CarDB.sqlite"))
>>>>>>> origin/master

    if test_config is None:
        # If there is a configured instance, load it. config.py can store values
        # you don't want visible, like a real secret key.
        myApp.config.from_pyfile("config.py", silent=False)
    else:
        # otherwise, test configuration
        myApp.config.from_mapping(test_config)
        
    try:
        os.makedirs(myApp.instance_path)
    except OSError:
        pass
    
<<<<<<< HEAD
    #import your blueprints here
    from myApp import database ##MOVED INSTANCE INTO APP AND CHANGED THIS FROM (FROM . IMPORT DATABASE TO IMPORT DATABASE) DUE TO RELATIVE FILE RETREVIAL
    #from . import dummyTester
    
    #register your blueprints here.
    #Can use flask tutorial
    #Ex: myApp.register_blueprint(index.bp)
=======
    # import your blueprints here
    from app import database
    from app import index
    import dummyTester
>>>>>>> origin/master
    
    # register your blueprints here.
    # Can use flask tutorial
    # Ex: myApp.register_blueprint(index.bp)

    myApp.register_blueprint(index.bp)
    database.init_app(myApp)
    
    return myApp

<<<<<<< HEAD

#Justas's version of this file is signficantly more complicated
#and probably better so if a) we're getting a lot of errors we can't
#explain or b) we have the time, we should maybe go back to that.
=======
# Justas's version of this file is significantly more complicated
# and probably better so if a) we're getting a lot of errors we can't
# explain or b) we have the time, we should maybe go back to that.
>>>>>>> origin/master
