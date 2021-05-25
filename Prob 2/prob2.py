# modules
from bs4 import BeautifulSoup
import requests
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# nltk.download('punkt')
# nltk.download('stopwords')


# imports for scatter plots
import numpy as np
import plotly
import plotly.graph_objects as go
import plotly.offline as pyo
from plotly.offline import init_notebook_mode


class p2:


    positive=[]
    negative=[]

    wordcount = []
    stopwordscount = []

    def __init__(self):

        rating=[]

        # citylink, poslaju, gdex, j&t, dhl
        urls = [
            [
            'https://www.truckandbusnews.net/latest-news/posts/2018/november/city-link-express-aims-for-fast-delivery-and-customer-satisfaction-with-isuzu/',
            'https://themalaysianreserve.com/2020/05/28/courier-service-a-lifeline-in-time-of-enforced-isolation/',
            'https://www.theedgemarkets.com/article/crossing-borders-and-boundaries',
            ],
            [
            'https://themalaysianreserve.com/2020/06/09/delivery-firms-focus-on-efficient-operations/',
            'https://www.theborneopost.com/2020/07/08/poslaju-customers-urged-to-bear-with-longer-waiting-time/',
            'https://soyacincau.com/2020/08/15/pos-malaysia-e-consignment-notes-qr-code-available/',
            ],
            [
            'https://www.thestar.com.my/business/business-news/2020/05/30/brisk-business-for-gdex',
            'https://www.thestar.com.my/business/business-news/2021/01/30/digitalisation-a-game-changer-for-gdex',
            'https://www.thestar.com.my/news/nation/2021/01/29/couriers-and-postmen-should-also-get-vaccination-priority',
            ],
            [
            'https://www.malaymail.com/news/malaysia/2021/02/07/courier-company-jt-express-explains-staffs-violent-handling-of-parcels-caug/1947791',
            'https://www.thestar.com.my/news/nation/2019/11/10/jt-express-anticipates-promising-1111-big-sale',
            'https://hype.my/2021/212126/jt-express-courier-truck-has-only-a-few-items-to-deliver-following-bad-publicity/',
            ],
            [
            'https://www.trackingmore.com/review-dhl.html',
            'https://www.trustpilot.com/review/dhl-express.de',
            'https://www.asiaone.com/business/dhl-ecommerce-integrated-shopee-offering-malaysians-nextday-delivery-service',
            ]
        ]

        #rabin karp function
        def rabinkarpsearch(pat, txt, q):
            M = len(pat)
            N = len(txt)
            i = 0
            j = 0
            keyword = 0
            text= 0
            hvalue = 1
            global found
            found=0

            for i in range(M-1):
                hvalue = (hvalue*10)%q
            for i in range(M):
                keyword = (10*keyword + ord(pat[i]))%q
                text = (10*text + ord(txt[i]))%q
            for i in range(N-M+1):
                if keyword==text:
                    for j in range(M):
                        if  txt[i+j]!= pat[j]:
                            break
                        else: j+=1
                    if j==M:
                        found=1
                        # print ("Pattern found at index " + str(i))
                        break
                if i < N-M:
                    text = (10*(text-ord(txt[i])*hvalue) + ord(txt[i+M]))%q
                    if text < 0:
                        text = text+q

        #Test each word
        def testword(pat,count):
            positive=open("positive.txt","r",encoding='utf-8')
            negative=open("negative.txt","r",encoding='utf-8')
            q = 131
            global cpositive,cnegative,cneutral
            rabinkarpsearch(pat,positive.read(),q)
            if found == 1:
                count[0]+=1
            else:
                rabinkarpsearch(pat,negative.read(),q)
                if found == 1:
                    count[1]+=1
                else:
                    count[2]+=1

        def remove(string):
            string = string.replace("'", "")
            string = string.replace(".", " ")
            string = string.replace("(", "")
            string = string.replace(")", "")
            string = string.replace("%", "")
            string = string.replace(",", " ")
            string = string.replace("\"", "")
            string = string.lower()
            return string

        def scrape(link):
            # positive = 0
            # negative = 0
            # for link in courier: 
            r = requests.get(link)
            soup = BeautifulSoup(r.content, 'lxml')
            news = soup.find_all('p')

            newsstring = ''

            # get text form for each line and add it into newsstring, remove symbols etc
            for string in news:
                s = str(string.get_text())
                newsstring += remove(s)

            # count words in article
            wordcount = len(newsstring.split())
            self.wordcount.append(wordcount)

            # count stopwords in article
            stopcount = 0
            
            # sw = [word for word in newsstring if word in stopwords.words()]
            for word in newsstring.split():
                if word in stopwords.words():
                    stopcount += 1
            self.stopwordscount.append(stopcount)

            # delete stopwords and updated text without stopwords
            tokenized_newsstring = word_tokenize(newsstring)
            newsstring_without_sw = [word for word in tokenized_newsstring if not word in stopwords.words()]

            # filtered newsstring free from stopwords
            filtered_newsstring = (" ").join(newsstring_without_sw)

            # get frequency of every word
            newslist = filtered_newsstring.split()

            # empty array for putting frequency of each word
            newsfreq = []
            for word in newslist:
                newsfreq.append(newslist.count(word))

            # print each word and its respective frequencies in each article
            # print("Pairs\n" + str(list(zip(newslist, newsfreq))))

            # scatter plots for every link
            # fig = go.Figure(data=go.Scatter(x=newslist, y=newsfreq, mode='markers'))
            # fig.show()

            pw=list()
            nw=list()

            # Drive Code
            # count array is for number of +ve, -ve and neutral words. count[0] is for +ve, count[1] is for -ve, count[2] is
            # for neutral
            count=[0,0,0]
            for i in newslist:
                testword(i,count)
                pw.append(count[0])
                nw.append(count[1])
            self.positive.append(count[0])
            self.negative.append(count[1])
            rating.append(count)
            
        # loop for every url in urls
        for courier in urls:
            for url in courier:
                scrape(url)
            print('Done analyzing courier')
        # print(rating)

    def getPositive(self):
        return self.positive

    def getNegative(self):
        return self.negative

    def getWordcount(self):
        return self.wordcount

    def getStopwordscount(self):
        return self.stopwordscount







