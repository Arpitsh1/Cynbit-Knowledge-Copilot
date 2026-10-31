\# Cynbit Knowledge Copilot



A document-based question-answering proof of concept built with Python and Streamlit. The application retrieves relevant information from a small knowledge base using TF-IDF and cosine similarity.



\## Project Overview



Cynbit Knowledge Copilot allows users to ask questions about company services, products, and contact information. It searches the available knowledge documents and displays the most relevant passages.



The project demonstrates how information retrieval techniques can support an AI-powered company knowledge assistant.



\## Features



\- Loads text documents from a local knowledge base.

\- Splits documents into smaller overlapping passages.

\- Converts text into numerical representations using TF-IDF.

\- Ranks passages using cosine similarity.

\- Retrieves the top three relevant passages.

\- Displays answers and supporting source passages through Streamlit.

\- Includes an optional Ollama-based local LLM generation function.



\## Technology Stack



\- Python

\- Streamlit

\- Scikit-learn

\- TF-IDF

\- Cosine Similarity

\- Requests

\- Ollama (optional; model integration not tested)



\## Project Structure



```text

Cynbit\_Knowledge\_Copilot/

│

├── app.py

├── knowledge.py

├── evaluate.py

├── ingest\_url.py

├── requirements.txt

├── README.md

│

└── data/

&#x20;   ├── cynbit\_services.txt

&#x20;   ├── cynbit\_products.txt

&#x20;   └── cynbit\_contact.txt

```



\## Installation



\### 1. Clone the repository



```bash

git clone https://github.com/Arpitsh1/Cynbit-Knowledge-Copilot.git

cd Cynbit-Knowledge-Copilot

```



\### 2. Create a virtual environment



```bash

python -m venv .venv

```



Activate it on Windows PowerShell:



```powershell

.venv\\Scripts\\Activate.ps1

```



\### 3. Install dependencies



```bash

pip install -r requirements.txt

```



\## Run the Application



Start the Streamlit application:



```bash

streamlit run app.py

```



Open the local URL displayed in the terminal, usually:



```text

http://localhost:8501

```



Enter a question in the application and click Ask to retrieve relevant information.



\## Evaluation



The retrieval pipeline was tested using five sample questions.



| Metric | Result |

|---|---:|

| Test questions | 5 |

| Recall@3 | 1.00 |

| Mean Reciprocal Rank (MRR) | 0.90 |



These results are from a small smoke test and should not be interpreted as production-level accuracy.



\## Current Implementation and Limitations



The current working implementation uses TF-IDF retrieval and extractive answering.



The application also contains an optional Ollama integration function. However, a local language model was not downloaded or tested during this proof of concept.



Current limitations:



\- Small knowledge base containing three text documents.

\- Evaluation performed on only five sample questions.

\- No production-scale document management.

\- No PDF or DOCX ingestion in the current implementation.

\- No validated LLM-generated answers.



\## Future Improvements



\- Integrate a locally hosted language model through Ollama.

\- Add embedding-based semantic retrieval.

\- Support PDF and DOCX documents.

\- Expand the evaluation dataset.

\- Improve source citations and answer verification.

\- Add authentication and production deployment.



\## Author



Arpit Sharma



\## Project Purpose



Developed as an AI/ML proof of concept for the Cynbit AI/ML Engineer Intern assessment.

