from flask import Flask,render_template, request
import model 


app = Flask(__name__)

@app.route("/",methods = ['GET','POST'])
def home():
    if request.method == 'GET':

       return render_template('Index.html', message = 'Welcome')
    else:
        username = request.form['username']
        password = request.form['password']
        db_password = model.check_pw(username)

        if password == db_password:
            messsage = model.show_color(username)
            return render_template('football.html', message = messsage)
        else:
            error_message = "Oops check deteils"
            return render_template('Index.html', message = error_message)

@app.route("/football", methods = ['GET'])
def football ():
    return render_template('football.html')

@app.route("/signup", methods = ['GET','POST'])
def signup():
    if request.method == 'GET':
        message = "please Sign UP!"
        return render_template('signup.html', message=message)
    else:
        username = request.form["username"]
        password = request.form["password"]
        favourite_color = request.form["favourite_color"]
        message = model.signup(username,password,favourite_color)

        
        return render_template('signup.html',message=message)


if __name__ =='__main__':
    app.run(port=5000, debug=True)