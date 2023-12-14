import os

from flask import Flask, send_from_directory


app = Flask(__name__, static_folder='dist/')
# html renders
@app.route('/test/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        print('1')
        return send_from_directory(app.static_folder, path)
    else:
        print('2')
        return send_from_directory(app.static_folder, 'index.html')
    
if __name__ == '__main__':
    app.run(debug=True)