
from flask import Flask,render_template, request
import random
import requests
from bs4 import BeautifulSoup
import csv
import datetime


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
    
@app.route("/welcome") # 경로
def welcome():
    return "Hello World!!"
    
    
@app.route("/html_tag")
def html_tag():
    return "<h1>안녕하세요</h1>"
    
@app.route("/html_line")


def html_line():
    return """
    <h1>여러 줄을 보내봅시다</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>    
    """
    
    
@app.route("/html_file")
def html_fle():
    return render_template("file.html")
    
    
@app.route("/hello_p/<string:name>")
def hello_p(name):
    return render_template("hello.html", name = name)
    
@app.route("/cube/<int:num>")
def cube(num):
    result = num**3
    return render_template("cube.html", result=result, num=num)
    



@app.route("/lunch")
def lunch():
    lst = ["샤브샤브", "짜장면", "김밥"]
    dict = {lst[0]:"http://www.2000n.net/news/photo/201506/11073_11635_3220.jpg", 
    lst[1]:"https://www.noodlelovers.com/upload_data/m_product_noodle_set/shutterstock_543369610.jpg",
    lst[2]:"https://d3af5evjz6cdzs.cloudfront.net/images/uploads/800x0/2018-03-22--125246_c85cbe064417ecd0f96789d1ba25a730.jpg"
    }
    pick = random.choice(lst)
    return render_template("lunch.html",pick=pick, img = dict[pick])
    
    
    
@app.route("/lotto")
def lotto():
    list = random.sample(range(1,46),6)
    # lucky =random.sample(list,6)
    return render_template("lotto.html", list=list)
    
@app.route("/naver")
def naver():
    return render_template('naver.html')

@app.route("/google")
def google():
    return render_template('google.html')
    
@app.route("/hell")
def hell():
    return render_template("hell.html")
    
    
@app.route("/hi")
def hi():
    user_name = request.args.get("name")
    return render_template("hi.html", user_name = user_name)


@app.route("/summoner")
def summoner():
    return render_template("summoner.html")

@app.route("/opgg")
def opgg():
    name = request.args.get('sum')
    url = 'http://www.op.gg/summoner/userName='
    html = requests.get(url+name).text
    
    soup = BeautifulSoup(html, 'html.parser')
    win = soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')
    lose = soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses')

    if len(win) == 0:
        win_i = "0승"
    else:
        win_i = win[0].text
        
    if len(lose) == 0:
        lose_i = "0패"
    else:
        lose_i = lose[0].text
    
    # f = open("list.txt", "a+")
    # data = "소환사의 이름은 {},{},{}입니다.".format(name,win_i,lose_i) 
    # f.write(data)
    # f.close()
    
    
    f = open("list.csv", "a+", encoding="utf-8", newline='')
    csvfile = csv.writer(f)
    data = [name, win_i, lose_i, datetime.datetime.now()]
    csvfile.writerow(data)
    f.close()
    
    return render_template("opgg.html", summoner=name, win=win_i, lose=lose_i)
    
    
    
    
    
@app.route("/log")
def log():
    f = open("list.csv", "r", encoding="utf-8")
    logs = csv.reader(f)
    return render_template("log.html", logs=logs)    