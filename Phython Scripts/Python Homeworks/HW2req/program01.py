digits = [3,3]
bases = [5,6]


def decode_digits(digits: list[int], bases:list[int])->int:
    n=0
    Decoded_Digits=0
    for digit, base in zip(digits, bases):
        Decoded_Digits= (digit*base**n)+Decoded_Digits
        n=n+1
    return Decoded_Digits
    
def generate_digits(bases : list[int] ) -> list[list[int]]:
    def generate_combinations(combination, base):
        if base == len(bases):
            Generated_Combinations.append(combination[:])
            return
        current_base = bases[base]
        for digit in range(current_base):
            combination.append(digit)
            generate_combinations(combination, base+ 1)
            combination.pop()

    Generated_Combinations = []
    generate_combinations([], 0)
    return Generated_Combinations  

def find_doubles(bases : list[int]) -> set[int]:
   combinations = generate_digits(bases)
   Seen_numbers = set()
   Found_Doubles = set()
   for combination in combinations:
       integer = decode_digits(combination, bases)
       if integer in Seen_numbers:
           Found_Doubles.add(integer)
       Seen_numbers.add(integer)
   return Found_Doubles

print(decode_digits(digits, bases))
print(generate_digits(bases))
print(find_doubles(bases))