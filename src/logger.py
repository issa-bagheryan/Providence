import json
from datetime import datetime
from pathlib import Path


class EventLogger:

    def __init__(self, path):

        self.path = Path(path)

        self.path.parent.mkdir(
            exist_ok=True
        )


    def log(self, stats):

        if not stats["alert"]:
            return


        event = {
            "timestamp": datetime.now().isoformat(),
            "cars": stats["cars"],
            "people": stats["people"],
            "traffic": stats["traffic"]
        }


        with open(self.path, "a") as file:

            file.write(
                json.dumps(event) + "\n"
            )