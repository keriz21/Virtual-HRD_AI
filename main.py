import os
import asyncio
from dotenv import load_dotenv

from flow.flow import (
    a_generate_questions,
    b_create_summary,
    c_review_summary,
    d_ask_questions
)

import tools.tools as tools

from models.question_model import generate_questions

from agent.question_agent import interview_agent

from agents import Runner
# Load environment variables from .env file
load_dotenv()



async def main():
    # print(await a_generate_questions('682c2a2e08157ab12005f047'))
    # tools.push_answered_questions('682c2a2e08157ab12005f047', 'saya juga suka manusia kok')
    # print(await d_ask_questions('682c2a2e08157ab12005f047'))
    # tools.push_answered_questions('682c3b26d60e12ac9c94dc5c', 'saya sangat suka jawaban anda? anda pantas menerima jabatan ini')
    # print(tools.get_answered_questions('682c3b26d60e12ac9c94dc5c'))
    # print(await c_review_summary('682c44e2a31ffac7c69ffcd5'))
    # print(await c_review_summary('682d5c32401b5af76cf861ca'))
    # print(tools.get_status_interview('682f493a6bf9b22e5c0b3168'))
    print(await c_review_summary('684a49bbbb946aef7d7705ff'))
    print(tools.get_status_interview('684a49bbbb946aef7d7705ff'))
    pass

asyncio.run(main())