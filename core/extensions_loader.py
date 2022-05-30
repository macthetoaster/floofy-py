import os

from core.base import FloofyClient


def load_extensions(bot: FloofyClient):
    bot.logger.info("Loading Extensions...")

    for root, dirs, files in os.walk("extensions"):
        for file in files:
            if file.endswith(".py") and not file.startswith("__init__"):
                file = file.removesuffix(".py")
                path = os.path.join(root, file)
                python_import_path = path.replace("/", ".").replace("\\", ".")

                print(f"Loading {python_import_path}")
                bot.load_extension(python_import_path)

    bot.logger.info(f"< {len(bot.interactions[0])} > Global Interactions Loaded")
