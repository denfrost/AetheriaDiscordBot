from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "Your bot is alive!"

def runDasbboard():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=runDasbboard)
    server.start()