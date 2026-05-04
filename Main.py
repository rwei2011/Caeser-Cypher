# w3 for these functions(list) (index) (join)
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q" "r" "s", "t", "u", "v", "w", "x", "y", "z"]
def cipher(values):
  word = input("What word do you want to cipher?\n")
  try:
    shifts = int(input("How many values do you want to shift?\n"))
  except ValueError: #if its not a number
    print("That's not a number")
  newword = []
  word1 = word.lower()
  wordlist = list(word1) #makes it a list
  for n1 in wordlist:
    if n1.isalpha == False:
      break
    #print(values.index(n1)) #helped me reason the rest of the loop and see whaat it was printing out
    try:
      newword.insert(-1, values[(values.index(n1)) + (shifts % 26)]) #inserts the letter in the list + however much it was shifted (index was where it is in the alphabet list)
    except:
      return "Error"
  end = "".join(newword) #makes a string
  return end
def uncipher(values):
  word = input("What is your ciphered word?\n")
  shifts = int(input("How much was it shifted"))
  newword = []
  word1 = word.lower()
  wordlist = list(word1)
  for n1 in wordlist:
    #print(n1) #check if it is going to this loop
    try: #tries this and if it is wrong value say error
      newword.insert(-1, values[(values.index(n1)) - (shifts % 26)]) #inserts the letter in the list + however much it was shifted (index was where it is in the alphabet list)
    except:
      return "Error"
  end = "".join(newword) #string
  return end #list
choice = int(input("Do you want to cipher(1) or uncipher(2)?\n")) #askes user what they want to do
if choice == 1:
  print(cipher(alphabet))
else:
  print(uncipher(alphabet))
