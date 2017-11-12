## Introduction
A tf-idf based Search Engine for research papers on Arxiv. The main purpose of this project is understand how vector space based retrieval models work.
More on [Tf-Idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf).

## Data
The data has been scraped from [Arxiv](https://arxiv.org). The scraper is present in scraper.py which can be found in the directory scraper.

We use the following data  of papers from all categories present on Arxiv:
1. Title
2. Abstract
3. Authors
4. Subjects

*Total terms in vocabulary = 38773.*
*Total documents in corpus = 15686.*
**Note*: Only Abstract data has been used for searching.*

The data is organized into directories as follows:

Data/

├── abstracts &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   (text files containing the abstract)

├── authors     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (text files containing authors) 

├── link       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (text files containing link to the pdf of the paper)

├── subject     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (text files containing subjects)

└── title       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (text files containing the title) 


## Text Preprocessing
We processed the raw text scraped from Arxiv by applying the following operations-
1. Tokenization
2. Stemming
3. Lemmatization
4. Stopwords removal

## Data Structures used
We used a Trie to store words and their Term frequencies in the different Documents and their Document Frequencies. The Trie is also used to generate typing suggestions while querying.

## Time complexity of Inserting and Querying
The time complexity of querying and inserting an element into the Trie is *O(n)*.
n → number of charcters in the query term.

## Tf-Idf formulation
Tf-Idf score = tf*log(N/df)

tf &nbsp;→ &nbsp;Term frequency of the term in the current document
df → &nbsp;Document frequency of the term
N → &nbsp;Total number of documents in corpus

## Machine specs:
Processor: i7
Ram: 8 GB DDR4
OS: Ubuntu 16.04 LTS

## Results
Index building time:
    * No stemming/lemmatization - 41.67s
    * Lemmatized text - 76.97s
    * Stemmed text - 146.13 s

Memory usage: around 410 MB.

## Screenshots

Retrieval time statistics:

![alt text][logo]

[logo]: img/time.JPG "Logo Title Text 2"

---

Search results:
![alt text][logo1]

[logo1]: img/results.JPG "Logo Title Text 2"

---

Search suggestions:
![alt text][logo2]

[logo2]: img/suggestions.JPG "Logo Title Text 2"

---

Document view:
![alt text][logo3]

[logo3]: img/docview.JPG "Logo Title Text 2"

## Members
[Shubham Jha](http://github.com/shubhamjha97)

[Praneet Mehta](http://github.com/praneetmehta)

[Abhinav Jain](http://github.com/abhinav1112)

[Saurabh Khandelwal](http://github.com/stgstg27)