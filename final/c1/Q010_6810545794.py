# Name: Pasin Makcharoen # Student ID: 6810545794

vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    in_ = input("Enter a sentence (or 'exit' to quit): ").lower()
    
    if in_ == "exit":
        print("Goodbye!")
        break

    vowel_cou = 0
    letters = [i for i in in_ if i != " "]
    
    for this_ in letters:
        if this_ in vowel:
            vowel_cou += 1
    
    print(f"Vowels: {vowel_cou}")