import sqlite3


def get_data_blogger(id_blogger):
    blogger_data = ""
    conn = sqlite3.connect("ad_sphere.db")
    cursor = conn.cursor()
    return blogger_data