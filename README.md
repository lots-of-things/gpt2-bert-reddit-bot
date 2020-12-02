# gpt2-bert-reddit-bot

series of scripts to fine-tune GPT-2 and BERT models using reddit data for generating realistic replies.

jupyter notebooks also available on Google Colab [here](https://drive.google.com/drive/folders/1by97qt6TBpi_o644uKnYmQE5AJB1ybMK?usp=sharing)

see [my blog post](https://www.bonkerfield.org/2020/02/reddit-bot-gpt2-bert/) for a walkthrough on running the scripts

### processing training data
I use pandas [read_gbq](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_gbq.html) to read from google bigquery.  `get_reddit_from_gbq.py` automates the download.  `prep_data.py` cleans and transforms the data into a format that is usable by the GPT2 and BERT fine-tuning scripts.  I manually upload the results from `prep_data.py` into Google Drive to be used by the Google Colab notebooks.

```0
"Is there any way this could be posted as a document so it can be saved permanently, outwith reddit? [SEP] Could you not just copy and paste it yourself into a word processor document?"
"Seems like alt-history is a format that would almost *require* a detailed outline before writing [SEP] Are you aware of any good outliners or character sheets for writing novels? I like to organize and plan on the macro level and then, knowing what I want to accomplish and with which character, I can then discovery write at the micro level. "
"This is depressing [SEP] There are the books and they are excellent. There are also audiobooks which are also outstanding. Including side story novellas!

Also there is no apparent sign of James S. A. Corey (which is actually two authors: Daniel Abraham and Ty Franck) going all George R. R. Martin / Robert Jordan."
```

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


