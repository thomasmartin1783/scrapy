from operator import mod
import re

myvar = 'sky    cloud..  blue red'

# print(re.split('\d+', myvar))
print(re.split('\s+', myvar))


# unmodified = "egula ektu besi somoy sapekko,, tai try korina.. amr eto dorjo nai… Kali Nethunter or AircrackNG diye hack kora jai, YouTube and google korle jante parven…."
unmodified = "Youtube 'Video... Dile.. Valo Hoito…Jara. Bujtece.Nah. Tara Video Dekhe Bujte Parto…!"
# modified = re.split('\s+|\…|\.\.\.|\.\.|\.+', unmodified)
modified = re.split('\s+|\…|\.+', unmodified)
print(modified)
