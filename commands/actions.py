import re
from random import choice
from typing import Optional

from dis_snek import (
    Scale,
    Snake,
    listen,
    Message,
    Member,
    AllowedMentions,
    message_command,
    MessageContext,
    Embed,
    Button,
    component_callback,
    ComponentContext
)
from dis_snek.api.events import MessageCreate

from static.action_texts import actions

MENTION_REGEX = re.compile(r"(<@!?(\d{17,19})>)")


class Actions(Scale):
    def __init__(self, bot: Snake):
        self.bot: Snake = bot

        self.furpiles: dict[int, set[int]] = {}

    # For the actions to be dynamic, this needs to be an event listener. If not, each action would need to be its
    # own command.
    @listen()
    async def on_message_create(self, event: MessageCreate):
        msg = event.message

        if not msg.content.lower().startswith(self.bot.default_prefix):
            return

        command, *args = msg.content.split()
        action = command[2:]
        action = action.lower()

        if actions.get(action) is None:
            return

        user = msg.author.display_name
        receivers = self._get_receivers(msg, " ".join(args))

        if receivers is None:
            self_reply = f"> {actions[action]['self']} {actions[action]['emoji']}"
            return await msg.channel.send(self_reply.format(user=f"**{user}**"))

        action_reply = choice(actions[action]["with_receivers"])
        action_emoji = actions[action]["emoji"]
        formatted_reply = action_reply.format(user=f"**{user}**", receivers=receivers)

        await msg.channel.send(
            f"> {formatted_reply} {action_emoji}",
            allowed_mentions=AllowedMentions.none()
        )

    @staticmethod
    def _get_receivers(msg: Message, phrase: Optional[str] = None) -> Optional[str]:
        if phrase is None:
            phrase = msg.content

        if not phrase:
            if not msg.message_reference:
                return None

            reply = msg.channel.get_message(msg.message_reference.message_id)
            return f"**{reply.author.display_name}**"

        mentions = re.findall(MENTION_REGEX, phrase)

        if not mentions:
            return phrase

        # transform to Member objects
        mentions: list[Member] = [msg.guild.get_member(int(uid)) for _, uid in mentions]

        mention_string = ""
        for (idx, men) in enumerate(mentions):
            men_name = men.display_name

            if idx == 0:
                mention_string += f"**{men_name}**"
            elif idx == len(mentions) - 1:
                mention_string += f" and **{men_name}**"
            else:
                mention_string += f", **{men_name}**"

        return mention_string

    @message_command()
    async def furpile(
            self, ctx: MessageContext
    ):  # too lazy to mess with the auto-arg things
        # clear the previous pile
        self.furpiles[ctx.channel.id] = set()

        msg = ctx.message
        receivers: list[Member] = []

        # This is a bit of wet code, but I found it easier to do
        if content := msg.content[10:]:
            mentions = re.findall(MENTION_REGEX, content)
            receivers.extend([msg.guild.get_member(int(id)) for _, id in mentions])

        if msg.message_reference:
            reply = msg.channel.get_message(msg.message_reference.message_id)
            receivers.append(reply.author)

        text = ""
        if receivers:
            for (idx, men) in enumerate(receivers):
                men_name = men.display_name

                if idx == 0:
                    text += f"**{men_name}**"
                elif idx == len(receivers) - 1:
                    text += f" and **{men_name}**"
                else:
                    text += f", **{men_name}**"
        else:
            text = content or "themselves"

        # add author and any victims to the pile
        receivers.append(ctx.author)
        self.furpiles[ctx.channel.id] |= {receiver.id for receiver in receivers}

        # Get the message prepared
        str_format = f"**{ctx.author}** starts a furpile on {text}!"
        embed = Embed(description=str_format)
        embed.add_field(
            name="Furs:",
            value="\n".join(receiver.display_name for receiver in receivers),
        )
        button = Button(style=1, label="Join the pile!", custom_id="furpile_join")

        # send the message
        await ctx.send(embeds=embed, components=button)

    @component_callback("furpile_join")
    async def furpile_join(self, ctx: ComponentContext):
        pile = self.furpiles.get(ctx.channel.id)

        if not pile:  # Possible due to restarts
            return await ctx.send("Invalid button", ephemeral=True)

        if ctx.author.id in pile:
            return await ctx.send("You're already in the pile!", ephemeral=True)

        old_embed = ctx.message.embeds[0]
        old_embed.fields[0].value += "\n" + ctx.author.display_name

        pile.add(ctx.author.id)

        await ctx.edit_origin(embeds=old_embed)


def setup(bot):
    Actions(bot)
