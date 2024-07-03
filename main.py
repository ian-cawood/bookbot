def main():
  file_path = "books/frankenstein.txt"
  text = open_file(file_path)
  num_words = count_words(text)
  char_count = char_characters(text)
  char_count = convert_to_list(char_count)
  char_count.sort(key=sort_on, reverse=True)

  print_report(num_words, char_count)

def open_file(file_path):
  with open(file_path) as f:
    return f.read()
  
def count_words(text):
  words = text.split()
  return len(words)

def char_characters(text):
  text = text.lower()
  char_count = {}
  for char in text:
    if char.isalpha():
      if char in char_count:
        char_count[char] += 1
      else:
        char_count[char] = 1

  return char_count

def convert_to_list(dict):
    char_list = []
    for key in dict:
        char_list.append({"char": key, "count": dict[key]})
    return char_list

def sort_on(dict):
    return dict["count"]

def print_report(num_words, char_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")

    for item in char_count:
        print(f"The '{item['char']}' character was found {item['count']} times")

    print("--- End report ---")

main()