import sqlite3


class SQLiteDB:
    def __init__(self, path: str):
        self._path = path

    def create_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self._path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_db(self):
        with self.create_connection() as conn:
            conn.execute("""
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                is_active BOOLEAN
            )
            """)
