from flask import Flask, render_template, request

#from flask import Flask
app = Flask(__name__)
 
@app.route('/result',methods = ['POST'])
def result():

    city =  request.form["city"]
    city = reverse_string(city)
    return render_template("result.html",result = city)

@app.route('/') #rest api
def hello():
    return render_template('test.html')

def reverse_string(content):
    return content[::-1]

if __name__ == '__main__':
    app.run()