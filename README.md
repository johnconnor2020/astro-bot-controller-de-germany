# 🎮 PlayStation Astro Bot Controller Stock Checker Bot for Germany / DE / Deutschland

A Python bot designed to monitor the stock status of the Astro Bot limited edition DualSense wireless controller on the German PlayStation Direct store. The bot sends notifications via Telegram and WhatsApp using CallMeBot and includes a real-time monitoring dashboard.

## 📋 Table of Contents
- [✨ Features](#-features)
- [🔧 Requirements](#-requirements)
- [⚙️ Installation](#️-installation)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Install Dependencies](#2-install-dependencies)
  - [3. Configure the Bot](#3-configure-the-bot)
  - [4. Set Up Telegram Bot](#4-set-up-telegram-bot)
  - [5. Set Up WhatsApp with CallMeBot](#5-set-up-whatsapp-with-callmebot)
  - [6. Run the Bot](#6-run-the-bot)
  - [7. Access the Dashboard](#7-access-the-dashboard)
- [🖥️ Flask Dashboard Overview](#️-flask-dashboard-overview)
- [🚀 Bot Behavior on Startup and Shutdown](#-bot-behavior-on-startup-and-shutdown)
  - [Startup Behavior](#startup-behavior)
  - [Shutdown Considerations](#shutdown-considerations)
- [🔄 How It Works](#-how-it-works)
  - [Stock Checks](#stock-checks)
  - [Status Updates](#status-updates)
  - [Error Handling](#error-handling)
- [⏱️ Modifying Timings](#️-modifying-timings)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [⚠️ Disclaimer](#-disclaimer)

---

## ✨ Features
- **Automated Stock Monitoring**: Periodically checks the stock status of the specified PlayStation product.
- **Multi-Platform Notifications**: Sends notifications via Telegram and WhatsApp for key events such as startup, in-stock alerts, and errors.
- **Web Dashboard**: Provides a real-time web-based dashboard to monitor bot activity and metrics.
- **Error Handling**: Logs errors and sends notifications when API calls fail.

## 🔧 Requirements
- **Python 3.7+**: Download the latest version [here](https://www.python.org/downloads/).
- **Telegram Bot API Key**: Create a Telegram bot using [BotFather](https://t.me/botfather).
- **WhatsApp API Key from CallMeBot**: Follow instructions on the [CallMeBot website](https://www.callmebot.com/blog/free-api-whatsapp-messages/).
- **Basic understanding of Python and API usage**.

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/playstation-stock-checker.git
cd playstation-stock-checker
```

### 2. Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### 3. Configure the Bot

Edit the `settings` dictionary in the `main.py` file with your details:

```python
settings = {
    'API_URL': "https://api.direct.playstation.com/commercewebservices/ps-direct-de/users/anonymous/products/productList?fields=BASIC&lang=de_DE&productCodes=1000044988-DE",
    'TELEGRAM_BOT_TOKEN': "YOUR_TELEGRAM_BOT_TOKEN",
    'TELEGRAM_CHAT_ID': "YOUR_TELEGRAM_CHAT_ID",
    'WHATSAPP_PHONE': "YOUR_WHATSAPP_PHONE",
    'WHATSAPP_APIKEY': "YOUR_WHATSAPP_APIKEY",
    'CHECK_INTERVAL': 60,
    'STATUS_INTERVAL': 3600,
}
```

### 4. Set Up Telegram Bot

1. Create a bot using [BotFather](https://t.me/botfather).
2. Copy the Bot Token provided and paste it into the `TELEGRAM_BOT_TOKEN` field.
3. Get your `TELEGRAM_CHAT_ID` by sending a message to your bot and then visiting `https://api.telegram.org/bot<YourBotToken>/getUpdates`.

### 5. Set Up WhatsApp with CallMeBot

1. Visit the [CallMeBot WhatsApp API page](https://www.callmebot.com/blog/free-api-whatsapp-messages/).
2. Follow the instructions to register your phone number.
3. Use the API key provided by CallMeBot in the `WHATSAPP_APIKEY` field.

### 6. Run the Bot

To start the bot, run:

```bash
python main.py
```

### 7. Access the Dashboard

Monitor the bot's activity by navigating to `http://localhost:5000` in your web browser. The dashboard displays the number of API calls made, any errors encountered, and other useful metrics.

## 🖥️ Flask Dashboard Overview

The Flask dashboard provides a real-time view of the bot’s operations:

- **API Calls**: Number of successful API requests.
- **Errors**: Number of API request failures.
- **Last Response**: Time taken by the last API response.
- **Last In Stock**: Last time the product was found in stock.
- **Check Interval**: How often the bot checks the stock status.
- **Status Interval**: How often the bot sends status updates.

## 🚀 Bot Behavior on Startup and Shutdown

### Startup Behavior

When the bot starts, it sends a notification to both Telegram and WhatsApp to confirm that it has begun monitoring.

Example Notification:
```
Stock checker bot started and monitoring the product.
```

### Shutdown Considerations

- **Manual Shutdown**: Stop the bot by terminating the Python process (e.g., Ctrl+C). No shutdown notification is sent.
- **Restarting**: On restart, the bot sends a startup notification.

## 🔄 How It Works

### Stock Checks

- The bot checks the product's stock status every 60 seconds (by default).
- If the product is in stock, the bot sends a notification to Telegram and WhatsApp.
- The bot also sends a startup notification when it begins monitoring.

### Status Updates

- The bot sends a status update every hour, summarizing its activity.
- This interval can be adjusted using the `STATUS_INTERVAL` setting.

### Error Handling

- If an error occurs during an API call, the bot logs the error and sends a notification to both Telegram and WhatsApp. It continues to operate and will attempt the next scheduled check.

## ⏱️ Modifying Timings

Adjust the checking and notification intervals by modifying the `CHECK_INTERVAL` and `STATUS_INTERVAL` in the `settings` dictionary.

### Example

To check the stock every 30 seconds and send a status update every 2 hours, set:

```python
settings = {
    'CHECK_INTERVAL': 30,
    'STATUS_INTERVAL': 7200,
}
```

## 🤝 Contributing

Contributions are welcome! 

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This bot is intended for personal use only. Be mindful of the terms of service of the APIs and websites you interact with using this bot. The author is not responsible for any misuse of this bot.

