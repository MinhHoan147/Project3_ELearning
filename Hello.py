from flask import Flask, redirect, url_for, request, render_template,make_response
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/admin')
def hello_admin():
   return 'hello admin'

@app.route('/guest/<name>')
def hello_guess(name):
   return 'welcome %s as guest' % name

@app.route('/home/<name>')
def hello_world(name):
   if name == 'admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guess', name = name))

@app.route('/home/<int:id>')
def getID(id):
   my_id = 'Your id is %d' % id
   return my_id

@app.route('/home/<float:salary>')
def getsalary(salary):
   my_salary = 'Your salary is %f' % salary
   return my_salary

@app.route('/flask')
def hello_flask():
   return 'Hello Flask'

@app.route('/python/')
def hello_python():
   return 'Hello Python'

@app.route('/success/<name>/<int:age>')
def success(name,age):
   return render_template('success.html',name = name,age = age)

@app.route('/infor')
def infor():
   my_dict = {
      'emp1': {
         'name': 'Mason',
         'age': 24,
         'gender': 'Male',
         'address': 'Hanoi',
         'phone': '0888888888',
      },
      'emp2': {
         'name': 'Mary',
         'age': 20,
         'gender': 'Female',
         'address': 'SaiGon',
         'phone': '0888888888',
      },
   }
   return render_template('infor.html',infor = my_dict)
   
@app.route('/login_form')
def login_form():
   return render_template('login_form.html')

@app.route('/welcome_page',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      infor = request.form
      return render_template('success.html', infors = infor)

@app.route('/custom_response')
def custom_response():
  myResponse = make_response('Response')
  myResponse.headers['customHeaderabc'] = 'This is a custom header abc'
  myResponse.status_code = 404
  myResponse.mimetype = 'text/html'

  return myResponse

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
      user = request.form['nm']
   
   resp = make_response(render_template('readcookie.html'))
   resp.set_cookie('userID', user)
   
   
   return resp

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome '+name+'</h1>'

if __name__ == '__main__':
   app.run(debug=True)