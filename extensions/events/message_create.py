import re
from random import choice
from typing import Optional

from naff import Extension, listen, Message, Member, AllowedMentions
from naff.api.events import MessageCreate

from core.base import FloofyClient
from static.actions import actions

MENTION_REGEX = re.compile(r"(<@!?(\d{17,19})>)")


class MessageCreateExtension(Extension):
    bot: FloofyClient

    @listen()
    async def on_message_create(self, event: MessageCreate):
        msg = event.message

        # Check if the message starts with the prefix
        prefixed_message = False

        for prefix in self.bot.default_prefix:
            if msg.content.startswith(prefix):
                prefixed_message = True

        if not prefixed_message:
            return

        # Split the message into its parts so we can work with them
        command, *args = msg.content.split()
        action = command[2:].lower()

        if actions.get(action) is None:
            return

        # Get the user's display name and receivers
        user = msg.author.display_name
        receivers = self._get_receivers(msg, " ".join(args))

        if receivers is None:
            self_reply = f"> {user} {actions[action]['self']} {actions[action]['emoji']}"
            return await msg.channel.send(self_reply)

        # Format the reply if there are any receivers
        action_reply = choice(actions[action]["with_receivers"])
        action_emoji = actions[action]["emoji"]
        formatted_reply = action_reply.format(receivers=receivers)

        # Send the message
        await msg.channel.send(
            f"> {user} {formatted_reply} {action_emoji}",
            allowed_mentions=AllowedMentions.none()
        )

    @staticmethod
    def _get_receivers(msg: Message, custom_content: Optional[str] = None) -> Optional[str]:
        if custom_content is None:
            custom_content = msg.content

        if not custom_content:
            if not msg.message_reference:
                return None

            reply = msg.channel.get_message(msg.message_reference.message_id)
            return f"**{reply.author.display_name}**"

        mentions = re.findall(MENTION_REGEX, custom_content)

        if not mentions:
            return custom_content

        mentions: list[Member] = [msg.guild.get_member(int(uid)) for _, uid in mentions]

        mention_string = ""

        for (idx, mention) in enumerate(mentions):
            mention_name = mention.display_name

            if idx == 0:
                mention_string += f"**{mention_name}**"
            elif idx == len(mentions) - 1:
                mention_string += f" and **{mention_name}**"
            else:
                mention_string += f", **{mention_name}**"

        return mention_string


def setup(bot: FloofyClient):
    MessageCreateExtension(bot)
