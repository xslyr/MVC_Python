import sys
sys.path.append('..')

from . import app_types
from .main_controller import Main_Controller
from flask import Flask

app = Main_Controller( 'nome_app' )
webpath = Flask( __name__,  template_folder='../views/templates')


@webpath.route('/')
def main():
    return app.main()


def run_app():
    webpath.run( debug=app.config['debug'])




