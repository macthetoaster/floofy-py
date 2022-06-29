from naff import Extension, prefixed_command, PrefixedContext

from core.base import FloofyClient


class DavoExtension(Extension):
    bot: FloofyClient

    @prefixed_command(name="davo", aliases=["david"])
    async def davo_cmd(self, ctx: PrefixedContext) -> None:
        name = ctx.message.author.display_name
        await ctx.reply(f"> **{name}** totally, completely denies that they're a furry! >.<")


def setup(bot: FloofyClient):
    DavoExtension(bot)
