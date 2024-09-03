import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.hats = {}
        self.contents = []
         
        for key,value in kwargs.items():
            self.hats[key] = value
            
            for _ in range(value):
                self.contents.append(key)
    def draw(self, times):
        
        contents = self.contents
        
        if times > len(contents):
            contents = copy.copy(self.contents)
            self.contents = []
            return contents
        
        drawn_items = random.sample(contents, k = times)
        for item in drawn_items:
            contents.remove(item)
                
        return drawn_items



        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
 
    match_times = 0
    
    for _ in range(num_experiments):
        
        oth_hat = copy.deepcopy(hat)
        draws = oth_hat.draw(num_balls_drawn)

        match = True
        for key,value in expected_balls.items():
            if draws.count(key) < value:
                match = False
                break
        if match == True:
            match_times += 1
            

    prob = match_times / num_experiments
    return prob



    




# hat1 = Hat(yellow=3, blue=2, green=6)
# hat2 = Hat(red=5, orange=4)
# hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
# print(hat3.draw(3))


# hat = Hat(black=6, red=4, green=3)
# probability = experiment(hat=hat,
#                   expected_balls={'red':2,'green':1},
#                   num_balls_drawn=5,
#                   num_experiments=2000)



