import datetime
import time

from lib import *

class Webtoon():

    def __init__(self):
        self.url = ""
        self.name = ""
        self.recommend_webtoon={} #이름과 url

        """크롤링 사전 옵션"""
        service = Service(executable_path='chromedriver.exe')
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        self.driver = webdriver.Chrome(service=service, options=options)

    def crawling(self):
        self.driver.get(self.url)
        time.sleep(1)
        if self.name == "네이버":
            weekday = str(datetime.datetime.today().weekday() + 1)

            time.sleep(1)

            for x in range(4):
                n = str(x+1)
                url = self.driver.find_element(By.XPATH,
                                               "/html/body/div[1]/div/div[2]/div[3]/div[2]/div["+weekday+"]/ul/li["+n+"]/div/a")
                url = url.get_attribute("href")
                title = self.driver.find_element(By.XPATH,
                                                 "/html/body/div[1]/div/div[2]/div[3]/div[2]/div["+weekday+"]/ul/li["+n+"]/div/a/span/span")
                title = title.text

                self.recommend_webtoon[title] = url

        elif self.name == "카카오":
            # recommend_webtoon_name = self.driver.find_elements(By.CLASS_NAME, "whitespace-pre-wrap break-all break-words support-break-word ml-7 s16-bold-white leading-18 light:text-black") #이름 가져오기
            html = self.driver.page_source
            soup = BeautifulSoup(html, "html.parser")

            list = soup.find_all("a", {"class":"relative overflow-hidden"})
            tmp = list[1]["href"][9:-5]
            tmp = tmp.replace("-", " ")
            self.recommend_webtoon[tmp] = self.url + list[1]["href"]  #1등 웹툰

            list = soup.find_all("a", {"class":"w-full h-full relative overflow-hidden rounded-8 before:absolute before:inset-0 before:bg-grey-01 before:-z-1"})
            for x in range(8,11): # 2~4등까지 웹툰
                tmp = list[x]["href"][9:-5]
                tmp = tmp.replace("-", " ")
                self.recommend_webtoon[tmp] = self.url + list[x]["href"]

        for x in self.recommend_webtoon.keys():
            print(f"{x} : {self.recommend_webtoon[x]}")
            print("#######")

        self.driver.close()

    def choose_platform(self):
        self.name = "네이버" # 이름
        if self.name == "네이버":
            self.url = "https://comic.naver.com/webtoon"
        elif self.name == "카카오":
            self.url = "https://webtoon.kakao.com"
        else:
            print("네이버, 카카오 중에 선택해주세요")
            self.choose_platform()


a = Webtoon()
a.choose_platform()
a.crawling()