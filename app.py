import streamlit as st
import plotly.graph_objects as go
from dotenv import load_dotenv

from src.evaluator import evaluate_llm_response
from src.utils import create_result_row, convert_to_dataframe

load_dotenv()

st.set_page_config(
    page_title="LLM Evaluation Dashboard",
    page_icon="🧠",
    layout="wide"
)

st.title("LLM Evaluation and Hallucination Detection Dashboard")

st.write(
    "Evaluate LLM responses for faithfulness, relevance, context quality, "
    "and hallucination risk."
)

with st.sidebar:
    st.header("Project Info")
    st.write("This tool evaluates whether an LLM answer is grounded in retrieved context.")
    st.write("Useful for RAG evaluation, chatbot QA testing, and GenAI reliability checks.")

question = st.text_area(
    "User Question",
    placeholder="Example: What is retrieval augmented generation?",
    height=100
)

context = st.text_area(
    "Retrieved Context",
    placeholder="Paste retrieved context here...",
    height=180
)

answer = st.text_area(
    "LLM Answer",
    placeholder="Paste the LLM-generated answer here...",
    height=180
)

if st.button("Evaluate Response"):
    if not question or not context or not answer:
        st.warning("Please fill in the question, context, and answer.")
    else:
        with st.spinner("Evaluating LLM response..."):
            evaluation = evaluate_llm_response(question, context, answer)

        st.subheader("Evaluation Results")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Faithfulness", evaluation.get("faithfulness_score", 0))
        col2.metric("Answer Relevance", evaluation.get("answer_relevance_score", 0))
        col3.metric("Context Relevance", evaluation.get("context_relevance_score", 0))
        col4.metric("Hallucination Risk", evaluation.get("hallucination_risk", "Unknown"))

        scores = {
            "Faithfulness": evaluation.get("faithfulness_score", 0),
            "Answer Relevance": evaluation.get("answer_relevance_score", 0),
            "Context Relevance": evaluation.get("context_relevance_score", 0)
        }

        fig = go.Figure(
            data=[
                go.Bar(
                    x=list(scores.keys()),
                    y=list(scores.values())
                )
            ]
        )

        fig.update_layout(
            title="LLM Response Evaluation Scores",
            yaxis=dict(range=[0, 100])
        )

        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Unsupported Claims")
        unsupported_claims = evaluation.get("unsupported_claims", [])

        if unsupported_claims:
            for claim in unsupported_claims:
                st.warning(claim)
        else:
            st.success("No major unsupported claims detected.")

        st.subheader("Evaluator Explanation")
        st.write(evaluation.get("explanation", ""))

        result_row = create_result_row(question, context, answer, evaluation)
        result_df = convert_to_dataframe(result_row)

        st.download_button(
            label="Download Evaluation as CSV",
            data=result_df.to_csv(index=False),
            file_name="llm_evaluation_result.csv",
            mime="text/csv"
        )
