import datetime

from naff import slash_command, InteractionContext, Embed

from core.base import FloofyClient
from extensions.checks.owner_check import OwnerCheckExtension
from static.constants import embed_colors


class BotStatusExtension(OwnerCheckExtension):
    bot: FloofyClient

    @slash_command(
        name="botstatus",
        description="OWNER ONLY | Check the status of the bot"
    )
    async def bot_status(self, ctx: InteractionContext):
        # Set up variables for the different data points
        now = datetime.datetime.now()
        socket_created = ctx.bot.start_time
        uptime = now - socket_created

        guild_count = len(ctx.bot.guilds)
        guild_text = "server" if guild_count == 1 else "servers"

        latency = ctx.bot.average_latency * 1000

        # Create a new embed object
        status_embed = Embed(
            title="FloofyBot Status",
            description=f"Current status of the bot is: **{ctx.bot.status.value}**",
            color=embed_colors["main_color"],
            timestamp=now,
            thumbnail=ctx.bot.user.avatar.url
        )

        # Add fields for the status data
        status_embed.add_field(
            name="Servers LOL",
            value=f"{guild_count} {guild_text}",
            inline=True
        )
        status_embed.add_field(
            name="Members",
            value=f"Who knows?",
            inline=True
        )
        status_embed.add_field(
            name="Uptime",
            value=f"{str(uptime)[:-4]}",
            inline=True
        )
        status_embed.add_field(
            name="Avg. Latency",
            value=f"{latency:,.2f}ms",
            inline=True
        )
        status_embed.add_field(
            name="Shards",
            value=f"{ctx.bot.total_shards}",
            inline=True
        )
        status_embed.add_field(
            name="Prefixed Commands",
            value=f"{len(ctx.bot.prefixed_commands)}"
        )
        status_embed.add_field(
            name="Slash Commands",
            value=f"{len(ctx.bot.interactions)}"
        )

        await ctx.send(embed=status_embed)


def setup(bot: FloofyClient):
    BotStatusExtension(bot)
