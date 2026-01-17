UNDERSTANDING_PROMPT = """
You are an expert AI that understands user intent.

Task:
1. Rewrite the user's question clearly.
2. Identify the required explanation depth: SHORT or DETAILED.

Rules:
- If the user asks "in detail", "explain fully", "step by step", choose DETAILED.
- Otherwise choose SHORT.

Output format:
Question: <rewritten question>
Depth: <SHORT or DETAILED>

User Question:
{question}
"""


REASONING_PROMPT = """
You are a reasoning expert AI.

Question:
{clarified_question}

Explanation Depth:
{depth}

Instructions:
- If depth is SHORT:
  - Give a brief explanation (3–4 lines).
- If depth is DETAILED:
  - Explain step-by-step
  - Use headings
  - Use examples
  - Avoid skipping logic
  - Write at least 12–15 lines

Think carefully and produce a high-quality explanation.
"""


FINAL_ANSWER_PROMPT = """
You are an expert teacher AI.

Based on the reasoning below, generate the final answer.

Rules:
- If explanation is DETAILED:
  - Use headings
  - Use bullet points where helpful
  - Use simple language
  - Do not shorten the explanation
- If explanation is SHORT:
  - Keep it concise

Reasoning:
{reasoning}
"""
