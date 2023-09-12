


#O(N)
def solution(string):
    return string[::-1]    #O(N) runs through length of the string


#O(N)
def positive_sum(arr):
    c = 0                  #O(1)
    for a in arr:          #O(N)
        if a > 0:          #O(1)
            c = c + a      #O(1)
    return c              


#O(N)
def friend(listofnames):
     newlist = []                                     #O(1)
     for name in listofnames:                         #O(N)
         if len(name) == 4 and not name.isdigit():    #O(1)
             newlist.append(name)                     #O(1)
     return newlist                                   #O(1)
print(friend(["Ryan", "Kieran", "1234", "Mark"]))


#O(logn)
def create_show(fireworks, show_time):
    fireworks.sort()                                  #O(logn) sorting through a list 
    show = []                                         #O(1)
    remaining_time = show_time                        #O(1)
    while remaining_time > 0 and fireworks:           #O(N)
           # Select a random firework
           firework = random.choice(fireworks)        #O(1)
           if firework <= remaining_time:             #O(1)
               # Add the firework to the show
               show.append(firework)                  #O(1)
               remaining_time -= firework             #O(1)
           else:
              # This firework is too long, 
              # remove it from consideration
              fireworks.remove(firework)              #O(1)
    return show                                      