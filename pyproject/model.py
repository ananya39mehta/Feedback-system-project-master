from flask_sqlalchemy import SQLAlchemy # type: ignore

db = SQLAlchemy()

class Feedback(db.Model):
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
        return f"Feedback(id={self.id}, question_1={self.question_1}, question_2={self.question_2}, question_3={self.question_3}..., additional_feedback={self.additional_feedback})"