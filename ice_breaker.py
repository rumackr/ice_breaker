from typing import Tuple

from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parsers import person_intel_parser, PersonIntel
from third_parties.linkedin import scrape_linkedin_profile


def ice_break(name: str) -> Tuple[PersonIntel, str]:
    linkedin_profile_url = linkedin_lookup_agent(name=name)

    summary_template = """
        Given the Linkedin {information} about a person from I want you create:
        1. a short summary
        2. two interesting facts about them
        3. A topic that may interest them.
        4. 2 creative Ice breakers to open A Conversation with them
        \n{format_instructions} 
        """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": person_intel_parser.get_format_instructions()
        },
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_profile_url
    )

    result = chain.run(information=linkedin_data)
    print(linkedin_data.get("profile_pic_url"))
    return person_intel_parser.parse(result), linkedin_data.get("profile_pic_url")


if __name__ == "__main__":
    print("Hello LangChain!")
    result, profial_pic_url = ice_break(name="Reid Rumack")
    print(profial_pic_url)
