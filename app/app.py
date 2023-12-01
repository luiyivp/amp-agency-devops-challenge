from flask import Flask, jsonify, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db/database'
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    return redirect('/greetings')

@app.route('/greetings', methods=['GET'])
def get_greetings():
    total_rows = Message.query.count()
    last_three_rows = Message.query.order_by(Message.timestamp.desc()).limit(3).all()

    response_data = {
        'total_rows': total_rows,
        'last_three_rows': [{'content': row.content, 'timestamp': row.timestamp} for row in last_three_rows]
    }

    return jsonify(response_data), 200

@app.route('/messages', methods=['POST'])
def add_message():
    new_message = Message(content='Some Message')
    db.session.add(new_message)
    db.session.commit()

    return jsonify({'content': new_message.content, 'timestamp': new_message.timestamp}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
