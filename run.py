import seldom
from seldom.utils import cache

if __name__ == "__main__":
    # 清理缓存
    cache.clear()

    # 执行测试用例目录
    seldom.main(
        path="./test_dir",
        case="test_dir.request.test_request.TestRequest",
        base_url="http://dev.kejinshou.com",
        title="Debug 接口测试",
        tester="多厘",
        language="zh-CN",
        description="接口测试"
    )
