      

from tkinter import *

class Application(Frame):

    def __init__(self, master):
        """ Initialize the Frame """
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        # Title label
        self.instruction = Label(self, text = "PlayFair", font=("arial",17,"bold"))
        self.instruction.grid(row = 1, column = 0, columnspan = 2, padx = 5, sticky = W)


        # Message label
        self.instruction = Label(self, text = "Enter message: ")
        self.instruction.grid(row = 4, column = 0, columnspan = 150, padx = 5, sticky = W)

        # Message entry
        self.message= Entry(self)
        self.message.grid(row = 5, column = 0, padx = 5, sticky = W)

        # Key label
        self.instruction = Label(self, text = "Enter key ")
        self.instruction.grid(row = 6, column = 0, columnspan = 2, padx = 5, sticky = W)

        # Key entry
        self.key= Entry(self)
        self.key.grid(row = 7, column = 0, padx = 5, sticky = W)

        # Submit 
        self.submit_button = Button(self, text = "Submit", command = self.playfair)
        self.submit_button.grid(row = 8, column = 0, padx = 5, sticky = W)

        # Result label
        self.instruction = Label(self, text = "Result", font=("arial",14,"bold"))
        self.instruction.grid(row = 9, column = 0, columnspan = 2, padx = 5, sticky = W)

        # Result 
        self.result = Text(self, width = 45, height = 6, wrap = WORD)
        self.result.grid(row = 10, column = 0, columnspan = 3, padx = 5, sticky = W)





    def playfair(self):
        key=str(self.key.get())
        key=key.replace(" ", "")
        key=key.upper()
        def matrix(x,y,initial):
            return [[initial for i in range(x)] for j in range(y)]
            
        result=list()
        for c in key: 
            if c not in result:
                if c=='J':
                    result.append('I')
                else:
                    result.append(c)
        flag=0
        for i in range(65,91): 
            if chr(i) not in result:
                if i==73 and chr(74) not in result:
                    result.append("I")
                    flag=1
                elif flag==0 and i==73 or i==74:
                    pass    
                else:
                    result.append(chr(i))
        k=0
        my_matrix=matrix(5,5,0) 
        for i in range(0,5): 
            for j in range(0,5):
                my_matrix[i][j]=result[k]
                k+=1




        def locindex(c): 
            loc=list()
            if c=='J':
                c='I'
            for i ,j in enumerate(my_matrix):
                for k,l in enumerate(j):
                    if c==l:
                        loc.append(i)
                        loc.append(k)
                        return loc
            

        def encrypt():  
            msg=str(self.message.get())
            msg=msg.upper()
            msg=msg.replace(" ", "")             
            i=0
            for s in range(0,len(msg)+1,2):
                if s<len(msg)-1:
                    if msg[s]==msg[s+1]:
                        msg=msg[:s+1]+'X'+msg[s+1:]
            if len(msg)%2!=0:
                msg=msg[:]+'X'
            print("CIPHER TEXT:",end=' ')

            string = str()
            while i<len(msg):
                loc=list()
                loc=locindex(msg[i])
                loc1=list()
                loc1=locindex(msg[i+1])
                if loc[1]==loc1[1]:
                    string = string + "{}{}".format(my_matrix[(loc[0]+1)%5][loc[1]],my_matrix[(loc1[0]+1)%5][loc1[1]]) + " "
                    print("{}{}".format(my_matrix[(loc[0]+1)%5][loc[1]],my_matrix[(loc1[0]+1)%5][loc1[1]]),end=' ')
                elif loc[0]==loc1[0]:
                    string = string + "{}{}".format(my_matrix[loc[0]][(loc[1]+1)%5],my_matrix[loc1[0]][(loc1[1]+1)%5]) + " "
                    print("{}{}".format(my_matrix[loc[0]][(loc[1]+1)%5],my_matrix[loc1[0]][(loc1[1]+1)%5]),end=' ')  
                else:
                    string = string + "{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]) + " "
                    print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
                i=i+2 

            return string       
                         
                


        


        ciphertext = encrypt()
        

        self.result.delete(0.0, END)
        self.result.insert(0.0, ciphertext )
        return ciphertext
    

root = Tk()
root.title("PlayFair")
root.geometry("330x350")
app = Application(root)
root.mainloop()