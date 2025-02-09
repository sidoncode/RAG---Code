## RAG System Using Excel Sheets

###  This project demonstrates how to create a Retrieval-Augmented Generation (RAG) system using Excel sheets as a data source. It leverages sentence-transformers for text embeddings and cosine similarity to retrieve the most relevant contexts based on user queries.

Features

Load and process data from Excel sheets.

Generate embeddings for text data using pre-trained models.

Retrieve relevant contexts based on similarity to user queries.

Easily extendable for larger datasets or more complex queries.

Prerequisites

Make sure you have the following installed:

Python 3.x

Required Python packages:

pip install pandas openpyxl scikit-learn sentence-transformers

Setup

Clone the Repository:

git clone https://github.com/your_username/rag-excel.git
cd rag-excel

Prepare Your Excel File:

Create an Excel file named data.xlsx in the project directory.

Ensure the file has at least the following columns:

ID

Context

1

"Azure Policy helps enforce compliance..."

2

"AWS EC2 instances can be scaled using..."

Run the Script:

python rag_with_excel.py

Code Overview

Load Data: Reads data from data.xlsx and ensures the necessary columns (ID, Context) are present.

Generate Embeddings: Uses the sentence-transformers library to convert text contexts into embeddings.

Retrieve Context: Computes cosine similarity between the query and existing contexts, returning the top relevant results.

Example Usage

query = "How does Azure Policy enforce compliance?"
results = retrieve_context(query)

for idx, row in results.iterrows():
    print(f"ID: {row['ID']}\nContext: {row['Context']}\n")

Sample Output:

Top relevant contexts:

ID: 1
Context: Azure Policy helps enforce compliance...

ID: 3
Context: Compliance rules in cloud environments...

Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

License

This project is licensed under the MIT License.
