import json
import datetime

class Logger:
    def __init__(self, log_file):
        """
        Initializes the Logger with the specified log file.
        
        :param log_file: The filename where logs will be appended.
        """
        self.log_file = 'game_logs/' + log_file + '.jsonl'

    def _write_log(self, log_entry):
        """
        Writes a single log entry to the JSONL file.
        
        :param log_entry: A dictionary representing the log event.
        """
        with open(self.log_file, 'a', encoding="utf-8") as f:
            f.write(json.dumps(log_entry) + "\n")

    def log_event(self, event, extra_data=None):
        """
        Logs a generic event.
        
        :param event: A string describing the event.
        :param extra_data: Optional dictionary with extra details about the event.
        """
        log_entry = {
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "event": event
        }
        if extra_data is not None:
            log_entry["extra_data"] = extra_data
        self._write_log(log_entry)

    def log_chat(self, sender, message):
        """
        Logs a chat message.
        
        :param sender: The sender of the message.
        :param message: The content of the chat message.
        """
        log_entry = {
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "event": "chat",
            "sender": sender,
            "message": message
        }
        self._write_log(log_entry)

    def log_vote(self, sender, vote):
        """
        Logs a player's final vote.
        
        :param sender: The name of the player.
        :param vote: The final decision ('split' or 'steal').
        """
        log_entry = {
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "event": "vote",
            "sender": sender,
            "vote": vote
        }
        self._write_log(log_entry)
