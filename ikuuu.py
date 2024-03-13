import requests, json, re, os,time

session = requests.session()
# 配置用户名（一般是邮箱）

# 配置用户名对应的密码 和上面的email对应上
# server酱
SCKEY = os.environ.get('SCKEY')

login_url = 'https://ikuuu.pw/auth/login'
check_url = 'https://ikuuu.pw/user/checkin'
info_url = 'https://ikuuu.pw/user/profile'
logout_url='https://ikuuu.pw/user/logout'
header = {
        'origin': 'https://ikuuu.me',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
# 多个账户名密码
data = [{'email': '12345@gmail.com','passwd': '12345'},{'email': '账号2@gmail.com','passwd': '12345'}] 
for account in data:
  try:
      print('进行登录...')
      print(account.get('email'))
      response = json.loads(session.post(url=login_url,headers=header,data=account).text)
      print(response['msg'])
    # 获取账号名称
      info_html = session.get(url=info_url,headers=header).text
      #print(info_html)
#     info = "".join(re.findall('<span class="user-name text-bold-600">(.*?)</span>', info_html, re.S))
#     print(info)
    # 进行签到
      result = json.loads(session.post(url=check_url,headers=header).text)
      print(result['msg'])
      content = result['msg']
    # 进行推送
      if SCKEY != '':
          push_url = 'https://sctapi.ftqq.com/{}.send?title=ikuuu自动签到任务提示&desp={}'.format(SCKEY, content)
          requests.post(url=push_url)
          print('推送成功')
          logout_html = session.get(url=logout_url,headers=header).text
          print(account.get('email')+'退出登录中...')
          #time.sleep(10)
  except:
      content = '签到失败'
      print(content)
      if SCKEY != '':
          push_url = 'https://sctapi.ftqq.com/{}.send?title=ikuuu自动签到任务提示&desp={}'.format(SCKEY, content)
