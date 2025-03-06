from pydantic import BaseModel, Field
from typing import Optional, List, Tuple
from openai import OpenAI
import os, logging

# ============================
# Set up logging configuration
# ============================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = "gpt-4o-mini"

# ===========================================
# Step 1 - Define data models for each stage
# ===========================================

class Context(BaseModel):
    """First LLM call: Extract any inputs provided by user"""
    
    goals: List[str] = Field(default_factory=list, input="Extract fitness / diet goals")
    constraints: Optional[List[str]] = Field(default_factory=list, input="Extract any constraints (e.g. allergies, caloric deficit)")
    requirements: Optional[List[str]] = Field(default_factory=list, input="Extract any requirements provided (e.g. diet type, vitamin needs)")
    
class Fidelity(BaseModel):
    """Parallel LLM call: Assess level of fidelity given by user"""
    
    fidelity: str = Field(input="How detailed are the requested recommendations [low, medium, high]")
    fidelity_score: float = Field(description="How detailed is the request between 0 and 1, with being the highest. Consider detail of goals, constraints and requirements.")

# ==========================================
# Step 2 - Define functions
# ==========================================

def extract_details(input: str) -> Context:
    """First LLM call to extract user details"""
    logger.info("Extracting user provided details")

    completion = client.beta.chat.completions.parse(
        model = model,
        messages = [
            {
                "role" : "system",
                "content" : "Extract relevant nutritional details provided by the user"
            },
            {
                "role" : "user",
                "content" : input
            }
        ],
        response_format = Context,
    )
    result = completion.choices[0].message.parsed
    logger.info(f"Tokens spent: {completion.usage.total_tokens}")
    return result


def fidelity_level(input: str) -> Fidelity:
    """Parallel LLM call to determine level of fidelity"""
    logger.info("Determining fidelity level provided by the user")

    completion = client.beta.chat.completions.parse(
        model = model,
        messages = [
            {
                "role" : "system",
                "content" : "Assess level of fidelity of input from user"
            },
            {
                "role" : "user",
                "content" : input
            }
        ],
        response_format = Fidelity,
    )
    
    logger.info(f"Tokens spent: {completion.usage.total_tokens}")
    result_2 = completion.choices[0].message.parsed
    print(result_2)
    return result_2

def identify_missing_details(details: Context):
    
    missing_fields = []
    present_fields = []
    prompt = []
    
    if not details.goals:
        missing_fields.append("goals")
    else:
        present_fields.append(f"Goals are: {details.goals}")
        
    if not details.constraints:
        missing_fields.append("constraints")
    else:
        present_fields.append(f"Constraints are: {details.constraints}")
        
    if not details.requirements:
        missing_fields.append("requirements")
    else:
        present_fields.append(f"Requirements are: {details.requirements}")
    
    if present_fields:
        present_fields_str = ', '.join(present_fields)
        prompt = f"The user has specified the following: {present_fields_str}."
        
    if missing_fields:
        missing_fields_str = ', '.join(missing_fields)
        prompt2 = prompt + f"Please ask relevant questions for the user's: {missing_fields_str}."
        
    logger.info(f"Present fields: {present_fields}, Missing fields: {missing_fields}")
    
    return prompt2
        

def request_info(prompt2: str):

    completion = client.beta.chat.completions.parse(
        model = model,
        messages = [
            {
                "role" : "system",
                "content" : "You are a helpful nutritionist that asks clarifying questions. Split questions into 3 possible categories: goals, constraints, resources"
            },
            {
                "role" : "user",
                "content" : prompt2
            }
        ],
    )
    
    logger.info(f"Tokens spent: {completion.usage.total_tokens}")
    # add_context = completion.choices[0].message.parsed
    
    print(completion.choices[0].message.content)
    
    get_context = input("Please answer some of the questions so we can help you more effectively! \n")
    
    return get_context


def nutrition_assessment(final_prompt):

    completion = client.beta.chat.completions.parse(
        model = model,
        messages = [
            {
                "role" : "system",
                "content" : "You are a helpful nutritionist and dietician."
            },
            {
                "role" : "user",
                "content" : final_prompt
            }
        ],
    )
    
    logger.info(f"Tokens spent: {completion.usage.total_tokens}")
    # add_context = completion.choices[0].message.parsed
    
    return completion.choices[0].message.content

# ==========================================
# Testing functions
# ==========================================

user_input = "Please create a meal plan for me, I want to lose weight by 5 kgs"

details = extract_details(user_input)
fidel = fidelity_level(user_input)
prompt2 = identify_missing_details(details)
add_context = request_info(prompt2)

# Append extra input to current prompt
final_prompt = user_input + add_context

# Final prompt to nutritionist
print(nutrition_assessment(final_prompt))