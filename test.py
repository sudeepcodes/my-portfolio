from flask import Flask
from flask import send_file
import os
app = Flask(__name__)

@app.route('/download')
def downloadFile ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "./static/Resume.pdf"
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(port=5000,debug=True)