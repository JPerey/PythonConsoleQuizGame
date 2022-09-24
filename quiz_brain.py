class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        question_amount = len(self.question_list)
        if question_amount > self.question_number:
            return True
        else:
            return False

    def next_question(self):
        current_number = self.question_number + 1
        player_answer = input(f"Q{current_number}: {self.question_list[self.question_number].text}. True/False?: ")
        self.check_answer(player_answer, self.question_list[self.question_number].answer, current_number)
        self.question_number += 1

    def check_answer(self, player_answer, question_answer, current_number):
        if player_answer.lower() == question_answer.lower():
            self.score += 1
            print(f"correct! current score: {self.score}/{current_number}")
        else:
            print(f"incorrect! current score: {self.score}/{current_number}")

