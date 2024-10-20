# Survey-Analysis-using-RAG
This project allows you to upload an Excel file containing survey data and ask questions about the survey. The app is built with **Streamlit** for the frontend and uses a **Retrieval Augmented Generation (RAG)** based approach to answer questions using the data in the Excel file. The backend leverages **FAISS** for vector search and a language model for generating responses.

## Features
- Upload Excel files with survey data
- Ask questions based on the survey content
- Retrieve and display relevant answers
- Show source documents for context

## Project Structure
```
.
├── backend/
│   └── main.py                # Contains SurveyAnalysis class and helper functions
├── frontend/
│   └── app.py                 # Streamlit app to interact with the user
├── requirements.txt           # Python package dependencies
└── README.md                  # Project documentation (this file)
```

## Setup Instructions

### Prerequisites
- Python 3.8 or above
- `virtualenv` (optional but recommended)

### Step 1: Clone the repository
First, clone this repository to your local machine:
```bash
git clone https://github.com/your-username/survey-analysis.git
cd survey-analysis
```

### Step 2: Create and Activate a Virtual Environment
It's recommended to use a virtual environment to manage dependencies. You can set it up using the following commands:

#### On macOS/Linux:
```bash
python3 -m venv env
source env/bin/activate
```

#### On Windows:
```bash
python -m venv env
env\Scripts\activate
```

### Step 3: Install Required Packages
Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Streamlit App
Now, navigate to the `frontend` directory and run the Streamlit app:

```bash
cd frontend
streamlit run app.py
```

This will start a local server, and you can open your browser to `http://localhost:8502` to interact with the app.

## Backend - Survey Analysis
The backend logic is handled by the `SurveyAnalysis` class located in the `backend/main.py` file. This class is responsible for:
- Loading the survey data from an Excel file
- Embedding the document into vector space using **FAISS**
- Retrieving the most relevant documents based on user questions
- Generating an answer using a language model (like **Ollama** for local inferencing)

### How the Backend Works:
1. **Loading Excel Data**: The Excel file is parsed into chunks (or elements) for easier processing.
2. **Vectorization**: Each chunk is embedded using the **HuggingFaceBgeEmbeddings** model.
3. **Vector Store**: A **FAISS** index is created for fast document retrieval.
4. **Question Answering**: When the user asks a question, the system retrieves the most relevant chunks and generates an answer using the language model.

## Example Usage
Once the Streamlit app is running, follow these steps:
1. **Upload your Excel file**: Click on the "Browse" button to upload your survey file.
2. **Ask a Question**: Enter your question related to the survey data (e.g., "What is the most preferred dietary plan?").
3. **View Results**: The app will show a concise answer based on the survey data and the most relevant documents.

## Dependencies
All dependencies are listed in the `requirements.txt` file. Key libraries include:
- **Streamlit**: For building the web UI
- **FAISS**: For fast vector search
- **LangChain**: For handling language models and question answering
- **HuggingFace Embeddings**: For embedding document chunks into vector space
- **Unstructured**: For handling Excel document parsing

## Future Improvements

To further optimize the model and enhance the accuracy of the survey analysis, the following steps can be considered for future versions:

- **Data Cleaning and PDF Conversion**: A potential improvement would be to clean the tabular data and convert it into a PDF format before processing. This can lead to:
  - **Faster Execution**: PDFs are more compact, which can reduce processing time.
  - **Improved Accuracy**: Cleaned and well-structured data in a standardized format like PDF will allow the retrieval model to provide more accurate responses.
  - **Better Resource Management**: Optimized file formats help manage memory and resources more efficiently.

Implementing this step would contribute to an overall more robust and optimized pipeline.

Now you're all set to analyze surveys using this code! Enjoy using and extending the project.
