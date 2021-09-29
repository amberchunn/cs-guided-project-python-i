def csRemoveTheVowels(input_str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return (''.join([i for i in input_str if i not in vowels]))

print(csRemoveTheVowels('Amber'))