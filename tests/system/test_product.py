from unittest import TestCase

from mypage2 import app
import json
class ProductTest(TestCase):
    def test_welcome(self):
        with app.test_client() as c:
            resp = c.get('/api/products')
            self.assertEqual(resp.status_code, 200)

            self.assertEqual(json.loads(resp.get_data()) ,
        [{"price":75542.5,"productId":1,"productName":"Iphone13","rating":4.8},
         {"price":149999.5,"productId":4,"productName":"SamsungFlip","rating":4.8},
         {"price":69999.9,"productId":2,"productName":"Oneplus","rating":4.6},
         {"price":"38554","productId":"5","productName":"Redmi","rating":"4.3"},
         {"price":"24352","productId":"10","productName":"Xaomi","rating":"4.1"},
         {"price":"55435.5","productId":"100","productName":"GalaxySNote","rating":"4.1"}
         ])

