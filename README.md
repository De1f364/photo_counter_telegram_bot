# photo_counter_telegram_bot
The Telegram-based bot that counts objects on photos received.

<a href="https://ibb.co/Ns46QnL"><img src="https://i.ibb.co/drh01JQ/2019-06-23-20-07-49.png" alt="2019-06-23-20-07-49" border="0"></a><br /><a target='_blank' href='https://ru.imgbb.com/'></a><br />

**TO RUN**
1. Install Python3
2. PIP install imageAI and all dependencies form requirements.txt
`pip install -r requirements.txt`
3. Put ResNet model at the root (e.g. "resnet50_coco_best_v2.0.1")
4. Set your bot's API token to BOT_API_TOKEN environment variable
`export BOT_API_TOKEN=your_token`
5. Run main

**Big Ups**
The project utilizes PyTorch, Python-Telegram-Bot and ImageAI brilliant tools.
