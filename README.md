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
