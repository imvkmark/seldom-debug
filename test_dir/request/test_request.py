import requests
import seldom
from pydash import has_substr
from seldom import data, Seldom


class TestRequest(seldom.TestCase):
    """
    测试请求
    """

    @data([
        {"scene": "home", "url": "/"},
    ])
    def test_pc(self, _, url):
        """
        测试PC
        """

        resp = requests.get(Seldom.base_url + url)
        self.assertTrue(resp.status_code, 200)
        self.assertTrue(has_substr(resp.text, "id=\"pre-loading\""))
        self.assertTrue(has_substr(resp.text, "pc-assets"))

    @data([
        {"scene": "m_home", "url": "/m"},
    ])
    def test_m(self, _, url):
        """
        测试手机端
        """
        resp = self.get(url)
        self.assertTrue(resp.status_code, 200)
        self.assertTrue(has_substr(resp.text, "id=\"pre-loading\""))
