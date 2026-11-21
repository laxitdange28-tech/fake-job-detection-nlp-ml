from pydantic import BaseModel, Field


class JobInput(BaseModel):

    title: str
    company_profile: str = ""
    description: str
    requirements: str = ""
    benefits: str = ""

    employment_type: str = "Missing"
    required_experience: str = "Missing"
    required_education: str = "Missing"

    industry: str = "Missing"
    function: str = "Missing"
    location: str = "Missing"

    telecommuting: int = Field(default=0, ge=0, le=1)
    has_company_logo: int = Field(default=0, ge=0, le=1)
    has_questions: int = Field(default=0, ge=0, le=1)