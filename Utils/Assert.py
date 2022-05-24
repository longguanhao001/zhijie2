from Page.BasePage import BasePage


class Assert():


    def assert_equal(self, actul, expect):
        try:
            assert actul == expect, "{0}不等于{1}".format(actul, expect)
        except Exception as e:
            BasePage().save_screenShot()
            raise e

    def assert_not_equal(self, actul, expect):
        try:
            assert actul != expect, "{0}等于{1}".format(actul, expect)
        except Exception as e:
            BasePage().save_screenShot()
            raise e

    def assert_in(self, actul, expect):
        try:
            assert actul in expect, "{0}不包含{1}".format(expect, actul)
        except Exception as e:
            BasePage().save_screenShot()
            raise e

    def assert_not_in(self, actul, expect):
        try:
            assert actul not in expect, "{0}包含{1}".format(expect, actul)
        except Exception as e:
            BasePage().save_screenShot()
            raise e

    def assert_less(self, actul, expect):
        try:
            assert actul < expect, "{0}小于{1}".format(expect, actul)
        except Exception as e:
            BasePage().save_screenShot()
            raise e

    def assert_greater(self, actul, expect):
        try:
            assert actul > expect, "{0}大于{1}".format(expect, actul)
        except Exception as e:
            BasePage().save_screenShot()
            raise e

    def assert_greaterAndEqual(self, actul, expect):
        try:
            assert actul >= expect, "{0}大于{1}".format(expect, actul)
        except Exception as e:
            BasePage().save_screenShot()
            raise e

    def assert_lessAndEqual(self, actul, expect):
        try:
            assert actul <= expect, "{0}小于{1}".format(expect, actul)
        except Exception as e:
            BasePage().save_screenShot()
            raise e
