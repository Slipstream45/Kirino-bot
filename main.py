import discord
import commands

intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    if message.content.startswith("!react"):
        command = message.content[7:]
        if command in commands.react_commands:
            await commands.react_commands[command].run(message)
    if message.content.startswith("!sfw"):
        command = message.content[5:]
        if command in commands.sfw_commands:
            await commands.sfw_commands[command].run(message)
    if message.content.startswith("!nsfw"):
        command = message.content[6:]
        if command in commands.nsfw_commands:
            await commands.nsfw_commands[command].run(message)


client.run('<BOT_TOKEN_HERE>')


