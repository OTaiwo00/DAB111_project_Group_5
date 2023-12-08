## Final Project
- This project uses dataset from UCI Repository at https://archive.ics.uci.edu/dataset/14/breast+cancer.
- The dataset name is Breast Cancer dataset which has 10 attributes/variables.
- The **data_processing** folder has two files: the datasset and the Python Notebook for preprocessing the dataset.
- There is another folder called **database** that contains the file **db-creation-from-data** which load the dataset into a Sqlite3 database called **breastcancer.db**. The Sqlite3 database is automatically created from the Pandas dataframe that loads the data.
- There is also a folder called **website** that stores the website part of this project. Inside it, you will find the template folder that holds the HTML files for the basic website.
- To install the requirement packages, simply run `pip install -r requirements.txt`