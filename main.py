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
        if username == 'Gordon' and password == 'Ramsy':
            messsage = model.show_color('Gordon')
            return render_template('football.html', message = messsage)
        else:
            error_message = "Oops check deteils"
            return render_template('Index.html', message = error_message)

@app.route("/football", methods = ['GET'])
def football ():
    return render_template('football.html')


if __name__ =='__main__':
    app.run(port=5000, debug=True)