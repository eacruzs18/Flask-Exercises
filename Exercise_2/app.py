from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/result', methods=['GET'])
    
def result():
    num = request.args.get('number')
    if num is None:
        return render_template('error.html')
    try:
        num = int(num)
        if num % 2 == 0:
            result_message = f"{num} is an even number."
        else:
            result_message = f"{num} is an odd number."
    except ValueError:
        result_message = f"{num} is not an integer!"
    return render_template('result.html', result_message=result_message)

if __name__ == "__main__":
    app.run(debug=True)