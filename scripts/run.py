import subprocess
import os


os.chdir("devsearch")


def run_dev() -> None:
    subprocess.run(["poetry", "run", "python", "manage.py", "runserver"])
