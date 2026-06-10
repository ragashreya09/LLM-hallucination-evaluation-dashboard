EVALUATION_PROMPT = """
You are an expert LLM evaluation system.

Your task is to evaluate whether the LLM answer is grounded in the provided context.

Evaluate the answer using these criteria:

1. Faithfulness:
Does the answer only use information supported by the context?

2. Answer Relevance:
Does the answer directly answer the user question?

3. Context Relevance:
Is the provided context useful for answering the question?

4. Hallucination Risk:
Does the answer include unsupported, fabricated, or exaggerated claims?

Return your response in this exact JSON format:

{
  "faithfulness_score": 0,
  "answer_relevance_score": 0,
  "context_relevance_score": 0,
  "hallucination_risk": "Low/Medium/High",
  "unsupported_claims": [],
  "explanation": ""
}

Scoring:
0 = very poor
100 = excellent

User Question:
{question}

Retrieved Context:
{context}

LLM Answer:
{answer}
"""
