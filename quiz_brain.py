class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        guess = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False)? ")
        if self.is_answer_correct(guess):
            print("Correct!")
            self.score += 1
        else:
            print("Sorry, wrong.")

        self.question_number += 1


    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def is_answer_correct(self, guess):
        return guess == self.question_list[self.question_number].get_answer()

