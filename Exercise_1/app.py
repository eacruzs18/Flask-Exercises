from flask import Flask, render_template, url_for
from datetime import datetime

app = Flask(__name__)

@app.get('/')
def index():
    now = datetime.now() # current date and time
    current_time = now.strftime("%A, %B %d %Y %H:%M:%S")
    return render_template('index.html', current_time=current_time)

if __name__ == "__main__":
    app.run(debug=True)
