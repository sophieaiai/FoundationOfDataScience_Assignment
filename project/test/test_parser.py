from crawler.src.news.news import News
from crawler.src.news_parser.lizhi_news_parser import LiZhiNewsParser
from bs4 import BeautifulSoup
import requests
from crawler.src.util.util import set_encoding
from crawler.src.util.util import to_mark_down



def test_lizhi():
    news = LiZhiNewsParser().parse("http://news.jstv.com/a/20201130/1606733984697.shtml")
    to_mark_down(news.to_string())

def test_requests():
    resoponse = requests.get("https://finance.sina.com.cn/money/future/fmnews/2020-12-03/doc-iiznctke4505057.shtml")
    set_encoding(resoponse)
    print(resoponse.text)
