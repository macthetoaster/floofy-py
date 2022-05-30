import datetime

from naff import Extension, prefixed_command, PrefixedContext, Embed

from core.base import FloofyClient


class PingExtension(Extension):
    bot: FloofyClient

    @prefixed_command(name="ping")
    async def ping_cmd(self, ctx: PrefixedContext):
        latency = self.bot.latency * 1000
        avatar_url = self.bot.user.avatar.url

        reply = Embed(
            title="Discord API Latency",
            description=f"What's up, dog? :wolf:\nCurrent latency: `{latency:,.2f}ms`",
            thumbnail=avatar_url,
            timestamp=datetime.datetime.now().astimezone()
        )

        await ctx.reply(embed=reply)


def setup(bot: FloofyClient):
    PingExtension(bot)
