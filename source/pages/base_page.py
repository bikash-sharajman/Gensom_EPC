from pathlib import Path
from datetime import date

class BasePage:
    
    @staticmethod
    def get_file(file_p):
        root_dir = Path(__file__).resolve().parents[2]
        file_dir = root_dir/f"{file_p}"
        return file_dir
    
    @staticmethod
    def get_expected_complition_date(date):
        pass
    
        
