from langchain.agents import create_agent

from llm import get_llm
from tools import get_job_recommendations, get_resume_data, web_search

tool_list = [web_search, get_job_recommendations, get_resume_data]
llm_model = get_llm()

system_message = """
You are an Expert Job Matcher. Your task is to find live jobs matching the candidates
resume.

Follow these 4 execution steps sequestionally:

1. Retriever Resume:Call `get_resume_data` using simple keywords
2. Extract Logic: From the retrieve resume, identify candidate experience
and pick 1 or 2 job keywords and set a realistic minimum annual salary in INR.
3. Search Jobs: Call `get_job_recommendation` using extracted parameters.

Present live job results returned by the tool
"""
agent = create_agent(
    model=llm_model,
    tools=tool_list,
    system_prompt=system_message,
)

def run_agent():
    response = agent.invoke(
        {"messages": [{"role": "user","content":"Find me a job based on my resume"}]}
    )

    return response

response = run_agent()
print(response)