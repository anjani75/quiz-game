from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

num = 1
question_bank = []
for ques in question_data:
    question_bank.append(Question(ques["text"], ques["answer"]))

#for obj in question_bank:
#    print(obj.text)

new_quiz = Quizbrain(question_bank)
while new_quiz.still_has_question():
    new_quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score was: {new_quiz.score}/{new_quiz.question_num}")