import pyautogui
import time
print("开始")
pyautogui.moveTo(10,10)
time.sleep(3)
print("等待启动结束")

print("找图标")
location = pyautogui.locateOnScreen('imgs/wechat.png',confidence=0.8)
if location is not None:
    print('Image center found at:', location)
    pyautogui.moveTo(location.left/2+location.width/4,location.top/2+location.height/4)
    pyautogui.click()
else:
    print('Image not found on screen. Please check the image and try again.')
time.sleep(3)

print("找图标")
location = pyautogui.locateOnScreen('imgs/666.png',confidence=0.8)
if location is not None:
    print('Image center found at:', location)
    pyautogui.moveTo(location.left/2+location.width/4,location.top/2+location.height/4)
    pyautogui.click()
else:
    print('Image not found on screen. Please check the image and try again.')
time.sleep(3)

print("找图标")
location = pyautogui.locateOnScreen('imgs/emoji_btn_area.png',confidence=0.8)
if location is not None:
    print('Image center found at:', location)
    pyautogui.moveTo(location.left/2+location.width/4,location.top/2+location.height/4)
    pyautogui.click()
    pyautogui.write("Hello")
    pyautogui.press("enter")
else:
    print('Image not found on screen. Please check the image and try again.')
time.sleep(3)