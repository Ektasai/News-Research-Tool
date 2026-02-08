# 📰 News Research Tool

A powerful AI-powered tool that allows you to analyze and extract insights from news articles using natural language queries. Built with Streamlit, LangChain, and Groq's LLM, this tool processes news URLs and enables intelligent question-answering based on the article content.

## 🌟 Features

- **URL Processing**: Load and process multiple news article URLs simultaneously
- **Intelligent Text Splitting**: Automatically chunks articles into manageable segments for better analysis
- **Free Local Embeddings**: Uses HuggingFace's sentence transformers for cost-effective vector embeddings
- **Vector Database**: Implements FAISS for efficient similarity search
- **AI-Powered Q&A**: Ask questions about the news articles and get accurate answers using Groq's Llama 3.1 model
- **Chat Interface**: Interactive chat-style interface to maintain conversation history
- **Context-Aware Responses**: Answers are generated based only on the provided article content

## � Demo Video

Watch the News Research Tool in action! This demo showcases how to process news articles and ask intelligent questions:

https://github.com/Ektasai/News-Research-Tool/assets/demo.mp4

**What the demo shows:**
- Loading multiple news article URLs
- Processing and indexing the content
- Asking natural language questions
- Getting AI-powered answers based on article content
- Interactive chat interface in action

> **Note**: You can also find the demo video in the repository as `Video Project.mp4`

## �🎯 Use Cases

- **Journalists & Researchers**: Quickly extract key information from multiple news sources
- **Students**: Analyze news articles for assignments and research projects
- **Content Creators**: Gather insights and facts from news articles efficiently
- **Business Analysts**: Monitor and analyze news related to specific industries or topics
- **General Users**: Stay informed by querying news articles in natural language

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **LLM**: Groq (Llama 3.1-8b-instant)
- **Embeddings**: HuggingFace Sentence Transformers (all-MiniLM-L6-v2)
- **Vector Store**: FAISS
- **Framework**: LangChain
- **Document Processing**: UnstructuredURLLoader

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)
- Git
- A Groq API key (free to obtain from [Groq Console](https://console.groq.com/))

## 🚀 Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/Ektasai/News-Research-Tool.git
cd News-Research-Tool
```

### Step 2: Create a Virtual Environment (Recommended)

**For Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**For macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

The project uses specific versions of libraries. Install them using:

```bash
pip install -r requirements.txt
```

**Note**: The current `requirements.txt` has outdated dependencies. For better compatibility, use these updated versions:

```bash
pip install langchain-community langchain-groq langchain-text-splitters
pip install streamlit
pip install python-dotenv
pip install unstructured
pip install faiss-cpu
pip install sentence-transformers
pip install tiktoken
```

### Step 4: Set Up Environment Variables

1. Create a `.env` file in the project root directory:

```bash
# For Windows
copy .env.example .env

# For macOS/Linux
cp .env.example .env
```

2. Get your Groq API key:
   - Visit [Groq Console](https://console.groq.com/)
   - Sign up or log in
   - Navigate to API Keys section
   - Create a new API key
   - Copy the key

3. Edit the `.env` file and add your API key:

```env
GROQ_API_KEY=your_actual_groq_api_key_here
```

### Step 5: Run the Application

```bash
streamlit run main.py
```

The application will open in your default web browser at `http://localhost:8501`

## 📖 How to Use

### Processing News Articles

1. **Enter URLs**: In the sidebar, paste news article URLs (one per line)
2. **Process**: Click the "Process URLs" button
3. **Wait**: The tool will:
   - Load the articles
   - Split them into chunks
   - Create embeddings
   - Store them in a vector database

### Asking Questions

1. **Type Your Question**: Enter your question in the text input field
2. **Get Answers**: The AI will analyze the processed articles and provide relevant answers
3. **Continue Conversation**: Ask follow-up questions to dig deeper
4. **Clear Chat**: Use the "Clear Chat" button to start a new conversation

### Example Workflow

```
1. Add URLs:
   https://example.com/article1
   https://example.com/article2

2. Click "Process URLs"

3. Ask questions like:
   - "What are the main points discussed in these articles?"
   - "Who are the key people mentioned?"
   - "What are the implications of this news?"
   - "Summarize the articles in 3 bullet points"
```

## 📁 Project Structure

```
News-Research-Tool/
│
├── main.py                    # Main application file
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (API keys)
├── .gitattributes            # Git configuration
├── faiss_store.pkl           # Vector database (generated after processing)
├── Video Project.mp4         # Demo video
└── .vscode/                  # VS Code settings
```

## 🔧 Configuration

### Customizing Parameters

You can modify these parameters in `main.py`:

- **Chunk Size**: Change `chunk_size=2000` to adjust text splitting
- **Chunk Overlap**: Modify `chunk_overlap=50` for context preservation
- **Number of Documents**: Adjust `docs = docs[:25]` to process more/fewer chunks
- **Similarity Search Results**: Change `k=4` in `similarity_search()` for more/fewer context documents
- **LLM Temperature**: Modify `temperature=0.2` for more creative (higher) or deterministic (lower) responses

### Switching LLM Models

To use a different Groq model, change the model name in `main.py`:

```python
llm = ChatGroq(
    model="llama-3.1-70b-versatile",  # or other available models
    temperature=0.2
)
```

Available Groq models:
- `llama-3.1-8b-instant` (default, fastest)
- `llama-3.1-70b-versatile` (more capable)
- `mixtral-8x7b-32768` (good for longer contexts)

## 🐛 Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'langchain'`
- **Solution**: Install the updated dependencies as mentioned in Step 3

**Issue**: `Invalid API Key`
- **Solution**: Ensure your `.env` file has the correct Groq API key without quotes

**Issue**: `Error loading articles`
- **Solution**: Check if the URLs are accessible and contain text content

**Issue**: `FAISS installation fails`
- **Solution**: Use `pip install faiss-cpu` instead of `faiss-gpu` (unless you have CUDA)

**Issue**: Application doesn't start
- **Solution**: Ensure you're in the correct directory and virtual environment is activated

## 🔮 Future Improvements

### Planned Features

1. **Multi-Language Support**
   - Add support for processing and querying articles in multiple languages
   - Implement automatic language detection

2. **Enhanced Document Processing**
   - Support for PDF documents
   - Support for Word documents and other formats
   - Better handling of images and tables in articles

3. **Advanced Search Capabilities**
   - Semantic search with filters (date, source, topic)
   - Keyword highlighting in source documents
   - Citation tracking (which article answered which question)

4. **User Experience Improvements**
   - Save and load conversation history
   - Export Q&A sessions as PDF/Markdown
   - Bookmark important answers
   - Dark/Light theme toggle

5. **Performance Enhancements**
   - Caching mechanism for frequently accessed articles
   - Parallel processing for multiple URLs
   - Incremental updates to vector database

6. **Analytics Dashboard**
   - Visualize article topics
   - Track most asked questions
   - Show article sentiment analysis
   - Display entity extraction (people, organizations, locations)

7. **Collaboration Features**
   - Share research sessions with team members
   - Collaborative annotation of articles
   - Team workspaces

8. **Integration Options**
   - Browser extension for one-click article processing
   - API endpoint for programmatic access
   - Integration with note-taking apps (Notion, Evernote)

9. **Advanced AI Features**
   - Automatic summarization of articles
   - Fact-checking capabilities
   - Bias detection in news sources
   - Related article recommendations

10. **Database Improvements**
    - Persistent database (PostgreSQL/MongoDB)
    - Article metadata storage
    - Version control for processed articles

---

**Happy Researching! 📰🔍**
