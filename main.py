import os
import json
import requests
import json
import re
import pickle
import praw
import random
import torch
import numpy as np
import subprocess
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from dateutil import parser
from datetime import datetime
from bs4 import BeautifulSoup
from tkinter import * 
import tkinter as tk
from tkinter import StringVar
from tkinter import ttk
from tkinter import scrolledtext
from matplotlib.figure import Figure
from pyserini.search.lucene import LuceneSearcher
from pyserini.index.lucene import LuceneIndexReader
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pyserini.search.lucene import LuceneImpactSearcher
from pyserini.encode import TctColBertQueryEncoder
from pyserini.search.lucene import LuceneHnswDenseSearcher
from transformers import AutoTokenizer, AutoModelForSequenceClassification

from pyserini.search.faiss import FaissSearcher
import faiss



# Please update "PROJECT_BASE_DIR" to your real project directory in your computer
PROJECT_BASE_DIR = "/home/johnlee/UIUC-CS410/Course_project/CS410-Course-Project-submit-version"



MAX_NUM_OF_PAGES_BUSINESS_INSIDER_WEB = 236
MAX_NUM_OF_PAGES_CBS_NEWS_WEB = 17

counter = 0

def save_first_corpus_count_to_binary_file(s):
    with open("storage/first_corpus_counter.pkl", "wb") as file:
        pickle.dump(s, file)

def get_first_corpus_count_to_binary_file():
    with open("storage/first_corpus_counter.pkl", "rb") as file:
        stored_number = pickle.load(file)
    return stored_number    

def save_second_corpus_count_to_binary_file(s):
    with open("storage/second_corpus_counter.pkl", "wb") as file:
        pickle.dump(s, file)

def get_second_corpus_count_to_binary_file():
    with open("storage/second_corpus_counter.pkl", "rb") as file:
        stored_number = pickle.load(file)
    return stored_number        

def save_third_corpus_count_to_binary_file(s):
    with open("storage/third_corpus_counter.pkl", "wb") as file:
        pickle.dump(s, file)

def get_third_corpus_count_to_binary_file():
    with open("storage/third_corpus_counter.pkl", "rb") as file:
        stored_number = pickle.load(file)
    return stored_number       

"""
This function will responsible for data scrapping
"""
def scrape_data():
    global counter
    cname = "scrapedEvNews"
    base_dir = f"data/{cname}"
    corpus_file = os.path.join(base_dir, f"{cname}.dat")
    # columns = ['datatime', 'title', 'source', 'link']
    columns = ['title']
    df = pd.DataFrame(columns=columns)

    counter = 0
    # for page in range(1, 150):
    for page in range(1, MAX_NUM_OF_PAGES_BUSINESS_INSIDER_WEB+1):

        url = f'https://markets.businessinsider.com/news/tsla-stock?p={page}'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'lxml')

        articles = soup.find_all('div', class_ = 'latest-news__story')
        for article in articles:
            datetime = article.find('time', class_ = 'latest-news__date').get('datetime')
            title = article.find('a', class_ = 'news-link').text
            if title.startswith('"'):
                title = title.strip()
                # title_cleaned = re.sub(r'"', '', title)
                title = title[1:-1]
            else:
                title = title    

            title_cleaned = datetime + "  - " + title
            # new_title = title.replace('"', '')
            if title_cleaned.startswith('"'):
                title_cleaned = title_cleaned.strip()
                # title_cleaned = re.sub(r'"', '', title)
                title_cleaned = title_cleaned[1:-1]
            else:
                title_cleaned = title_cleaned   

            df = pd.concat([pd.DataFrame([[title_cleaned]], columns=df.columns), df], ignore_index=True)
            counter +=1
    print(f'{counter} pages scraped of 50 headlines')  
    save_first_corpus_count_to_binary_file(counter)

    counter = 0
    # for page in range(1, 150):
    for page in range(1, MAX_NUM_OF_PAGES_CBS_NEWS_WEB+1):

        url = f'https://www.cbsnews.com/tag/electric-vehicles/{page}'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'lxml')

        articles = soup.find_all('div', class_ = 'item__title-wrapper')
        for article in articles:
            datetime = article.find('li', class_ = 'item__date').text
            # print(f"@@@ datetime == {datetime}")
            if "ago" in datetime:
                continue

            if parse_year_month(datetime)[0] < 2020:
                continue    

            title = article.find('h4', class_ = 'item__hed').text
            title = title.strip()
            if title.startswith('"'):
                title = title.strip()
                # title_cleaned = re.sub(r'"', '', title)
                title = title[1:-1]
            else:
                title = title    

            description = article.find('p', class_ = 'item__dek').text
            description = description.strip()
            if description.startswith('"'):
                description = description.strip()
                # title_cleaned = re.sub(r'"', '', title)
                description = description[1:-1]
            else:
                description = description    

            title += ", " + description 
            title_cleaned = datetime + " - " + title
            # new_title = title.replace('"', '')
            if title_cleaned.startswith('"'):
                title_cleaned = title_cleaned.strip()
                title_cleaned = title_cleaned[1:-1]
            else:
                title_cleaned = title_cleaned   

            df = pd.concat([pd.DataFrame([[title_cleaned]], columns=df.columns), df], ignore_index=True)
            counter +=1
    print(f'{counter} pages scraped of 25 headlines')  
    save_second_corpus_count_to_binary_file(counter)


    # Reddit scrapping
    # reddit = praw.Reddit(
    # client_id="abcd1234efgh567",
    # client_secret="x1y2z3A4B5C6D7E8F9G0H1I2J3K4L5",
    # user_agent="python:praw_test_app:v1.0 (by u/johnlee2898)"
    # )

    # subreddit = reddit.subreddit("electricvehicles")
    counter = 0
    # for post in subreddit.hot(limit=20000):
    #     timestamp = post.created_utc
    #     date = datetime.fromtimestamp(timestamp)
    #     if parse_year_month(date)[0] < 2020:
    #             continue    
    #     #e.g., 2025-05-12 14:22:11
    #     # print("TITLE:", post.title)
    #     # print("BODY:", post.selftext)
    #     # print("----- COMMENTS -----")
    #     content = post.title.strip() + ", " + post.selftext.strip()
    #     post.comments.replace_more(limit=0)
    #     for comment in post.comments[:5]:
    #         content += ", " + comment.body.strip()
        
    #     title_cleaned = date + " - " + content
    #     df = pd.concat([pd.DataFrame([[title_cleaned]], columns=df.columns), df], ignore_index=True)
    #     counter +=1
    # print(f'{counter} Reddit posts scraped')  
    save_third_corpus_count_to_binary_file(counter)        

  
    df.to_csv(f'{PROJECT_BASE_DIR}/{corpus_file}', index=False, header=False)  




def preprocess_corpus(input_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    with open(input_file, 'r') as f:
        # for i, line in enumerate(tqdm(f, desc="Preprocessing corpus")):
        for i, line in enumerate(f):
            doc = {
                "id": f"{i}",  # Changed to match qrels format
                "contents": line.strip()
            }
            with open(os.path.join(output_dir, f"doc{i}.json"), 'w') as out:
                json.dump(doc, out)




def build_index(input_dir, index_dir):
    if os.path.exists(index_dir) and os.listdir(index_dir):
        print(f"Index already exists at {index_dir}. Skipping index building.")
        return

    cmd = [
        "python", "-m", "pyserini.index.lucene",
        "--collection", "JsonCollection",
        "--input", input_dir,
        "--index", index_dir,
        "--generator", "DefaultLuceneDocumentGenerator",
        "--threads", "1",
        "--storePositions", "--storeDocvectors", "--storeRaw"
    ]

    try:
      subprocess.run(cmd, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
      print(f"Error executing command: {e.cmd}")
      print(f"Return code: {e.returncode}")
      print(f"Standard output:\n{e.stdout}")
      print(f"Standard error:\n{e.stderr}")



def load_queries(query_file):
    with open(query_file, 'r') as f:
        return [line.strip() for line in f]



def load_qrels(qrels_file):
    qrels = {}
    with open(qrels_file, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 3:
                qid, docid, rel = parts
            else:
                raise Exception(f"incorrect line: {line.strip()}")

            if qid not in qrels:
                qrels[qid] = {}
            qrels[qid][docid] = int(rel)
    return qrels



def search(searcher, queries, top_k=10, query_id_start=0):
    results = {}
    # for i, query in enumerate(tqdm(queries, desc="Searching")):
    for i, query in enumerate(queries):    
        hits = searcher.search(query, k=top_k)
        results[str(i + query_id_start)] = [(hit.docid, hit.score, hit.lucene_document.get('raw')) for hit in hits]
    return results
    
def preprocess_corpus_faiss(input_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    cmd = [
    "python", "-m", "pyserini.encode",
    "input", "--corpus", "data/scrapedEvNews",
    "--fields", "text",
    "--delimiter", "\n",
    "--shard-id", "0",
    "--shard-num", "1",
    "output", "--embeddings", output_dir,
    # "to-faiss",
    "encoder", "--encoder", "castorini/tct_colbert-v2-hnp-msmarco",
    "--fields", "text",
    "--batch", "32",
    "--fp16"]

    try:
      subprocess.run(cmd, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
      print(f"Error executing command: {e.cmd}")
      print(f"Return code: {e.returncode}")
      print(f"Standard output:\n{e.stdout}")
      print(f"Standard error:\n{e.stderr}")    

def build_index_faiss(input_dir, index_dir):
    if os.path.exists(index_dir) and os.listdir(index_dir):
        print(f"Index already exists at {index_dir}. Skipping index building.")
        return

   
    # 1>  HNSWPQ
    # cmd = [
    #     "python", "-m", "pyserini.index.faiss",
    #     "--input", "processed_corpus/scrapedEvNews-faiss",
    #     "--output", "indexes/scrapedEvNews-faiss",
    #     "--hnsw",
    #     "--pq"]
    # apnews: NDCG@10: 0.1001  Precision@10: 0.0778
    
    
    # 2>  HNSW
    cmd = [
        "python", "-m", "pyserini.index.faiss",
        "--input", "processed_corpus/scrapedEvNews-faiss",
        "--output", "indexes/scrapedEvNews-faiss",
        "--hnsw"]
        
    # apnews:  NDCG@10: 0.1390   Precision@10: 0.1121
    # cranfield:   NDCG@10: 0.3252     Precision@10: 0.2138
    # new_faculty:   NDCG@10: 0.3524      Precision@10: 0.2790


    
    # 3>  PQ
    # cmd = [
    #     "python", "-m", "pyserini.index.faiss",
    #     "--input", "processed_corpus/apnews-faiss",
    #     "--output", "indexes/apnews",
    #     "--pq"]
    # apnews:  NDCG@10: 0.1251     Precision@10: 0.0980
 


    # 4> Flat
    # cmd = [
    #     "python", "-m", "pyserini.index.faiss",
    #     "--input", "processed_corpus/apnews-faiss",
    #     "--output", "indexes/apnews"]

    # cmd = [
    #     "python", "-m", "pyserini.index.faiss",
    #     "--collection", "JsonCollection",
    #     "--input", input_dir,
    #     "--index", index_dir,
    #     "--generator", "DefaultLuceneDocumentGenerator",
    #     "--threads", "1",
    #     "--storePositions", "--storeDocvectors", "--storeRaw"
    # ]
    try:
      subprocess.run(cmd, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
      print(f"Error executing command: {e.cmd}")
      print(f"Return code: {e.returncode}")
      print(f"Standard output:\n{e.stdout}")
      print(f"Standard error:\n{e.stderr}")



def main():

    """======= Choose Dataset======="""
    cname = "scrapedEvNews"
    """============================"""

    base_dir = f"data/{cname}"
    # Paths to the raw corpus, queries, and relevance label files
    corpus_file = os.path.join(base_dir, f"{cname}.dat")

    query_id_start = {
        "scrapedEvNews": 0,
    }[cname]

    """ Step 1: scrape data """
    if not os.path.isfile(corpus_file):
        scrape_data()
    else:
        print(f"Scraped text corpus already exists at {corpus_file}. Skipping preprocessing.")

   
    # Directories where the processed corpus and index will be stored for toolkit
    # 1> BM25
    # processed_corpus_dir = f"processed_corpus/{cname}"
    # 2> Faiss - Dense Retrieval Model
    processed_corpus_dir = f"processed_corpus/{cname}-faiss"
   
    os.makedirs(processed_corpus_dir, exist_ok=True)
   
    # 1> BM25
    # index_dir = f"indexes/{cname}"
    # 2> Faiss - Dense Retrieval Model
    index_dir = f"indexes/{cname}-faiss"

    # Preprocess corpus
    if not os.path.exists(processed_corpus_dir) or not os.listdir(processed_corpus_dir):
        # 1> BM25
        # preprocess_corpus(corpus_file, processed_corpus_dir)
        # 2> Faiss - Dense Retrieval Model
        # preprocess_corpus_faiss(corpus_file, processed_corpus_dir)
        preprocess_corpus(corpus_file, processed_corpus_dir)
    else:
        print(f"Preprocessed corpus already exists at {processed_corpus_dir}. Skipping preprocessing.")
    # return

    # Build index
    os.makedirs(index_dir, exist_ok=True)

    # 1> BM25
    # build_index(processed_corpus_dir, index_dir)
    # 2> Faiss - Dense Retrieval Model
    build_index_faiss(processed_corpus_dir, index_dir)
   

    # Search
    # 1> BM25
    # searcher = LuceneSearcher(index_dir)

    # 2> Faiss - Dense Retrieval Models
    encoder = TctColBertQueryEncoder('castorini/tct_colbert-v2-hnp-msmarco')
    faiss_searcher = FaissSearcher(index_dir, encoder)


    """======= Set Ranking Hyperparameters======="""
    #Algorithm 1: BM25 
    #bm25:  b must be [0, 1]
    # searcher.set_bm25(k1=0.9, b=0.33)
    """========================================="""



#### Global scope:  ####

#Initialize LLM
model = AutoModelForSequenceClassification.from_pretrained("mervp/SentimentBERT")
tokenizer = AutoTokenizer.from_pretrained("mervp/SentimentBERT")


"""
This function will generate sentiment analysis label
Input:  text
Output: label
"""
def predict_sentiment(text):
    model.eval()
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        prediction = torch.argmax(logits, dim=-1).item()
    label = model.config.id2label[prediction]
    return label    


def parse_year_month(s):
    if s.startswith('"'):
        s = s[1:]
    p = parser.parse(s)
    return (p.year, p.month)

NEGATIVE = "negative"
NEUTRAL = "neutral"
POSITIVE = "positive"
data_source_all = {NEGATIVE:[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
   NEUTRAL:[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
   POSITIVE:[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}

index_date_year_mapping = {
    (2020, 1): 0, (2020, 2): 1, (2020, 3): 2, (2020, 4): 3, (2020, 5): 4, (2020, 6): 5,
    (2020, 7): 6, (2020, 8): 7, (2020, 9): 8, (2020, 10): 9, (2020, 11): 10, (2020, 12): 11,
    (2021, 1): 12, (2021, 2): 13, (2021, 3): 14, (2021, 4): 15, (2021, 5): 16, (2021, 6): 17,
    (2021, 7): 18, (2021, 8): 19, (2021, 9): 20, (2021, 10): 21, (2021, 11): 22, (2021, 12): 23,
    (2022, 1): 24, (2022, 2): 25, (2022, 3): 26, (2022, 4): 27, (2022, 5): 28, (2022, 6): 29,
    (2022, 7): 30, (2022, 8): 31, (2022, 9): 32, (2022, 10): 33, (2022, 11): 34, (2022, 12): 35,
    (2023, 1): 36, (2023, 2): 37, (2023, 3): 38, (2023, 4): 39, (2023, 5): 40, (2023, 6): 41,
    (2023, 7): 42, (2023, 8): 43, (2023, 9): 44, (2023, 10): 45, (2023, 11): 46, (2023, 12): 47,
    (2024, 1): 48, (2024, 2): 49, (2024, 3): 50, (2024, 4): 51, (2024, 5): 52, (2024, 6): 53,
    (2024, 7): 54, (2024, 8): 55, (2024, 9): 56, (2024, 10): 57, (2024, 11): 58, (2024, 12): 59,
    (2025, 1): 60, (2025, 2): 61, (2025, 3): 62, (2025, 4): 63, (2025, 5): 64, (2025, 6): 65,
    (2025, 7): 66, (2025, 8): 67, (2025, 9): 68, (2025, 10): 69, (2025, 11): 70, (2025, 12): 71
    }

def reset_data_resource_all():
    global data_source_all
    data_source_all = {NEGATIVE:[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    NEUTRAL:[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    POSITIVE:[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}


def update_accumulated_frequency_for_negative_neutral_positive(label, time):
    print("@@@ update_accumulated_frequency_for_negative_neutral_positive()")
    print(f"time == {time}")
    global data_source_all
    time_tuple = parse_year_month(time)

    data_source_all[label][index_date_year_mapping[time_tuple]] += 1

raw_contents = []
search_performed_flag = False
previous_query_string = None
new_query_and_has_serach_result = False




def perform_search():
    global raw_contents, search_performed_flag, previous_query_string, new_query_and_has_serach_result
    search_performed_flag = False 
    new_query_and_has_serach_result = False
    raw_contents = []
    cname = "scrapedEvNews"

    # 1> BM25 :  default 
    # index_dir = f"indexes/{cname}"
    # 2> Faiss - Dense Retrieval Models
    index_dir = f"indexes/{cname}-faiss"

    # Search
    # 1> BM25 :  default 
    # searcher = LuceneSearcher(index_dir)
    # searcher.set_bm25(k1=0.9, b=0.33) 

    # 2> Faiss - Dense Retrieval Models
    encoder = TctColBertQueryEncoder('castorini/tct_colbert-v2-hnp-msmarco')
    faiss_searcher = FaissSearcher(index_dir, encoder)

    query_id_start = {
        "scrapedEvNews": 0,
    }[cname]

    text_area.delete("1.0", tk.END)
    query = search_string.get()
    # In a real application, you would perform your search logic here
    # e.g., searching a list, a database, or an external API
    # 1> BM25 :  default 
    # results = search(searcher, [query], top_k=5000, query_id_start=query_id_start)
    # 2> Faiss - Dense Retrieval Models
    results = search(faiss_searcher, [query], top_k=5000, query_id_start=query_id_start)

    resultList = list(results.values())[0]
    raw_contents_json_obj = [item[2] for item in resultList]
    raw_contents = [json.loads(item).get("contents") for item in raw_contents_json_obj]

    if len(raw_contents):
        search_performed_flag = True
        reset_data_resource_all()
        if previous_query_string is None or query != previous_query_string:
            previous_query_string = query
            new_query_and_has_serach_result = True

    # -------------------------------------------------------------------------
    results = f"Searching for: '{query}'\n"
    for i, item in enumerate(raw_contents):
        results += f"Result {i}: {item}\n"
        
    text_area.insert(tk.END, results)




"""  This function will draw sentiment tread diagram """
def draw_sentiment_trend():
    global search_performed_flag
    print(f"draw_sentiment_trend()") 
    # print(f"raw_contents == {raw_contents}")

    #experiment:
    value = parse_year_month("Dec 13, 2021")
    # value = parse_year_month("2/11/2025, 3:11:23 PM")
    print(f"@@@ parser.parse(\"Dec 13, 2021\") == {value}")
    value = parse_year_month("Dec 13")
    print(f"@@@ parser.parse(\"Dec 13\") == {value}")
    
    if search_performed_flag or new_query_and_has_serach_result:
        search_performed_flag = False
        new_query_and_has_serach_result = False
        for i, item in enumerate(raw_contents):
            print(f"@@@@@@@@@@@@ item = {item}")
            label = predict_sentiment(item)
            update_accumulated_frequency_for_negative_neutral_positive(label, item[0:item.find("-")])

    # Example data
    time_span = ["2020-01", "2020-02", "2020-03",  "2020-04", "2020-05", "2020-06", "2020-07", "2020-08", "2020-09", "2020-10", "2020-11", "2020-12",
        "2021-01", "2021-02", "2021-03",  "2021-04", "2021-05", "2021-06", "2021-07", "2021-08", "2021-09", "2021-10", "2021-11", "2021-12",
        "2022-01", "2022-02", "2022-03",  "2022-04", "2022-05", "2022-06", "2022-07", "2022-08", "2022-09", "2022-10", "2022-11", "2022-12",
        "2023-01", "2023-02", "2023-03",  "2023-04", "2023-05", "2023-06", "2023-07", "2023-08", "2023-09", "2023-10", "2023-11", "2023-12",
        "2024-01", "2024-02", "2024-03",  "2024-04", "2024-05", "2024-06", "2024-07", "2024-08", "2024-09", "2024-10", "2024-11", "2024-12",
        "2025-01", "2025-02", "2025-03",  "2025-04", "2025-05", "2025-06", "2025-07", "2025-08", "2025-09", "2025-10", "2025-11", "2025-12",
        ]
        
    data_positive = {
        "date": time_span,
        "sentiment": data_source_all[POSITIVE]
    }

    data_negtive = {
        "date": time_span,
        "sentiment": data_source_all[NEGATIVE]        
    }

    data_neural = {
        "date": time_span,
        "sentiment": data_source_all[NEUTRAL]        
    }   


    # Convert to DataFrame, Convert the date column to datetime and smooth trend with rolling average
    df_positive = pd.DataFrame(data_positive)
    df_positive["date"] = pd.to_datetime(df_positive["date"])
    df_positive["rolling"] = df_positive["sentiment"].rolling(3, min_periods=1).mean()

    df_negtive = pd.DataFrame(data_negtive)
    df_negtive["date"] = pd.to_datetime(df_negtive["date"])
    df_negtive["rolling"] = df_negtive["sentiment"].rolling(3, min_periods=1).mean()

    df_neural = pd.DataFrame(data_neural)
    df_neural["date"] = pd.to_datetime(df_neural["date"])
    df_neural["rolling"] = df_neural["sentiment"].rolling(3, min_periods=1).mean()

    # Clear old plot if exists
    for widget in plot_frame.winfo_children():
        widget.destroy()

    # Create Matplotlib figure
    fig = Figure(figsize=(12, 5), dpi=100)
    ax = fig.add_subplot(111)

    # Plot the sentiment trend
    # ax.plot(x_values, sentiment_scores, marker='o', linestyle='-', color='blue')
    ax.plot(df_positive["date"], df_positive["rolling"], marker='o', linestyle='-', color='blue', alpha=0.7, label='Positive')
    ax.plot(df_negtive["date"], df_negtive["rolling"], marker='o', linestyle='-', color='red', alpha=1.0, label='Negtive')
    ax.plot(df_neural["date"], df_neural["rolling"], marker='o', linestyle='-', color='green', alpha=0.5, label='Neural')
    ax.set_ylim(0, 170)
    ax.set_title("Electric Vehicle Sentiment Trend Over Time")
    ax.set_xlabel("Date (2020-2026)")
    ax.set_ylabel("Sentiment frequency")

    ax.legend()

    ax.grid(True)

    # Embed into Tkinter
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)    



if __name__ == "__main__":
    main()



#### Global scope:  ####

# UI interface implementaton

##############################################################
# Create the main window
root = tk.Tk()
root.title("Python Search UI")
root.grid_rowconfigure(0, weight=1)  # first frame row expands
root.geometry("1500x1000") 

top_frame = ttk.Frame(root)
top_frame.grid_columnconfigure(0, weight=1)
top_frame.grid_columnconfigure(1, weight=1)
top_frame.pack(side="top", fill="x")

middle_frame = ttk.Frame(root)
middle_frame.pack(side="top", fill="x", anchor="center")
middle_frame.grid_columnconfigure(0, weight=1)  # empty left column
middle_frame.grid_columnconfigure(1, weight=0)  # content column
middle_frame.grid_columnconfigure(2, weight=0)  # content column
middle_frame.grid_columnconfigure(3, weight=1)  # empty right column

bottom_frame = ttk.Frame(root)
bottom_frame.pack(side="bottom", fill="both", expand=True)

style = ttk.Style()
style.configure("MyCustom.TEntry",
                background="lightblue",  # Background color
                foreground="darkblue",   # Text color
                font=("Arial", 20),      # Font family and size
                fieldbackground="white", # Background color of the text entry area # lightgray
                bordercolor="red",       # Border color
                borderwidth=8,           # Border width
                padding=(7, 7))          # Padding around the text           

# # Search input field
# Search result display area
search_result_label = tk.Label(top_frame, text="Enter your query and click Search.", justify="left", width=600, wraplength=600).grid(row=0, column=0, pady=0)
# search_result_label.pack(pady=10)

search_string = StringVar(value="")
placeholder = "Enter your query"
placeholder_color = "grey"
normal_color = "blue"
placeholder_font = ("Arial", 22, "italic")  # Italic for placeholder
normal_font = ("Arial", 18, "normal")


search_entry = ttk.Entry(top_frame, textvariable=search_string, width=60, style="MyCustom.TEntry", font=("Arial", 24, "bold"))
# search_entry.pack(padx=10, pady=10)     
search_entry.grid(row=1, column=0, pady=12)

# search_entry.pack(pady=10)
# Function to add placeholder
def add_placeholder(event=None):
    if not search_entry.get():
        search_entry.insert(0, placeholder)
        search_entry.config(foreground=placeholder_color, width=40, style="MyCustom.TEntry", font=placeholder_font)

# Function to remove placeholder when typing
def remove_placeholder(event):
    if search_entry.get() == placeholder:
        search_entry.delete(0, tk.END)
        search_entry.config(foreground=normal_color, width=40, style="MyCustom.TEntry", font=("Arial", 24, "bold"))

search_entry.bind("<FocusIn>", remove_placeholder)
search_entry.bind("<FocusOut>", add_placeholder)

# Initialize placeholder
add_placeholder()

# Search button
style.configure("MyCustom.TButton", font=("Verdana", 16, "bold"), background="green", foreground="white", padding=10)
search_button = ttk.Button(middle_frame, text="Search", command=perform_search, style="MyCustom.TButton").grid(row=0, column=1, pady=6, padx=(0,5))
# search_button.pack(pady=5)

# Draw sentiment trend diagram button
style.configure("Blue.TButton", font=("Verdana", 14, "bold"), background="#094986", foreground="white", padding=10)
ttk.Button(middle_frame, text="Draw Sentiment Trend", command=draw_sentiment_trend, style="Blue.TButton").grid(row=0, column=2, pady=6, padx=(5,0))
    # .pack(pady=10)

normal_font = ("Arial", 18, "normal")
data_corpus_detail_label = tk.Label(root, text="Total number of scrapped data: " + str(get_first_corpus_count_to_binary_file()+get_second_corpus_count_to_binary_file() + get_third_corpus_count_to_binary_file())
 + ", " + str(get_first_corpus_count_to_binary_file()) + " from Businessinsider news" + ", " + str(get_second_corpus_count_to_binary_file()) + " from CBS news"  + ", " + str(get_third_corpus_count_to_binary_file()) + " from Reddit electricvehicles customer review channel.", justify="left", font=normal_font)
data_corpus_detail_label.pack()    

plot_frame = ttk.Frame(root)
plot_frame.pack(fill=tk.BOTH, expand=True)


# # Search result display area
# search_result_label = tk.Label(root, text="Enter your query and click Search.", justify="left")
# search_result_label.pack(pady=10)

# Bind Enter key to search
root.bind('<Return>', lambda event: perform_search())

# Create a ScrolledText widget
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=1200, height=400)
text_area.pack(padx=10, pady=10)


# Insert some text
# text_area.insert(tk.END, "This is a sample text for the ScrolledText widget. " * 50)

Button(root, text="Quit", command=root.destroy).pack()

spinner_label = tk.Label(root, text="", font=("Arial", 24))
spinner_label.pack(pady=20)
index = 0
spinner_chars = ['|', '/', '-', '\\']

def spin():
    global index, spinner_label, spinner_chars, root
    spinner_label.config(text=spinner_chars[index])
    index = (index + 1) % len(spinner_chars)
    root.after(100, spin)  # update every 100ms

spin() 

root.mainloop()    

