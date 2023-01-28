# commands/nsfw.py
import requests

async def run(message):
    # Fetch image from waifu.pics API
    response = requests.get('https://api.waifu.pics/sfw/yeet')
    image_url = response.json()["url"]

    # Send image in the channel
    await message.channel.send(image_url)

