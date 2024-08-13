    import asyncio
    import logging
    from datetime import datetime
    import pytz
    from flask import Flask, render_template_string
    from threading import Thread
    import aiohttp
    from telegram import Bot

    # Configuration and Settings
    settings = {
        'API_URL': "https://api.direct.playstation.com/commercewebservices/ps-direct-de/users/anonymous/products/productList?fields=BASIC&lang=de_DE&productCodes=1000044988-DE",
        'TELEGRAM_BOT_TOKEN': "YOUR_TELEGRAM_BOT_TOKEN",
        'TELEGRAM_CHAT_ID': "YOUR_TELEGRAM_CHAT_ID",
        'WHATSAPP_PHONE': "YOUR_WHATSAPP_PHONE",
        'WHATSAPP_APIKEY': "YOUR_WHATSAPP_APIKEY",
        'CHECK_INTERVAL': 60,
        'STATUS_INTERVAL': 3600,
    }

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    bot = Bot(token=settings['TELEGRAM_BOT_TOKEN'])

    metrics = {'last_api_response_time': None, 'failure_count': 0, 'api_call_count': 0, 'last_in_stock_time': None}

    app = Flask(__name__)

    @app.route('/')
    def dashboard():
        return render_template_string(DASHBOARD_TEMPLATE, **metrics, **settings)

    DASHBOARD_TEMPLATE = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Bot Status</title>
        <style>
            body{font-family:sans-serif;margin:0;padding:20px;background:#f4f4f4;display:flex;justify-content:center;align-items:center;height:100vh}
            .container{background:#fff;border-radius:10px;box-shadow:0 0 10px rgba(0,0,0,.1);padding:20px;text-align:center}
            h1{color:#4CAF50}
            .item{margin:10px 0;padding:10px;background:#f9f9f9;border-radius:5px}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Bot Status</h1>
            <div class="item">API Calls: {{ api_call_count }}</div>
            <div class="item">Errors: {{ failure_count }}</div>
            <div class="item">Last Response: {{ last_api_response_time }} seconds</div>
            <div class="item">Last In Stock: {{ last_in_stock_time or 'N/A' }}</div>
            <div class="item">Check Interval: {{ CHECK_INTERVAL }} seconds</div>
            <div class="item">Status Interval: {{ STATUS_INTERVAL }} seconds</div>
        </div>
    </body>
    </html>
    """

    async def send_message(message, platform="telegram"):
        urls = {
            "telegram": f"https://api.telegram.org/bot{settings['TELEGRAM_BOT_TOKEN']}/sendMessage?chat_id={settings['TELEGRAM_CHAT_ID']}&text={message}",
            "whatsapp": f"https://api.callmebot.com/whatsapp.php?phone={settings['WHATSAPP_PHONE']}&text={message}&apikey={settings['WHATSAPP_APIKEY']}"
        }
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(urls[platform]) as response:
                    response.raise_for_status()
                logging.info(f"{platform.capitalize()} message sent: {message}")
            except Exception as e:
                logging.error(f"Failed to send {platform} message: {e}")

    async def check_stock(session):
        try:
            start_time = asyncio.get_event_loop().time()
            async with session.get(settings['API_URL']) as response:
                response.raise_for_status()
                data = await response.json()
                metrics['last_api_response_time'] = asyncio.get_event_loop().time() - start_time
                logging.info(f"API response time: {metrics['last_api_response_time']:.2f} seconds")
                metrics['api_call_count'] += 1
                metrics['failure_count'] = 0

                if data['products'][0]['stock']['stockLevelStatus'] == "inStock":
                    metrics['last_in_stock_time'] = datetime.now(pytz.timezone('Europe/Berlin')).strftime("%Y-%m-%d %H:%M:%S")
                    message = "Product in stock! https://direct.playstation.com/de-de/buy-accessories/dualsense-wireless-controller-astro-bot-limited-edition"
                    await asyncio.gather(send_message(message, "telegram"), send_message(message, "whatsapp"))
                    return True
                return False
        except aiohttp.ClientError as e:
            logging.error(f"HTTP Request failed: {e}")
            metrics['failure_count'] += 1
            await asyncio.gather(send_message(f"API call failed: {e}", "telegram"), send_message(f"API call failed: {e}", "whatsapp"))
            return None

    async def main():
        logging.info("Starting stock checker...")
        await asyncio.gather(
            send_message("Stock checker bot started and monitoring the product.", "telegram"),
            send_message("Stock checker bot started and monitoring the product.", "whatsapp")
        )

        async with aiohttp.ClientSession() as session:
            last_status_time = datetime.now()
            while True:
                await check_stock(session)

                if (datetime.now() - last_status_time).total_seconds() >= settings['STATUS_INTERVAL']:
                    status_message = f"Bot running. Last API response: {metrics['last_api_response_time']:.2f}s. Calls: {metrics['api_call_count']}, Failures: {metrics['failure_count']}"
                    await asyncio.gather(send_message(status_message, "telegram"), send_message(status_message, "whatsapp"))
                    last_status_time = datetime.now()

                await asyncio.sleep(settings['CHECK_INTERVAL'])

    def run_flask():
        app.run(host='0.0.0.0', port=5000)

    if __name__ == "__main__":
        Thread(target=run_flask).start()
        asyncio.get_event_loop().run_until_complete(main())