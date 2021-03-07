import time

from selenium import webdriver

import config


class AquilaClass():

    @staticmethod
    def loadPageAndLogin(flag):
        webdr = webdriver.Chrome(config.web_driver_dir)
        webdr.get(config.aquila_link)
        time.sleep(3)
        for i in range(20):
            if webdr.execute_script("return document.readyState") == "complete":
                webdr.find_element_by_xpath(config.xpath_log).send_keys(config.username)
                webdr.find_element_by_xpath(config.xpath_pass).send_keys(config.password)
                webdr.find_element_by_xpath(config.xpath_subb).click()
                time.sleep(10)
                if flag == 1:
                    webdr.find_element_by_xpath(config.xpath_inizio).click()
                elif flag == 0:
                    webdr.find_element_by_xpath(config.xpath_inizio).click()
                    time.sleep(1)
                    webdr.find_element_by_xpath(config.xpath_inizio).click()
                time.sleep(5)
                webdr.get_screenshot_as_file('bot/package/screen/screen.png')
                webdr.close()
                return True

    # @staticmethod
    # def loadPageAndLogout():
    #     webdr = webdriver.Chrome("C:\\bin\\chromedriver.exe")
    #     webdr.get('http://10.24.48.120/bee/jsp/login#aquila-my-logs/68546000')
    #     time.sleep(3)
    #     for i in range(20):
    #         if webdr.execute_script("return document.readyState") == "complete":
    #             webdr.find_element_by_xpath(config.xpathLog).send_keys('crm0174')
    #             webdr.find_element_by_xpath(config.xpathPass).send_keys('xX19cGLyMarty')
    #             webdr.find_element_by_xpath(config.xpathSubb).click()
    #             time.sleep(10)
    #             webdr.find_element_by_xpath(config.xpathInizio).click()
    #             time.sleep(5)
    #             webdr.find_element_by_xpath(config.xpathInizio).click()
    #             time.sleep(5)
    #             webdr.get_screenshot_as_file('bot/package/screen/screen.png')
    #             webdr.close()
    #             return True
