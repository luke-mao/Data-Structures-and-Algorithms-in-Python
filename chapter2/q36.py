# sketch a simple eco-system including bear and fish
import random

# list boundary
LIST_LENGTH = 1000
LIST_LOWER_BOUNDARY = 0
LIST_HIGHER_BOUNDARY = LIST_LENGTH - 1

# initial percentage of each animal
INITIAL_ANIMAL_PERCENT = 0.3
INITIAL_NONE_PERCENT = 1 - INITIAL_ANIMAL_PERCENT

INITIAL_FISH_TO_BEAR_RATIO = 2.5        
INITIAL_FISH_PERCENT = INITIAL_ANIMAL_PERCENT * INITIAL_FISH_TO_BEAR_RATIO / (INITIAL_FISH_TO_BEAR_RATIO + 1)
INITIAL_BEAR_PERCENT = 1 - INITIAL_NONE_PERCENT - INITIAL_FISH_PERCENT

# strength
FISH_STRENGTH = 20
BEAR_STRENGTH = 100

class Animal:
    def __init__(self, location):
        self._location = location
        self._strength = 0          # default strength = 0, modify later
    
    def move(self):
        # return the location index

        if self._location == LIST_HIGHER_BOUNDARY:
            rand = random.randint(0, 1)
            if rand == 1: self._location -= 1   # 50% chance move
        
        elif self._location == LIST_LOWER_BOUNDARY:
            rand = random.randint(0, 1)
            if rand == 1: self._location += 1   # 50% chance move
        
        else:   # 3 choice to move
            rand = random.randint(0, 2)
            if rand == 2: self._location += 1   # 33%
            elif rand == 1: self._location -= 1 # 33%
        
        return self._location
        
        
class Bear(Animal):
    def __init__(self, location):
        super().__init__(location)
        self._strength = BEAR_STRENGTH


class Fish(Animal):
    def __init__(self, location):
        super().__init__(location)
        self._strength = FISH_STRENGTH


# initial generation of the list
def generate():
    """
    initial generation of the list, return the list "model".
    fill the list with specified % of animals and None
    """

    model = [None] * LIST_LENGTH       # this is the list, each element is also a list
    
    # fill in animals, according to the percentage
    index_list = [i for i in range(LIST_LENGTH)]
    random.shuffle(index_list)                                                  # shuffle the list in place
    bear_position = index_list[:int(LIST_LENGTH * INITIAL_BEAR_PERCENT)]
    fish_position = index_list[int(LIST_LENGTH * INITIAL_BEAR_PERCENT) : int(LIST_LENGTH * (INITIAL_BEAR_PERCENT + INITIAL_FISH_PERCENT))]

    for i in bear_position: model[i] = [Bear(i)]
    for i in fish_position: model[i] = [Fish(i)]

    return model


def find_none_position_in_list(model, length):
    """find the position of none in a list, return a shuffed index list"""
    index_list = []
    for i in range(length):
        if model[i] is None: index_list.append(i)
    
    # shuffle
    random.shuffle(index_list)      # shuffle the list in place!!! in place!!!
    return index_list


def test_find_none_position_in_list():
    list1 = [None, None, Bear(3), Fish(4), None, None]
    list2 = [[Bear(0), Fish(0)], None, None, None]

    print(find_none_position_in_list(list1, len(list1)))
    print(find_none_position_in_list(list2, len(list2)))


def find_survivor(animal_list, index):
    """
    the input definitely contains more than 1 animal.
    so only need to count the number of bears
    determine the survivor, return a new list.
    return flag = True if need give birth to a new animal
    """

    animal_number = len(animal_list)    # animal_number >= 2
    bear_num = 0

    for i in range(len(animal_list)):
        if isinstance(animal_list[i], Bear): bear_num += 1
    
    if bear_num == 0 or bear_num == animal_number:  # if all bears or all fish
        return animal_list, True
    else:                                           # some bears and some fish
        if bear_num == 1:
            return [Bear(index)], False             # consider only 1 bear
        else:
            return [Bear(index)] * bear_num, True   # consider multiple bears 


def test_find_survivor():
    list1 = [Bear(3), Bear(3), Fish(3), Fish(3), Fish(3)]
    list2 = [Fish(2), Fish(2), Fish(2)]
    list3 = [Bear(5), Bear(5), Fish(5)]

    r1, f1 = find_survivor(list1, 3)
    r2, f2 = find_survivor(list2, 2)
    r3, f3 = find_survivor(list3, 5)
    print("return = {}, flag = {}".format(r1, f1))
    print("return = {}, flag = {}".format(r2, f2))
    print("return = {}, flag = {}".format(r3, f3))


def simulate(model):
    """
    input the last model, then simulate and return the new model.
    simulate for one cycle only.
    first move each animal,
    then, for multiple animals on the same position, determine the survivor or give new birth.
    
    the rule for multiple animals on the same position:
        if same animals, then give birth to the identical animal on a None position
        if different animals, then the stronger survive
    
    variables:
        model: input
        model2: record the model after move
        model3: the resulting model after survivor test
    """
    
    # first move everything
    # in order to avoid issue with list pop and insert, put everything on a new model
    model2 = [None] * LIST_LENGTH

    for i in range(LIST_LENGTH):
        current = model[i]
        if current is None:
            continue
        else:
            for j in range(len(current)):
                new_position = current[j].move()    # get the new position, the old position is i
                
                if model2[new_position] is None:         # insert into the new model
                    model2[new_position] = [current[j]]
                else:
                    model2[new_position].append(current[j])
    
    
    """
    now every animal move to the new position, determine the survivor.
    check every entry:
        if the entry is None, pass
        if not, count the number of bears and fish
            if both present, bear(s) wins
            if only bear or only fish present, then give birth to a new same class animal on a None position
    """


    none_position_list = find_none_position_in_list(model2, LIST_LENGTH)      # the list is shuffled already
    none_index = 0                                               # start from 0
    model3 = [None] * LIST_LENGTH                                # record the result after survivor test  

    # scan the whole model
    for i in range(LIST_LENGTH):
        if model2[i] is None:        
            continue    # pass None
        
        elif len(model2[i]) == 1:
            if model3[i] is None: model3[i] = model2[i]
            else:                 model3[i].append(model2[i])

        else:                                       # for multiple animals                        
            # first get the survivor list
            survivor_list, new_birth = find_survivor(model2[i], i)
            
            # insert into model3
            if model3[i] is None: model3[i] = survivor_list
            else:                 model3[i].extend(survivor_list)
            
            # if need to give birth to a new animal
            if new_birth:                           
                birth_num = len(survivor_list) // 2
                
                for _ in range(birth_num):

                    birth_index = none_position_list[none_index]
                    none_index += 1
                    
                    if isinstance(survivor_list[0], Fish):
                        if model3[birth_index] is None: model3[birth_index] = [Fish(birth_index)]
                        else:                           model3[birth_index].append(Fish(birth_index))
                    elif isinstance(survivor_list[0], Bear):
                        if model3[birth_index] is None: model3[birth_index] = [Bear(birth_index)]
                        else:                           model3[birth_index].append(Bear(birth_index))
                    else:
                        raise ValueError(survivor_list)

    # del model2
    return model3


def test_simulate():
    model = [None] * LIST_LENGTH
    model[3] = [Bear(3)]
    model[300] = [Fish(300)]
    print(summary(model))
    model = simulate(model)
    print(summary(model))


# at a regular time, summarise the model
def summary(model):
    """
    at a regular time, summarise the model,
    return the number of fish and bear at this iteration
    """
    fish_num = 0
    bear_num = 0

    for i in range(LIST_LENGTH):
        if model[i] is None: continue
        else:
            position = model[i]
            for j in range(len(position)):
                if isinstance(position[j], Bear): bear_num += 1
                if isinstance(position[j], Fish): fish_num += 1
    
    return "fish number = {}, bear number = {}".format(fish_num, bear_num)


def main():
    model = generate()
    print("At iteration {}: {}".format(0, summary(model)))
    
    try:
        for i in range(50):
            model = simulate(model)
            #if i % 50 == 0 or i == 500-1:
            print("At iteration {}: {}".format(i+1, summary(model)))
    except IndexError:
        print("Iteration stop due to few None entry left")


if __name__ == '__main__':
    main()

