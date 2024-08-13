# PlayStation Direct Stock Checker Bot for Astro Bot Contoller (German Website)

This repository contains a customizable Python bot that checks the stock status of the Astro Bot limited edition DualSense wireless controller on the German PlayStation Direct store. The bot will notify you via Telegram and WhatsApp when the product is in stock, providing you with a real-time alert. This bot is designed to be used by developers who want to monitor stock levels for personal use or share the functionality with others.

## Features

- **Stock Checking**: Monitors the German PlayStation Direct store for the availability of the Astro Bot limited edition DualSense wireless controller.
- **Real-time Alerts**: Sends notifications via Telegram and WhatsApp when the product is in stock.
- **Status Updates**: Sends periodic status updates every hour to keep you informed about the bot's performance.
- **Web Dashboard**: Provides a simple web interface to monitor the bot's metrics like API call count, errors, and last response time.
- **Customizable Settings**: Adjust the API endpoints, check intervals, and notification settings to suit your needs.

## Prerequisites

1. **Python**: Ensure you have Python 3.8 or higher installed on your machine. You can download Python from the [official website](https://www.python.org/downloads/).

2. **Telegram Bot**: You need a Telegram bot token to send messages. You can create a Telegram bot by talking to [BotFather](https://t.me/botfather) on Telegram.
   
3. **WhatsApp CallMeBot API**: To send WhatsApp messages, you'll need to set up an API with CallMeBot. Follow the instructions on the [CallMeBot website](https://www.callmebot.com/blog/free-api-whatsapp-messages/) to get your API key and phone number.

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/playstation-stock-checker.git
    cd playstation-stock-checker
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Edit the `settings` dictionary in `stock_checker.py` with your personal API keys and phone numbers:

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

4. Start the bot by running the script:

    ```bash
    python stock_checker.py
    ```

## Usage

- **Telegram Bot Setup**:
  - Create a bot using [BotFather](https://t.me/botfather) on Telegram.
  - Obtain your bot token and chat ID. The chat ID is where the bot will send messages. You can obtain the chat ID by sending a message to your bot and then accessing `https://api.telegram.org/bot<YourBotToken>/getUpdates`.

- **WhatsApp CallMeBot Setup**:
  - Follow the instructions on [CallMeBot's WhatsApp API page](https://www.callmebot.com/blog/free-api-whatsapp-messages/) to get your API key.
  - Use the API key and phone number in the `settings` dictionary.

- **Bot Operations**:
  - The bot checks the stock status every 60 seconds (configurable).
  - If the product is in stock, it sends an instant alert via Telegram and WhatsApp.
  - The bot provides a status update every hour, informing you of its operational status, API response times, and any errors encountered.

- **Web Dashboard**:
  - The bot runs a small Flask server accessible on `http://localhost:5000` (or `http://<your-ip>:5000` if running on a server).
  - The dashboard provides a live overview of API calls, errors, last stock check, and more.

## Customization

- **Changing the Product**:
  - The bot is currently configured to monitor the Astro Bot limited edition DualSense controller. To monitor a different product, change the `productCodes` parameter in the `API_URL` setting.

- **Adjusting Check and Status Intervals**:
  - Modify the `CHECK_INTERVAL` and `STATUS_INTERVAL` values in the `settings` dictionary to change how frequently the bot checks for stock and sends status updates.

- **Additional Features**:
  - The bot can be extended to support additional notification platforms or track multiple products. Advanced users can add new features by modifying the provided codebase.

## Troubleshooting

- **Bot Not Sending Messages**:
  - Ensure that your Telegram bot token and chat ID are correct.
  - Verify that your WhatsApp API key and phone number are correctly configured.
  - Check the logs for any error messages related to network issues or incorrect configurations.

- **Web Dashboard Not Loading**:
  - Make sure Flask is installed correctly (`pip install Flask`).
  - Verify that the server is running by checking the terminal output for any errors.
  - Ensure that the port (5000 by default) is not being used by another application.

## Contributing

Contributions are welcome! If you have any ideas for new features, improvements, or bug fixes, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Python Telegram Bot](https://python-telegram-bot.org/)
- [CallMeBot](https://www.callmebot.com/) for the WhatsApp messaging API
- Flask for providing the web dashboard framework

This bot provides a simple and effective way to monitor product availability and is perfect for anyone looking to ensure they never miss out on the limited-edition controller again!
