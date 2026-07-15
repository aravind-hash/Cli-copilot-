"""Command executor module"""

import subprocess
from typing import Tuple
from cli_copilot.ai.models import AIModel


class CommandExecutor:
    """Executes commands with AI assistance"""

    def __init__(self):
        self.ai = AIModel()

    def execute_command(self, command: str) -> Tuple[int, str, str]:
        """
        Execute a shell command

        Args:
            command: Command to execute

        Returns:
            Tuple of (return_code, stdout, stderr)
        """
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=30,
            )
            return result.returncode, result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            return -1, "", "Command timed out"
        except Exception as e:
            return -1, "", str(e)

    def execute_with_confirmation(self, command: str, confirm: bool = True) -> bool:
        """
        Execute command with optional confirmation

        Args:
            command: Command to execute
            confirm: Ask for confirmation before executing

        Returns:
            True if executed successfully
        """
        if confirm:
            response = input(f"Execute: {command}? (y/n): ")
            if response.lower() != "y":
                return False

        return_code, stdout, stderr = self.execute_command(command)

        if return_code == 0:
            if stdout:
                print(stdout)
            return True
        else:
            print(f"Error: {stderr}")
            return False

    def get_help_for_command(self, command: str) -> str:
        """
        Get AI-powered help for a command

        Args:
            command: The command to get help for

        Returns:
            Help text
        """
        return self.ai.explain_command(command)

    def suggest_command_for_task(self, task: str) -> str:
        """
        Get AI suggestion for a task

        Args:
            task: Description of the task

        Returns:
            Suggested command
        """
        return self.ai.suggest_command(task)
