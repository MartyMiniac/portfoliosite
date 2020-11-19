from flask import *

app=Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/contact',methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/contactpost',methods=['POST'])
def contactpost():
    print(request.form['name'])
    print(request.form['email'])
    print(request.form['msg'])
    return 'received'

if __name__ == '__main__':
    app.run(debug=True)