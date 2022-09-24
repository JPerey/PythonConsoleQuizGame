from question_model import Question
import data
from quiz_brain import QuizBrain

# global variables
question_bank = []

for q in data.question_data:
    new_q = Question(q["text"], q["answer"])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"your done! total score: {quiz.score}/12")

