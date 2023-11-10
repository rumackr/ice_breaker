from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain


information = """
Gabe Logan Newell (born November 3, 1962), nicknamed Gaben, is an American businessman and the president of the video game company Valve.

Newell was born in Colorado and grew up in Davis, California. He attended Harvard University in the early 1980s but dropped out to join Microsoft, where he helped create the first versions of the Windows operating system. He and another employee, Mike Harrington, left Microsoft in 1996 to found Valve, and funded the development of their first game, Half-Life (1998). Harrington left in 2000, making Newell the sole owner.

Newell led the development of Valve's digital distribution service, Steam, which was launched in 2003 and controlled most of the market for downloaded PC games by 2011. As of 2021, Newell owned at least one quarter of Valve. He has been estimated as one of the wealthiest people in the United States and the wealthiest person in the video games industry, with a net worth of $3.9 billion as of 2021. He is also the owner of Inkfish, a marine research organization

Gabe Logan Newell (born November 3, 1962), nicknamed Gaben, is an American businessman and the president of the video game company Valve.

Newell was born in Colorado and grew up in Davis, California. He attended Harvard University in the early 1980s but dropped out to join Microsoft, where he helped create the first versions of the Windows operating system. He and another employee, Mike Harrington, left Microsoft in 1996 to found Valve, and funded the development of their first game, Half-Life (1998). Harrington left in 2000, making Newell the sole owner.

Newell led the development of Valve's digital distribution service, Steam, which was launched in 2003 and controlled most of the market for downloaded PC games by 2011. As of 2021, Newell owned at least one quarter of Valve. He has been estimated as one of the wealthiest people in the United States and the wealthiest person in the video games industry, with a net worth of $3.9 billion as of 2021. He is also the owner of Inkfish, a marine research organization

"""

if __name__ == "__main__":
    print("Hello LangChain!")

    summary_template = """
        given the {information} about a person from I want you create:
        1. a short summary
        2. two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    print(chain.run(information=information))
