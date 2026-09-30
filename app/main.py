from analyzer import analyze_query
from llm import generate_sql
from database import execute_sql


def main():

    question = input("Ask a question: ")

    print("\nAnalyzing your question...\n")

    analysis = analyze_query(question)

    print("RAW ANALYSIS:")
    print(analysis.model_dump_json(indent=2))

    if analysis.status == "needs_clarification":

        print("\nI need some clarification:")
        print(analysis.clarification_question)

        return

    print("\nQuestion is clear.")
    print("\nGenerating SQL...")

    sql = generate_sql(question)

    print("\nGenerated SQL:")
    print(sql)


if __name__ == "__main__":
    main()