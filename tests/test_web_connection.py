import unittest
from urllib.request import urlopen


class TestWiki(unittest.TestCase):
    # soup = None

    def setUp(self):
        pass
        # global soup
        # r = requests.get('https://en.wikipedia.org/wiki/Monty_Python')
        # soup = BeautifulSoup(r.text, 'lxml')

    def test_chart_url(self):
        chart_url = 'https://movie.douban.com/chart'
        http_status_code = urlopen(chart_url).getcode()
        self.assertEqual(200, http_status_code)

    # def test_content_exists(self):
    #     global soup
    #     content = soup.find('div', id='mw-content-text')
    #     self.assertIsNotNone(content)


if __name__ == '__main__':
    unittest.main(argv=['ignored', '-v'], exit=False)
