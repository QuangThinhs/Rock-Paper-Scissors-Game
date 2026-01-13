import hashlib

def hash_password(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

def login(db, username, password):
    conn = db.connect()
    cur = conn.cursor(dictionary=True)
    cur.execute(
        "SELECT * FROM users WHERE username=%s AND password_hash=%s",
        (username, hash_password(password))
    )
    user = cur.fetchone()
    conn.close()
    return user
