
import pymysql
import ssl #https용
import jaydebeapi # h2 DB api
#import psycopg

context = ssl._create_unverified_context()

------------------------------------------------



from urllib.request import urlopen
from bs4 import BeautifulSoup  #bs모듈의 BeautifulSoup함수를 사용 하기 위해 bs4모듈을 읽어 들임


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




conn = jaydebeapi.connect('org.h2.Driver', ['jdbc:h2:~/test', 'sa', ''],
                          '/Users/m6ydz642/git/SpringNoMaven/WebContent/WEB-INF/lib/h2-1.4.200.jar')
curs = conn.cursor()
curs.execute('create table PERSON ("PERSON_ID" INTEGER not null, "NAME" VARCHAR not null, '
             'primary key ("PERSON_ID"))')
curs.execute("insert into PERSON values (1, 'John')")
curs.execute("select * from PERSON")
data = curs.fetchall()
print(data)

