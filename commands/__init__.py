import discord
import os
from discord.ext import commands

intents = discord.Intents.all()
client = discord.Client(intents=intents)

react_commands = {}
sfw_commands = {}
nsfw_commands = {}

def load_commands():
    for filename in os.listdir(os.path.join(os.path.dirname(__file__), "react")):
        if filename.endswith(".py"):
            name = filename[:-3]
            react_commands[name] = __import__("commands.react." + name, fromlist=["commands"])
    for filename in os.listdir(os.path.join(os.path.dirname(__file__), "sfw")):
        if filename.endswith(".py"):
            name = filename[:-3]
            sfw_commands[name] = __import__("commands.sfw." + name, fromlist=["commands"])
    for filename in os.listdir(os.path.join(os.path.dirname(__file__), "nsfw")):
        if filename.endswith(".py"):
            name = filename[:-3]
            nsfw_commands[name] = __import__("commands.nsfw." + name, fromlist=["commands"])

load_commands()
