# Intro to writing classes
class QuizBrain:

    def __init__(self, q_list):
        self.question_num = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"Q.{self.question_num}: {question.text} (True/False)?: ")
        self.check_answer(user_answer, question.answer)

    def still_has_questions(self):
        return self.question_num < len(self.question_list)

    def check_answer(self, guess, ans):
        if guess.lower() == ans.lower():
            self.score += 1
            print("That's right!")
        else:
            print("That's incorrect.")

        print(f"The correct answer was {ans}")
        print(f"You're current score is {self.score}/{self.question_num}\n")
