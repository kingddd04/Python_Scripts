s =  "davidedistefano04@gmail.com"

character_position = s.find("@")

print("name = " + s[0:character_position])
print("Domain = " + s[character_position:len(s)])
