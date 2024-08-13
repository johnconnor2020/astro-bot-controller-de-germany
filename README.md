Certainly! Below is an enhanced README that combines the strengths and additional features from both versions, providing a comprehensive guide for users who want to use and customize the PlayStation Astro Bot Controller Stock Checker Bot.

---

# PlayStation Astro Bot Controller Stock Checker Bot

This repository contains a Python bot designed to monitor the stock status of the Astro Bot limited edition DualSense wireless controller on the German PlayStation Direct store. The bot sends notifications via Telegram and WhatsApp using the CallMeBot service. It also includes a Flask server to provide a real-time dashboard for monitoring the bot's status.

## Features

- **Automated Stock Monitoring**: Periodically checks the stock status of the specified PlayStation product (Astro Bot limited edition DualSense wireless controller).
- **Multi-Platform Notifications**: Sends notifications via Telegram and WhatsApp when:
  - The bot starts monitoring.
  - The product becomes available (in stock).
  - Errors occur during API calls.
  - Regular status updates are sent every hour to keep the user informed.
- **Web Dashboard**: A simple web-based dashboard to track metrics such as API response times, the number of API calls made, and any failures.
- **Customizable Settings**: Allows users to adjust check intervals, notification intervals, and other settings according to their needs.
- **Error Handling**: Logs errors and sends notifications when API calls fail, ensuring the user is always informed.

## Requirements

- **Python 3.7+**: Ensure you have Python installed. Download the latest version [here](https://www.python.org/downloads/).
- **Telegram Bot API Key**: Create a Telegram bot using [BotFather](https://t.me/botfather) and obtain your bot token.
- **WhatsApp API Key from CallMeBot**: Follow instructions on the [CallMeBot website](https://www.callmebot.com/blog/free-api-whatsapp-messages/) to get your API key and register your phone number.
- **Basic understanding of Python and API usage**.

## Installation

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

Edit the `settings` dictionary in the `main.py` file to include your API URL, Telegram Bot Token, Telegram Chat ID, WhatsApp phone number, and WhatsApp API key:

```python
settings = {
    'API_URL': "https://api.direct.playstation.com/commercewebservices/ps-direct-de/users/anonymous/products/productList?fields=BASIC&lang=de_DE&productCodes=1000044988-DE",
    'TELEGRAM_BOT_TOKEN': "YOUR_TELEGRAM_BOT_TOKEN",
    'TELEGRAM_CHAT_ID': "YOUR_TELEGRAM_CHAT_ID",
    'WHATSAPP_PHONE': "YOUR_WHATSAPP_PHONE",
    'WHATSAPP_APIKEY': "YOUR_WHATSAPP_APIKEY",
    'CHECK_INTERVAL': 60,  # Time between each stock check in seconds
    'STATUS_INTERVAL': 3600,  # Time between status updates in seconds
}
```

### 4. Set Up Telegram Bot

1. Create a Telegram bot by talking to [BotFather](https://t.me/botfather).
2. Copy the Bot Token provided by BotFather and paste it into the `TELEGRAM_BOT_TOKEN` field.
3. To get your `TELEGRAM_CHAT_ID`, send a message to your bot and then visit `https://api.telegram.org/bot<YourBotToken>/getUpdates`. Look for the chat section in the response to find your Chat ID.

### 5. Set Up WhatsApp with CallMeBot

1. Go to the [CallMeBot WhatsApp API page](https://www.callmebot.com/blog/free-api-whatsapp-messages/).
2. Follow the instructions to register your phone number with CallMeBot.
3. Use the API key provided by CallMeBot in the `WHATSAPP_APIKEY` field.

### 6. Run the Bot

To start the bot, run the following command:

```bash
python main.py
```

### 7. Access the Dashboard

Once the bot is running, monitor its activity by opening your web browser and navigating to `http://localhost:5000`. The dashboard will display the number of API calls made, any errors encountered, and other useful metrics.

## Flask Dashboard Overview

The Flask dashboard provides a real-time view of the bot’s operations:

- **API Calls**: Total number of successful API requests made by the bot since it started.
- **Errors**: Number of API request failures (e.g., network issues, API problems).
- **Last Response**: Time (in seconds) taken by the last API response, which helps in understanding the API's performance.
- **Last In Stock**: Last time the product was found to be in stock. If the product has never been in stock since the bot started, this will show "N/A."
- **Check Interval**: Frequency (in seconds) at which the bot checks the product's stock status, as set by the `CHECK_INTERVAL`.
- **Status Interval**: Interval (in seconds) at which the bot sends status updates to Telegram and WhatsApp, as defined by the `STATUS_INTERVAL`.

## Bot Behavior on Startup and Shutdown

### Startup Behavior

- **Notifications**: When the bot starts, it immediately sends a notification to both Telegram and WhatsApp to inform you that it has begun monitoring the product.

  Example Notification:
  ```
  Stock checker bot started and monitoring the product.
  ```

### Shutdown Considerations

- **Manual Shutdown**: If you stop the bot (e.g., by pressing Ctrl+C), it does not send a shutdown notification. You may want to notify yourself manually if stopping the bot for an extended period.
- **Restarting**: If the bot restarts, it sends a startup notification to confirm that it is running.

## How It Works

### Stock Checks

- The bot checks the PlayStation product's stock status every 60 seconds by default. This interval is defined by the `CHECK_INTERVAL` setting.
- If the product is in stock, the bot sends an instant notification to both Telegram and WhatsApp.
- The bot also sends a notification when it starts monitoring the product.

### Status Updates

- The bot sends a status update every hour (3600 seconds by default), summarizing its activity, including API calls made, errors encountered, and the last recorded API response time.
- This interval can be adjusted using the `STATUS_INTERVAL` setting.

### Error Handling

- If an error occurs during an API call (e.g., network issues), the bot logs the error and sends a notification to both Telegram and WhatsApp. The bot will continue to operate and attempt the next scheduled check.

## Modifying Timings

The bot's checking and notification intervals are controlled by:

- **CHECK_INTERVAL**: How often (in seconds) the bot checks the PlayStation product's stock status. For example, setting `CHECK_INTERVAL` to 60 means the bot checks every minute.
- **STATUS_INTERVAL**: How often (in seconds) the bot sends a status update to Telegram and WhatsApp. For example, setting `STATUS_INTERVAL` to 3600 means the bot sends an update every hour.

To change these timings:

1. Open the `main.py` file.
2. Modify the values of `CHECK_INTERVAL` and `STATUS_INTERVAL` as desired.
3. Save the file and restart the bot.

### Example

If you want the bot to check the stock every 30 seconds and send a status update every 2 hours, set:

```python
settings = {
    'CHECK_INTERVAL': 30,
    'STATUS_INTERVAL': 7200,
}
```

## Security Considerations

To protect your sensitive data, it is recommended to use environment variables for storing API keys, chat IDs, and phone numbers. This prevents accidentally sharing these details if the code is shared or pushed to a public repository.

### Example

You can set up environment variables in your operating system or by using a `.env` file with the following structure:

```env
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
WHATSAPP_PHONE=your_whatsapp_number
WHATSAPP_APIKEY=your_api_key
```

Modify your script to read from these environment variables:

```python
import os

settings = {
    'API_URL': os.getenv('API_URL', "default_url"),
    'TELEGRAM_BOT_TOKEN': os.getenv('TELEGRAM_BOT_TOKEN', "default_token"),
    'TELEGRAM_CHAT_ID': os.getenv('TELEGRAM_CHAT_ID', "default_chat_id"),
    'WHATSAPP_PHONE': os.getenv('WHATSAPP_PHONE', "default_phone"),
    'WHATSAPP_APIKEY': os.getenv('WHATSAPP_APIKEY', "default_apikey"),
    'CHECK_INTERVAL': int(os.getenv('CHECK_INTERVAL', 60)),
    'STATUS_INTERVAL': int(os.getenv('STATUS_INTERVAL', 3600)),
}
```


