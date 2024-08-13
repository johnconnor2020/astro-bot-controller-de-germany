# PlayStation Astro Bot Controller Stock Checker Bot

This repository contains a Python bot designed to monitor the stock status of a PlayStation product on the official PlayStation store. The bot is capable of sending notifications via Telegram and WhatsApp using the [CallMeBot](https://www.callmebot.com/). Additionally, the bot runs a Flask server to provide a real-time dashboard for monitoring its status.

## Features

- **Automated Stock Monitoring**: Periodically checks the stock status of a specified PlayStation product.
- **Notifications**: Sends notifications to Telegram and WhatsApp when:
  - The bot starts monitoring.
  - The product becomes available (in stock).
  - There are any errors in the API calls.
  - Regular status updates are sent once an hour to keep the user informed.
- **Dashboard**: A simple web-based dashboard is available to track metrics such as API response times, the number of API calls made, and any failures.

## Requirements

- Python 3.7+
- Telegram Bot API Key
- WhatsApp API Key from CallMeBot
- Basic understanding of Python and API usage

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ps5-stock-checker.git
cd ps5-stock-checker
```

### 2. Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### 3. Configure the Bot

Open the `main.py` file and modify the `settings` dictionary to include your API URL, Telegram Bot Token, Telegram Chat ID, WhatsApp phone number, and WhatsApp API key.

```python
settings = {
    'API_URL': "https://api.direct.playstation.com/commercewebservices/ps-direct-de/users/anonymous/products/productList?fields=BASIC&lang=de_DE&productCodes=1000044988-DE",
    'TELEGRAM_BOT_TOKEN': "YOUR_TELEGRAM_BOT_TOKEN",
    'TELEGRAM_CHAT_ID': "YOUR_TELEGRAM_CHAT_ID",
    'WHATSAPP_PHONE': "YOUR_WHATSAPP_PHONE_NUMBER",
    'WHATSAPP_APIKEY': "YOUR_WHATSAPP_API_KEY",
    'CHECK_INTERVAL': 60,  # Check product stock every 60 seconds
    'STATUS_INTERVAL': 3600,  # Send a status update every 3600 seconds (1 hour)
}
```

### 4. Set Up Telegram Bot

1. Create a Telegram bot by talking to [BotFather](https://core.telegram.org/bots#botfather).
2. Copy the Bot Token provided by BotFather and paste it into the `TELEGRAM_BOT_TOKEN` field.
3. To get your `TELEGRAM_CHAT_ID`, send a message to your bot and then visit `https://api.telegram.org/bot<YourBOTToken>/getUpdates`. Look for the `chat` section in the response to find your Chat ID.

### 5. Set Up WhatsApp with CallMeBot

1. Go to the [CallMeBot WhatsApp API](https://www.callmebot.com/blog/free-api-whatsapp-messages/) page.
2. Follow the instructions to register your phone number with CallMeBot.
3. Use the API key provided by CallMeBot in the `WHATSAPP_APIKEY` field.

### 6. Run the Bot

To start the bot, run the following command:

```bash
python main.py
```

### 7. Access the Dashboard

Once the bot is running, you can monitor its activity by opening your web browser and navigating to `http://localhost:5000`. The dashboard will display the number of API calls made, any errors encountered, and other useful metrics.

## Flask Dashboard Overview

The Flask dashboard provides a real-time view of the bot’s operations. Here’s a breakdown of the information it displays:

- **API Calls**: Shows the total number of successful API requests made by the bot since it started.
- **Errors**: Displays the number of API request failures, which could be due to network issues or problems with the API itself.
- **Last Response**: Indicates the time in seconds taken by the last API response. This helps in understanding the API's performance.
- **Last In Stock**: Records the last time the product was found to be in stock. If the product has never been in stock since the bot started, this will show "N/A."
- **Check Interval**: Shows the frequency (in seconds) at which the bot checks the product's stock status. This is set by the `CHECK_INTERVAL` setting.
- **Status Interval**: Displays the interval (in seconds) at which the bot sends status updates to Telegram and WhatsApp. This is defined by the `STATUS_INTERVAL` setting.

## Bot Behavior on Startup and Shutdown

### Startup Behavior

- **Startup Notifications**: When the bot starts running, it immediately sends a notification to both Telegram and WhatsApp to inform you that it has begun monitoring the product. This helps confirm that the bot is running correctly and that notifications are working.

  Example Notification:
  ```
  Stock checker bot started and monitoring the product.
  ```

### Shutdown Considerations

- **Manual Shutdown**: If you need to stop the bot, you can do so by terminating the Python process (e.g., pressing `Ctrl+C` in the terminal). However, note that the bot does not send a shutdown notification. If you plan to stop the bot for an extended period, you may want to notify yourself manually.

- **Restarting**: If the bot is restarted (manually or automatically), it will again send a startup notification to confirm that it is running.

## How It Works

### Stock Checks

- The bot checks the PlayStation product's stock status every 60 seconds (by default). This interval is defined by the `CHECK_INTERVAL` setting.
- If the product is found to be in stock, the bot sends an instant notification to both your Telegram and WhatsApp.
- The bot also sends a notification when it starts to inform you that it has begun monitoring the product.

### Status Updates

- The bot sends a status update every hour (3600 seconds by default), summarizing its activity, including the number of API calls made, any errors encountered, and the last recorded API response time.
- This interval can be adjusted using the `STATUS_INTERVAL` setting.

### Error Handling

- If an error occurs during an API call (e.g., network issues), the bot will log the error and send a notification to both Telegram and WhatsApp. The bot will then continue to operate and will attempt the next scheduled check.

## Modifying Timings

The bot's checking and notification intervals are controlled by the following settings:

- **`CHECK_INTERVAL`**: This determines how often (in seconds) the bot checks the PlayStation product's stock status. For example, setting `CHECK_INTERVAL` to `60` means the bot checks every minute.
- **`STATUS_INTERVAL`**: This determines how often (in seconds) the bot sends a status update to Telegram and WhatsApp. For example, setting `STATUS_INTERVAL` to `3600` means the bot sends an update every hour.

To change these timings:

1. Open the `main.py` file.
2. Modify the values of `CHECK_INTERVAL` and `STATUS_INTERVAL` as desired.
3. Save the file and restart the bot.

### Example

If you want the bot to check the stock every 30 seconds and send a status update every 2 hours, you would set:

```python
settings = {
    'CHECK_INTERVAL': 30,
    'STATUS_INTERVAL': 7200,
}
```

## Security Considerations

- **API Key Protection**: To protect your sensitive data, it is recommended to use environment variables for storing your API keys, chat IDs, and phone numbers. This prevents accidentally sharing these details if the code is shared or pushed to a public repository.

### Example

You can set up environment variables in your operating system or by using a `.env` file with the following structure:

```plaintext
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

## Advanced Usage

### Monitoring Multiple Products

If you want to monitor multiple products, you will need to modify the script to handle multiple API URLs and check each one independently. This requires managing multiple requests and processing each product’s stock status separately.

### Running the Bot Continuously

For continuous monitoring, you might want to deploy the bot on a cloud server or use a virtual private server (VPS). Tools like `screen` or `tmux` can help you keep the bot running in the background. Alternatively, you could set up the bot as a `systemd` service on Linux.

## Contributing

If you want to contribute to this project:

1. Fork the repository.
2. Create a feature branch (`git checkout -b

 feature-branch`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License.

## Disclaimer

This bot is intended for personal use only. Be mindful of the terms of service of the APIs and websites you interact with using this bot. The author is not responsible for any misuse of this bot.

