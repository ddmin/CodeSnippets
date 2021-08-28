import re; look_and_say = lambda n: ''.join([str(len(match.group(0))) + match.group(0)[0] for match in re.finditer(re.compile(r'(\d)\1*'), n)])

i = '1'
for n in range(15):
    print(i)
    print()
    i = look_and_say(i)
