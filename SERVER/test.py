
field = ["username", "userid"]
values = ["shem", "0"]

sql = "INSERT INTO userinfo (" + ", ".join(field) + ") VALUES (" + ", ".join(values) + ")"

print(sql)