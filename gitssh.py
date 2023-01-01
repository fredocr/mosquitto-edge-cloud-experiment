import subprocess

def execute_ssh_commands():
subprocess.run(["eval", "$(ssh-agent -s)"])
subprocess.run(["ssh-add", "~/.ssh/id_ed25519"])

execute_ssh_commands()