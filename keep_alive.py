from flask import Flask, render_template
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return render_template("index.html")

def runDasbboard():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=runDasbboard)
    server.start()