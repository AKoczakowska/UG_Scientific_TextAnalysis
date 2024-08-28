# UG-History-Articles-Analysis

## Overview
This project is dedicated to the analysis of scientific articles from the University of Gdansk, Department of History. The goal of this project was to analyze the text of these articles to identify common themes, word frequencies, and patterns within the abstracts. The analysis was conducted using Python, with several libraries such as nltk, pandas, matplotlib, and wordcloud.

## Project Description
As part of a group project for our coursework, we were provided with a dataset of scientific articles from the Department of History at the University of Gdansk by our lecturer. My specific responsibility in this project was to perform text analysis on the abstracts of these articles.

The project includes the following key steps:
1. **Data Preprocessing:** Loading and cleaning the data, including removing stopwords and handling any inconsistencies in the text.
2. **Text Analysis:** Analyzing word frequencies, merging related terms, and identifying the most common words used in the abstracts.
3. **Visualization:** Creating visual representations of the data, including word clouds and bar charts, to clearly present the results of the analysis.

## Code Explanation

### Libraries and Setup
- The script utilizes the following Python libraries:
  - **`nltk`** for natural language processing tasks such as tokenization and stopword management.
  - **`pandas`** for efficient data loading and manipulation.
  - **`matplotlib`** for creating informative plots and charts.
  - **`wordcloud`** for generating visual representations of word frequency data.
- Custom stop words are added to the standard list of English stopwords provided by `nltk` to refine the text cleaning process further.

### Data Loading
- The script loads the abstracts data from an Excel file named `abstract.xlsx` using `pandas`.
- The data is read into a DataFrame for easy processing and analysis.

### Text Processing
- All text in the abstracts is converted to lowercase to ensure consistency during analysis.
- Stop words (common words that do not carry significant meaning) are removed from the text.
- The frequency of each word is calculated to identify the most commonly occurring terms.
- Similar words (e.g., "Polish" and "Poland") are merged to consolidate their frequencies and provide more accurate insights.

### Visualization
- A **word cloud** is generated to provide a visual representation of the most frequent words across all abstracts, with the size of each word corresponding to its frequency.
- A **bar chart** is created to display the top 20 most common words along with their respective frequencies, offering a clear and concise overview of prevalent themes in the articles.

