
import pandas as pd


for y in ['2018', '2019']:
	for m in ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
		ym = y+'_'+m

		quer = f"""SELECT s.subreddit as subreddit, 
		s.selftext as submission, a.body AS comment, b.body as reply, 
		s.score as submission_score, a.score as comment_score, b.score as reply_score, 
		s.author as submission_author, a.author as comment_author, b.author as reply_author
		FROM `fh-bigquery.reddit_comments.{ym}` a
		LEFT JOIN `fh-bigquery.reddit_comments.{ym}` b 
		ON CONCAT('t1_',a.id) = b.parent_id
		LEFT JOIN  `fh-bigquery.reddit_posts.{ym}` s
		ON CONCAT('t3_',s.id) = a.parent_id
		where b.body is not null 
		  and s.selftext is not null and s.selftext != ''
		  and b.author != s.author
		  and b.author != a.author
		  and s.subreddit IN ('writing', 'scifi', 'sciencefiction', 'MachineLearning', 'philosophy', 'cogsci', 'neuro', 'Futurology')
		"""
		try:
			tst = pd.read_gbq(quer,project_id='reddit-commentor',dialect='standard')
			tst.to_csv(f'raw_data/myreddit_{ym}.csv')
		except:
			pass