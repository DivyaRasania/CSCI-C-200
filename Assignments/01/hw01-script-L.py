famous_quote = input("Give me a famous quote from a movie: ")
# print(f"Screaming: {famous_quote.upper()}, whispering: {famous_quote.lower()}")

original_word = input("Choose a word you want to replace: ")
replace_word = input(f"Give me a word you want to replace '{original_word}' with: ")

new_quote = famous_quote.replace(original_word, replace_word)

print(f"Final quote: {new_quote}")
