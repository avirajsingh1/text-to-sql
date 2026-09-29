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

def create_prompt(user_question):
    return f"""
You are an expert PostgreSQL SQL generator.

Your job is to convert the user's natural language question
into a valid PostgreSQL SQL query.

Use ONLY the tables and columns provided in the schema.

{SCHEMA}

Rules:

1. Return only SQL.
2. Do not use markdown.
3. Do not explain the SQL.
4. Do not create tables.
5. Do not modify data.
6. Only generate SELECT queries.

User question:

{user_question}
"""