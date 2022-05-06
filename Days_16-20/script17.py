# Day 17 of 100 Days of Code Challenge
# Quiz Game
import script17_question as q
from data import question_data
import script17_quiz_brain as qb

question_bank = []
for question in question_data:
    question_bank.append(q.Question(question["text"], question["answer"]))

quiz = qb.QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is {quiz.score}/{quiz.question_num}")
