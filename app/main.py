# from llm import generate_sql
# from database import execute_sql
# from analyzer import analyze_query
# from models import QueryAnalysis

# def validate_sql(sql):
#     normalized = sql.strip().lower()
    
#     if not normalized.startswith("select"):
#         raise ValueError("Only Select queries are allowed")
    
#     dangerous_keywords = [
#         "insert",
#         "update",
#         "delete",
#         "drop",
#         "truncate",
#         "alter",
#         "create"
#     ]
    
#     for keyword in dangerous_keywords:
#         if keyword in normalized:
#             raise ValueError(
#                 f"Potentially dangerous keyword detected {keyword}"
#             )
    
#     return True

# def main():
    
#     question = input("Ask a question: ")
    
#     print("\nAnalyzing your question\n")
    
#     analysis = analyze_query(question)
    
#     if analysis.status == "needs_clarification":
#         print("I need some clarification:")
#         print(analysis.clarification_question)
        
#         return
    
#     print("Question is clear.")
#     print("\nGenerating SQL...\n")
    
#     sql = generate_sql(question)
#     print(sql)
    
#     print("\nExecuting the query...\n")
    
#     results = execute_sql(sql)
#     print("Results: ")
    
#     for row in results:
#         print(row)
        
# if __name__ == "__main__":
#     main()


from analyzer import analyze_query
from llm import generate_sql
from database import execute_sql


def main():

    question = input("Ask a question: ")

    while True:
        analysis = analyze_query(question)
        
        if analysis.status == "clear":
            print("\nQuestion is clear.")            
            sql = generate_sql(question)
            
            print("\nGenerated SQL: ")
            print(sql)
            
            break
        
        print("\nI need some clarifying : ")
        print(analysis.clarification_question)
        
        answer = input("\nEnter your answer: ")
        
        question = f"""
        Original Question : {question}
        Clarification Question : {analysis.clarification_question}
        User's answer : {answer}
        """

if __name__ == "__main__":
    main()