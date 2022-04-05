import os

from dotenv import load_dotenv
from dis_snek import Intents, Snake, listen

load_dotenv()

intents = Intents.DEFAULT | Intents.GUILD_MEMBERS
discord_token = os.environ["DISCORD_TOKEN"]

bot = Snake(
    default_prefix="x!",
    intents=intents,
    sync_interactions=True
)


@listen()
async def on_startup():
    lat = round(bot.latency * 1000, 2)

    print("👍 Floofy is ready to serve!")
    print(f"❤ Currently logged in as {bot.user} (ID: {bot.user.id})")
    print(f"Current average latency to Discord is {lat}ms")

    await bot.change_presence(activity="with new features!")


bot.grow_scale("commands.actions")

bot.start(discord_token)
