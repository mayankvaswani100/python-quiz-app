class QuizBrain:
    def __init__(self, question_list):
        self.question_num = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_num < len(self.question_list)

    def next_question(self):
        user_correct_answer = input(
            f"Q.{self.question_num} {self.question_list[self.question_num].question} (True/False)?: ")
        self.question_num += 1
        self.check_correct_answer(
            user_correct_answer, self.question_list[self.question_num].correct_answer)

    def check_correct_answer(self, user_correct_answer, correct_correct_answer):
        if user_correct_answer.lower() == correct_correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("The correct_answer is wrong")
        print(f"The correct correct_answer was {correct_correct_answer}")
        print(f"Your current score is {self.score}/{self.question_num}")
        print("\n")
