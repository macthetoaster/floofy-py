from naff import slash_command, InteractionContext, slash_option, OptionTypes, Embed, Button

from core.base import FloofyClient
from extensions.checks.owner_check import OwnerCheckExtension
from static.constants import embed_colors


class GenerateInviteExtension(OwnerCheckExtension):
    bot: FloofyClient

    @slash_command(
        name="generateinvite",
        description="OWNER ONLY | Generate an invite link for the bot"
    )
    @slash_option(
        name="admin_perms",
        description="If the bot should have administration permissions or not",
        opt_type=OptionTypes.BOOLEAN,
        required=False
    )
    async def generate_invite(self, ctx: InteractionContext, admin_perms: bool = False):
        permissions = "8" if admin_perms else "412317173824"
        embed_perm_string = "administrator" if admin_perms else "normal"
        base_url = "https://discord.com/api/oauth2/authorize"
        client_id = self.bot.app.id
        full_url = f"{base_url}?client_id={client_id}&permissions={permissions}&scope=bot%20applications.commands"

        invite_button = Button(
            label="Invite",
            style=5,
            url=full_url
        )

        embed = Embed(
            title="Invite me to your server!",
            description=f"Click the button below to invite me to your server with `{embed_perm_string}` permissions.",
            color=embed_colors["main_color"]
        )

        await ctx.send(embed=embed, components=[invite_button])


def setup(bot: FloofyClient):
    GenerateInviteExtension(bot)
