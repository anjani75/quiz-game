class QuizBrain:
    def __init__(self, q_list):
        self.question_num = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_num < len(self.question_list)

    def next_question(self):
        current_ques = self.question_list[self.question_num]
        answer = input(f"Q{self.question_num + 1}. {current_ques.text} (True/False)?: ").lower()
        correct_answer = current_ques.answer.lower()
        self.check_answer(answer, correct_answer)
        self.question_num += 1

    def check_answer(self, user_answer, correct_ans):
        if user_answer == correct_ans:
            print("You got it correct!")
            self.score += 1
        else:
            print("Wrong")
        print(f"The correct answer was: {correct_ans}")
        print(f"Your current score is: {self.score}/{self.question_num + 1}")
        print("\n")
