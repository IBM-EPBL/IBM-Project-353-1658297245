from flask import Flask, render_template,url_for,request,redirect
import Mail_Send
app = Flask(__name__)
@app.route('/', methods=['POST','GET'])
def Home():
  return render_template('index.html',status='')

@app.route("/Submit", methods=['POST','GET'])
def Submit():
    if request.method == 'POST':
        name = (request.form['name'])
        email = (request.form['email'])
        phone_number = (request.form['phone_number'])
        feedback = (request.form['feedback'])
        Mail_Send.send_mail(name,phone_number,email,feedback)
        return render_template('index.html',status='Form submission successful!')

if __name__ == '__main__':
    app.run(debug=True)
