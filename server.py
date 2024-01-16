from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import logging

app = Flask(__name__)

logging.basicConfig(filename='/app/python_server.log', level=logging.INFO)

# Replace 'your_mysql_host_ip' with the actual IP address of your MySQL server
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Kailas11!@localhost/test_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)

@app.route('/')
def hello():
    app.logger.info("Endpoint '/' was accessed.")
    return "Hey, it's the Python server speaking!"

@app.route('/receive-node-call', methods=['POST'])
def call_node_endpoint():
    try:
        # Extract the message from the request
        message_content = request.json.get('message')

        # Log the received message
        print('Received Message from Node.js:', message_content)

        # Return a response to Node.js
        return "Hey Node server, how are you?"
    except Exception as e:
        print('Error:', str(e))
        return "Error processing the message", 500

@app.route('/python-save-message-endpoint', methods=['POST'])
def receive_message():
    try:
        # Extract the message from the request
        json_data = request.json if request.json else "No JSON data in the request"

        # Log the endpoint access and JSON data
        app.logger.info(f"Endpoint '/document_saving' was accessed. JSON data: {request.json.get('message')}")

        print(request.json,'ffffffff')
        message_content = request.json.get('message')
        print("invoked")

        # Log the message
        print('Received Message:', message_content)

        # Save the message to the database
        new_message = Message(text=message_content)
        db.session.add(new_message)
        db.session.commit()

        return "Message received and saved!"
    except Exception as e:
        print('Error:', str(e))
        return "Error processing the message", 500

# Flask command to create the database tables
@app.cli.command('create-db')
def create_db():
    db.create_all()
    print("Database tables created successfully.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
