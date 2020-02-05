import pandas as pd
import glob

## load reddit comment data
# https://stackoverflow.com/questions/20906474/import-multiple-csv-files-into-pandas-and-concatenate-into-one-dataframe
all_files = glob.glob("raw_data/*.csv")

li = []

for filename in all_files:
    dff = pd.read_csv(filename, index_col=None, header=0)
    li.append(dff)

df = pd.concat(li, axis=0, ignore_index=True)

## put data into comment [SEP] reply format for gpt fine-tuning
(df['comment']+' [SEP] '+df['reply'] ).to_csv('gpt2_finetune.csv', index=False, header=True)

## store comments to be seeds for creating a fake reply dataset for BERT classifier
df['comment'].drop_duplicates().to_csv('gpt2_generate.csv', index=False, header=True)

## generate the datasets for BERT classifiers
# all of these are marked as real=1, the fakes from GPT2 will be real=0
df['real']=1

# bin the upvote scores into 4 bins
df['rating'] = df['reply_score'].apply(lambda x: '0' if x<1 else '1' if x==1 else '2' if x<5 else '3')

df[['comment','reply','real','rating']].to_csv('bert_gan_real.csv', index=False, header=True)
