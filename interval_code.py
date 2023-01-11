import random
import itertools
import io
import os


# Create a dictionary mapping numbers to words
intervals = {
    1: "m2",
    2: "M2",
    3: "m3",
    4: "M3",
    5: "P4",
    6: "Tt"
}

# Create a dictionary to store the count of each note
pitch_counts = {
    "C": 0,
    "C#": 0,
    "D": 0,
    "D#": 0,
    "E": 0,
    "F": 0,
    "F#": 0,
    "G": 0,
    "G#": 0,
    "A": 0,
    "A#": 0,
    "B": 0
}

# Create an empty list to store the selected words
selected_intervals = []
####################################################################################################################################

#NAME SECTION
let_1 = ['Inkwell', 'Ion', 'Trinity', 'Ceti', 'Echo', 'Kilo', 'Lightfoot', 'Nightwind', 'Panic', 'Sierra', 'Whiskey', 'X-ray', 'Zebra', 'Fallen', 'Hunter', 'Iceberg', 'Advantage', 'Blockade', 'Ricochet', 'Shakedown', 'Thunder', 'Switchblade', 'Cutlass', 'Sabre', 'Marduk', 'Enkidu', 'Omega']

let_12 = ['part_I', 'part_II', 'part_III', 'part_IV', 'part_V', 'part_VI', 'part_VII', 'part_VIII', 'part_IX', 'part_X']

#['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon', 'Zeta', 'Theta', 'Omicron', 'Ion', 'Iota', 'Kappa', 'Lambda', 'Sigma', 'Omega']

t_4 = ['Ridge', 'Canyon', 'Mountain', 'Creek', 'Hollow', 'Point', 'Bluff', 'Path', 'Tower', 'Cove', 'Plains', 'Valley', 'Bay', 'Channel', 'Gulf', 'Reef', 'Ravine', 'Deep', 'Quadrant', 'Triangle', 'Highway', 'Parkway']

random_word = (random.choice(let_1))

zrandom_word = (random.choice(let_12))

rise_word = (random.choice(t_4)) 

def namen(random_word, zrandom_word, rise_word):
    return random_word + '_' + zrandom_word + '_' + rise_word


dave = namen(random_word, rise_word, zrandom_word)

# Generate a random 4 digit number
unique_number = str(random.randint(1000, 9999))

# Create the file name 
filename = dave + '.txt'

# Create the file name with the unique number
filenamex = 'output_raw' + unique_number + '.txt'

#########################################################################################################################
x = 0 ##AKA number of intervals
y = []  ###AKA sequence of intervals

print("Intervals must be entered as number of half steps \n1=minor 2nd, 2=Major 2nd, 3=minor 3rd, \n4=Major 3rd, 5=Perfect 4th, 6=Tri-tone")

def get_list_of_intervals():
    user_input = input("Enter a sequence of intervals separated by a comma: \nonly valid intervals: 1 - 6\n")
    interval_list = [int(x) for x in user_input.split(',')]
    return interval_list, len(interval_list)

# Keep asking for input until the user enters a valid list of intervals
while True:
    interval_list, num_intervals = get_list_of_intervals()
    x = num_intervals
    y = interval_list
    # Check if all numbers are between 1 and 6
    if all(1 <= number <= 6 for number in interval_list):
        break
    print("Error: all intervals must be between 1 and 6")




#print(y)
#print(x)

#########################################################################################################################
#########################################################################################################################


numbers_str = y

#print(numbers_str)

# Iterate through the list of numbers
for number_str in numbers_str:
  # Convert the number string to an integer
  number = int(number_str)
  
  # If the number is in the dictionary, add the corresponding word to the list
  if number in intervals:
    selected_intervals.append(intervals[number])
  # Otherwise, print an error message
  else:
    print(f"{number} is not a valid interval")

# Print the selected intervals
print("Selected intervals:")
print(selected_intervals)
##print(x)

totally = (2 ** x) * x + 1

#print(totally) 

########################################################################################################
# 3 DECK SHUFFLE
def special(x):
    #generate list of all possible permutations of 0 and 1 with x length
    permutations = list(itertools.product([0,1], repeat=x))
    random.shuffle(permutations)
        #create list to hold permutations
    perm_list = []
        #print each permutation in the list and append to perm_list
    for perm in permutations:
            #print(perm)
        perm_list.append(perm)
        #return perm_list and choice so it can be used in a later function
    return perm_list

special(x)
one_j = special(x)

special(x)
two_j = special(x)

special(x)
three_j = special(x)



def mergers():
    lunge = []
    lunge = one_j + two_j + three_j 
    #print(lunge)
    random.shuffle(lunge)
    hbomb = []
    for v in lunge:
        hbomb.append(v)
    return hbomb, len(hbomb)


r, t = mergers()
            
mergers()

def create_short_list(r):
    half_length = len(r) // 3 
    first_half_list = r[:half_length]
    return(first_half_list)


jdog = create_short_list(r)
##########################################################################################################
##########################################################################################################
# 12 DECK SHUFFLE

def miller(x):
    #generate list of all possible permutations of 0 and 1 with x length
    permutations = list(itertools.product([0,1], repeat=x))
    random.shuffle(permutations)
        #create list to hold permutations
    perm_list = []
        #print each permutation in the list and append to perm_list
    for perm in permutations:
            #print(perm)
        perm_list.append(perm)
        #return perm_list and choice so it can be used in a later function
    return perm_list

miller(x)
one_k = miller(x)

miller(x)
two_k = miller(x)

miller(x)
three_k = miller(x)

miller(x)
four_k = miller(x)

miller(x)
five_k = miller(x)

miller(x)
six_k = miller(x)

miller(x)
seven_k = miller(x)

miller(x)
eight_k = miller(x)

miller(x)
a_k = miller(x)

miller(x)
b_k = miller(x)

miller(x)
c_k = miller(x)

miller(x)
d_k = miller(x)

def mergers_big():
    lunges = []
    lunges = one_k + two_k + three_k + four_k + five_k + six_k + seven_k + eight_k + a_k + b_k + c_k + d_k
    #print(lunge)
    random.shuffle(lunges)
    hbomba = []
    for vvv in lunges:
        hbomba.append(vvv)
    return hbomba, len(hbomba)


robo, t1000 = mergers_big()
            
mergers_big()

def create_part_list(robo):
    cut_length = len(robo) // 12
    first_cut_list = robo[:cut_length]
    return(first_cut_list)


kdog = create_part_list(robo)

##########################################################################################################
def permutation_generator(x):
    #generate list of all possible permutations of 0 and 1 with x length
    permutations = list(itertools.product([0,1], repeat=x))


    print("\nChoose a method of permutation:\n\nORDERED - using all combinations of up/down once in order \nREGULAR RANDOM - using all combinations of up/down once in random order \nMORE RANDOM - a 3 set shuffle returning a 1 set sized portion of random combinations w/ possible repeats\nSUPER RANDOM - a 12 set shuffle, like the previous but even more random \n\nEnter: [ord], [ran], [more], or [super] \n")
    next = input("< ")


    choice = next



    if "ran" in next:
        #shuffle list to randomize order
        random.shuffle(permutations)
        #create list to hold permutations
        perm_list = []
        #print each permutation in the list and append to perm_list
        for perm in permutations:
            #print(perm)
            perm_list.append(perm)
        #return perm_list and choice so it can be used in a later function
        return perm_list, choice

    elif "ord" in next:
        #create list to hold permutations
        perm_list = []
        #print each permutation in the list and append to perm_list
        for perm in permutations:
            #print(perm)
            perm_list.append(perm)
        #return perm_list and choice so it can be used in a later function
        return perm_list, choice

    elif "more" in next:
        choice = ("more")
        return jdog, choice    

    elif "super" in next:
        choice = ("super")
        return kdog, choice   

    else:
        print("\nerror\n")
        exit(0)

#store output in variables perm_output and choice
perm_output, choice = permutation_generator(x)

# Convert perm_output to a string
perm_output_str = '\n'.join([' '.join(map(str, item)) for item in perm_output])

# Use the choice variable in a later function
def later_function(perm_output_str, choice):

    if choice == 'ord':
        decision = ("a systematically ordered set of")
        return decision
    elif choice == 'ran': 
        # do something with perm_output_str
        decision = ("a randomly ordered set of")
        return decision
    elif choice == 'more':
        decision = ("a random selection of")
        return decision 
    elif choice == 'super':
        decision = ("a highly random selection of")
        return decision
    else:
        exit(0)

        




decision = later_function(perm_output_str, choice)

def user_pr_option():
    print("Would you like the binary code sequence pattern \nprinted on the generated text file? ")
    dt = input("Enter [y or n] < ")
    return dt

dtf = user_pr_option()
#print(dtf)
    


def blip_blop(dtf):
    if dtf == 'y':
        with open(filename, 'a') as file:
            file.write(explain_str)
            file.write(perm_output_str)
            #print('yes sir')
    elif dtf == 'n': 
        with open(filename, 'a') as file:
            file.write('\n')
            #print("""no ma'am""")
    else:
        exit(0)




ultima_str = "\nPossible pitch outcomes using [{}] interval permutations for the [{}] entered intervals: \n\n{}\n\n".format(decision, x, selected_intervals)

explain_str = "\n--------------------------------\nbinary sequence\n[0=up, 1=down]\n\n"

credit = "\n\n--------------------------------\nfor more info visit:\nhttps://www.gregpfeiffer.com\n\n"



pitches_list = []  

def generate_pitches(y, permutation, x, initial_pitch):
    pitches = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    for i in range(len(y)):
        interval = y[i]
        direction = permutation[i]
        if direction == 0:
            initial_pitch_index = pitches.index(initial_pitch)
            new_pitch_index = (initial_pitch_index + interval) % len(pitches)
            new_pitch = pitches[new_pitch_index]
            pitches_list.append(new_pitch)  
            initial_pitch = new_pitch
        else:
            initial_pitch_index = pitches.index(initial_pitch)
            new_pitch_index = (initial_pitch_index - interval) % len(pitches)
            new_pitch = pitches[new_pitch_index]
            pitches_list.append(new_pitch)  
            initial_pitch = new_pitch




def where_start():
    print("Enter the starting pitch: \nenter choice as: C, C#, D, D#, E, F, F#, G, G#, A, A#, B\n ")
    start_pitch = input("Enter < ")
    return start_pitch

    

while True:
    start_pitch = where_start()
    initial_pitch = start_pitch

    if start_pitch in ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'):
        break
    else:
        print("Only sharps or none. Only letters A thru G accepted.")

with open(filename, 'a') as file:
    file.write(ultima_str)
    file.write(initial_pitch + ' ')

with open(filenamex, 'a') as file:
    file.write(initial_pitch + ' ')
    



for permutation in perm_output:
    pitches_list = []  # reset the pitches_list for each permutation
    generate_pitches(y, permutation, x, initial_pitch)
    #print(pitches_list)
    initial_pitch = pitches_list[-1]  # update the starting pitch for the next line



    
    with open(filename, 'a') as file:
  # Iterate through the pitches list and write each item to the file
        counter = 1
        for pitch in pitches_list:
            file.write(pitch)
            
            if counter % x == 0:
                file.write('\n')
                
            else:
                file.write(' ')
                
            counter += 1
            #



for permutation in perm_output:
    pitches_list = []  # reset the pitches_list for each permutation
    generate_pitches(y, permutation, x, initial_pitch)
    #print(pitches_list)
    initial_pitch = pitches_list[-1]  # update the starting pitch for the next line



    
    with open(filenamex, 'a') as file:
  # Iterate through the pitches list and write each item to the file
        counter = 1
        for pitch in pitches_list:
            file.write(pitch)
            
            if counter % x == 0:
                file.write('\n')
                
            else:
                file.write(' ')
                
            counter += 1


            
print("Output written to file", filename)



with open(filenamex, 'r') as f:
    pit_list = f.read()
    junk = pit_list.split()


for pitch in junk:
    if pitch in pitch_counts:
      pitch_counts[pitch] += 1


with open(filename, 'a') as file:
    file.write("--------------------------------\n")
    file.write("\nTotal # of piches: {}\n".format(totally))
    file.write("\nPitch tally:\n\n")





def write_to_file(filename, pitch_counts):
    with open(filename, 'a') as file:
        for key, value in pitch_counts.items():
            file.write("{}: {}\n".format(key, value))


write_to_file(filename, pitch_counts)

with open(filename, 'a') as file:
    file.write("\n")

    
blip_blop(dtf)


with open(filename, 'a') as file:
    file.write(credit)
    file.write(filename) 
    file.write("\ngenerated with THE INTERVAL CODE")
    file.write("\n\ncopyright G.C.Pfeiffer ©2022")



os.remove(filenamex)




