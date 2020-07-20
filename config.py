from selenium import webdriver

target = {
    "phone": "15567678801",
    "name": "刘成",
    "email": "2434479840@qq.com",
    "address": "吉林",
    "comment": "咨询"
}

settings = {
    "times": 20,
    "timeout": 5,
    "driver": webdriver.Firefox(),
}
