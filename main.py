def sentence_code(sentence):
  words = sentence.split()
  shift_sentence = ""
  for j in range(len(words)):
    for i in words[j]:
      res = ord(i)
      res += (j+1)
      shift_sentence += chr(res)
    shift_sentence += " "
  return shift_sentence

def sentence_decode(sentence):
  words = sentence.split()
  unshift_sentence = ""
  for j in range(len(words)):
    for i in words[j]:
      res = ord(i)
      res -= (j+1)
      unshift_sentence += chr(res)
    unshift_sentence += " "
  return unshift_sentence

sentence = input("Enter a sentence: ")
choice = input("Would you like to \"code\" the sentence or \"decode\" the sentence(code/decode): ")
if choice == "code": 
  print(f"Your input was \"{sentence}\" and your coded sentence is \"{sentence_code(sentence)}\"")
elif choice == "decode":
  print(f"Your input was \"{sentence}\" and your decoded sentence is \"{sentence_decode(sentence)}\".")
else:
  print("Please enter either code or decode.")