from tkinter import *
import backend

root = Tk()
root.title("Smart Search")
frame = Frame(root)
frame.pack()

paper_list = []
p_list = backend.Backend("testdata")
p_list = p_list.get_table_data()
for x in p_list:
  paper_list.append(x["title"])


paper_list2 = ["Cyclin B Translation Depends on mTOR Activity after Fertilization in Sea Urchin Embryos.",
              "Stoichiometry and Change of the mRNA Closed-Loop Factors as Translating Ribosomes Transit from Initiation to Elongation.",
              "Components of the eIF4F complex are potential therapeutic targets for malignant peripheral nerve sheath tumors and vestibular schwannomas.",
              "eIF4E-phosphorylation-mediated Sox2 upregulation promotes pancreatic tumor cell repopulation after irradiation.",
              "Dietary vitamin C deficiency depresses the growth, head kidney and spleen immunity and structural integrity by regulating NF-κB, TOR, Nrf2, apoptosis and MLCK signaling in young grass carp (Ctenopharyngodon idella).",
              "Antibiotic drug rifabutin is effective against lung cancer cells by targeting the eIF4E-β-catenin axis.",
              "4EGI-1 induces apoptosis and enhances radiotherapy sensitivity in nasopharyngeal carcinoma cells via DR5 induction on 4E-BP1 dephosphorylation.",
              "N-Hydroxyphthalimide exhibits antitumor activity by suppressing mTOR signaling pathway in BT-20 and LoVo cells.",
              "Elevated Translation Initiation Factor eIF4E is an Attractive Therapeutic Target in Multiple Myeloma.",
              "Regulation of mTORC1 by growth factors, energy status, amino acids and mechanical stimuli at a glance.",
              "Amplified in Breast Cancer Regulates Transcription and Translation in Breast Cancer Cells.",
              "[Corrigendum] Knockdown of eukaryotic translation initiation factor 4E suppresses cell growth and invasion, and induces apoptosis and cell cycle arrest in a human lung adenocarcinoma cell line.",
              "Overexpression of eIF4E in colorectal cancer patients is associated with liver metastasis."]


def test():
  print(Lb1.curselection())
  lis = []
  for x in Lb1.curselection():
      lis.append(index_title[int(x)])
  if lis == []:
      foo(["none"])
  else:
      foo(lis)


frame0 = LabelFrame(frame, text = "Training set parameters")
frame0.pack(fill = X, padx = 10, pady = 10)

l1 = Label(frame0, text = "Number of papers to train neural network (default = 50)")
l1.pack(side = LEFT)

l1 = Entry(frame0, text = "100")
l1.pack(side = LEFT)

l1 = Button(frame0, text = "Refresh training list")
l1.pack(side = LEFT)

frame1 = LabelFrame(frame, text = "Select papers for training neural network")
frame1.pack(padx = 10, pady = 10)

but = Button(frame, text = "Select / Remove from selected", command = test)
but.pack()

frame2 = LabelFrame(frame, text = "Selected papers")
frame2.pack(padx = 10, pady = 10)

s1 = Scrollbar(frame1)
s1.pack(side = RIGHT, fill = Y)

Lb1 = Listbox (frame1, selectmode = MULTIPLE, width = 300)

s1['command'] = Lb1.yview
Lb1['yscrollcommand'] = s1.set


s2 = Scrollbar(frame2)
s2.pack(side = RIGHT, fill = Y)
Lb2 = Listbox (frame2, selectmode = MULTIPLE, width = 300)
s2['command'] = Lb2.yview
Lb2['yscrollcommand'] = s2.set
Lb2.pack()


def foo(papers_selected = ["none selected"]):
    Lb2.delete(0, 100)
    all_paps = []
    index_selected_titles = {}
    selected_count = 0
    for x in papers_selected:
        all_paps.append(selected_count)
        index_selected_titles[selected_count] = x
        Lb2.insert(selected_count, x)
        Lb2.selection_set(selected_count)
        selected_count += 1
    print(all_paps)

foo()

index_title = {}
counter = 0
for x in paper_list:
    index_title[counter] = x
    Lb1.insert(counter, x)
    counter+= 1

Lb1.pack()

def test():
  print(Lb1.curselection())
  lis = []
  for x in Lb1.curselection():
      lis.append(index_title[int(x)])
  if lis == []:
      foo(["none"])
  else:
      foo(lis)



root.mainloop()
