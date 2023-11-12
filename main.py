import os
import logging
from contextlib import suppress
from dotenv import load_dotenv

import zenbo


def get_config() -> dict:
    load_dotenv()
    return {
        "debug": os.getenv("LOGGING_DEBUG"),
        "zenbo_ip": os.getenv("ZENBO_IP_ADDRESS"),
        "zenbo_name": os.getenv("ZENBO_NAME"),
    }


if __name__ == "__main__":
    config = get_config()
    level = logging.DEBUG if config["debug"] else logging.INFO
    logging.basicConfig(level=level)
    with suppress(KeyboardInterrupt):
        zenbo.init(config)
