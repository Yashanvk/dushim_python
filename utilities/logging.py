import logging

class LastLinesFileHandler(logging.FileHandler):
    def emit(self, record):
        super().emit(record)
        self._trim_file()

    def _trim_file(self):
        log_lenght = 77
        with open(self.baseFilename, "r") as f:
            lines = f.readlines()

        if len(lines) > log_lenght:
            with open(self.baseFilename, "w") as f:
                f.writelines(lines[-log_lenght:])
