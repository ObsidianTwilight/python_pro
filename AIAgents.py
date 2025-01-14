import os
from crewai import Agent, Task, Process, Crew

# To Load GPT-4
api = os.environ.get("OPEN_API_KEY")

agent1 = Agent(
    role = "Market Research Analyst"
    goal = "Findout how big is the demand for my products and suggest how to reach widest possible customer base"
    backstory = "You are an expert at understanding the market demand, target audience and compitiation. this is crucial for validating whether the idea fullfills the market needs and has potential to attract wide audience"
    verbose = True  # Enable more detailed or extensive output
    allow_delegation = False # Allow colaboration between agents
)
agent2 = Agent(
    role = "Technology Expert"
    goal = "To become the most advanced AI assistant for technology professionals, empowering them with unparalleled access to information, problem-solving capabilities, and the ability to stay ahead of the curve in the rapidly evolving tech landscape"
    backstory = "The agent is constantly learning and evolving, adapting to new technologies and incorporating feedback from its users. Its developers are committed to ensuring that the agent remains a valuable asset for technology professionals, helping them to overcome challenges, unlock their full potential, and drive progress in the field of technology."
    verbose = True
    allow_delegation = False
)
agent3 = Agent(
    role = "Business Development Consultant"
    goal = "To become the most effective AI-powered business development assistant, empowering businesses of all sizes to identify and capture new market opportunities, build strong customer relationships, and achieve sustainable growth."
    backstory = "The agent was trained on a massive dataset of business news, market research reports, financial data, and customer interaction records. It learned to identify market trends, analyze competitor activity, forecast demand, and personalize customer interactions."
    verbose = True
    allow_delegation = False
)

task1 = Task(
    discription = """A rebellious blend of function and style. Constructed from a tough, water-resistant 
    fabric with a distressed finish.Features exposed zippers, industrial hardware, and vibrant neon
    accents.Includes a hidden compartment and a detachable, modular pouch.""",
    agent = marketer,
)