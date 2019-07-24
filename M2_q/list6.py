'''11.	Following are the initials of players who play various games. Some of these players play more than one game.
Cricket: [ "PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"]
Football: [ "PKM", "ALN","RMZ","CS", "MCS"]
Badminton: [ "PKM", "ALN", "NV", "KM","RMV"]

Write a program to:
a.	List those players who play all three games.
b.	List those players who play exactly one game.'''




c = [ "PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"]
f = [ "PKM", "ALN","RMZ","CS", "MCS"]
b = [ "PKM", "ALN", "NV", "KM","RMV"]
players = []
players.extend(c)
players.extend(f)
players.extend(b)
u_name = []
for name in players:
    if name in u_name:
        pass
    else:
        u_name.append(name)
print(u_name)