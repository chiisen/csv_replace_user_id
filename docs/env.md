# 概要：可選的傳遞方式（優先順序建議）
1. 環境變數（相對安全、適合 CI / server）
2. OS 的密鑰庫（例如 keyring）或雲端秘密管理（AWS/Azure）— 用於生產
3. .env 檔搭配 python-dotenv（本機開發）
4. getpass.getpass() 互動式提示（避免在指令列顯示）
5. stdin（透過管線）或檔案（需注意檔案權限）
6. CLI 參數（不建議把密碼以參數傳，因為可被其他程式或使用者查到 process list）

## 1) 環境變數（推薦）
- 優點：不會出現在 process 列表，較容易與系統/CI（secret management）整合
- Windows 命令 (只在當前 cmd 視窗生效):
```bash
set DB_USER=alice
set DB_PASS=Secret123
python run_sql.py
```
- Python 範例：
```python
import os

user = os.environ.get("DB_USER")
password = os.environ.get("DB_PASS")
if not user or not password:
    raise RuntimeError("請先設定 DB_USER / DB_PASS 環境變數")
# 用 user/password 做 DB 連線
```
- .env:
```bash
DB_USER=alice
DB_PASS=Secret123
```
- Python:
```python
from dotenv import load_dotenv
import os

load_dotenv()  # 讀載 .env 檔
user = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
```

