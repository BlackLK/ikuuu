import requests, json, re, os,time

session = requests.session()
# 配置用户名（一般是邮箱）

# 配置用户名对应的密码 和上面的email对应上
# server酱
SCKEY = os.environ.get('SCKEY')

BASE_URL = 'https://ikuuu.win'
base_host = BASE_URL.replace('https://', '').replace('http://', '')
login_url = f'{BASE_URL}/auth/login'
check_url = f'{BASE_URL}/user/checkin'
info_url = f'{BASE_URL}/user/profile'
logout_url=f'{BASE_URL}/user/logout'
header = {
        'origin': BASE_URL,
        'referer': login_url,
        'x-requested-with': 'XMLHttpRequest',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
# 从环境变量读取账号，格式: 邮箱#密码，多账号用换行分隔
accounts_env = os.environ.get('IKUUU_ACCOUNTS', '')
data = []
if accounts_env:
    for line in accounts_env.splitlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split('#')
        if len(parts) >= 2:
            data.append({'email': parts[0], 'passwd': parts[1]})
        else:
            print(f'账号格式错误，已跳过: {line}')
else:
    print('未配置环境变量 IKUUU_ACCOUNTS，请设置后重试')
    exit(1)
for account in data:
  try:
      print('进行登录...')
      print(account.get('email'))
      login_data = account.copy()
      login_data.update({
          'host': base_host,
          'code': '',
          'twofa_step': 0,
          'captcha_result': '',
          'remember_me': '',
          'pageLoadedAt': int(time.time() * 1000)
      })
      response = json.loads(session.post(url=login_url,headers=header,data=login_data).text)
      print(response['msg'])
      if response.get('ret') != 1:
          content = response.get('msg', '登录失败')
          continue
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
      if SCKEY:
          push_url = 'https://sctapi.ftqq.com/{}.send?title=ikuuu自动签到任务提示&desp={}'.format(SCKEY, content)
          requests.post(url=push_url)
          print('推送成功')
          logout_html = session.get(url=logout_url,headers=header).text
          print(account.get('email')+'退出登录中...')
          #time.sleep(10)
  except:
      content = '签到失败'
      print(content)
      if SCKEY:
          push_url = 'https://sctapi.ftqq.com/{}.send?title=ikuuu自动签到任务提示&desp={}'.format(SCKEY, content)
