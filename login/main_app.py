from login.app1 import app as app1
from login.app2 import app as app2
from login.app3 import app as app3
from flask import Flask

main_app = Flask(__name__)

@main_app.route('/app1')
def app1_route():
    return app1

@main_app.route('/app2')
def app2_route():
    return app2

@main_app.route('/app3')
def app3_route():
    return app3

if __name__ == '__main__':
    main_app.run()
