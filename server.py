from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Replace 'your_mysql_host_ip' with the actual IP address of your MySQL server
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mysql:abc123@172.21.0.2/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)

@app.route('/')
def hello():
    return "Hey, it's the Python server speaking!"

@app.route('/python-endpoint', methods=['POST'])
def receive_message():
    try:
        # Extract the message from the request
        message_content = request.json.get('message')
        print("invoked")

        # Log the message
        print('Received Message:', message_content)

        # Save the message to the database
        new_message = Message(content=message_content)
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
