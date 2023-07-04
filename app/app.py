from flask import Flask
import socket
app = Flask(__name__)

@app.route('/app')
def main():
    return "Hi" + "  " +socket.gethostname()
if __name__ == "__main__":
   app.run(host='0.0.0.0',port=9001,debug=True)