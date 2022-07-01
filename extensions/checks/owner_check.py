from naff import Extension, InteractionContext

from core.base import FloofyClient


class OwnerCheckExtension(Extension):
    def __init__(self, bot: FloofyClient):
        self.bot = bot
        self.add_ext_check(self.owner_check)

    async def owner_check(self, ctx: InteractionContext) -> bool:
        is_bot_owner = (ctx.bot.owner.id == ctx.author.id)
        return is_bot_owner


def setup(bot: FloofyClient):
    OwnerCheckExtension(bot)
