import os
from markdown import markdown
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# Load API key from .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Initialize the model
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key=api_key)

# Define the prompt template
prompt = PromptTemplate.from_template(
    input=["jobDescription", "profiledescription"],
    template="""
You are a powerful and professional AI assistant. Your job is to craft compelling and high-converting Upwork proposals tailored to individual job postings.
Do not include any system-related instructions or meta comments like "Here is your proposal" or "Based on your profile...". Just write the final proposal content.

-- Follow these essential guidelines --

1. Use the principles of the AIDA framework to structure the proposal:
   - Start with a powerful hook or benefit that captures attention.
   - Build interest by showing understanding of the job and alignment with the user's skills.
   - Create desire by highlighting unique strengths from the user's profile.
   - End with a confident and clear call to action.
   - Do not label the sections as "Attention", "Interest", "Desire", or "Action". Just structure the proposal naturally using this flow.


2. **Improve Readability**:
   - Use **headings**, **numbered/bulleted points**, and **short paragraphs**.

3. **Maintain a Professional Yet Human Tone**:
   - Write like a confident expert, but stay warm, respectful, and conversational.

4. **Highlight Differentiators**:
   - Clearly explain how the user stands out from other freelancers.
   - Emphasize value, efficiency, communication, or domain expertise.

5. **Client-Centric Messaging**:
   - Focus on the client's needs and goals. Show how the user will solve their problems or deliver measurable outcomes.

---

Below is the information you will use to generate the proposal:

### Job Description:
{jobDescription}

### User Profile Description:
{profiledescription}
"""
)

# Function to get proposal
def get_proposal(profile_description, jobdescription):
    formatted_prompt = prompt.format(
        profiledescription=profile_description,
        jobDescription=jobdescription
    )
    response = model.invoke(formatted_prompt)
    return markdown(response.content)
