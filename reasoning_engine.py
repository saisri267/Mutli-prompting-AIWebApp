from prompts import (
    UNDERSTANDING_PROMPT,
    REASONING_PROMPT,
    FINAL_ANSWER_PROMPT
)
from hf_client import call_llm   # or groq client

def multi_prompt_reasoning(question):

    # Step 1: Understanding
    understanding = call_llm(
        UNDERSTANDING_PROMPT.format(question=question)
    )

    # Extract clarified question and depth
    lines = understanding.splitlines()
    clarified_question = ""
    depth = "SHORT"

    for line in lines:
        if line.startswith("Question:"):
            clarified_question = line.replace("Question:", "").strip()
        if line.startswith("Depth:"):
            depth = line.replace("Depth:", "").strip()

    # Step 2: Reasoning
    reasoning = call_llm(
        REASONING_PROMPT.format(
            clarified_question=clarified_question,
            depth=depth
        )
    )

    # Step 3: Final Answer
    final_answer = call_llm(
        FINAL_ANSWER_PROMPT.format(reasoning=reasoning)
    )

    return final_answer
