from flask import Flask, render_template, request

app = Flask(__name__)

# App 1 routes
@app.route('/app1')
def app1_index():
    return render_template('index1.html')

@app.route('/app1/result', methods=['POST'])
def app1_result():
    input_data = request.form['input1']
    return render_template('result1.html', result=input_data)

# App 2 routes
@app.route('/app2')
def app2_index():
    return render_template('index2.html')

@app.route('/app2/result', methods=['POST'])
def app2_result():
    input_data = request.form['input1']
    return render_template('result2.html', result=input_data)

# App 3 routes
@app.route('/app3')
def app3_index():
    return render_template('index3.html')

@app.route('/app3/result', methods=['POST'])
def app3_result():
    input_data = request.form['input1']
    return render_template('result3.html', result=input_data)

if __name__ == '__main__':
    app.run(debug=True)
