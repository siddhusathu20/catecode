# Catecode Encoder/Decoder
# Program and cipher by Siddharth Jai Gokulan

import customtkinter as ctk

alphabets = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiouy"
consonants = "bcdfghjklmnpqrstvwxz"

def encode() :
    toEncode = (toCode.get(0.0, "end")).lower()
    encoded = ""
    for i in toEncode :
        if i in vowels :
            encoded = encoded + alphabets[vowels.index(i)] + "•"
        elif i in consonants :
            encoded = encoded + alphabets[consonants.index(i)] + "-"
        else :
            encoded += i
    result.configure(state="normal")
    result.delete(0.0, "end")
    result.insert(0.0, encoded)
    result.configure(state="disabled")

def decode() :
    toDecode = (toCode.get(0.0, "end")).lower()
    decoded = ""
    for i in range(1, len(toDecode)) :
        if toDecode[i]=="•" :
            decoded += vowels[alphabets.index(toDecode[i-1])]
        elif toDecode[i]=="-" :
            decoded += consonants[alphabets.index(toDecode[i-1])]
        elif toDecode[i] not in alphabets :
            decoded += toDecode[i]
    result.configure(state="normal")
    result.delete(0.0, "end")
    result.insert(0.0, decoded)
    result.configure(state="disabled")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.geometry("400x400")
root.title("Catecode Encoder/Decoder")
title = ctk.CTkLabel(master=root, text=":: c a t e c o d e ::", font=("Lucida Console", 20))
title.place(relx=0.5, rely=0.05, anchor=ctk.N)
toCode = ctk.CTkTextbox(master=root, width=380, height=100, corner_radius=5)
toCode.place(relx=0.5, rely=0.2, anchor=ctk.N)
toCode.insert(0.0, "Type text here...")
dotButton = ctk.CTkButton(master=root, text="•", width=185, height=20, command=lambda: toCode.insert("end", "•"))
dotButton.place(relx=0.26, rely=0.47, anchor=ctk.N)
dashButton = ctk.CTkButton(master=root, text="-", width=185, height=20, command=lambda: toCode.insert("end", "-"))
dashButton.place(relx=0.74, rely=0.47, anchor=ctk.N)
encodeButton = ctk.CTkButton(master=root, text="Encode", width=380, height=30, command=encode)
encodeButton.place(relx=0.5, rely=0.53, anchor=ctk.N)
decodeButton = ctk.CTkButton(master=root, text="Decode", width=380, height=30, command=decode)
decodeButton.place(relx=0.5, rely=0.62, anchor=ctk.N)
result = ctk.CTkTextbox(master=root, state="disabled", width=380, height=100, corner_radius=5)
result.place(relx=0.5, rely=0.71, anchor=ctk.N)
result.configure(state="normal")
result.insert(0.0, "Encoded/decoded text appears here")
result.configure(state="disabled")
root.mainloop()