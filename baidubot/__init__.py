from typing import List, Optional
from bs4 import BeautifulSoup
from time import sleep
import requests


__version__ = "0.1.0"

CHROME_DEFAULT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'


class BaiduBot:

    def __init__(self, search_term: str, pages: int, proxy: Optional[str]=None, timeout: Optional[int]=30,
                 user_agent: Optional[str]=CHROME_DEFAULT, delay: Optional[int]=0):

        self.base_url = 'http://www.baidu.com/s?wd={}&pn={}'
        self.proxy = proxy
        self.search_term = search_term.rstrip(' ')
        self.page_count = pages
        self.timeout = timeout
        self.user_agent = user_agent
        self.delay = delay

    def __baidu_request(self, url: str) -> tuple:
        try:
            res = requests.get(url, timeout=30, proxies={'https': self.proxy, 'http': self.proxy},
                               headers={'User-Agent': self.user_agent})
            res.raise_for_status()
        except requests.HTTPError:
            return None, 'Baidu returned non-200 status code, Status Code: {}'.format(res.status_code)
        except requests.RequestException as e:
            return None, str(e)
        except ConnectionError:
            return None, 'Unable to connect to Baidu'
        else:
            return res, None

    def __parse_html(self, html: str) -> List[dict]:
        soup = BeautifulSoup(html, 'html.parser')
        result_containers = soup.find_all('div', {'class': 'c-container'})
        results = []
        for result in result_containers:
            title = result.find('h3', {'class': 't'}).get_text()
            url = result.find('a', href=True)['href']
            description = result.find('div', {'class':'c-abstract'})
            if description:
                description = description.get_text()
            results.append({'title': title, 'url': url, 'description': description})
        return results

    def __resolve_urls(self, url: str) -> str:
        try:
            final_url = requests.get(url, proxies={'http': self.proxy, 'https': self.proxy},
                                     headers={'User-Agent': self.user_agent}, timeout=self.timeout).url
        except requests.RequestException:
            return url
        except ConnectionError:
            return url
        else:
            return final_url

    def resolve_baidu_links(self, results):
        count = 1
        for i in results:
            i['url'] = self.__resolve_urls(i['url'])
            i['rank'] = count
            count += 1
        return results

    def scrape_baidu(self):
        results = []
        for i in range(self.page_count):
            pn = i * 10
            html, error = self.__baidu_request(self.base_url.format(self.search_term.replace(' ', '%20'), pn))
            if error:
                return {'results': self.resolve_baidu_links(results), 'error': error}
            elif html:
                scrape_results = self.__parse_html(html.text)
                for res in scrape_results:
                    results.append(res)
            sleep(self.delay)
        return {'results': self.resolve_baidu_links(results), 'error': None}


def scrape_baidu(search_term: str, pages: int, proxy: Optional[str]=None, timeout: Optional[int]=30,
                 user_agent: Optional[str]=CHROME_DEFAULT, delay: Optional[int]=0):
    b = BaiduBot(search_term, pages, proxy, timeout, user_agent, delay)
    b.scrape_baidu()