from flask import Flask, render_template, request, redirect, url_for # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://feedback_respa_user:Y5280FokEtUvaY5ZkkKb7bUnCyp5HRTw@dpg-coe4fs8l6cac73btq2c0-a.singapore-postgres.render.com/feedback_respa'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Feedback_sql(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_1 = db.Column(db.Integer, nullable=False)
    question_2 = db.Column(db.Integer, nullable=False)
    question_3 = db.Column(db.Integer, nullable=False)
    question_4 = db.Column(db.Integer, nullable=False)
    question_5 = db.Column(db.Integer, nullable=False)
    question_6 = db.Column(db.Integer, nullable=False)
    question_7 = db.Column(db.Integer, nullable=False)
    question_8 = db.Column(db.Integer, nullable=False)
    question_9 = db.Column(db.Integer, nullable=False)
    question_10 = db.Column(db.Integer, nullable=False)
    additional_feedback = db.Column(db.Text)

    def __repr__(self):
        return f"Feedback(id={self.id}, question_1={self.question_1}, question_2={self.question_2}, ..., additional_feedback={self.additional_feedback})"


# Sample questions for feedback
questions = [
    "How satisfied are you with our service?",
    "Was our website easy to navigate?",
    "Would you recommend us to a friend?",
    "How would you rate the quality of our products?",
    "Did you find the checkout process smooth and efficient?",
    "How likely are you to purchase from us again?",
    "Are you satisfied with the response time of our customer support?",
    "Do you have any suggestions for improvement?",
    "How did you hear about us?",
    "Overall, how satisfied are you with your experience?"
]

# Route for displaying feedback form
@app.route('/', methods=['GET', 'POST'])
def show_feedback_form():
    if request.method == 'POST':
        # Process the feedback data and save to database
        feedback_entry = Feedback_sql(
            question_1=request.form.get('answer_1'),
            question_2=request.form.get('answer_2'),
            question_3=request.form.get('answer_3'),
            question_4=request.form.get('answer_4'),
            question_5=request.form.get('answer_5'),
            question_6=request.form.get('answer_6'),
            question_7=request.form.get('answer_7'),
            question_8=request.form.get('answer_8'),
            question_9=request.form.get('answer_9'),
            question_10=request.form.get('answer_10'),
            additional_feedback=request.form.get('additional_feedback')
        )
        db.session.add(feedback_entry)
        db.session.commit()

        # Redirect to thank you page after saving feedback
        return redirect(url_for('thank_you'))
    
    # Render the feedback form template with questions
    return render_template('feedback_form.html', questions=enumerate(questions))

# Route for thank you page
@app.route('/thank-you')
def thank_you():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
