s1 = "123,456,788"
s2 = "1"

res = int(s1.replace(",","")) + int(s2)
output = "{:,}".format(res)
print(output)
