from crewai import Agent, Task, Crew, Process,LLM
from langchain.llms import Anthropic
import os
from dotenv import load_dotenv
import argparse
import json
from pathlib import Path
from src.config.agents import create_template_analyzer, create_content_generator, create_document_assembler
from src.config.tasks import create_tasks
import json
from pathlib import Path
import docx
import PyPDF2
import mammoth
import mimetypes
import magic

class DocumentTransformer:
    def __init__(self):
        # Create agents
        self.template_analyzer = create_template_analyzer()
        self.content_generator = create_content_generator()
        self.document_assembler = create_document_assembler()

        # Create tasks
        self.tasks = create_tasks(
            self.template_analyzer,
            self.content_generator,
            self.document_assembler
        )

        # Setup crew
        self.crew = Crew(
            agents=[
                self.template_analyzer,
                self.content_generator,
                self.document_assembler
            ],
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )

    def transform_document(self, template, query):
        # Update task descriptions
        self.crew.tasks[0].description += f"\n\nTEMPLATE:\n{template}\n\nQUERY:\n{query}"
        self.crew.tasks[1].description += f"\n\nQUERY:\n{query}"
        self.crew.tasks[2].description += f"\n\nORIGINAL TEMPLATE:\n{template}"

        # Run crew
        result = self.crew.kickoff()
        return result
def extract_text_from_file(file_path):
    """
    Extract text from various file formats (txt, docx, pdf)
    
    Args:
        file_path (Path): Path to the file
        
    Returns:
        str: Extracted text content
    """
    # Detect file type using python-magic
    mime = magic.Magic(mime=True)
    file_type = mime.from_file(str(file_path))
    
    # Alternative detection using file extension if magic detection fails
    if file_type == 'application/octet-stream':
        ext = file_path.suffix.lower()
        if ext == '.docx':
            file_type = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        elif ext == '.pdf':
            file_type = 'application/pdf'
        elif ext == '.txt' or ext == '.md':
            file_type = 'text/plain'
    
    print(f"Detected file type: {file_type}")
    
    # Extract text based on file type
    if file_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' or '.docx' in str(file_path).lower():
        # Process DOCX
        with open(file_path, 'rb') as docx_file:
            result = mammoth.extract_raw_text(docx_file)
            return result.value
    
    elif file_type == 'application/pdf' or '.pdf' in str(file_path).lower():
        # Process PDF
        text = ""
        with open(file_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text() + "\n"
        return text
    
    else:  # Default to text file
        # Process TXT/MD
        with open(file_path, "r", encoding="utf-8") as text_file:
            return text_file.read()

def save_output(content, output_file):
    """
    Save output to the appropriate format based on file extension
    
    Args:
        content (str): Content to save
        output_file (str): Path to save the content
    """
    output_path = Path(output_file)
    ext = output_path.suffix.lower()
    
    if ext == '.docx':
        # Save as DOCX
        doc = docx.Document()
        
        # Split content by lines and add to document
        paragraphs = content.split('\n')
        for para in paragraphs:
            if para.strip():  # Skip empty lines
                # Check if paragraph is a heading (starts with #)
                if para.startswith('# '):
                    doc.add_heading(para[2:], 0)  # Title
                elif para.startswith('## '):
                    doc.add_heading(para[3:], 1)
                elif para.startswith('### '):
                    doc.add_heading(para[4:], 2)
                elif para.startswith('#### '):
                    doc.add_heading(para[5:], 3)
                else:
                    doc.add_paragraph(para)
        
        doc.save(output_path)
        print(f"Transformed document saved as DOCX to '{output_file}'")
    
    elif ext == '.pdf':
        # For PDF, we'll save as text for now and inform the user
        # (Full PDF creation would require additional libraries like reportlab)
        with open(output_path.with_suffix('.txt'), "w", encoding="utf-8") as f:
            f.write(content)
        print(f"PDF output requested, but saved as text to '{output_path.with_suffix('.txt')}' instead.")
        print("Note: For proper PDF creation, consider using a dedicated PDF library.")
    
    else:  # Default to text file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Transformed document saved to '{output_file}'")

def main():
    parser = argparse.ArgumentParser(description="Transform document templates based on queries")
    parser.add_argument("--template_file", type=str, required=True, help="Path to the template file (txt, docx, pdf)")
    parser.add_argument("--query", type=str, required=True, help="Query for content transformation")
    parser.add_argument("--output_file", type=str, default="transformed_document.txt", help="Path to save the transformed document (supports txt, docx)")
    
    args = parser.parse_args()
    
    # Read the template file
    template_path = Path(args.template_file)
    if not template_path.exists():
        print(f"Error: Template file '{args.template_file}' not found.")
        return
    
    # Detect file type and extract text accordingly
    template_content = extract_text_from_file(template_path)
    
    # Transform the document
    transformer = DocumentTransformer()
    result = transformer.transform_document(template_content, args.query)
    
    # Save the result
    save_output(str(result), args.output_file)

if __name__ == "__main__":
    main()