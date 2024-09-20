# 3. Develop a Flask app that uses URL parameters to display dynamic content.

from flask import Flask ,render_template

app=Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    return render_template("hello.html",name=name)

@app.route('/profile/<name>/<int:age>')
def profile(name,age):
    return render_template('profile.html',name=name,age=age)

if __name__ =="__main__":
    app.run(debug=True)


    #use this in the link 127.0.0.1 - - 
    # [20/Sep/2024 13:26:23] "GET / HTTP/1.1" 404 -
# 127.0.0.1 - - [20/Sep/2024 13:26:45] "GET /hello/Siddhartha HTTP/1.1" 200 -
# 127.0.0.1 - - [20/Sep/2024 13:27:10] "GET /profile/Siddhartha/22 HTTP/1.1" 200 -