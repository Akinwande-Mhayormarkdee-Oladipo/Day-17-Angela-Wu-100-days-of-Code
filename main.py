from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

def create_question_objects():
    questions = []
    for question in question_data:
        question_text = question['text']
        answer = question['answer']
        q = Question(question_text, answer)
        questions.append(q)
    return questions


question_bank = create_question_objects()
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
