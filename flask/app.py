from flask import Flask,request
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
@app.route('/api/authenticate', methods=['POST'])
def auth():
   data = request.get_json()
   user=data['email']
   pas=data['password']
   #Authenticate data from the database and return result
   return "Succes"

@app.route('/api/user/create', methods=['POST'])
def adduser():
   data = request.get_json()
   name, email, password, dob, address, prob=data['name'], data['email'], data['password'], data['DOB'], data['address'], data['prob'] 
   #Add Data to the database and return status
   return "Succes"
   
if __name__ == '__main__':
   app.run(debug=True)
