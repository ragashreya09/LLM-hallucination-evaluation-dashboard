import json
from openai import OpenAI
from src.prompts import EVALUATION_PROMPT

client = OpenAI()


def evaluate_llm_response(question, context, answer):
    prompt = EVALUATION_PROMPT.format(
        question=question,
        context=context,
        answer=answer
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a precise LLM evaluation and hallucination detection assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    raw_output = response.choices[0].message.content

    try:
        return json.loads(raw_output)
    except json.JSONDecodeError:
        return {
            "faithfulness_score": 0,
            "answer_relevance_score": 0,
            "context_relevance_score": 0,
            "hallucination_risk": "Unknown",
            "unsupported_claims": [],
            "explanation": raw_output
        }
