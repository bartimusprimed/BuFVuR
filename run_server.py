import os
import app

# The name of your Application python file. Default: app.py
bufvur_app = 'app.py'

if os.environ.get('FLASK_APP'):
    print('Setting up BuFVur app: {0}'.format(os.environ['FLASK_APP']))
else:
    print('Setting BuFVur App')
    os.environ['FLASK_APP'] = bufvur_app
    print('Setting up BuFVur app: {0}'.format(os.environ['FLASK_APP']))

app.app.run(port=5000, debug=True)
