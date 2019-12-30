# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from konlpy.tag import Twitter
import re

#twitter = Twitter()
user = []
date = []
msg_ = []

def read_f():
    lines_no_emoji = []
    
    # read kakao chat text file
    filename = './input/KakaoTalk_20191228_2200_19_145_group.txt'
    f = open(filename, 'r', encoding="utf-8")

    if 'group' in filename:
        lines = f.readlines()[5:]
    else:
        lines = f.readlines()[3:]
        
    for x in lines:
        emoji_pattern = re.compile("["
                                   u"\U0001F600-\U0001F64F"  # emoticons
                                   u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                   u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                   u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                   "]+", flags=re.UNICODE) 
        x = emoji_pattern.sub(r'', x)

        lines_no_emoji.append(str(x))

    return lines_no_emoji

def edit_text(lines):
    # val settings
    global user
    global date
    global msg_
    
    # remove date in list
    p = re.compile("(['-*-'].['-*-'])")
    for x in lines:
        if p.match(x) is not None:
            lines.remove(x)

    # split
    p = re.compile("(\[.*\]) (\[.*\])")
    for x in lines:
        try:
            msg_start_p = p.match(x).end()
            user.append(list(p.findall(x))[0][0])
            date.append(list(p.findall(x))[0][1])
            msg_.append(x[msg_start_p:].replace('\n', '').strip())
        except:
            pass
    # edit list
    user = [x.replace('[','').replace(']','') for x in user]
    date = [x.replace('[','').replace(']','').split(' ')[0] for x in date]
    for x in msg_:
        print(x)

def chat_time(s,n):
    total = s+n
    am = "%0.2f" % float(s/total*100)
    pm = "%0.2f" % float(n/total*100)
    ratio = [am, pm]
    return ratio
    
def all_userlist():
    # Edit all User list
    All_username = list(set(user))
    for x in All_username:
        if ('오전' in x) or ('오후' in x):
            All_username.remove(x)
    return Azll_username

def pie_graph():
    # Categorized by Chat Time
    print("\n- Chatting times [AM(%), PM(%)]")
    print(chat_time(date.count('오전'), date.count('오후')))

    pi_names = ['AM', 'PM']
    plt.pie(chat_time(date.count('오전'), date.count('오후')), labels=pi_names, autopct='%1.2f%%')
    plt.title("Categorized by Chat Time")
    plt.show()

if __name__ == "__main__":
    edit_text(read_f())

    print("- All user name ({})".format(len(all_userlist())))
    print(x for x in all_userlist())

    pie_graph()
