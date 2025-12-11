# EV-market-sentiment-trend-analysis
CS410 course project at UIUC. Jiwen Li (NetId: jiwenli2) 

<br>

Project Description:
-
This project will build a tool to get the electric vehicle market sentiment trend analysis based on real-time data from some well-known internet news article platforms. Sentiment analysis for the EV market involves using data—often text—to measure how people feel and what they think about electric vehicles, including related brands, policies, technologies, and market trends, in order to understand overall perception and future demand. Within this tool, user can input queries to generate ranked search results, a built-in AI model will classify sentiment for each search result as positive, negative, or neutral, based on accumulated sentiment data, the tool will produce a sentiment trend diagram covering the most recent five years, allowing users to observe how public perception has shifted over time. 


<br>

Data sources:
-
News article platforms:
  
   BusinessInsider news,  CBS news
   


<br>

Setup environment:
-
1. Create a virtual environment

   -- python3.10 -m venv myenv
   
3. Activate the environment
   
   -- source myenv/bin/activate
   
5. Install packages inside the venv
   
   -- pip install --upgrade pip;
   -- pip install pyserini;
   -- pip install seaborn;
   -- pip install pandas
   -- pip install beautifulsoup4;
   -- pip install lxml
   -- pip install praw;
   -- pip install requests
   -- pip install torch torchvision torchaudio

  
<br>

Project directory:
-
<img width="467" height="356" alt="image" src="https://github.com/user-attachments/assets/ab343153-b7b4-4cfa-980d-8fb0135df80a" />
   

<br><br>

How to run:
-
First, please change the project base directory in main.py to your real location on your computer:

PROJECT_BASE_DIR = "/home/XXX/UIUC-CS410/Course_project/CS410-Course-Project-submit-version"    # change this to your real location 


execute main.py   -- python3.10 main.py

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
<img width="1852" height="1160" alt="image" src="https://github.com/user-attachments/assets/089a4000-6e47-4743-86f7-2c9618093074" />
 

<br>

<img width="1544" height="477" alt="image" src="https://github.com/user-attachments/assets/af123077-6420-48e9-a7a6-df0ee3969feb" />







<br><br>

Implementation:
-
Python, Html, Javascript

Numpy, Pandas, Pyserini

BeautifulSoup,  Praw

Tkinter, Matplotlib, Seaborn




