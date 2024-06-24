# prompt the user to give words
adjective1 = input("enter an  adjective: ")
adjective2 = input("enter another adjective: ")
adjective3 = input("enter another adjective: ")

#build a story template
story = f"On a beautiful {adjective1} day, I went to the zoo. I saw a funny {adjective2} monkey swinging from the trees. Then, I spotted a majestic {adjective3} lion lounging in the sun. What a wild and {adjective3} experience!"

# ascertain if the user used the same adjective twice
if adjective1 == adjective2:
      story += "she was surprised she felt that way"
else:
      story += "the teargas was worth it"

  #display story
print(story)          