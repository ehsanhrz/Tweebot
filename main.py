from pyrogram import Client
import csv
import os
import pandas as pd
from tweepy import API, OAuthHandler
import configparser
from datetime import date
import time
import re

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><

def telegram():

    api_hash = 9659698
    api_key =  "d31a844c171b841c5889ebaedcd86acf"
    app = Client('Food_For_All',api_hash, api_key, bot_token="5331853611:AAFAYSYr_dJRp9vFC_q_t-GZU_9A5mtv0xA")

    twee = []
    with open("./tweets.csv", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            twee.append(row)
        twee.remove(twee[0])
        with app:
            j = 0
            for i in twee:
                text = i[2]

                # if not '@' in text:
                    # if not 'https' in text:
                        # clean_tweet = re.sub("#[A-Za-z0-9_]","", text)
                        # clean_tweet = re.sub("#[\u0600-\u06FF\s0-9_]","", clean_tweet)
                app.send_message("Food_For_All", f"\n<div><h1>\n{i[1]}\n</h1></div><p>\n{text}\n</p>")
                time.sleep(2)
                twee.remove(i)
                j += 1
                    # else:
                        # twee.remove(i)    
                # else:
                    # twee.remove(i)
                if j == 10:
                    break
    df = pd.DataFrame(columns=['username','text'])
    for i in twee:
        username = i[1]
        text = i[2]
        test = [username, text]
        df.loc[len(df)] = test
    
    filename = 'tweets.csv'
    df.to_csv(filename)


if __name__ == '__main__':
    telegram()



          
    