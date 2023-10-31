import data

class Question:

    def __init__(self, q_text, q_answer) -> None:
        self.text = q_text
        self.answer = q_answer
        
# class question:
    
#     def __init__(self, list_number) -> None:
        
#         dictionary = data.question_data[list_number]
#         self.question = dictionary["text"]
#         self.answer = dictionary["answer"]