import unittest
from selenium import webdriver

class Whatsapp_hacking(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_whatsapp(self):
		driver = self.driver;
		driver.get('http://web.whatsapp.com')
		a = raw_input("Enter something")
		elem = driver.find_element_by_xpath('//span[contains(text(),"Person name")]')
		elem.click()	
		elem1 = driver.find_elements_by_class_name('input')
		while True:
			elem1[1].send_keys('message')
			driver.find_element_by_class_name('send-container').click()

	def tearDown(self):
		self.driver.close()
if __name__ == "__main__" :
	unittest.main()
