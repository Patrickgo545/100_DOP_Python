from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# PUT JSON IN LIST TO PREP FOR QUIZ_BRAIN
for entree in question_data:
    question_text = entree["text"]
    question_answer = entree["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    # question = Question(question_data[question_number]['text'], question_data[question_number]['answer'])
    question_bank.append(new_question)


# EXECUTE QUIZBRAIN AS AN OBJECT
quiz = QuizBrain(question_bank)

# LOOP THROUGH ALL QUESTIONS
while quiz.still_has_questions():
    quiz.next_question()

quiz.quiz_complete()