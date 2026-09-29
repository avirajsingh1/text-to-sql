SCHEMA = """
Database schema:

customers:
- id: integer, primary key
- name: varchar
- email: varchar
- city: varchar

orders:
- id: integer, primary key
- customer_id: integer, foreign key referencing customers.id
- amount: decimal
- order_date: date
- status: varchar
"""


def create_analysis_prompt(user_question):

    return f"""
You are a query analysis system for a Text-to-SQL application.

Your job is NOT to generate SQL.

Your job is to determine whether the user's question
contains enough information to generate a correct SQL query.

Database schema:

{SCHEMA}

Analyze this user question:

"{user_question}"

Rules:

1. Mark the question as "clear" if a reasonable SQL query
   can be generated without asking the user for additional
   information.

2. Mark it as "needs_clarification" if an important part
   of the request is ambiguous or missing.

3. Do not ask unnecessary questions.

4. If clarification is needed, identify exactly what
   information is missing.

5. Generate ONE concise clarification question.

6. Do not generate SQL.

7. Do not invent information that the user did not provide.
"""