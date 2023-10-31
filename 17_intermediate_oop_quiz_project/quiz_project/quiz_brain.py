# CLASS - HANDLE ALL LOGIC OF GAME

class QuizBrain:

    # ATTRIBUTES
    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.question_list = q_list
        self.score = 0


    # METHODS TO KEEP THE GAME GOING
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1 
        user_answer = input(f"Q.{self.question_number} {current_question.text}? (True/False): ")
        # user_answered_correct = self.check_answer(user_answer, current_question.answer)
        if self.check_answer(user_answer, current_question.answer) == True:
            self.score += 1

        print(f"Your current score is: {self.score}/{self.question_number}")

        print("\n\n")



    # KEEP THE PROGRAM IN A LOOP IF THERE ARE MORE QUESTIONS
    def still_has_questions(self):
        list_length = len(self.question_list)

        if self.question_number < list_length:
            return True

        else: 
            return False
        
        # OR 
        # return self.question_number < len(self.question_list)


    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct")
            print(f"Answer is: {correct_answer}")
            return True
        else:
            print("Incorrect")
            print(f"Answer is: {correct_answer}")
            return False



    # METHOD TO COMPLETE THE GAME 
    def quiz_complete(self):
        print("Congratulations, you have completed today's quiz")
        print(f"Quiz Final Score: {self.score}/{self.question_number}")