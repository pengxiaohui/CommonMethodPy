
# coding=utf8
# 准备购买票的车次，
interested = [
    'G1379', 'G1377', 'D3295', 'G7393'
]


# 12306账号
username = 'pppoe4444'

# 每隔多少秒刷新一次，设定一定的间隔，防止服务器认为是攻击
refreshRate = 5



# 导入selenium 库里面的webdriver 模块
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from winsound import  Beep
import time,sys

# 下面的代码指定是chrome 的驱动，注意这个driver 对象是后面自动化的入口
#  成功后返回一个WebDriver 实例对象，通过它的方法，可以控制浏览器


driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(10)

# get 方法 打开指定网址
driver.get('https://kyfw.12306.cn/otn/login/init')
driver.find_element_by_id('username').send_keys(username)

input('### 现在显示的是登录界面，请输入密码和验证码，点击登录\n登录成功后，请选择出发地、目的地、日期，再按回车')

driver.get('https://kyfw.12306.cn/otn/leftTicket/init')


# # 接下来我们要在出发地选输入南京南。
#
# #  driver找到了该元素的话，就会返回一个表示该元素的WebElement对象。
# fromEle = driver.find_element_by_id('fromStationText')
#
#
# # 先点击一下它，这是12306的限制，不点击不行
# fromEle.click()
#
# fromEle.clear()
# fromEle.send_keys(fromStation + '\n')
#
# # 目的地也是一样的操作
# toEle = driver.find_element_by_id('toStationText')
# #这里也要点击一下
# toEle.click()
# toEle.clear()
# toEle.send_keys(toStation + '\n')

# # 选择开始时间，F12 看出来 是Select,
# timeSelect =  Select(driver.find_element_by_id('cc_start_time'))
# timeSelect.select_by_visible_text(timeRange)

# 第3个tab就是第3天
query = driver.find_element_by_css_selector('#query_ticket')


i = 0
# 循环不断的搜索
while True:
    i += 1
    isGet = False # 设置为没有找到

    # 点击这个，就会搜索车次了
    query.click()

    # 选择2等座有票的的车次
    xpath ='//*[@id="queryLeftTable"]//td[4][@class]/../td[1]//a'


    theTrains = driver.find_elements_by_xpath(xpath)

    for one in theTrains:
        name = one.text
        if name in interested:
            isGet = True
            print('***  有剩余车票 ' + name)
            # 找到当前元素的上层节点
            target = one.find_element_by_xpath('../../../../../td[last()]')
            # print(target.get_attribute('outerHTML'))
            target.click()

            time.sleep(4)
            driver.find_element_by_id('normalPassenger_1').click()
            driver.find_element_by_id('submitOrder_id').click()
            # one.find_element_by_css_selector('#qr_submit_id').click()
            Beep(1500, 2000)  # freqency and duration

            sys.exit()


    if not isGet:
        print(f'#{i}轮搜索没有找到')

    # 隔5秒钟，进行下一轮搜索，
    time.sleep(refreshRate)




