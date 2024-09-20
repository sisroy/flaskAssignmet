#4. Create a Flask app with a form that accepts user input and displays it.
from flask import Flask,request ,render_template

app=Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit',methods=['POST'])
def submit():
    name=request.form['name']
    email=request.form['email']
    message=request.form['message']
    return f"Recived:name :{name},email:{email},message:{message}"



if __name__=='__main__':
    app.run(debug=True)