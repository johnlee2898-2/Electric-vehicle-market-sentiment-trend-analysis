
<h1 align="center">Electric vehicle market sentiment trend analysis</h1>

<p align="center">
  <strong>2025 Fall CS410 Final Project — University of Illinois Urbana-Champaign</strong><br>
  <strong>Instructor: Prof. ChengXiang Zhai<br>
  <strong>Project Author: Jiwen Li <br>
  <strong>NetID: jiwenli2<br>
  <strong>Email: jiwenli2@illinois.edu<br>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/LLM-SentimentBERT-orange">
  <img src="https://img.shields.io/badge/BM25-Indexing-blue">
</p>

---

<br>

## Project overview:
This project will build a tool to get the electric vehicle market sentiment trend analysis based on real-time data from some well-known internet news article platforms. Sentiment analysis for the EV market involves using data—often text—to measure how people feel and what they think about electric vehicles, including related brands, policies, technologies, and market trends, in order to understand overall perception and future demand. Within this tool, user can input queries to generate ranked search results, a built-in AI model will classify sentiment for each search result as positive, negative, or neutral, based on accumulated sentiment data, the tool will produce a sentiment trend diagram covering the most recent five years, allowing users to observe how public perception has shifted over time. 


<br>

## Data sources:
News article platforms:
  
  - BusinessInsider news
  
  - CBS news
   


<br>

Setup environment:
-
## 1. Create a virtual environment

```text
$ python3.10 -m venv myenv
```
   
## 2. Activate the environment
```text
$ source myenv/bin/activate
```

## 3. Install packages inside the venv
```text   
$ pip install --upgrade pip;
$ pip install pyserini;
$ pip install seaborn;
$ pip install pandas
$ pip install beautifulsoup4;
$ pip install lxml
$ pip install praw;
$ pip install requests
$ pip install torch torchvision torchaudio
```


<br>


## Project Structure

```text
Electric-vehicle-market-sentiment-trend-analysis/
│
├── data/
    └── scrapedEvNews            # Directory which save the scrapped converged data  
        └── scrapedEvNews.dat    # File to save all raw data
│── indexes
        └── scrapedEvNews        # All generated indexes will be saved here
├── instruction.md
├── main.py                      # This is the python file contains all source code
├── processed_corpus
│   └── scrapedEvNews            # Processed corpus
│
├── storage/                     # Local storage to save labels to distinquish different data sources
│   ├── first_corpus_counter.pkl
│   ├── second_corpus_counter.pkl
│   └── third_corpus_counter.pkl
├── LICENSE
└── README.md                     
```

---



<br><br>

How to run:
-
## 1. Pull project repository to your local computer
```text
$ git clone git@github.com:johnlee2898-2/Electric-vehicle-market-sentiment-trend-analysis.git
$ cd Electric-vehicle-market-sentiment-trend-analysis
```

## 2. Change the project base directory to your real location on your computer:
in main.py:
```text
PROJECT_BASE_DIR = "/home/XXX/UIUC-CS410/Course_project/CS410-Course-Project-submit-version"    # change this to your real location 
```

## 3. Execute main.py
```text
$ python3.10 main.py
```

<img width="1250" height="91" alt="image" src="https://github.com/user-attachments/assets/eb068535-4a9b-4b5d-b7dd-d5a1467a8030" />

After about 5 minutes data scraping, a window will prompt, the UI interface inludes query input field, sentiment trend diagam displaying area, "Search" and "Draw Sentiment Trend" buttons, search results display area. First please input any EV related queries like "EV", "EV Electric vehicle", "Electric vehicle tesla", "Electric vehicle range", "EV battery life" etc. Once the search results are generated, it will display on the result displaying area, then please click the "Draw Sentiment Trend" button to generate the sentiment trend diagram.

Operation sequence:

Execute the python file:  $ python3.10 main.py >>> On UI interface, input queries  >>> click "Search" button  >>> Once search results displayed, click "Draw Sentiment Trend" button, wait some time until sentiment trend displayed.

<br>

How to re-generate data?
-
Delete file "project directory/data/scrapedEvNews/scrapedEvNews.dat"
(Note: only delete the file scrapedEvNews.dat, but keep the direcotry: "project directory/data/scrapedEvNews/")r

Delete directory:    "project directory/processed_corpus/scrapedEvNews", after deletion it will look like "./processed_corpus"

Delete directory:    "project directory/indexes/scrapedEvNews", after deletion it will look like "project directory/indexes"

Re-execute main.py   -- python3.10 main.py

<img width="1250" height="91" alt="image" src="https://github.com/user-attachments/assets/eb068535-4a9b-4b5d-b7dd-d5a1467a8030" />



<br><br>
UI interface:
-
<img width="1669" height="228" alt="image" src="https://github.com/user-attachments/assets/dcceca1c-8f7f-468a-a437-5c236f493b78" />
<img width="1544" height="477" alt="image" src="https://github.com/user-attachments/assets/af123077-6420-48e9-a7a6-df0ee3969feb" />
<img width="1671" height="383" alt="image" src="https://github.com/user-attachments/assets/7d8b64fa-2c5f-4f8c-a878-9b245115246f" />
 
<br>









<br><br>

Implementation:
-
Python, Html, Javascript

Numpy, Pandas, Pyserini

BeautifulSoup,  Praw

Tkinter, Matplotlib, Seaborn




