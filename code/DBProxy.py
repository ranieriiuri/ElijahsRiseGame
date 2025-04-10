import sqlite3


class DBProxy:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.connection.execute('''
                                   CREATE TABLE IF NOT EXISTS elijahsRiseplayerData(
                                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                                   name TEXT NOT NULL,
                                   score INTEGER NOT NULL,
                                   date TEXT NOT NULL)
                                '''
                                )

    def save(self, score_dict: dict):
        self.connection.execute('INSERT INTO elijahsRiseplayerData (name, score, date) VALUES (:name, :score, :date)', score_dict)
        # esse 'commit' é padrão tbm do sqlite3 pra confirmar a query criada
        self.connection.commit()

    # método q mostra os ultimos 10 scores
    def retrieve_top10(self) -> list:
        return self.connection.execute('SELECT * FROM elijahsRiseplayerData ORDER BY score DESC LIMIT 10').fetchall()

    def close(self):
        return self.connection.close()
