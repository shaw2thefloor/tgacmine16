from tkinter import *
from wordcloud import Wordcloud

root = Tk()
frame = Frame(root)
frame.pack()

root.title("Paper refine")

titles_list = ["Battling Zika in Brazil",
               "A crucial time for public health preparedness: Zika virus and the 2016 Olympics, Umrah, and Hajj",
               "Offline: Brazil-the unexpected opportunity that Zika presents",
               "Zika Virus on the Move.",
               "Zika, and rapid diagnostic tests for malaria",
               "Research bodies vow to share data on Zika",
               "Scientists probe Zika link to birth defects",
               "Proving Zika link to birth defects poses huge challenge.",
               "Severe eye damage in infants with microcephaly is presumed to be due to Zika virus",
               "Healthcare staff encouraged to warn patients of the risks of the Zika virus"]

def screen(titles_list):
    global buttons
    buttons = []

#    titles_list = ["Battling Zika in Brazil",
#                   "A crucial time for public health preparedness: Zika virus and the 2016 Olympics, Umrah, and Hajj",
#                   "Offline: Brazil-the unexpected opportunity that Zika presents",
#                   "Zika Virus on the Move.",
#                   "Zika, and rapid diagnostic tests for malaria",
#                   "Research bodies vow to share data on Zika",
#                   "Scientists probe Zika link to birth defects",
#                   "Proving Zika link to birth defects poses huge challenge.",
#                   "Severe eye damage in infants with microcephaly is presumed to be due to Zika virus",
#                   "Healthcare staff encouraged to warn patients of the risks of the Zika virus"]

    for x in titles_list[:5]:
        var = IntVar()
        # Create the checkbutton
        button = Checkbutton(frame, text = str(x), variable=var)
        button.pack(anchor=W)            
        # Add a tuple of (button, var) to the list buttons
        buttons.append((button, var))

def print_results():
    new_list = []
    for button, var in buttons:
        # If var.get() is True, the checkbutton was clicked
        if var.get():
            print(button["text"])
            new_list.append(button["text"])
    screen(new_list)
            

screen(titles_list)

def create_wordle(text):
    wordcloud = WordCloud(max_font_size=80, relative_scaling=1).generate(text)
    fig = plt.figure(figsize=(12,12))
    plt.imshow(wordcloud)
    plt.axis("off")
    return fig


results = Button(frame, text = "Refine results", command = print_results)
results.pack()
root.mainloop()
