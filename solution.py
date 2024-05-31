def create_staircase(nums):
    step = 1
    subsets = []
    while len(nums) != 0:
        if len(nums) >= step:
            subsets.append(nums[0:step])
            nums = nums[step:]
            step += 1
        else:
            return False
    return subsets

def create_pattern(subsets):
    pattern = []
    for subset in subsets:
        element = subset[len(subset)-1]
        pattern.append(element)
    return pattern

def create_sentence(input, pattern): 
    pattern_done = [False] * len(pattern)
    count = 0 
    for word in input: 
        if(count==len(pattern)):
            break
        split = word.strip().split(' ')
        index = int(split[0])
        word_to_use = split[1]

        for i in range(0, len(pattern)): 
            if(pattern_done[i]==False):
                if(pattern[i]==index): 
                    pattern_done[i] = word_to_use
                    count += 1 
                    break 

    result = ' '.join(pattern_done)
    return result



    


def load_input(file_name):

    input = []
    file = open(file_name, "r")
    for word in file:
        input.append(word)
    return input

def decode(message_file): 
    input = load_input(message_file)

    nums = list(range(1, len(input)+1))
    subsets = create_staircase(nums)
    if(subsets!=False):

        pattern = create_pattern(subsets)
        result = create_sentence(input, pattern)
        return result
    else: 
        return False

sentense = decode("TestCases/coding_qual_input.txt"); 
print(sentense)
