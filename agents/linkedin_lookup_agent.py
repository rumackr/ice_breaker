import re

from langchain.agents import initialize_agent, Tool, AgentType
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

from tools.tools import get_profile_url


def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """Given this persons full name {fullname} Please provide the LinkedIn profile Page.
    Provide only the URL link.
    """

    agent_tools = [
        Tool(
            name="Crawl Google for LinkedIn Profile Page",
            func=get_profile_url,
            description="useful for when you need get the Linkedin Page URL",
        )
    ]
    agent = initialize_agent(tools=agent_tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    get_url_prompt_template = PromptTemplate(
        input_variables=["fullname"], template=template
    )

    # runs the llm agent using the formated template for the prompted
    agent_return = agent.run(get_url_prompt_template.format_prompt(fullname=name))

    # gets URL link from the string thata agent.run returns.
    # I was unable to get the new implention of _process_result to just return the URL

    searchList = re.search(
        r'(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])',
        agent_return
    )

    linkedin_url = searchList.group(0)
    return linkedin_url
