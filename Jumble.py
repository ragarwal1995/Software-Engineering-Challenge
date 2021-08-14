#!/usr/bin/env python
# coding: utf-8

# In[28]:


# Importing the words_alpha.txt file conatining list of words

a_file = open("words_alpha.txt", "r")

# Coverting .txt file to list of lists
list_of_lists = [(line.strip()).split() for line in a_file]

a_file.close()

# Coneverting lists of list to a single list i.e. flattening the list
flat_list = [item for sublist in list_of_lists for item in sublist]


print('Transformed list', flat_list) 


# In[39]:


# Importing the required libraries

from tkinter import *
from random import choice
from random import shuffle


root = Tk()
# Title
root.title('Jumble Word Game')
# Dimensions
root.geometry("700x500-10-10")


label = Label(root, text="", font=("Helvetica", 40))
label.pack(pady=20)

def Jumble():
    
    entry_answer.delete(0, END)
    answer_label.config(text ='')
    
    
    #Picking a random word from the flattened list
    global chosen_word
    chosen_word = choice(flat_list)

    
    # Breaking the chosen word picked from the flattend list 
    break_word = list(chosen_word)
    
    # Shuffling the list randomly
    shuffle(break_word)
    
    # Converting the randomly generated shuffled list to word and printing the random word
    global jumbled_word 
    jumbled_word = ''
    for letter in break_word:
        jumbled_word += letter
     # printing shuffled word to screen   
    label.config(text=jumbled_word)

        
#Creating an answer Function and comapring the user entered answer with the chosen word
def answer():
    if chosen_word == entry_answer.get():
        answer_label.config(text="Answer is correct!")
    else:
        answer_label.config(text="Answer is incorrect!")

    
        
global entry_answer        
entry_answer = Entry(root, font=("Helvetica", 24))
entry_answer.pack(pady=20)

# Button to pick different word
button_pick_word = Button(root, text="Pick Another Word", command=Jumble)
button_pick_word.pack(pady=20)


answer_button = Button(root, text="Answer", command=answer)
answer_button.pack(pady=20)


answer_label = Label(root, text='', font=("Helvetica", 18))
answer_label.pack(pady=20)


substring_label = Label(root, text='', font=("Helvetica", 18))
substring_label.pack(pady=90)

Jumble()
    
root.mainloop()  

# # Time Complexity analysis
# Big O nottaion = O(n)


# In[ ]:




