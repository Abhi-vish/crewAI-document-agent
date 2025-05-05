from crewai import Agent,LLM
from dotenv import load_dotenv
import os
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from dotenv import load_dotenv

load_dotenv()

os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

# Initialize tools
search_tool = SerperDevTool()
scraper_tool = ScrapeWebsiteTool()

# Load environment variables from .env file
load_dotenv()

os.environ['GEMINI_API_KEY']= os.getenv('GEMINI_API_KEY')

# Initialize the language model
llm = LLM(
    model="gemini/gemini-1.5-flash",
    temperature=0.7
)

def create_research_agent():
    return Agent(
        role="Research Specialist",
        goal="Gather up-to-date information and data relevant to the transformation query",
        backstory="""You are an expert researcher with exceptional skills in finding and synthesizing 
                    relevant information from the web. You excel at identifying key trends, data, and 
                    insights that will make document content accurate, current, and compelling.""",
        llm=llm,
        verbose=True,
        allow_delegation=False,
        tools=[search_tool, scraper_tool],
        max_iter=4,
    )

def create_template_analyzer():
    return Agent(
        role="Template Structure Analyst",
        goal="Deeply analyze document templates to identify their structure, format, and key components",
        backstory="""You are an expert in document analysis with years of experience in breaking down
                    documents into their structural elements. Your specialty is understanding document
                    templates regardless of their content or domain.""",
        llm=llm,
        verbose=True,
        allow_delegation=False
    )

def create_content_generator():
    return Agent(
        role="Content Transformation Specialist",
        goal="Generate new content based on query requirements and research findings while maintaining template structure",
        backstory="""You are a creative content specialist who can take any query and research data to transform it into 
                    appropriate content that fits a given template structure. You have a talent for adapting
                    content across different domains while preserving the original document's style and format.""",
        llm=llm,
        verbose=True,
        allow_delegation=False
    )

def create_document_assembler():
    return Agent(
        role="Document Assembly Expert",
        goal="Assemble the final document by integrating new content into the template structure",
        backstory="""You are a document engineering specialist who excels at bringing together structural 
                    elements and content into cohesive, polished documents. You ensure the final document 
                    maintains proper formatting, style consistency, and professional quality.""",
        llm=llm,
        verbose=True,
        allow_delegation=False
    )