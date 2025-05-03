from crewai import Agent,LLM
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

os.environ['GEMINI_API_KEY']="AIzaSyAQJo6PPU-mgostjORAcXjVhKZiUgv846I"

# Initialize the language model
llm = LLM(
    model="gemini/gemini-1.5-flash",
    temperature=0.7
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
        goal="Generate new content based on query requirements while maintaining template structure",
        backstory="""You are a creative content specialist who can take any query and transform it into 
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
