from slippi import Game
from slippi.id import InGameCharacter
from slippi.id import ActionState

game = Game('MyReplays/Test1.slp')

port_number = 0;
for i in range (0,4): #this loop gets the port number of the Falco player
	if game.frames[0].ports[1].leader.post.character != InGameCharacter.FALCO:
		port_number = i
		break


back_air_count = 0
attacking = False

for num, frame in enumerate(game.frames, start=1):
	data = frame.ports[port_number].leader 
	post = data.post
	if post.state == ActionState.ATTACK_AIR_B and not attacking:
		attacking = True
		back_air_count+= 1
		print("Used Back Air On Frame {}".format(num))
	elif post.state == ActionState.ATTACK_AIR_B and attacking:
		pass
	else:
		attacking = False
	if (num == 1000):
		print(data)
		

test = True
if test:
	print(back_air_count)