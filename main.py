from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []

for each_question in question_data:
    question_bank.append(
        Question(each_question["question"], each_question["correct_answer"]))

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

if quiz.still_has_questions() == False:
    print("Congrats! You have completed the quiz")
    print(f"Your final score was {quiz.score}/{quiz.question_num}")
