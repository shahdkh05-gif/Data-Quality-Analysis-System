import sqlite3


def save_to_sqlite(data, database_path, table_name):
    """Store the cleaned DataFrame in a SQLite database table."""
    connection = sqlite3.connect(database_path)
    data.to_sql(table_name, connection, if_exists="replace", index=False)
    connection.close()
