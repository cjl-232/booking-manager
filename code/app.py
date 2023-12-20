from flask import Flask

app = Flask(__name__)

def create_app(test_config = None):

    app = Flask(__name__, instance_relative_config = True)
    
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
        
    return app

# Connect to the database
