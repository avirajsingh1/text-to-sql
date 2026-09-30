class converstaionState:
    def __init__(self):
        self.original_question = None
        self.clarification = []
    
    def set_question(self, question):
        self.original_question = question
        
    def add_clarification(self, question, answer):
        self.clarification.append({
            "question":question,
            "answer":answer
        })