from llm import generate_sql
from database import execute_sql

def validate_sql(sql):
    normalized = sql.strip().lower()
    
    if not normalized.startswith("select"):
        raise ValueError("Only Select queries are allowed")
    
    dangerous_keywords = [
        "insert",
        "update",
        "delete",
        "drop",
        "truncate",
        "alter",
        "create"
    ]
    
    for keyword in dangerous_keywords:
        if keyword in normalized:
            raise ValueError(
                f"Potentially dangerous keyword detected {keyword}"
            )
    
    return True

def main():
    
    question = input("Ask a question: ")
    
    print("\nGenerating Sql...\n")
    
    sql = generate_sql(question)
    print(sql)
    
    validate_sql(sql)
    
    print("\nExecuting the query...\n")
    
    results = execute_sql(sql)
    print("results: ")
    
    for row in results:
        print(row)
        
if __name__ == "__main__":
    main()


