from agno.agent import Agent
from agno.tools.yfinance import YFinanceTools
from agno.models.ollama import Ollama
from agno.tools import tool
from agno.team.team import Team
import random
from rich.pretty import pprint
from GmailEmailSender import GmailEmailSender
from agno.embedder.ollama import OllamaEmbedder
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.knowledge.pdf import PDFKnowledgeBase, PDFReader
from ollama import Client
from pydantic import BaseModel, Field
client = Client(host='http://ollama.ollama.svc.cluster.local:11434')


#receiver: This argument contains the recipient's email address, message_body: This argument contains the body of the message, email_subject: This argument contains the subject line of the message. 

class Email_message(BaseModel):
    receiver: str = Field(..., description="Contains the recipient's email address.")
    message_body: str = Field(..., description="Contains the body of the message.")
    email_subject: str = Field(..., description="Contains the subject line of the message.")
    
# @tool(show_result=True, stop_after_tool_call=True)
# def Print_Email(email_message:Email_message ) -> str:
#     """This tool is for Print email."""
   
#     try:

#           # Unique ID per user
#         print(email_message.receiver)
#         print(email_message.message_body)
#         print(email_message.email_subject)
        
#         return "Print successfully"
#     except Exception as e:
       
#         return "Print failed"






Writing_Email_agent = Agent(
    name="Writing Email agent",
    role="Writing an email about a topic",
    model=Ollama(id="Qwen2.5-Coder-32B-Instruct-Q6_K_L:latest",client=client),
    instructions=["You are an Agent who writes the email.",
                  "Write a professional email, and prepare the receiver (email address), email_subject (subject line), and message_body (body of the message).",
                  "Implement things, use tools, and do not overthink and explain"],
    markdown=True,
    response_model=Email_message,
    use_json_mode=True,
)


# Print_Email_agent = Agent(
#     name="Print Email agent",
#     role="Print an email about a topic",
#     tools=[Print_Email],
#     model=Ollama(id="Qwen2.5-Coder-32B-Instruct-Q6_K_L:latest",client=client),
#     instructions=["You are an Agent who Print the email.",
#                   "Just use the tool, don't do anything yourself."],
#     markdown=True,
# )




agent_team = Team(
    name="Team leader",
    model=Ollama(id="Qwen2.5-Coder-32B-Instruct-Q6_K_L:latest",client=client),  # You can use a different model for the team leader agent
    members=[Writing_Email_agent],
    instructions=["""Always use the info that is available in the tools only.
                    If you receive 'Print successfully' or 'Print failed' from the tool, stop sending another email.""",
                    "Implement things, use tools, and do not overthink and explain",
                    "Writing_Email_agent for writing emails"
                     "Print_Email_agent to print email"],
    show_tool_calls=True,  # Uncomment to see tool calls in the response
    markdown=True,
)

# Give the team a task
agent_team.print_response("Write an email and Print it to Yahya(y75910@gmail.com) to come today for dinner at 8 pm.", stream=True)

# if __name__ == "__main__":

#     agent_team.print_response("Who is the best singer in my country KSA song ?")
#     agent_team.print_response("What is the weather like in my country?")

    # Print all messages in this session
    #messages_in_session = agent_team.get_messages_for_session()
    #pprint(messages_in_session)



 

