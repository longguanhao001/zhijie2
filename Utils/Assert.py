from Page.BasePage import BasePage


class Assert():
    def __init__(self):
        # 断言前，先截图保存到测试报告
        BasePage().save_screenShot()

    def assert_equal(self, actul, expect):
        assert actul == expect, "{0}不等于{1}".format(actul, expect)

    def assert_not_equal(self, actul, expect):
        assert actul != expect, "{0}等于{1}".format(actul, expect)

    def assert_in(self, actul, expect):
        assert actul in expect, "{0}不包含{1}".format(expect, actul)

    def assert_not_in(self, actul, expect):
        assert actul not in expect, "{0}包含{1}".format(expect, actul)

    def assert_less(self, actul, expect):
        assert actul < expect, "{0}小于{1}".format(expect, actul)

    def assert_greater(self, actul, expect):
        assert actul > expect, "{0}大于{1}".format(expect, actul)

    def assert_greaterAndEqual(self, actul, expect):
        assert actul >= expect, "{0}大于{1}".format(expect, actul)

    def assert_lessAndEqual(self, actul, expect):
        assert actul <= expect, "{0}小于{1}".format(expect, actul)
