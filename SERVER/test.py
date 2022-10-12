temp = "("
item = [("username", "char(20)"), ("msgcontent", "char(20)"), ("msgtime", "char(20)"), ("msgtype", "char(20)")]
for i in item:
    temp += " ".join(i)
    if item.index(i) != len(item) - 1:
        temp += ", "
    else:
        temp += ")"

print(temp)