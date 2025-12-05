# EV-market-sentiment-trend-analysis
CS410 course project at UIUC. Jiwen Li (NetId: jiwenli2) 

Project Description:
-
This project will build a tool to get the electric vehicle market sentiment trend analysis based on real-time data from some well-known internet news platforms and social media platforms. Sentiment analysis for the EV market involves using data—often text—to measure how people feel and what they think about electric vehicles, including related brands, policies, technologies, and market trends, in order to understand overall perception and future demand. Within this tool, user can input queries to generate ranked search results, a built-in AI model will classify sentiment for each search result as positive, negative, or neutral, based on accumulated sentiment data, the tool will produce a sentiment trend diagram covering the most recent five years, allowing users to observe how public perception has shifted over time. 



Data sources:
-
1. News article platforms:
  
   BusinessInsider news,  CBS news
   
2. Social medias:

   Reddit



Setup enviroment:
-
1. Create a virtual environment

   -- python3.10 -m venv myenv
   
3. Activate the environment
   
   -- source myenv/bin/activate
   
5. Install packages inside the venv
   
   -- pip install --upgrade pip;
   -- pip install pyserini;
   -- pip install seaborn;
   -- pip install beautifulsoup4;
   -- pip install praw;


   

How to run:
-
execute main.py
   -- python3.10 main.py


UI interface:
-
<img width="1852" height="1160" alt="image" src="https://github.com/user-attachments/assets/089a4000-6e47-4743-86f7-2c9618093074" />


<img width="1544" height="477" alt="image" src="https://github.com/user-attachments/assets/af123077-6420-48e9-a7a6-df0ee3969feb" />



Implementation:
-
