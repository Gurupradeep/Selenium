
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Facebook_login(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_whatsapp(self):
		driver = self.driver
		driver.get("https://www.facebook.com")
		driver.maximize_window()
		email = driver.find_element_by_xpath("//*[@id='email']")
		email.send_keys('gurupradeept@gmail.com')
		password = driver.find_element_by_xpath("//*[@id='pass']")
		password.send_keys("9603982107")
		Facebook_loginn_button = driver.find_element_by_xpath("//*[@id='u_0_m']")
		Facebook_loginn_button.click()
	def tearDown(self):
		self.driver.close()
if __name__ == "__main__" :
	unittest.main()
