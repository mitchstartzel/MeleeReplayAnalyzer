from slippi import Game
from slippi.id import InGameCharacter
from slippi.id import ActionState
print("test")
game = Game('MyReplays/Mango1.slp')
print("test")
port_number = 2;
#for i in range (1,3): #this loop gets the port number of the Falco player
#	if game.frames[0].ports[i] != None and game.frames[0].ports[i].leader.post.character == InGameCharacter.FALCO:
#		port_number = i
#		break

print(port_number)
back_air_count = 0
attacking = False

for num, frame in enumerate(game.frames, start=1):
	data = frame.ports[port_number].leader 
	post = data.post
	if post.state == ActionState.ATTACK_AIR_LW and not attacking:
		attacking = True
		back_air_count+= 1
	elif post.state == ActionState.ATTACK_AIR_LW and attacking:
		pass
	else:
		attacking = False
	if (num < 300):
		print("Frame {}".format(num))
		print(post.state)
	
			

test = True
if test:
	print("Number of Back Airs: {}".format(back_air_count))





#NOTES:
#laser sequence: wait_4, wait_item