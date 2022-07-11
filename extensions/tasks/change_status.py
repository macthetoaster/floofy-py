from random import choice

from naff import Extension, Task, IntervalTrigger, Activity, Status, ActivityType, listen

from core.base import FloofyClient
from static.constants import statuses


class ChangeStatusExtension(Extension):
    bot: FloofyClient

    @Task.create(IntervalTrigger(minutes=10))
    async def change_status(self):
        new_status = choice(statuses)

        await self.bot.change_presence(
            status=Status.ONLINE,
            activity=Activity(
                name=new_status,
                type=ActivityType.PLAYING
            )
        )

    @listen()
    async def on_ready(self):
        # Start up the change status task
        self.change_status.start()

        # Log to the console that we've started the task
        self.bot.logger.info("Started status change task!")


def setup(bot: FloofyClient):
    ChangeStatusExtension(bot)
