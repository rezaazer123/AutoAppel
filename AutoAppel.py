from selenium import webdriver
import time
import os

file = open("settings.txt")
data = []
for line in file:
	data.append(line[:-1])
data = data[1::2]
mail = data[0]
mdp = data[1]
delay = int(data[2])

driver = webdriver.Chrome()

driver.get("https://www.leonard-de-vinci.net/student/presences/")

driver.find_element_by_id("login").send_keys(mail)
driver.find_element_by_id("btn_next").click()
time.sleep(1)
driver.find_element_by_id("passwordInput").send_keys(mdp)
driver.find_element_by_id("submitButton").click()
time.sleep(1)

appel = False

while not appel:

	driver.get("https://www.leonard-de-vinci.net/student/presences/")

	courses = driver.find_elements_by_class_name("btn-primary")
	print(str(len(courses)-1) + " cours aujourd'hui")

	i = 0

	for j in range(i,len(courses) - 1):
		i = i + 1

		try:
			courses[j].click()
			try:
				driver.find_element_by_id("set-presence").click()
				print("Appel validé !")
				appel = True
				break
			except:
				print("next")
		finally:
			time.sleep(1)
			driver.get("https://www.leonard-de-vinci.net/student/presences/")
			courses = driver.find_elements_by_class_name("btn-primary")

	time.sleep(delay)

input("Press any key to exit")
driver.close()