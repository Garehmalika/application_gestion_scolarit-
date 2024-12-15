from tkinter import *
from tkinter import filedialog, messagebox
import shutil
import os

class Administrateur:
   def __init__(self, master):
       self.master = master
       self.create_widgets()
   # Création de l'interface principale
   def create_widgets(self):
       label_title4 = Label(self.master, text='Bienvenue chère administrateur', font=('Imprint MT Shadow', 38),bg='#39CEA8', fg='white')
       label_title4.place(x=250, y=180)
       # Ajouter l'image à la fenêtre (image PPM)
       image_path = 'LOGO.ppm'
       tk_image = PhotoImage(file=image_path).subsample(3, 3)
       label_image = Label(window3, image=tk_image)
       label_image.place(x=510, y=0)
       #creation des bouttons pour differentes action
       Button(self.master, text='Ajouter étudiant', font=("Algerian", 20), bg='white', fg='black',command=self.ajouter_etudiant).place(x=200, y=320)
       Button(self.master, text='Supprimer étudiant', font=("Algerian", 20), bg='white', fg='black',command=self.supprimer_etudiant).place(x=200, y=390)
       Button(self.master, text='Chercher étudiant', font=("Algerian", 20), bg='white', fg='black',command=self.cherche_etudiant).place(x=200, y=450)
       Button(self.master, text='Modifier étudiant', font=("Algerian", 20), bg='white', fg='black',command=self.modifier_etudiant).place(x=200, y=510)
       Button(self.master, text='Ajouter professeur', font=("Algerian", 20), bg='white', fg='black',command=self.ajouter_prof).place(x=650, y=320)
       Button(self.master, text='Supprimer professeur', font=("Algerian", 20), bg='white', fg='black',command=self.supprimer_prof).place(x=650, y=390)
       Button(self.master, text='Chercher professeur', font=("Algerian", 20), bg='white', fg='black',command=self.cherche_prof).place(x=650, y=450)
       Button(self.master, text='Modifier professeur', font=("Algerian", 20), bg='white', fg='black',command=self.modifier_prof).place(x=650, y=510)
       Button(self.master, text='Statisatique ', font=("Algerian", 20), bg='white', fg='black',command=self.stati).place(x=500, y=600)
       window3.mainloop()
   #fonction d"ajout de l etudiant
   def ajouter_etudiant(self):
       window3.destroy()
       window4 = Tk()
       window4.title('Centrale Casablanca')
       window4.geometry('1200x720')
       window4.minsize(480, 360)
       window4.iconbitmap('download (1) (2).ico')
       window4.config(background='white')
       Label_title1 = Label(window4, text='Prénom', font=('Times new roman', 14), fg='black',bg='white').place(x=400, y=250)
       p= Entry(window4, width=40)
       p.place(x=500, y=250)
       Label_title2 = Label(window4, text='Nom', font=('Times new roman', 14),  fg='black',bg='white').place(x=400, y=290)
       p1 = Entry(window4, width=40)
       p1.place(x=500, y=290)
       Label_title3 = Label(window4, text='Code', font=('Times new roman', 14),  fg='black',bg='white').place(x=400, y=330)
       p2 = Entry(window4, width=40)
       p2.place(x=500, y=330)
       def add_etudiant(): #fonction ajouter etudiant
           with open('etudiant.txt', 'a') as f:
               f.write(f'E{str(p2.get())}\t{str(p.get())}.{str(p1.get())}@centrale-casablanca.ma\n')
               print(f'E{str(p2.get())}\t{str(p.get())}.{str(p1.get())}@centrale-casablanca.ma\n')
               label_title3 = Label(window4, text='Étudiant a été ajouté avec succès.', font=('Times new roman', 14),bg='white', fg='black').place(x=550, y=460)
           f.close()
       Button(window4, text='Ajouter', font=("Algerian", 20), bg='black', fg='white', command=add_etudiant).place(x=550, y=400)
       window4.mainloop()
#fonction supprimer un etudiant
   def supprimer_etudiant(self):
       window3.destroy()
       window4 = Tk()
       window4.title('Centrale Casablanca')
       window4.geometry('1200x720')
       window4.minsize(480, 360)
       window4.iconbitmap('download (1) (2).ico')
       window4.config(background='white')
       Label_title2 = Label(window4, text='Adresse mail', font=('Times new roman', 14),bg='white', fg='black').place(x=400, y=200)
       no = Entry(window4, width=40)
       no.place(x=600, y=200)
       Label_title1 = Label(window4, text='Code étudiant ', font=('Times new roman', 14),bg='white', fg='black').place(x=400, y=250)
       co= Entry(window4, width=40)
       co.place(x=600, y=250)

       def supri_etudiant():
           num = co.get()
           nom=no.get()
           with open('etudiant.txt', 'r') as f:
               lines = f.readlines()
           with open('etudiant.txt', 'w') as f:
               for line in lines:
                   if line.split("\t")[0] != num and line.split("\t")[1] != nom :
                       f.write(line)
                       label_title3 = Label(window4, text='Étudiant a été supprimé avec succès.',font=('Times new roman', 14), bg='white', fg='black').place(x=550, y=460)
           print(f"Étudiant avec le code {co} et le nom {no} a été supprimé avec succès.")
       Button(window4, text='Supprimer', font=("Algerian", 20), bg='black', fg='white', command=supri_etudiant).place(x=550, y=380)
       window4.mainloop()
   #fonction pour modifier le nom ,prenom et code d'un etudiant
   def modifier_etudiant(self):
       window3.destroy()
       window4 = Tk()
       window4.title('Centrale Casablanca')
       window4.geometry('1200x720')
       window4.minsize(480, 360)
       window4.iconbitmap('download (1) (2).ico')
       window4.config(background='white')
       Label_title2 = Label(window4, text='adresse étudiant à supprimer', font=('Times new roman', 14), fg='black',
                            bg='white').place(x=380, y=200)
       no = Entry(window4, width=40)
       no.place(x=600, y=200)
       Label_title1 = Label(window4, text='Code étudiant à supprimer', font=('Times new roman', 14), fg='black',
                            bg='white').place(x=380, y=250)
       co = Entry(window4, width=40)
       co.place(x=600, y=250)
       Label_title3 = Label(window4, text='saisir la nouveaulle adresse', font=('Times new roman', 14), fg='black',
                            bg='white').place(x=380, y=300)
       no1 = Entry(window4, width=40)
       no1.place(x=600, y=300)
       Label_title4 = Label(window4, text='saisir le nouveau code', font=('Times new roman', 14), fg='black',
                            bg='white').place(x=380, y=350)
       co1 = Entry(window4, width=40)
       co1.place(x=600, y=350)

       def modif_etudiant():
           num1 = co1.get()
           nom1 = no1.get()
           num = co.get()
           nom = no.get()
           label_title3 = Label(window4, text='Étudiant a été modifié avec succès.', font=('Times new roman', 14),
                                bg='white', fg='black').place(x=550, y=460)
           print(f"Étudiant avec le code {co} et le nom {no} a été modifié avec succès.")

       Button(window4, text='modifier', font=("Algerian", 20), bg='black', fg='white', command=modif_etudiant).place(
           x=550, y=400)
       window4.mainloop()

# fonction pour accéder à l'autre window qui contient le processus de rechercher un étudiant
   def cherche_etudiant(self):
       window3.destroy() #fermer la fenetre window 3
       window4 = Tk() #créer une nouvelle fenetre
       window4.title('Centrale Casablanca')
       window4.geometry('1200x720')
       window4.minsize(480, 360)
       window4.iconbitmap('download (1) (2).ico')
       window4.config(background='white')
       Label_title1 = Label(window4, text='Code étudiant à chercher', font=('Times new roman', 14), fg='black',bg='white').place(x=340, y=250)
       code_entry = Entry(window4, width=40)
       code_entry.place(x=600, y=250)
       # fonction pour chercher un étudiant
       def cherche_etudiant_action():
           code = code_entry.get()
           found = False
           with open('etudiant.txt', 'r') as f:
               for line in f:
                   if code in line:
                       found = True
                       break
           if found:
               result_label = Label(window4, text=f"Étudiant avec le code {code} trouvé.", font=('Times new roman', 16),fg='black',bg='white')
           else:
               result_label = Label(window4, text=f"Aucun étudiant trouvé avec le code {code}.",font=('Times new roman', 16),fg='red',bg='white')
           result_label.place(x=400, y=350)
       Button(window4, text='Chercher', font=("Algerian", 20), bg='black', fg='white',command=cherche_etudiant_action).place(x=550, y=400)
       window4.mainloop()
   def ajouter_prof(self):
       window3.destroy()
       window4 = Tk()
       window4.title('Centrale Casablanca')
       window4.geometry('1200x720')
       window4.minsize(480, 360)
       window4.iconbitmap('download (1) (2).ico')
       window4.config(background='white')
       Label_title1 = Label(window4, text='Prénom', font=('Times new roman', 14), fg='black',bg='white').place(x=400, y=250)
       p = Entry(window4, width=40)
       p.place(x=500, y=250)
       Label_title2 = Label(window4, text='Nom', font=('Times new roman', 14), fg='black',bg='white').place(x=400, y=290)
       p1 = Entry(window4, width=40)
       p1.place(x=500, y=290)
       Label_title3 = Label(window4, text='Code', font=('Times new roman', 14), fg='black',bg='white').place(x=400, y=330)
       p2 = Entry(window4, width=40)
       p2.place(x=500, y=330)

       def add_prof():
           with open('professeur.txt', 'a') as f:
               f.write(f'P{str(p2.get())}\t{str(p.get())}.{str(p1.get())}@centrale-casablanca.ma\n')
               print(f'P{str(p2.get())}\t{str(p.get())}.{str(p1.get())}@centrale-casablanca.ma\n')
               label_title3 = Label(window4, text='Professeur a été ajouté avec succès.', font=('Times new roman', 14),bg='white', fg='black').place(x=550, y=460)
           f.close()
       Button(window4, text='Ajouter', font=("Algerian", 20), bg='black', fg='white', command=add_prof).place( x=550, y=400)
       window4.mainloop()

   def supprimer_prof(self):
       window3.destroy()
       window4 = Tk()
       window4.title('Centrale Casablanca')
       window4.geometry('1200x720')
       window4.minsize(480, 360)
       window4.iconbitmap('download (1) (2).ico')
       window4.config(background='white')
       Label_title2 = Label(window4, text='adresse professeur à supprimer', font=('Times new roman', 14),fg='black',bg='white').place(x=350, y=200)
       no = Entry(window4, width=40)
       no.place(x=600, y=200)
       Label_title1 = Label(window4, text='Code professeur à supprimer', font=('Times new roman', 14),fg='black',bg='white').place(x=350, y=250)
       co = Entry(window4, width=40)
       co.place(x=600, y=250)
       def supri_prof():
           num = co.get()
           nom = no.get()
           with open('professeur.txt', 'r') as f:
               lines = f.readlines()
           with open('professeur.txt', 'w') as f:
               for line in lines:
                   if line.split("\t")[0] != num and line.split("\t")[1] != nom:
                       f.write(line)
                       label_title3 = Label(window4, text='Professeur a été supprimé avec succès.',font=('Times new roman', 14), bg='white', fg='black').place(x=550, y=460)
           print(f"professeur avec le code {co} et le nom {no} a été supprimé avec succès.")
       Button(window4, text='Supprimer', font=("Algerian", 20), bg='black', fg='white', command=supri_prof).place( x=550, y=400)
       window4.mainloop()
   def modifier_prof(self):
       window3.destroy()
       window4 = Tk()
       window4.title('Centrale Casablanca')
       window4.geometry('1200x720')
       window4.minsize(480, 360)
       window4.iconbitmap('download (1) (2).ico')
       window4.config(background='white')
       Label_title2 = Label(window4, text='adresse professeur à supprimer', font=('Times new roman', 14),bg='white',fg='black').place(x=350, y=200)
       no = Entry(window4, width=40)
       no.place(x=600, y=200)
       Label_title1 = Label(window4, text='Code professeur à supprimer', font=('Times new roman', 14), fg='black',bg='white').place( x=350, y=250)
       co = Entry(window4, width=40)
       co.place(x=600, y=250)
       Label_title3 = Label(window4, text='saisir la nouveaulle adresse', font=('Times new roman', 14), fg='black',bg='white').place( x=350, y=300)
       no1 = Entry(window4, width=40)
       no1.place(x=600, y=300)
       Label_title4 = Label(window4, text='saisir le nouveau code', font=('Times new roman', 14), fg='black',bg='white').place(x=350,y=350)
       co1 = Entry(window4, width=40)
       co1.place(x=600, y=350)
       def modif_prof():
           num1 = co1.get()
           nom1 = no1.get()
           num = co.get()
           nom = no.get()
           with open('professeur.txt', 'r') as f:
               lines = f.readlines()
           with open('professeur.txt', 'w') as f:
               for line in lines:
                   if line.split("\t")[0] != num and line.split("\t")[1] != nom:
                       f.write(line)
           with open('professeur.txt', 'a') as f:
               f.write(f'P{str(num1)}\t{str(nom1)}')
               label_title3 = Label(window4, text='Professeur a été modifié avec succès.', font=('Times new roman', 14),bg='white', fg='black').place(x=550, y=460)
           f.close()
           print(f"le professeur avec le code {co} et le nom {no} a été modifié avec succès.")

       Button(window4, text='modifier', font=("Algerian", 20), bg='black', fg='white', command=modif_prof).place(
           x=550, y=400)
       window4.mainloop()

   def cherche_prof(self):
       window3.destroy()
       window4 = Tk()
       window4.title('Centrale Casablanca')
       window4.geometry('1200x720')
       window4.minsize(480, 360)
       window4.iconbitmap('download (1) (2).ico')
       window4.config(background='white')

       Label_title1 = Label(window4, text='Code professseur à chercher', font=('Times new roman', 14), fg='black',bg='white').place(x=350, y=250)
       code_entry = Entry(window4, width=40)
       code_entry.place(x=600, y=250)

       def cherche_prof_action():
           code = code_entry.get()
           found = False
           with open('professeur.txt', 'r') as f:
               for line in f:
                   if code in line:
                       found = True
                       break
           if found:
               result_label = Label(window4, text=f"Le professeur avec le code {code} trouvé.", font=('Times new roman', 16),bg='white',fg='black')
           else:
               result_label = Label(window4, text=f"Aucun professeur trouvé avec le code {code}.", font=('Times new roman', 16),fg='red',bg='white')

           result_label.place(x=400, y=350)

       Button(window4, text='Chercher', font=("Algerian", 20), bg='black', fg='white',
              command=cherche_prof_action).place(x=550, y=400)
       window4.mainloop()

   def stati(self):
       window3.destroy()
       window4 = Tk()
       window4.title('Centrale Casablanca')
       window4.geometry('1200x720')
       window4.minsize(480, 360)
       window4.iconbitmap('download (1) (2).ico')
       window4.config(background='#39CEA8')
       def nbr_prof():
           with open('professeur.txt', 'r') as f:
               lines = f.readlines()
               l=len(lines)
               messagebox.showinfo("Statistique", f"Le nombre de professeur de l'école est: {l} .")
       def nbr_etudiant():
           with open('etudiant.txt', 'r') as f:
               lines = f.readlines()
               l = len(lines)
               messagebox.showinfo("Statistique", f"Le nombre des étudiants de l'école est: {l} .")
       Button(window4, text='Nombre prof', font=("Algerian", 20), fg='#39CEA8', bg='white',command=nbr_prof).place(x=350, y=250)
       Button(window4, text='nombre etudiant', font=("Algerian", 20), fg='#39CEA8', bg='white',command=nbr_etudiant).place(x=650,y=250)
       window4.mainloop()






def existe_administrateur(code,nom):
   with open("administrateur.txt", 'r') as f:
       lignes = f.readlines()
       for ligne in lignes:
           t = ligne.strip().split('\t')
           if  t[0] == code and t[1] == nom:
               print("Authentification réussie.")
               window2.destroy()
               global window3
               window3 = Tk()
               window3.title('Centrale Casablanca')
               window3.geometry('1200x720')
               window3.minsize(480, 360)
               window3.iconbitmap('download (1) (2).ico')
               window3.config(background='#39CEA8')
               app = Administrateur(window3)
               window3.mainloop()
               break
       else:
           label_title3 = Label(window2, text='code ou adresse mail incorrecte', font=('Times new roman', 14),  fg='black').place(x=550, y=450)
   f.close()

def authentifier():
   nom = Field.get()
   code = Field1.get()
   if code[0] =="E":
       existe_etudiant(code,nom)
   if code[0] == "P":
       existe_professeur(code, nom)
   if code[0] == 'A':
       existe_administrateur(code,nom)
   else:
       label_title3 = Label(window2, text='code ou adresse mail incorrecte', font=('Times new roman', 14),bg='white', fg='black').place(x=550, y=460)



class Professeur:
    def __init__(self, master2):
        self.master2 = master2
        self.create_widgets()

    def create_widgets(self):
        Button(self.master2, text='Ajouter note', font=("Algerian", 20), bg='white', fg='#1C677D',
               command=self.ajouter_note).place(x=180, y=320)
        Button(self.master2, text='Ajouter absence', font=("Algerian", 20), bg='white', fg='#1C677D',
               command=self.ajouter_absence).place(x=180, y=420)
        Button(self.master2, text='Ajouter cours', font=("Algerian", 20), bg='white', fg='#1C677D',
               command=self.ajouter_cours).place(x=180, y=520)
        Button(self.master2, text='modifier note', font=("Algerian", 20), bg='white', fg='#1C677D',
               command=self.modifier_note).place(x=650, y=320)
        Button(self.master2, text='modifier absence', font=("Algerian", 20), bg='white', fg='#1C677D',
               command=self.modifier_absence).place(x=650, y=420)
        Button(self.master2, text='supprimer cours', font=("Algerian", 20), bg='white', fg='#1C677D',command=self.supprimer_cours).place(x=650, y=520)

    def ajouter_note(self):
        window3.destroy()
        window4 = Tk()
        window4.title('Centrale Casablanca')
        window4.geometry('1200x720')
        window4.minsize(480, 360)
        window4.iconbitmap('download (1) (2).ico')
        window4.config(background='white')
        Label_title1 = Label(window4, text='numéro étudiant', font=('Times new roman', 14), fg='black',bg='white').place(x=350,                                                                                                       y=250)
        p = Entry(window4, width=40)
        p.place(x=500, y=250)
        Label_title2 = Label(window4, text='Matière', font=('Times new roman', 14), fg='black',bg='white').place(x=350, y=290)
        p1 = Entry(window4, width=40)
        p1.place(x=500, y=290)
        Label_title3 = Label(window4, text='Note', font=('Times new roman', 14), fg='black',bg='white').place(x=350, y=320)
        p2 = Entry(window4, width=40)
        p2.place(x=500, y=320)
        def override_line(file_path, line_number, new_content):
            # Open the file in read mode
            with open(file_path, 'r') as file:
                lines = file.readlines()

            # Check if the line_number is valid
            if 1 <= line_number <= len(lines):
                # Modify the specific line
                lines[line_number] = new_content + '\n'

                # Open the file in write mode to override its contents
                with open(file_path, 'w') as file:
                    file.writelines(lines)
                print(f"Line {line_number} overridden successfully.")
            else:
                print(f"Invalid line number: {line_number}")

        def ajouter_note_action():
            numero = p.get()
            matiere = p1.get()
            n = p2.get()

            with open('toutesnotes.txt', 'r') as f:
                lines = f.readlines()

            lines = [element.strip() for element in lines]
            if matiere not in lines[0]:
                lines[0] += f":{matiere}"

            imatiere = (lines[0].split("/")).index(matiere)
            exist = 0
            # Override the note if numero exists
            for i in range(1, len(lines)):
                L = lines[i].split("/")
                if L[0] == numero:
                    L[imatiere] = str(n)
                    lines[i] = "/".join(L)
                    exist = 1
                    print(lines)
                    override_line('toutesnotes.txt', i, "/".join(L))
                    break
            # Create new line as numero does not exist
            if exist == 0:
                L = [str(numero)] + [""] * (len(lines[0].split("/")) - 1)
                L[imatiere] = str(n)
                lines.append("/".join(L))

                with open('toutesnotes.txt', 'w') as f:
                    for i in range(len(lines)):
                        f.write(lines[i] + "\n")
                f.close()
            label_title4 = Label(window4, text='note a été ajouté avec succès.',font=('Times new roman', 14), bg='white', fg='black').place(x=550, y=460)
        Button(window4, text='Ajouter', font=("Algerian", 20), bg='black', fg='white', command=ajouter_note_action).place(x=550, y=400)
        window4.mainloop()

    def ajouter_absence(self):
        window3.destroy()
        window4 = Tk()
        window4.title('Centrale Casablanca')
        window4.geometry('1200x720')
        window4.minsize(480, 360)
        window4.iconbitmap('download (1) (2).ico')
        window4.config(background='white')
        Label_title1 = Label(window4, text='numéro étudiant', font=('Times new roman', 14), fg='black',bg='white').place(x=330,y=250)
        p = Entry(window4, width=40)
        p.place(x=500, y=250)
        Label_title2 = Label(window4, text='matière', font=('Times new roman', 14), fg='black',bg='white').place(x=330, y=290)
        p1 = Entry(window4, width=40)
        p1.place(x=500, y=290)
        Label_title3 = Label(window4, text='nombre des absences', font=('Times new roman', 14), fg='black',bg='white').place(x=330, y=330)
        p2 = Entry(window4, width=40)
        p2.place(x=500, y=330)
        def override_line(file_path, line_number, new_content):
            # Open the file in read mode
            with open(file_path, 'r') as file:
                lines = file.readlines()

            # Check if the line_number is valid
            if 1 <= line_number <= len(lines):
                # Modify the specific line
                lines[line_number] = new_content + '\n'

                # Open the file in write mode to override its contents
                with open(file_path, 'w') as file:
                    file.writelines(lines)
                print(f"Line {line_number} overridden successfully.")
            else:
                print(f"Invalid line number: {line_number}")

        def ajouter_absence_action():
            numero = p.get()
            matiere = p1.get()
            abs = p2.get()
            with open('absences.txt', 'r') as f:
                lines = f.readlines()

            lines = [element.strip() for element in lines]
            if matiere not in lines[0]:
                lines[0] += f":{matiere}"

            imatiere = (lines[0].split("/")).index(matiere)
            exist = 0
            # Override the note if numero exists
            for i in range(1, len(lines)):
                L = lines[i].split("/")
                if L[0] == numero:
                    L[imatiere] = str(abs)
                    lines[i] = "/".join(L)
                    exist = 1
                    print(lines)
                    override_line('absences.txt', i, "/".join(L))
                    break
            # Create new line as numero does not exist
            if exist == 0:
                L = [str(numero)] + [""] * (len(lines[0].split("/")) - 1)
                L[imatiere] = str(abs)
                lines.append("/".join(L))

                with open('absences.txt', 'w') as f:
                    for i in range(len(lines)):
                        f.write(lines[i] + "\n")

            label_title4 = Label(window4, text='absence  a été ajouté avec succès.', font=('Times new roman', 14),bg='white', fg='black').place(x=550, y=460)

        Button(window4, text='Ajouter', font=("Algerian", 20), bg='black', fg='white',
               command=ajouter_absence_action).place(x=550, y=400)

        window4.mainloop()

    def ajouter_cours(self):
        file_path = filedialog.askopenfilename(title="Choisissez un document", filetypes=[("Fichiers PDF", "*.pdf")])
        if file_path:
            destination_folder = 'documents'
            shutil.copy(file_path, destination_folder)
            messagebox.showinfo("Succès", "Le document a été ajouté avec succès.")
    def supprimer_cours(self):
        window4 = Tk()
        window4.title('Centrale Casablanca')
        window4.geometry('1200x720')
        window4.minsize(480, 360)
        window4.iconbitmap('download (1) (2).ico')
        window4.config(background='white')

        Label_title1 = Label(window4, text='nom du fichier', font=('Times new roman', 14), fg='black',bg='white').place(x=350, y=250)
        p = Entry(window4, width=40)
        p.place(x=500, y=250)

        def supprimer_fichier_action():
            nom_fichier = p.get()
            dossier_documents = 'documents'
            chemin_fichier = os.path.join(dossier_documents, nom_fichier)

            if os.path.exists(chemin_fichier):
                os.remove(chemin_fichier)
                messagebox.showinfo("Succès", f"Le document {nom_fichier} a été supprimé avec succès.")
            else:
                messagebox.showwarning("Avertissement", f"Le document {nom_fichier} n'existe pas.")
            label_title4 = Label(window4, text='cour a été supprimer avec succès.', font=('Times new roman', 14),bg='white', fg='black').place(x=550, y=460)
        Button(window4, text='Supprimer', font=("Algerian", 20), bg='black', fg='white',
               command=supprimer_fichier_action).place(x=550, y=400)
        window4.mainloop()


    def modifier_note(self):
        window3.destroy()
        window4 = Tk()
        window4.title('Centrale Casablanca')
        window4.geometry('1200x720')
        window4.minsize(480, 360)
        window4.iconbitmap('download (1) (2).ico')
        window4.config(background='white')
        Label_title1 = Label(window4, text='numèro étudiant', font=('Times new roman', 14), fg='black',bg='white').place(x=350,
                                                                                                              y=250)
        p = Entry(window4, width=40)
        p.place(x=500, y=250)
        Label_title2 = Label(window4, text='matière', font=('Times new roman', 14), fg='black',bg='white').place(x=350, y=290)
        p1 = Entry(window4, width=40)
        p1.place(x=500, y=290)
        Label_title3 = Label(window4, text='note', font=('Times new roman', 14), fg='black',bg='white').place(x=350, y=330)
        p2 = Entry(window4, width=40)
        p2.place(x=500, y=330)
        def modifier_note_action():
            numero = p.get()
            matiere = p1.get()
            n = p2.get()

            with open('toutesnotes.txt', 'r') as f:
                lines = f.readlines()

            lines = [element.strip() for element in lines]
            if matiere not in lines[0]:
                lines[0] += f"/{matiere}"

            imatiere = (lines[0].split("/")).index(matiere)
            exist = 0

            for i in range(1, len(lines)):
                L = lines[i].split("/")
                if imatiere < len(L):
                    if L[0] == numero:
                        lines.pop(i)
                        L[imatiere] = str(n)
                        lines.insert(i, "/".join(L))
                        exist = 1
                        break

            if exist == 0:
                L = [str(numero)] + [""] * (len(lines[0].split("/")) - 1)
                L[imatiere] = str(n)
                lines.append("/".join(L))

            with open('toutesnotes.txt', 'w') as f:
                for i in range(len(lines)):
                    f.write(lines[i] + "\n")
            label_title4 = Label(window4, text='note a été modifié avec succès.', font=('Times new roman', 14),bg='white', fg='black').place(x=550, y=460)


        Button(window4, text='Ajouter', font=("Algerian", 20), bg='black', fg='white',
               command=modifier_note_action).place(x=550, y=400)

        window4.mainloop()
    def modifier_absence(self):
        window3.destroy()
        window4 = Tk()
        window4.title('Centrale Casablanca')
        window4.geometry('1200x720')
        window4.minsize(480, 360)
        window4.iconbitmap('download (1) (2).ico')
        window4.config(background='white')
        Label_title1 = Label(window4, text='numéro étudiant', font=('Times new roman', 14), fg='black',bg='white').place(x=330,
                                                                                                              y=250)
        p = Entry(window4, width=40)
        p.place(x=500, y=250)
        Label_title2 = Label(window4, text='matière', font=('Times new roman', 14), fg='black',bg='white').place(x=330, y=290)
        p1 = Entry(window4, width=40)
        p1.place(x=500, y=290)
        Label_title3 = Label(window4, text='nombre des absences', font=('Times new roman', 14), fg='black',bg='white').place(x=330, y=330)
        p2 = Entry(window4, width=40)
        p2.place(x=500, y=330)


        def modifier_absence_action():
            numero = p.get()
            matiere = p1.get()
            n = p2.get()

            with open('toutesabsences.txt', 'r') as f:
                lines = f.readlines()

            lines = [element.strip() for element in lines]
            if matiere not in lines[0]:
                lines[0] += f"/{matiere}"

            imatiere = (lines[0].split("/")).index(matiere)
            exist = 0

            for i in range(1, len(lines)):
                L = lines[i].split("/")
                if imatiere < len(L):
                    if L[0] == numero:
                        lines.pop(i)
                        L[imatiere] = str(n)
                        lines.insert(i, "/".join(L))
                        exist = 1
                        break

            if exist == 0:
                L = [str(numero)] + [""] * (len(lines[0].split("/")) - 1)
                L[imatiere] = str(n)
                lines.append("/".join(L))

            with open('toutesabsences.txt', 'w') as f:
                for i in range(len(lines)):
                    f.write(lines[i] + "\n")
            label_title4 = Label(window4, text='absence a été modifié avec succès.', font=('Times new roman', 14),bg='white', fg='black').place(x=550, y=460)


        Button(window4, text='Ajouter', font=("Algerian", 20), bg='black', fg='white',command=modifier_absence_action).place(x=550, y=400)


def existe_professeur(code,nom):
   with open("professeur.txt", 'r') as f:
       lignes = f.readlines()
       for ligne in lignes:
           t = ligne.strip().split('\t')
           if  t[0] == code and t[1] == nom:
               print("Authentification réussie.")
               window2.destroy()
               global window3
               window3 = Tk()
               window3.title('Centrale Casablanca')
               window3.geometry('1200x720')
               window3.minsize(480, 360)
               window3.iconbitmap('download (1) (2).ico')
               window3.config(background='#1C677D')
               app = Professeur(window3)
               label_title2 = Label(window3, text='Bienvenue chère Professeur', font=('Imprint MT Shadow', 38), fg='white',bg='#1C677D').place(x=350, y=150)
               window3.mainloop()
               break
       else:
           label_title3 = Label(window2, text='code ou adresse mail incorrecte', font=('Times new roman', 14), bg='#1C677D', fg='white').place(x=550, y=420)
   f.close()

class Etudiant:
    def __init__(self, master3):
        self.master3 = master3
        self.create_widgets()

    def create_widgets(self):
        Button(self.master3, text='Chercher note', font=("Algerian", 20), bg='white', fg='#1C677D',
               command=self.checher_note).place(x=280, y=320)
        Button(self.master3, text='Chercher absence', font=("Algerian", 20), bg='white', fg='#1C677D',
               command=self.chercher_absence).place(x=280, y=420)
        Button(self.master3, text='Telecharger cours', font=("Algerian", 20), bg='white', fg='#1C677D',
               command=self.telecharger_cours).place(x=280, y=520)

    def checher_note(self):
        window3.destroy()
        window4 = Tk()
        window4.title('Centrale Casablanca')
        window4.geometry('1200x720')
        window4.minsize(480, 360)
        window4.iconbitmap('download (1) (2).ico')
        window4.config(background='white')
        Label_title1 = Label(window4, text='numéro étudiant', font=('Times new roman', 14), fg='black', bg='white').place(x=350, y=250)
        p = Entry(window4, width=40)
        p.place(x=500, y=250)
        Label_title2 = Label(window4, text='matiere', font=('Times new roman', 14), fg='black',bg='white').place(x=400, y=290)
        p1 = Entry(window4, width=40)
        p1.place(x=500, y=290)

        def chercher_note_action():
            numero = p.get()
            matiere = p1.get()
            with open('toutesnotes.txt', 'r') as f:
                lines = f.readlines()

            lines = [element.strip() for element in lines]
            header = lines[0].split('/')

            try:
                index_matiere = header.index(matiere)
            except ValueError:
                messagebox.showerror("Erreur", f"La matière {matiere} n'a pas été trouvée.")
                window4.destroy()
                return

            for line in lines[1:]:
                data = line.split('/')
                if data[0] == numero:
                    try:
                        note = int(data[index_matiere])
                        messagebox.showinfo("Note trouvée", f"La note de l'étudiant {numero} en {matiere} est : {note}")
                    except ValueError:
                        messagebox.showinfo("Note non trouvée", f"L'étudiant {numero} n'a pas de note en {matiere}.")
                    window4.destroy()
                    return

            messagebox.showinfo("Note non trouvée", f"L'étudiant {numero} n'a pas de note en {matiere}.")
            window4.destroy()

        Button(window4, text='Chercher', font=("Algerian", 20), bg='black', fg='white',
               command=chercher_note_action).place(x=550, y=400)

        window4.mainloop()

    def chercher_absence(self):
        window3.destroy()
        window4 = Tk()
        window4.title('Centrale Casablanca')
        window4.geometry('1200x720')
        window4.minsize(480, 360)
        window4.iconbitmap('download (1) (2).ico')
        window4.config(background='white')
        Label_title1 = Label(window4, text='numéro étudiant', font=('Times new roman', 14), fg='black',bg='white').place(x=350,
                                                                                                              y=250)
        p = Entry(window4, width=40)
        p.place(x=500, y=250)
        Label_title2 = Label(window4, text='matière', font=('Times new roman', 14), fg='black',bg='white').place(x=350, y=290)
        p1 = Entry(window4, width=40)
        p1.place(x=500, y=290)

        def chercher_absence_action():
            numero = p.get()
            matiere = p1.get()
            with open('toutesabsences.txt', 'r') as f:
                lines = f.readlines()

            lines = [element.strip() for element in lines]
            header = lines[0].split('/')

            try:
                index_matiere = header.index(matiere)
            except ValueError:
                messagebox.showerror("Erreur", f"La matière {matiere} n'a pas été trouvée.")
                window4.destroy()
                return

            for line in lines[1:]:
                data = line.split('/')
                if data[0] == numero:
                    try:
                        abs = int(data[index_matiere])
                        messagebox.showinfo("absence trouvée",
                                            f"Les absences de l'étudiant {numero} en {matiere} est : {abs}")
                    except ValueError:
                        messagebox.showinfo("Note non trouvée", f"L'étudiant {numero} n'a pas de note en {matiere}.")
                    window4.destroy()
                    return

            messagebox.showinfo("Note non trouvée", f"L'étudiant {numero} n'a pas de note en {matiere}.")
            window4.destroy()

        Button(window4, text='Chercher', font=("Algerian", 20), bg='black', fg='white',
               command=chercher_absence_action).place(x=550, y=400)

        window4.mainloop()


    def telecharger_cours(self):
        window4 = Tk()
        window4.title('Centrale Casablanca')
        window4.geometry('1200x720')
        window4.minsize(480, 360)
        window4.iconbitmap('download (1) (2).ico')
        window4.config(background='white')

        Label_title1 = Label(window4, text='nom du fichier', font=('Times new roman', 14), fg='black',bg='white').place(x=350,
                                                                                                             y=250)
        p = Entry(window4, width=40)
        p.place(x=500, y=250)

        def telecharger_fichier_action():
            nom_fichier = p.get()
            dossier_documents = 'documents'
            chemin_fichier_source = os.path.join(dossier_documents, nom_fichier)

            if os.path.exists(chemin_fichier_source):
                shutil.copy(chemin_fichier_source,
                            '.')  # Copier le fichier dans le répertoire courant (changer selon vos besoins)
                messagebox.showinfo("Succès", f"Le document {nom_fichier} a été téléchargé avec succès.")
            else:
                messagebox.showwarning("Avertissement", f"Le document {nom_fichier} n'existe pas.")

        Button(window4, text='Télécharger', font=("Algerian", 20), bg='black', fg='white',
               command=telecharger_fichier_action).place(x=550, y=400)
        window4.mainloop()
def existe_etudiant(code,nom):
   with open("etudiant.txt", 'r') as f:
       lignes = f.readlines()
       for ligne in lignes:
           t = ligne.strip().split('\t')
           if  t[0] == code and t[1] == nom:
               print("Authentification réussie.")
               window2.destroy()
               global window3
               window3 = Tk()
               window3.title('Centrale Casablanca')
               window3.geometry('1200x720')
               window3.minsize(480, 360)
               window3.iconbitmap('download (1) (2).ico')
               window3.config(background='#1C677D')
               app = Etudiant(window3)
               label_title2 = Label(window3, text='Bienvenue chère étudiant', font=('Imprint MT Shadow', 38), fg='white',bg='#1C677D').place(x=350, y=200)
               break
       else:
           label_title3 = Label(window2, text='code ou adresse mail incorrecte', font=('Times new roman', 14), bg='#1C677D', fg='white').place(x=550, y=420)
   f.close()

def open_fenetre():
   window1.destroy()
   global window2
   window2 = Tk()
   window2.title('Centrale Casablanca')
   window2.geometry('1200x720')
   window2.iconbitmap('download (1) (2).ico')
   window2.config(background='White')
   # Ajouter l'image à la fenêtre (image PPM)
   image_path = 'LOGO.ppm'  # Remplacez par le chemin réel de votre image PPM
   tk_image = PhotoImage(file=image_path).subsample(2, 2)
   label_image = Label(window2, image=tk_image)
   label_image.place(x=490, y=0)
   label_title = Label(window2,text='Adresse mail', font=('Times new roman', 15),fg='#1C677D',bg='white').place(x=390, y=300)
   global Field
   Field = Entry(window2, width=50)
   Field.place(x=500, y=300)
   Label_title1 = Label(window2, text='Mode passe', font=('Times new roman', 15),bg='white',fg='#1C677D').place(x=390, y=340)
   global Field1
   Field1 = Entry(window2, width=50)
   Field1.place(x=500, y=340)
   Button(window2, text='Connexion', font=("Algerian", 20), bg='#1C677D', fg='white', command=authentifier).place(x=550, y=390)
   window2.mainloop()


window1 = Tk()
window1.title('Centrale Casablanca')
window1.geometry('1200x720')
window1.iconbitmap('download (1) (2).ico')
window1.config(background='#39CEA8')
# Ajouter l'image à la fenêtre (image PPM)
# Remplacez par le chemin réel de votre image PPM
image_path = 'image.ppm'
tk_image = PhotoImage(file=image_path)
label_image = Label(window1, image=tk_image,bg='white')
label_image.place(x=300, y=300)
# Stocker la référence de l'image en tant qu'attribut de la fenêtre
window1.tk_image = tk_image
Label_title = Label(window1, text='Bienvenue chers utilisateurs', font=("Algerian", 40), bg='#39CEA8', fg='white').place(x=250, y=190)
Button(window1, text='Authentifier', font=("Algerian", 20), bg='white', fg='#39CEA8', command=open_fenetre).place(x=550, y=300)
window1.mainloop()