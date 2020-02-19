# gpt2-bert-reddit-bot

series of scripts to fine-tune GPT-2 and BERT models using reddit data for generating realistic replies.

jupyter notebooks also available on Google Colab [here](https://drive.google.com/drive/folders/1by97qt6TBpi_o644uKnYmQE5AJB1ybMK?usp=sharing)

see [my blog post](https://www.bonkerfield.org/2020/02/reddit-bot-gpt2-bert/) for a walkthrough on running the scripts

### processing training data
I use pandas [read_gbq](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_gbq.html) to read from google bigquery.  `get_reddit_from_gbq.py` automates the download.  `prep_data.py` cleans and transforms the data into a format that is usable by the GPT2 and BERT fine-tuning scripts.  I manually upload the results from `prep_data.py` into Google Drive to be used by the Google Colab notebooks.

### pulling reddit comments with praw
I use [praw to download comments](https://praw.readthedocs.io/en/latest/tutorials/comments.html). 
```
reddit = praw.Reddit(client_id='client_id', 
                     client_secret='client_secret',
                     password='reddit_password',
                     username='reddit_username',
                     user_agent='reddit user agent name')
                     
...
subreddit = reddit.subreddit(subreddit_name)
for h in subreddit.rising(limit=5):
  for c in h.comments:
    {do stuff}
 
```
See the code for more details.


### training, generating, classifying
more documentation to come soon...


