# CrewAI-Document-Agent

A powerful AI-driven application that transforms document templates into customized documents based on user queries. This project leverages multiple specialized AI agents working in sequence to research, analyze, generate content, and assemble professional-quality documents.

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/CrewAI-Framework-orange)](https://github.com/joaomdmoura/crewAI)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## 🚀 Features

- **Multi-agent AI system** with specialized roles
- **Template analysis** to understand document structure
- **Web research** to incorporate current information
- **Intelligent content generation** tailored to your needs
- **Professional document assembly** with consistent formatting
- **Multiple file format support** (DOCX, PDF, TXT, MD)
- **Interactive UI** with real-time progress tracking

## 🏗️ Architecture

The system employs four specialized AI agents working in sequence:

1. **Research Specialist**: Gathers up-to-date information relevant to your query
2. **Template Analyzer**: Analyzes document structures to identify format and components
3. **Content Generator**: Creates new content based on query and research findings
4. **Document Assembler**: Integrates content into the template structure

## 🛠️ Installation

### Prerequisites

- Python 3.9 or higher
- Pip package manager

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Abhi-vish/crewAI-document-agent.git
   cd crewAI-document-agent
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with your API keys:
   ```
   GEMINI_API_KEY=your_gemini_api_key
   SERPER_API_KEY=your_serper_api_key
   ```

### Running the Application

Start the Streamlit app:
```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

## 📊 Usage

1. **Upload your template document** (DOCX, PDF, TXT, or MD format)
2. **Enter your transformation query** describing how you want the document changed
3. **Click "Transform Document"** to start the process
4. **Monitor progress** as the AI agents work
5. **Preview the result** and download in your preferred format

## 💻 Example Queries

- "Transform this meeting minutes template for a marketing team's weekly sync"
- "Convert this business proposal template for a software development project"
- "Update this policy document to reflect current cybersecurity best practices"
- "Adapt this case study template for a healthcare implementation project"

## 📁 Project Structure

```
crewAI-document-agent/
├── app.py                 # Main Streamlit application
├── src/
│   └── config/
│       ├── agents.py      # AI agent definitions
│       └── tasks.py       # Task configuration for agents
├── assets/                # Images and other static assets
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## ⚙️ Dependencies

- **CrewAI**: Framework for creating and managing AI agent teams
- **Streamlit**: User interface framework
- **python-docx**: DOCX file handling
- **PyPDF2**: PDF processing
- **mammoth**: DOCX text extraction
- **python-magic**: File type detection

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## 📬 Contact

Project Link: [https://github.com/Abhi-vish/crewAI-document-agent](https://github.com/Abhi-vish/crewAI-document-agent)

---

Built with ❤️ using [CrewAI](https://github.com/joaomdmoura/crewAI) and [Streamlit](https://streamlit.io/)