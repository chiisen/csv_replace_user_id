import os

# 要從外部取得 MySQL 的帳密
# 安裝 pip install python-dotenv 可以讀取 .env 檔案
user = os.environ.get("DB_USER")
password = os.environ.get("DB_PASS")
if not user or not password:
    raise RuntimeError("請先設定 DB_USER / DB_PASS 環境變數")
# 用 user/password 做 DB 連線

print(f"使用者: {user}, 密碼長度: {len(password)}")
