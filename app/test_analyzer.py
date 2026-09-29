from analyzer import analyze_query


questions = [
    "Show me customers from Delhi.",
    "How many customers do we have?",
    "Show me the top customers.",
    "Show me customers who spent more than 50000.",
    "Show me the highest spending customers.",
]


for question in questions:

    print("\nQUESTION:")
    print(question)

    result = analyze_query(question)

    print("\nANALYSIS:")
    print(result.model_dump_json(indent=2))
    
    