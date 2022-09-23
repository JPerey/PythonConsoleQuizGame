from question_model import Question
import data

# global variables
question_bank = []

for q in data.question_data:
    new_q = Question(q["text"], q["answer"])
    question_bank.append(new_q)

print(question_bank[0].answer)
