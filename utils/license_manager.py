import json
import os
from datetime import datetime, timedelta

class LicenseManager:
    def __init__(self):
        self.license_file = "configs/license.json"
        self.load_license()
    
    def load_license(self):
        try:
            if os.path.exists(self.license_file):
                with open(self.license_file, 'r', encoding='utf-8') as f:
                    self.license_data = json.load(f)
            else:
                # Tạo license mặc định (demo 30 ngày)
                self.license_data = {
                    "user_name": "Người dùng Demo",
                    "license_type": "Trial",
                    "start_date": datetime.now().strftime("%Y-%m-%d"),
                    "end_date": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d"),
                    "max_tasks_per_day": 500,
                    "features": ["phone", "browser", "emulator"]
                }
                self.save_license()
        except:
            # Nếu có lỗi, tạo license mặc định
            self.license_data = {
                "user_name": "Người dùng Demo",
                "license_type": "Trial", 
                "start_date": datetime.now().strftime("%Y-%m-%d"),
                "end_date": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d"),
                "max_tasks_per_day": 500,
                "features": ["phone", "browser", "emulator"]
            }
    
    def save_license(self):
        os.makedirs("configs", exist_ok=True)
        with open(self.license_file, 'w', encoding='utf-8') as f:
            json.dump(self.license_data, f, ensure_ascii=False, indent=2)
    
    def is_license_valid(self):
        try:
            end_date = datetime.strptime(self.license_data["end_date"], "%Y-%m-%d")
            return datetime.now() <= end_date
        except:
            return False
    
    def get_days_remaining(self):
        try:
            end_date = datetime.strptime(self.license_data["end_date"], "%Y-%m-%d")
            remaining = (end_date - datetime.now()).days
            return max(0, remaining)
        except:
            return 0
    
    def get_license_info(self):
        return {
            "user_name": self.license_data.get("user_name", "Unknown"),
            "license_type": self.license_data.get("license_type", "Unknown"),
            "days_remaining": self.get_days_remaining(),
            "max_tasks_per_day": self.license_data.get("max_tasks_per_day", 0),
            "is_valid": self.is_license_valid()
        }