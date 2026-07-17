from pathlib import Path


class BasePage:
    
    @staticmethod
    def get_file(file_p):
        root_dir = Path(__file__).resolve().parents[2]
        file_dir = root_dir/f"{file_p}"
        return file_dir
