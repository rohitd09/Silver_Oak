from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool

import requests

import os
from dotenv import load_dotenv

from rag import vector_store

load_dotenv()

web_search = DuckDuckGoSearchRun()

# response = web_search.invoke("LA Olymipics")
# print(response)

@tool
def get_job_recommendations(what: str, salary_min: int) -> str:
    """
    Searches live Indian job listsing by keyword and minimum salary

    Input Parameters:
    what - One or more SINGLE KEYWORDS, space separated. This is
    NOT a job title. User only core keywords like "software", "data", 
    "python" etc. Do not use job titles like "Software Engineer", 
    "Data Scientist" etc.

    salary_min - Minimum salary in INR. 
    For example, 1000000 for 10 LPA.
    """
    url = f"https://api.adzuna.com/v1/api/jobs/in/search/1?app_id={os.getenv("ADZUNA_APP_ID")}&app_key={os.getenv("ADZUNA_API_KEY")}&what={what}&salary_min={salary_min}"

    response =requests.get(url)
    return response.json()

# jobs = get_job_recommendations.invoke({"what": "software", "salary_min": 1000000})
# print(jobs)

# print("Tool Name: ", get_job_recommendations.name)
# print("Tool Description: ", get_job_recommendations.description)
# print("Tool Arguments: ", get_job_recommendations.args)

@tool
def get_resume_data(query:str) -> str:
    """
    Retrieves chunks of the candidate's resume via similarity search.

    Input Parameters:
    query (str) - A resume TOPIC to search for, e.g. "skills", "work experience",
        "education", "years of experience". This must be a topic that appears IN
        the resume itself — not an instruction, judgment, or classification task
        (e.g. do NOT query "seniority level classification"; instead query "work
        experience" and determine seniority yourself from what's returned).

    Returns:
    A list of matching resume text chunks. Content is chunked, so multiple calls
    with different topic queries are usually needed to get a full picture.

    Example: get_resume_data(query="skills")
    """

    response = vector_store.similarity_search(query)
    return response

response = get_resume_data.invoke("skills")
print(response)