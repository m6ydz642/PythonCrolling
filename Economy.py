
import pymysql
import ssl #https용


context = ssl._create_unverified_context()

#---------------------------------------------------------------------------------------------------------------
# DB연결 부분
# conn = pymysql.connect(host='59.20.215.149', user = 'jspid', password='jsppass', db = 'Sample',charset = 'utf8')
# curs = conn.cursor(pymysql.cursors.DictCursor)
#---------------------------------------------------------------------------------------------------------------



# 모듈을 읽어 들입니다.


#urlopen모듈은 url에 접속하기 위한 라이브러리이다.
#웹크롤링을 위해서 반드시 사용해야 하는 라이브러이이다.
# from문은 특정 라이브러리에서 한 부분만을 불러와서 사용할 때 사용하는 구문이다.
# urllib.request모듈 내부에 있는 urlopen 이라는 함수만 불러와서 사용하겠다는 내용이다.
from urllib.request import urlopen
from bs4 import BeautifulSoup  #bs모듈의 BeautifulSoup함수를 사용 하기 위해 bs4모듈을 읽어 들임


#request모듈 내부에 있는 urlopen()함수를 이용해 기상청 페이지의 코드 내용을 읽어들입니다.
#urlopen()함수는 URL주소의 페이지를 열어 주는 함수 입니다.
# urlopen() 함수로 기상청의 전국 날씨를 읽습니다.

target = urlopen("https://www.hankyung.com/economy", context=context).read().decode('utf-8')
#
soup = BeautifulSoup(target, "html.parser")
# print("soup 내용 ", soup)
for list in soup.select("div .article"):
    # <list>...</list>태그내부의 thstrm_nm, sj_nm, account_nm, thstrm_amount 태그를 찾아 출력합니다.
    title = list.select_one("h3 > a").text
    subject = list.select_one("p").text
    print("제목 : ", title)
    print("본문 : " , subject)





