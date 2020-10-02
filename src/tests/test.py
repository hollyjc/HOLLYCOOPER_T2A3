import unittest
from mailer import Mailer
from conversion import Conversion

class TestMailer(unittest.TestCase):
    def test_sendmail(self):
        result = Mailer.send_mail("test email", " ")
        self.assertEqual(result, True)


class TestConversion(unittest.TestCase):
    def test_conversion(self):
        price = """Price:
                            AU$11.62"""
        result = Conversion.convert_price(price)
        self.assertEqual(result, 11.62)