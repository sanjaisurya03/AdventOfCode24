
import time
with open("input.txt", "r") as file:
    lines = file.readlines()

def secretStep(secret):
    # Multiply by 64
    temp = secret * 64
    # Mix result into secret num
    secret = temp ^ secret
    # Prune secret number (modulus 16777216)
    secret = secret % 16777216 # 4096 * 4096
    # Calculate result of secret / 32, round down to nearest int, 
    temp = secret // 32 # floor division
    # mix with secret (mix is bitwise xor)
    secret = temp ^ secret
    # prune secret (modulus 16777216)
    secret = secret % 16777216
    # multiply by 2048, mix and prune
    temp = secret * 2048
    secret = temp ^ secret
    secret = secret % 16777216
    return secret

def shiftStep(secret): # Same speed sadly though
    # Multiply by 64 using bitwise left shift
    secret = (secret << 6) ^ secret
    # Prune secret (modulus 16777216 using bitwise AND)
    secret &= 0xFFFFFF # hex represntation of 16777216 since its 2^24
    # Divide by 32 and round down using bitwise right shift
    secret = (secret >> 5) ^ secret
    # Prune secret again
    secret &= 0xFFFFFF
    # Multiply by 2048 using left shift, mix and prune
    secret = (secret << 11) ^ secret
    secret &= 0xFFFFFF
    return secret

# Timers for secretStep
start_secret = time.time()
totalSecret = 0
for line in lines:
    secret = int(line)
    for _ in range(2000):
        secret = secretStep(secret)
    totalSecret += secret
end_secret = time.time()

# Timers for shiftStep
start_shift = time.time()
totalShift = 0
for line in lines:
    shift = int(line)
    for _ in range(2000):
        shift = shiftStep(shift)
    totalShift += shift
end_shift = time.time()

# Results
print("Total Secret:", totalSecret)
print("Total Shift:", totalShift)
print(f"Time for secretStep: {end_secret - start_secret:.6f} seconds")
print(f"Time for shiftStep: {end_shift - start_shift:.6f} seconds")

# n = number of lines in the input

# Time Complexity:
# Reading Input: O(n)
# Outer Loop: O(n)
# Inner Loop: O(2000 * n) = O(n) (2000 is constant)
# Total: O(n)

# Space Complexity:
# Input Storage: O(n)
# Variables: O(1)
# Total: O(n)

with open("input.txt", "r") as file:
    lines = file.readlines()

def secretStep(secret):
    # Cleaned up
    secret = (secret * 64 ^ secret) % 16777216
    secret = (secret // 32 ^ secret) % 16777216
    secret = (secret * 2048 ^ secret) % 16777216
    return secret

# Custom implementation of max function
def findMax(sequence_totals):
    max_key = None
    max_value = float('-inf')  # Start with the smallest possible value

    for key, value in sequence_totals.items():
        if value > max_value:
            max_value = value
            max_key = key

    return max_key

def findMaxBananas(lines):
    sequence_totals = {}

    for line in lines:
        secret_number = int(line)
        price_list = [secret_number % 10]  # Store last digit of secret numbers

        # Generate 2000 price steps
        for _ in range(2000):
            secret_number = secretStep(secret_number)
            price_list.append(secret_number % 10)
        
        tracked_sequences = set()

        # Examine all sequences of 4 consecutive price changes
        for index in range(len(price_list) - 4):
            p1, p2, p3, p4, p5 = price_list[index:index + 5]  # Extract 5 consecutive prices
            price_change = (p2 - p1, p3 - p2, p4 - p3, p5 - p4)  # Calculate changes
            
            if price_change in tracked_sequences:  # Skip since we wont choose same again
                continue
            tracked_sequences.add(price_change)

            if price_change not in sequence_totals:
                sequence_totals[price_change] = 0
            sequence_totals[price_change] += p5  # Add the price to the total

    # Find highest total
    # best_sequence = max(sequence_totals, key=sequence_totals.get)
    best_sequence = findMax(sequence_totals)
    max_bananas = sequence_totals[best_sequence]

    return best_sequence, max_bananas

best_sequence, max_bananas = findMaxBananas(lines)

print("Best sequence: ", best_sequence)
print("Max bananas: ", max_bananas)


# n = number of lines in the input

# Time Complexity:
# Reading Input: O(n)
# Outer Loop over Lines: O(n)
# Price Generation (2000 iterations): O(2000 * n) = O(n) (2000 is constant)
# Inner Loop for Sequences: O(1996 * n) = O(n) (1996 = 2000 - 4 is constant)
# Sequence Operations (Set and Dict): O(1) per operation
# Total: O(n)

# Space Complexity:
# Input Storage: O(n)
# Price List: O(2000) = O(1) (constant space per buyer)
# Tracked Sequences: O(1) (bounded by unique 4-change sequences)
# Sequence Totals Dictionary: O(1) (bounded by unique sequences)
# Total: O(n)
