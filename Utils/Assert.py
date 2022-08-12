from Page.BasePage import BasePage


class Assert():


    def assert_equal(self,expect , actul):
        assert actul == expect, "{0}不等于{1}".format(actul, expect)

    def assert_not_equal(self, expect, actul):
        assert actul != expect, "{0}等于{1}".format(actul, expect)

    def assert_in(self, actul, expect):
        assert actul in expect, "{0}不包含{1}".format(expect, actul)

    def assert_not_in(self, actul, expect):
        assert actul not in expect, "{0}包含{1}".format(expect, actul)

    def assert_less(self, expect, actul):
        assert actul < expect, "{0}小于{1}".format(expect, actul)

    def assert_greater(self, expect, actul):
        assert actul > expect, "{0}大于{1}".format(expect, actul)

    def assert_greaterAndEqual(self, actul, expect):
        assert actul >= expect, "{0}大于等于{1}".format(expect, actul)

    def assert_lessAndEqual(self, actul, expect):
        assert actul <= expect, "{0}小于等于{1}".format(expect, actul)
