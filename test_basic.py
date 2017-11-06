import os
import unittest
from urllib.parse import urlparse
from app import addticket
from models import app,db,Ticket
 
 

 
 
class BasicTests(unittest.TestCase):
 
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql+pymysql://test_db:testpassword@localhost:8889/test_db'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
 
        
        self.assertEqual(app.debug, False)
 
    # executed after each test
    def tearDown(self):
        pass
 
 
###############
#### tests ####
###############
 
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_add_ticket(self):
        response = self.app.get('/addticket', follow_redirects=True)
        self.assertEqual(response.status_code, 200)  

    def test_add_donation(self):
        response = self.app.post('/addticket',data=dict(item='test', name='test',
              phone='1234567890',delivery='Can drop off',
              comments='',formtype = 'donate',pickup='',location='test'),follow_redirects=True)
        self.assertEqual(response.status_code, 200) 

    def test_add_request(self):
        response = self.app.post('/addticket',data=dict(item='test', name='test',
              phone='1234567890',delivery='',
              comments='',formtype = 'request',pickup='Can pick up',location='test'),follow_redirects=True)
        self.assertEqual(response.status_code, 200)  
    
    def test_view_tickets(self):
        response = self.app.get('/show_all', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_show_ticket(self):
        response = self.app.get('/view?tid=1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        #expectedPath = '/view?tid=1'
        #self.assertEqual(urlparse(response.location).path, expectedPath)
    
    '''def test_admin(self):
        response = self.app.get('/admin', follow_redirects=True)
        self.assertEqual(response.status_code, 404)
'''    
 
if __name__ == "__main__":
    unittest.main()