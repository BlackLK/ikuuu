# ikuuu 自动签到脚本

支持多账号、Server酱推送的 ikuuu.pw 自动签到 Python 脚本。

---

## 功能

- 自动登录并签到
- 支持多账号（通过环境变量配置）
- 支持 Server酱（sctapi）推送结果

---

## 依赖安装

仅需 `requests` 库：

```bash
pip install requests
```

---

## 本地使用

### 1. 配置环境变量

- **单账号**

  ```bash
  export IKUUU_ACCOUNTS="你的邮箱#你的密码"
  ```

- **多账号**（每行一个，换行分隔）

  ```bash
  export IKUUU_ACCOUNTS="user1@gmail.com#123456
  user2@gmail.com#abcdef"
  ```

- **Server酱推送**（可选）

  ```bash
  export SCKEY="你的SCTKey"
  ```

### 2. 运行

```bash
python ikuuu.py
```

---

## 青龙面板使用

当前 `ikuuu.win` 登录页已启用 Geetest V4 行为验证，Python 脚本可能无法直接通过账号密码自动登录。若遇到 `系统无法接受您的验证结果，请刷新页面后重试。`，建议改用下面的 **脚本猫 / 篡改猴使用** 方案。

### 1. 拉取脚本

在青龙面板的【订阅管理】或【脚本管理】中添加订阅：

```bash
ql raw https://raw.githubusercontent.com/你的用户名/你的仓库/main/ikuuu.py
```

或者使用 `ql repo` 命令拉取整个仓库：

```bash
ql repo https://github.com/你的用户名/你的仓库.git "ikuuu" "" ""
```

### 2. 添加依赖

进入青龙面板 **依赖管理 → Python3**，添加：

```
requests
```

### 3. 配置环境变量

进入 **环境变量** 页面，添加：

| 名称 | 值 | 说明 |
|------|-----|------|
| `IKUUU_ACCOUNTS` | `邮箱#密码` | 多账号用换行分隔 |
| `SCKEY` | `SCTxxxxxxxxxxxxx` | Server酱推送 Key（可选） |

### 4. 定时任务

添加定时任务：

```
名称：ikuuu 签到
命令：task ikuuu.py
定时：0 9 * * *    # 每天早上 9 点执行
```

---

## 脚本猫 / 篡改猴使用

脚本猫 / 篡改猴方案运行在浏览器中，适合新版 `ikuuu.win` 需要行为验证的情况。你只需要先在浏览器里手动登录一次并完成验证，之后脚本会使用浏览器登录态自动签到。

新增脚本文件：

```text
ikuuu-scriptcat.user.js
```

这个脚本不是在青龙面板或命令行里运行的，而是安装到浏览器扩展 **脚本猫** 或 **篡改猴 Tampermonkey** 里面使用。

适用场景：

- `ikuuu.win` 登录时出现 Geetest 行为验证
- Python 脚本提示 `系统无法接受您的验证结果，请刷新页面后重试。`
- 你希望在浏览器已登录状态下自动签到

### 1. 安装脚本管理器

任选一个浏览器脚本管理器安装：

- Chrome / Edge：在扩展商店搜索 `脚本猫`
- Chrome / Edge / Firefox：在扩展商店搜索 `Tampermonkey` 或 `篡改猴`
- GitHub 项目地址：<https://github.com/scriptscat/scriptcat>

### 2. 安装用户脚本

将仓库中的 `ikuuu-scriptcat.user.js` 添加到脚本猫或篡改猴。

如果仓库已推送到 GitHub，也可以通过 Raw 地址安装：

```text
https://raw.githubusercontent.com/BlackLK/ikuuu/main/ikuuu-scriptcat.user.js
```

安装方式：

- **脚本猫**：打开脚本猫扩展管理页面，新建脚本，将 `ikuuu-scriptcat.user.js` 内容粘贴进去并保存
- **篡改猴**：打开 Tampermonkey 管理面板，点击 `添加新脚本`，将 `ikuuu-scriptcat.user.js` 内容粘贴进去并保存
- **Raw 地址安装**：浏览器打开上面的 Raw 地址，脚本管理器会自动识别并提示安装

### 3. 使用方法

1. 打开 <https://ikuuu.win/auth/login>
2. 手动登录账号并完成 Geetest 验证
3. 登录成功后访问任意 `https://ikuuu.win/*` 页面
4. 脚本会每天自动执行一次签到
5. 签到结果会通过浏览器通知和控制台输出

### 4. 注意事项

- 需要保持浏览器中的 ikuuu 登录态有效
- 如果 Cookie 过期，需要重新手动登录
- 脚本猫 / 篡改猴方案不需要配置账号密码环境变量
- 脚本默认每天只执行一次，避免重复签到

---

## 环境变量格式说明

- `IKUUU_ACCOUNTS` 格式：`邮箱#密码`
- 多账号：每行一个，换行分隔
- 示例：

  ```
  13800000001#123456
  13800000002#abcdef
  ```

---

## 注意事项

- ikuuu 的用户名通常是邮箱，密码为服务密码
- 确保账号密码中的 `#` 仅用于分隔符，不含多余 `#`
- 如需推送，先去 [Server酱](https://sct.ftqq.com/) 获取 SendKey
