from naff import Extension, prefixed_command, cooldown, Buckets, PrefixedContext, Embed
from core.base import FloofyClient
from static.actions import actions
from static.constants import embed_colors


class HelpCommandExtension(Extension):
    bot: FloofyClient

    @prefixed_command(name="help")
    @cooldown(Buckets.MEMBER, 1, 10)
    async def help_command(self, ctx: PrefixedContext) -> None:
        actions_embed = self.get_actions_embed()

        await ctx.reply(embed=actions_embed)
        return

    @staticmethod
    def get_actions_embed() -> Embed:
        # Get all the action names available and sort them
        action_names = list(actions.keys())
        action_names.sort()

        # Create the embed object to show the user the actions
        embed: Embed = Embed(
            title="Action commands",
            color=embed_colors["main_color"],
            description=f"The following commands are available as actions:\n```{', '.join(action_names)}```"
        )

        return embed


def setup(bot: FloofyClient):
    HelpCommandExtension(bot)
