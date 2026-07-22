# 🚀 AI LinkedIn Post Generator

An AI-powered LinkedIn post generator built using **LangChain**, **Groq Llama**, **Few-Shot Prompting**, and **Streamlit**. The application generates high-quality LinkedIn posts by retrieving similar examples from a preprocessed dataset instead of fine-tuning a language model.

---

## Output : 
<img width="795" height="279" alt="image" src="https://github.com/user-attachments/assets/46fd1d02-b1ec-48dc-b544-6b7be65c77d9" />

## 📌 Features

- ✨ Generate LinkedIn posts on different topics
- 🌐 Supports multiple languages (English & Hinglish)
- 📏 Generate Short, Medium, or Long posts
- 🧠 Few-Shot Learning using real LinkedIn posts
- ⚡ Fast runtime using preprocessed metadata
- 🎨 Simple Streamlit interface

---

## 🛠️ Tech Stack

- Python
- LangChain
- Groq Llama 3
- Streamlit
- Pandas
- JSON
- Prompt Engineering

---

# 📂 Project Structure

```
AI_LinkedIn_Post_Generator/
│
├── app.py / main.py              # Streamlit application
├── preprocess.py                 # Offline preprocessing
├── few_shot.py                   # Loads and filters examples
├── post_generator.py             # Builds prompt & generates post
├── raw_posts.json                # Original LinkedIn dataset
├── processed_posts.json          # Metadata-enriched dataset
├── requirements.txt
└── README.md
```

---

# 🏗️ Project Architecture

```
                Raw LinkedIn Posts
                        │
                        ▼
              preprocess.py
                        │
        Extract Metadata using LLM
        • Language
        • Tags
        • Line Count
                        │
        Normalize Similar Tags
                        │
                        ▼
          processed_posts.json
                        │
                        ▼
                FewShotPosts
                        │
      Load JSON into DataFrame
                        │
                        ▼
      Filter by Topic, Length & Language
                        │
                        ▼
             Prompt Construction
                        │
          Add Matching Examples
                        │
                        ▼
                Groq LLM
                        │
                        ▼
          Generated LinkedIn Post
```

---

# ⚙️ How It Works

The project consists of **two phases**.

## Phase 1 – Offline Preprocessing

The preprocessing script runs only once.

It:

- Reads raw LinkedIn posts
- Uses an LLM to extract metadata
- Calculates:
  - Language
  - Number of lines
  - Tags
- Normalizes similar tags
- Saves everything into `processed_posts.json`

Example:

### Raw Post

```json
{
    "text": "Networking is more powerful than resumes."
}
```

↓

Metadata extracted

```json
{
    "language": "English",
    "line_count": 1,
    "tags": [
        "Job Search",
        "Networking"
    ]
}
```

↓

Saved as

```json
{
    "text": "...",
    "language": "English",
    "line_count": 1,
    "tags": [
        "Job Search",
        "Networking"
    ]
}
```

---

## Phase 2 – Runtime Generation

When the application starts,

`FewShotPosts`

loads

```
processed_posts.json
```

into a Pandas DataFrame.

Example

| text | language | line_count | tags |
|------|----------|------------|------|
| Resume... | English | 2 | Job Search |

The application then:

1. Receives user input
2. Filters matching posts
3. Builds the prompt
4. Sends it to Groq
5. Displays the generated post

---

# 📚 Few-Shot Learning

Instead of training a new model, this project uses **Few-Shot Prompting**.

Matching examples are retrieved dynamically and included inside the prompt.

Example prompt

```
Generate a LinkedIn post.

Topic:
Job Search

Length:
1-5 lines

Language:
English

Example 1

Networking matters more than resumes...

Example 2

Your resume gets you interviews.
Your network gets you opportunities.
```

The LLM learns the writing style from these examples and generates a similar post.

---

# 📈 Why Preprocessing?

Without preprocessing,

the application would need to ask the LLM to analyze every post every time it starts.

That would be

- slower
- expensive
- inefficient

Instead,

metadata is extracted only once.

Runtime only performs filtering.

---

# 🏷️ Why Normalize Tags?

Different posts may contain tags like

```
Job Hunting

Job Search

Jobseekers
```

Although they have the same meaning,

they are standardized into

```
Job Search
```

This improves filtering accuracy.

---

# ▶️ Running the Project

## Clone the repository

```bash
git clone https://github.com/yourusername/AI_LinkedIn_Post_Generator.git
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Add Groq API Key

Create a `.env` file.

```
GROQ_API_KEY=YOUR_API_KEY
```

---

## Run preprocessing

```bash
python preprocess.py
```

This generates

```
processed_posts.json
```

---

## Run the application

```bash
streamlit run main.py
```

---

# 📸 Application Workflow

```
User
 │
 ▼
Select Topic

Select Language

Select Length
 │
 ▼
FewShotPosts
 │
 ▼
Retrieve Matching Posts
 │
 ▼
Build Prompt
 │
 ▼
Groq LLM
 │
 ▼
Generated LinkedIn Post
```

---

# 💡 Future Improvements

Currently the project filters posts using metadata.

Possible improvements include:

- Embedding-based retrieval
- FAISS vector database
- ChromaDB
- Retrieval-Augmented Generation (RAG)
- Semantic similarity search
- User-defined writing styles
- Multi-language support

---

# 🎯 Learning Outcomes

This project demonstrates practical experience with:

- Prompt Engineering
- LangChain
- Groq API
- Few-Shot Learning
- Pandas
- JSON Processing
- Streamlit
- LLM Integration
- Metadata Extraction
- Data Preprocessing

---

# 📖 Key Concepts

- Few-Shot Learning
- Prompt Engineering
- LangChain Chains
- PromptTemplate
- JsonOutputParser
- Metadata Extraction
- Data Normalization
- Retrieval-Based Prompting

---

# 👨‍💻 Author

**Siddarth M P**

Built as a hands-on project to explore Large Language Models, Prompt Engineering, and Few-Shot Learning using LangChain and Groq.
