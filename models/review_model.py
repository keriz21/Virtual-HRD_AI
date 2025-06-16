from agents import Runner
from flask import jsonify
from agent.review_agent import review_agent
import tools.tools as tools

async def review_summary(list_pertanyaan, list_answered_question, data_ringkasan: str) -> bool:
    
    """
    Review the summary of the applicant's answers based on the interview questions.
    """
    list_pertanyaan_str =tools.list_question_to_string(list_pertanyaan)
    list_answered_question_str = "\n".join(list_answered_question) if list_answered_question else ""
    input_prompt = f"Daftar pertaynyaan yang perlu ditanyakan:\n{list_pertanyaan_str}\n\nRingkasan jawaban pelamar:\n{data_ringkasan}\n\nDaftar pertanyaan yang sudah dijawab:\n{list_answered_question_str}"

    result = await Runner.run(review_agent, input_prompt)
    review = result.final_output.is_finish
    return review
