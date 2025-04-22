"""Model for port operations."""
import os
import subprocess


class PortHelper:
    """Class for port operations."""

    @staticmethod
    def check_port(port):
        """Method to check port if running then stop it."""
        pid = PortHelper.__find_process_using_port(port)
        if pid:
            PortHelper.__kill_process(pid)

    @staticmethod
    def __find_process_using_port(port):
        """Method to find the process ID for the given port."""
        try:
            if os.name == 'nt':  # Windows
                result = subprocess.check_output(
                    f'netstat -ano | findstr :{port}', shell=True, text=True
                )
                for line in result.strip().split('\n'):
                    if f":{port}" in line:
                        parts = line.strip().split()
                        pid = parts[-1]
                        return int(pid)
            else:  # macOS/Linux
                result = subprocess.check_output(
                    f'lsof -ti:{port}', shell=True, text=True
                )
                pid = result.strip().split('\n', maxsplit=1)[0]
                return int(pid)
        except Exception:
            return None

    @staticmethod
    def __kill_process(pid):
        """Method to kill the given process by process ID"""
        try:
            if os.name == 'nt':
                subprocess.run(f'taskkill /PID {pid} /F', shell=True)
            else:
                os.kill(pid, 9)
        except Exception as e:
            print(f"Could not kill PID {pid}: {e}")
