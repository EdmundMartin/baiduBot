# About baidubot

baidubot is a small package that allows users to scrape search results from the Chinese search engine Baidu. The library allows you to use
a proxy and scrape multiple results pages. The package requires Python 3.5 or greater as the package makes use of type hints only 
availiable in these versions of Python

# Installing baidubot
```
pip install baidubot
```
The package is availiable through pypi and can be installed by running the above pip command.

# Using the package
```python3
from baidubot import BaiduBot, scrape_baidu

# Using BaiduBot class
b = BaiduBot('edmund martin', 1)
res = b.scrape_baidu()

# Using scrape_baidu
res = scrape_baidu('edmund martin', 1)
```
The package allows you to scrape Baidu through one of two interfaces. Firstly, it is possible to initialize the underlying BaiduBot class
and then call the scrape_baidu function.

The scrape_baidu function is simply a wrapper around the BaiduBot class, and provides users of the package a nicer interface.

# Arguments
```
search_term: str, # Term to be searched
pages: int, # Number of pages to scrape
proxy: Optional[str]=None, # Proxy to scrape Baidu with
timeout: Optional[int]=30, # Timeout - how long requests should take before timing out.
user_agent: Optional[str]=CHROME_DEFAULT,  # user agent, by default users Google chrome
delay: Optional[int]=0): # time to sleep between each page of search results.
```
BaiduBot takes to two positional arguments and allows users to pass a number kewyord arguments.

# Results
```python3
{'error': None,
 'results': [{'description': 'For 75 years Edmund Optics (EO) has been a '
                             'leading producer of optics, imaging, and '
                             'photonics technology.',
              'rank': 1,
              'title': '...Imaging - Photonics - Optomechanics - Lasers | '
                       'Edmund Optics',
              'url': 'https://www.edmundoptics.com/'},
             {'description': None,
              'rank': 2,
              'title': '\nEdmund_百度翻译\n',
              'url': 'http://fanyi.baidu.com/?aldtype=85#en/zh/Edmund'},
             {'description': 'For 76 years Edmund Optics (EO) has been a '
                             'leading producer of optics, imaging, and '
                             'photonics technology.',
              'rank': 3,
              'title': 'About Edmund Optics',
              'url': 'https://www.edmundoptics.com/company/'},
             {'description': 'Research new and used cars including car prices, '
                             'view incentives and dealer inventory listings, '
                             'compare vehicles, get car buying advice and '
                             'reviews at ...',
              'rank': 4,
              'title': 'New Cars, Used Cars, Car Reviews and Pricing | Edmunds',
              'url': 'https://www.edmunds.com/'},
             {'description': 'For 76 years Edmund Optics (EO) has been a '
                             'leading producer of optics, imaging, and '
                             'photonics technology.',
              'rank': 5,
              'title': 'Products | Edmund Optics',
              'url': 'https://www.edmundoptics.com/products/'},
             {'description': 'Edmund爱特蒙特光电产品爱特蒙特光学 '
                             '(EO)已经有70年的历史,如今已成为光学元件、成像元件以及光子技术行业的领跑企业。生产的产品应用于研发,电子,半导体,医药,生物...',
              'rank': 6,
              'title': 'Edmund光电产品,镜片,玻色智能科技有限公司',
              'url': 'http://www.bosontech.com.cn/Products/edmund.html'},
             {'description': '最佳答案: 您好, Edmund [ˈedmənd] 是男子名, '
                             '英格兰人姓氏;埃德蒙(Edmond)的变体昵称Ed, Eddie, Eddy, Ned, '
                             'Neddie, Neddy。 例句: Edmund ...更多关于edmund的问题>>',
              'rank': 7,
              'title': 'edmund什么意思_百度知道',
              'url': 'https://zhidao.baidu.com/question/1860148058256233067.html'},
             {'description': "Edmund['edmənd] «返回  中文拼写:埃德蒙 名字含义:富有的守护者 "
                             '名字来源:古英语 名字类别: 流行度: 使用Edmund英文名的人: Edmund Burke '
                             '爱德蒙•伯克...',
              'rank': 8,
              'title': 'Edmund英文名_Edmund英文名字大全_人名词典 - Dict.CN 海词',
              'url': 'http://ename.dict.cn/Edmund'},
             {'description': 'Edmund II (died 30 November 1016), usually known '
                             'as Edmund Ironside, was King of England from 23 '
                             'April to 30 November 1016. He was the son of ...',
              'rank': 9,
              'title': 'Edmund Ironside - Wikipedia',
              'url': 'https://en.wikipedia.org/wiki/Edmund_Ironside'},
             {'description': None,
              'rank': 10,
              'title': '\nEdmund_百度百科\n',
              'url': 'https://baike.baidu.com/item/Edmund/10114566?fr=aladdin'}]}
```
Contary to popular wisdom the package doesn't throw an exception. This is due to the fact that Baidu may block you after having
scraped several pages deep. Instead, BaiduBot returns you a dictionary containing two elements. Results is a list of dictionary objects
containing the search result title, url, description and rank. The second dictionary item returned is an error value, which by
default is None, but may contain a string should we have run into any problems. This due to the fact that we may have 
already collected a number of scrape results before the Exception was thrown. In future releases, this API is likely to change
with the introduction a strict mode, which will raise an exception if anything should go wrong.
