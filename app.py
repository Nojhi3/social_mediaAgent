import gradio as gr
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.prompts import ChatPromptTemplate
from tools import ContentIdeaTool, CaptionGeneratorTool, TrendAnalysisTool, PostSchedulerTool
from retriever import ContentRetrieverTool

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY", "AIzaSyDnIERqObCqx0nG9jGquUvskoN5A2Xs98A"),
    temperature=0.7
)

content_idea_tool = ContentIdeaTool(llm)
caption_tool = CaptionGeneratorTool(llm)
trend_tool = TrendAnalysisTool(llm)
scheduler_tool = PostSchedulerTool(llm)
retriever_tool = ContentRetrieverTool()

tools = [
    content_idea_tool,
    caption_tool,
    trend_tool,
    scheduler_tool,
    retriever_tool
]

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful social media content generation assistant. Use the available tools to help users create content ideas, captions, analyze trends, and plan their social media strategy."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    verbose=True, 
    handle_parsing_errors=True,
    max_iterations=5
)

def chat_with_agent(message, history):
    """Process user input and return agent response"""
    try:
        response = agent_executor.invoke({"input": message})
        return response["output"]
    except Exception as e:
        return f"Error: {str(e)}"

demo = gr.ChatInterface(
    fn=chat_with_agent,
    title="🎨 Social Media Content Generation Agent",
    description="Generate content ideas, captions, analyze trends, and plan your social media strategy!",
    examples=[
        "Generate 5 content ideas about AI trends",
        "Write a caption for a tech product launch",
        "Analyze current trends in the fitness niche",
        "Create a 7-day posting schedule for a SaaS company"
    ],
    chatbot=gr.Chatbot(height=500)
)

if __name__ == "__main__":
    demo.launch()
