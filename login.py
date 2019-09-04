from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe") #load chrome instance
check_timer = 43200 #how often program will retry name change
load_timer = 3 #how long the site waits at each new load

desired_name = "" #what you want the new username to be

current_username = "" #current username for login
current_password = "" #current password for login

#load url
def load():
	driver.get("https://www.twitch.tv") #load ??? url
	time.sleep(load_timer) #wait for site to load
	
#click on top right login button
def nav_login():
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[1]/button').click() #click on login button
	time.sleep(.1) #wait for modal to load
	
#fill in form to login
def login():
	username = driver.find_username = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div[1]/div/div/form/div/div[1]/div/div[2]/input') #find username within modal
	password = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div[1]/div/div/form/div/div[2]/div/div[1]/div[2]/div[1]/input') #find password within modal

	username.send_keys(current_username) #send login info
	password.send_keys(current_password)	#send login info
	
	driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div[1]/div/div/form/div/div[3]/button').click() #submit login info
	time.sleep(load_timer) #wait for login to complete
	
#navigate to user settings
def nav_user():
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/nav/div/div[3]/div[5]/div/div/div/div[1]/button/figure/img').click() #click on user button
	time.sleep(.1) #wait for menu to come up
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/nav/div/div[3]/div[5]/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div/div/div[1]/div[12]/a/div/div[2]').click() #click on settings button
	time.sleep(load_timer) #wait for settings to load
	
#click on button to change name
def change():
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/main/div[2]/div[3]/div/div/div/div/div[6]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/a/div/div/span').click() #click on change name button
	time.sleep(load_timer) #wait for form to load
	
#fill in form and hit submit
def fill():
	username = driver.find_username = driver.find_element_by_xpath('//*[@id="login"]') #find username within form
	username.send_keys(desired_name) #send new username info
	time.sleep(load_timer) #let stuff update
	check()
	
	
#check if name registered / repeat
def check():
	update = driver.find_element_by_id("update") #find update button
	if(update.get_attribute("disabled")): #if not available
		driver.close()
		time.sleep(check_timer)
		main()
	else:
		update.click()
		time.sleep(load_timer)
		driver.close()
		print("I updated your username")

#main
def main():
	#call functions
	load()
	nav_login()
	login()
	nav_user()
	change()
	fill()

#main
if __name__ == "__main__":
	main()