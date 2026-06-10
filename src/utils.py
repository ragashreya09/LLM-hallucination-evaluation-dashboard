import pandas as pd
from datetime import datetime


def create_result_row(question, context, answer, evaluation):
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "question": question,
        "context": context,
        "answer": answer,
        "faithfulness_score": evaluation.get("faithfulness_score"),
        "answer_relevance_score": evaluation.get("answer_relevance_score"),
        "context_relevance_score": evaluation.get("context_relevance_score"),
        "hallucination_risk": evaluation.get("hallucination_risk"),
        "unsupported_claims": "; ".join(evaluation.get("unsupported_claims", [])),
        "explanation": evaluation.get("explanation")
    }


def convert_to_dataframe(row):
    return pd.DataFrame([row])
