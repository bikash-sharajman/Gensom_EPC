from pathlib import Path
from datetime import date

class BasePage:
    
    @staticmethod
    def get_file(file_p):
        root_dir = Path(__file__).resolve().parents[2]
        file_path = Path(str(file_p).strip().strip('"').strip("'")).expanduser()

        if not file_path.is_absolute():
            file_path = root_dir / file_path

        return file_path
    
    @staticmethod
    def get_expected_complition_date(date):
        pass
    
        
