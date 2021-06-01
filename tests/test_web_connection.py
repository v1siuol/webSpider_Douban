import unittest
from urllib.request import Request, urlopen


class TestWiki(unittest.TestCase):
    # soup = None

    def setUp(self):
        pass
        # global soup
        # r = requests.get('https://en.wikipedia.org/wiki/Monty_Python')
        # soup = BeautifulSoup(r.text, 'lxml')

    def test_chart_url(self):
        chart_url = 'https://movie.douban.com/chart'
        fake_headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        req = Request(url=chart_url, headers=fake_headers)
        http_status_code = urlopen(req).getcode()
        self.assertEqual(200, http_status_code)

    # def test_content_exists(self):
    #     global soup
    #     content = soup.find('div', id='mw-content-text')
    #     self.assertIsNotNone(content)


if __name__ == '__main__':
    unittest.main(argv=['ignored', '-v'], exit=False)
