import pyautogui as pag
import config
import time

pag.FAILSAFE = True


class VPN():

    def loginVPN(token):
        pag.click(200, 1055)
        pag.PAUSE = 5
        pag.doubleClick(1624, 1055)
        pag.PAUSE = 10
        pag.click(856, 538)
        pag.PAUSE = 0
        pag.typewrite(config.vpn_pin)
        pag.click(846, 568)
        pag.typewrite(token)
        time.sleep(3)
        pag.click(698, 629)
        time.sleep(15)
        pag.screenshot(r'C:\Users\crm0174\Pictures\guiScreen\screen.png')


# print(pag.position())Connect VPN
def loginVPN(token):
    pag.click(200, 1055)
    pag.PAUSE = 5
    pag.doubleClick(1624, 1055)
    pag.PAUSE = 10
    pag.click(856, 538)
    pag.PAUSE = 0
    pag.typewrite(config.vpn_pin)
    pag.click(846, 568)
    pag.typewrite(token)
    time.sleep(3)
    pag.click(698, 629)
    time.sleep(15)
    pag.screenshot(config.imgPath)