from crewai import Task

def create_tasks(research_agent,template_analyzer, content_generator, document_assembler):
    research_task = Task(
        description="""
            Research relevant and up-to-date information related to the query.
            
            1. Analyze the query to identify key topics, industries, and focus areas
            2. Use the search tool to find current information, statistics, trends, and insights
            3. Use the web scraper to extract detailed information from relevant websites
            4. Synthesize the information into a comprehensive research report
            5. Organize the research in a way that will be useful for content generation
            
            Return a comprehensive research report with current information.
        """,
        agent=research_agent,
        expected_output="A detailed research report with current information related to the query"
    )
    
    template_analysis_task = Task(
        description="""
            Analyze the provided document template thoroughly.
            
            1. Identify the overall structure (sections, subsections, headers)
            2. Note any formatting patterns (bullet points, numbering, indentation)
            3. Identify placeholders or content areas that need to be replaced
            4. Determine the document's style, tone, and voice
            5. Create a detailed structural map of the document
            
            Return a JSON object with the complete analysis.
        """,
        agent=template_analyzer,
        expected_output="A comprehensive structural analysis of the template in JSON format"
    )
    
    content_generation_task = Task(
        description="""
            Using the template analysis, research findings, and the query, generate appropriate content.
            
            1. Review the structure analysis from the template analysis task
            2. Study the research findings carefully to incorporate current data and insights
            3. Understand the query's requirements and focus
            4. Generate content that addresses the query while fitting the template structure
            5. Incorporate relevant statistics, trends, and information from the research
            6. Ensure the content maintains consistent style, tone, and voice
            7. Format the content according to the template's patterns
            
            Return the generated content organized according to the template structure.
        """,
        agent=content_generator,
        expected_output="Generated content that addresses the query and fits the template structure",
        context=[template_analysis_task, research_task]
    )
    
    document_assembly_task = Task(
        description="""
            Assemble the final document by combining the template structure and new content.
            
            1. Review the template analysis and generated content
            2. Integrate the new content into the template structure
            3. Ensure formatting consistency throughout the document
            4. Verify that all research data is correctly incorporated
            5. Make adjustments as needed to maintain document coherence
            6. Finalize the document, ensuring it looks professional and well-structured
            
            Return the complete, transformed document.
        """,
        agent=document_assembler,
        expected_output="A complete, transformed document that maintains the template structure with new content",
        context=[template_analysis_task, content_generation_task]
    )
    
    return [research_task, template_analysis_task, content_generation_task, document_assembly_task]
