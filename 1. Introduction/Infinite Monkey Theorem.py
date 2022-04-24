import string
import random

final_string = "methinks it is like a weasel"

count = 0
best_score_so_far = 0.0
best_string_so_far = ""

#generates and returns a random string with the length of final string using random lower case letters and space, with repetition allowed
def generate():
    return ("".join(random.choices(string.ascii_lowercase + " ", k=len(final_string))))

#returns a score for each randomly generated string to indicate its closeness to the final_string
def score(random_string):
    no_of_matches = 0
    for i in range(len(final_string)):
        if final_string[i] == random_string[i]:
            no_of_matches += 1
        continue
    return (round((no_of_matches / len(final_string)) * 100, 2))

#calls generate() and score() until the final_string emerges randomly, also prints the best score and string so far for every 1,000,000 iterations
while best_score_so_far != 100.0:
    count += 1
    this_string = generate()
    this_score = score(this_string)
    if this_score > best_score_so_far:
        best_string_so_far = this_string
        best_score_so_far = this_score
    if count % 1000000 == 0:
        print(f"The best string so far is {best_string_so_far} with a score of {best_score_so_far}%")
print(f"The Infinite Monkey Theorem was proved after {count} iterations")