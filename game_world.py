# layer 0: Background Objects
# layer 1: character
# layer 2: jem
# layer 3: monster
# layer 4: skill
# layer 5: damage
# layer 10: UI objects
objects = [[],[],[],[],[],[],[],[],[],[],[]]
def add_object(o, layer):
    objects[layer].append(o)

def add_objects(l, layer):
    objects[layer] += l

def remove_object(o):
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o
            break

def clear():    
    for o in all_objects():
        del o

def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o