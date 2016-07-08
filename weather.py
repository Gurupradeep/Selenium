import unittest
import json
import urllib2

class weather_report(unittest.TestCase):
	self.Apiurl = "http://api.openweathermap.org/data/2.5/weather"
	self.Apikey = "212e4ab07607542ad7629754c0645bea"

	def test_weather_by_city_name(self):
		city_name = raw_input("Enter_City_name")
		url = (self.Apiurl+"?q="+city_name+"&"+"APPID="+self.Apikey)
		#print(url)
        response = urllib2.urlopen(url)
        html = response.read()
        #print(html)
        json_data = json.loads(html)
        city_name_test = json_data["name"]
        #print(city_name_test)
        city_name_test = json_data["name"]
		print("city_name = "+city_name_test)
		weather = json_data["weather"]
		main_data = json_data["main"]
		print("weather = "+ weather[0]["main"])
		print("Description = "+weather[0]["description"])
		print("Humidity = "+ str(main_data["humidity"]))
		print("Min temp = "+ str(main_data["temp_min"]))
		print("Max temp = "+str(main_data["temp_max"]))
	def tearDown(self):
        print("Test is Over")
if __name__ =="__main__"
	unittest.main()