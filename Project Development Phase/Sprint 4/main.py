from flask import Flask, render_template,url_for,request,redirect
import Feedback
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
        try:
          Feedback.submit(name,phone_number,email,feedback)
          return render_template('index.html',status='Form submission successful!')
        except:
          return render_template('index.html',status='Invalid data')


if __name__ == '__main__':
    app.run(debug=True)
