# 飞书接入配置指南

要完成飞书接入，您需要在飞书开放平台创建应用并获取以下信息：

## 第一步：在飞书开放平台创建应用

1. 访问 [飞书开放平台](https://open.feishu.cn/)
2. 登录后点击「创建应用」
3. 选择「自建应用」
4. 填写应用名称和描述

## 第二步：获取凭证信息

创建应用后，在应用详情页可以找到：
- App ID: 应用唯一标识符
- App Secret: 应用密钥

## 第三步：配置机器人权限

1. 在应用管理页面，点击「机器人」
2. 添加机器人并设置权限
3. 设置回调URL（如果使用webhook模式）

## 第四步：使用以下命令配置OpenClaw

```bash
# 设置基本配置
openclaw config set channels.feishu.appId "YOUR_APP_ID"
openclaw config set channels.feishu.appSecret "YOUR_APP_SECRET"
openclaw config set channels.feishu.domain "feishu" # 或 "lark"
openclaw config set channels.feishu.connectionMode "websocket" # 或 "webhook"

# 如果要限制谁能与机器人交互
openclaw config set channels.feishu.dmPolicy "allowlist"
openclaw config set channels.feishu.allowFrom '["+8618512519978"]'  # 替换为您的飞书ID
```

## 第五步：重启OpenClaw网关

```bash
openclaw gateway restart
```

完成后，我就能通过飞书与您交流了！