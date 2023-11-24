from typing import List

from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


class PersonIntel(BaseModel):
    summary: str = Field(description="Summary of person")
    facts: List[str] = Field(description="Interesting facts about the person")
    topics_of_interest: List[str] = Field(description="Topics that are interest to this person")
    ice_breakers: List[str] = Field(description="Create Ice breakers to start a converstion with this person")

    def to_dict(self):
        to_ret = {
            "summary": self.summary,
            "facts": self.facts,
            "topics_of_interest": self.topics_of_interest,
            "ice_breakers": self.ice_breakers,
        }

        return to_ret


person_intel_parser: PydanticOutputParser = PydanticOutputParser(
    pydantic_object=PersonIntel
)
