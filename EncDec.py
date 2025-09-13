from tkinter import *
from tkinter import messagebox
import base64
from datetime import datetime

# File where encryption/decryption history will be saved
history_file = "history.txt"

# ---------------- SAVE HISTORY FUNCTION ---------------- #
def save_history(action, original, result):
    """Save encryption/decryption actions into history.txt with timestamp"""
    with open(history_file, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {action}\n")
        f.write(f"Original: {original.strip()}\n")
        f.write(f"Result: {result.strip()}\n")
        f.write("-"*50 + "\n")

# ---------------- DECRYPT FUNCTION ---------------- #
def decrypt():
    password = code.get()  # Get the entered password from input
    
    # If no password has been set yet, show error
    if user_password.get() == "":
        messagebox.showerror("No Password Set", "Please set a password before proceeding.")
        return 

    # If entered password matches user set password
    if password == user_password.get():
        # Create a new popup window for decryption result
        window2 = Toplevel(window)
        window2.title("Decryption")
        window2.geometry("400x350")
        window2.configure(bg='green')

        # Get the encrypted message from text box
        message = box1.get(1.0, END)
        
        # Base64 decode the message
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("ascii")

        # Display the decrypted message in a new window
        Label(window2, text="DECRYPT", font="Arial", fg='white', bg="green").place(x=10, y=0)
        box2 = Text(window2, font="Roboto 10", bg='white', relief=GROOVE, wrap=WORD, bd=0)
        box2.place(x=10, y=40, width=380, height=150)
        box2.insert(END, decrypt)

        # Save the decryption history
        save_history("DECRYPTED", message, decrypt)

    elif password == "":
        messagebox.showerror("Decryption", "Input Password")
    else:
        messagebox.showerror("Decryption", "Invalid Password")

# ---------------- ENCRYPT FUNCTION ---------------- #
def encrypt():
    password = code.get()  # Get the entered password from input

    # If no password has been set yet, show error
    if user_password.get() == "":
        messagebox.showerror("No Password Set", "Please set a password before proceeding.")
        return 

    # If entered password matches user set password
    if password == user_password.get():
        # Create a new popup window for encryption result
        window1 = Toplevel(window)
        window1.title("Encryption")
        window1.geometry("400x350")
        window1.configure(bg='red')

        # Get plain text from input box
        message = box1.get(1.0, END)

        # Base64 encode the message
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        # Display the encrypted text in a new window
        Label(window1, text="ENCRYPT", font="Arial", fg='white', bg="red").place(x=10, y=0)
        box2 = Text(window1, font="Roboto 10", bg='white', relief=GROOVE, wrap=WORD, bd=0)
        box2.place(x=10, y=40, width=380, height=150)
        box2.insert(END, encrypt)

        # Save encryption history
        save_history("ENCRYPTED", message, encrypt)

    elif password == "":
        messagebox.showerror("Encryption", "Input Password")
    else:
        messagebox.showerror("Encryption", "Invalid Password")

# ---------------- SET PASSWORD SCREEN ---------------- #
def set_password_screen():
    """Popup screen to allow user to set their own password"""

    def save_password():
        password = new_password.get()
        
        # Check if password is not empty
        if password != "":
            user_password.set(password)  # Save user password in global variable
            messagebox.showinfo("Password Set", "Your password has been set successfully.")
            password_window.destroy()  # Close password window
        else:
            messagebox.showerror("Error", "Password cannot be empty.")

    global new_password 
    password_window = Toplevel(window)
    password_window.title("Set Password")
    password_window.geometry("400x200")
    
    Label(password_window, text="Set your Password", font=("Arial", 12)).place(x=10, y=10)
    
    new_password = StringVar()  
    password_entry = Entry(password_window, textvariable=new_password, show="*", font=("Arial", 15))
    password_entry.place(x=10, y=50, width=300)

    save_button = Button(password_window, text="Save Password", width=20, height=2, fg="white", bg="blue", bd=0, font=("Arial", 10), command=save_password)
    save_button.place(x=10, y=100)

# ---------------- MAIN SCREEN ---------------- #
def main_screen():
    """Main window of the app"""
    global window
    global code
    global box1
    global user_password

    window = Tk()
    window.geometry("378x398")
    window.title("EncDec App")
    
    # Stores user set password (default empty)
    user_password = StringVar()  

    # Reset function to clear text and password
    def reset():
        code.set("")
        box1.delete(1.0, END)

    # Label and text input for main message
    text1 = Label(window, text="Enter text to Encrypt or Decrypt", fg="black", font=("Arial", 13))
    text1.place(x=10, y=10)
    box1 = Text(font="Roboto 20", bg='white', relief=GROOVE, wrap=WORD, bd=0)
    box1.place(x=10, y=50, width=355, height=100)
    
    # Label and input for secret key
    text2 = Label(window, text="Enter Secret Key", fg="black", font=("Arial", 13))
    text2.place(x=10, y=170)
    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("Arial", 25), show='*').place(x=10, y=200)

    # Buttons for encrypt, decrypt, reset and set password
    encrypt_button = Button(text="ENCRYPT", width=20, height=2, fg='white', bg='red', bd=0, font=("Arial", 10), command=encrypt).place(x=10, y=250)
    decrypt_button = Button(text="DECRYPT", width=20, height=2, fg='white', bg='green', bd=0, font=("Arial", 10), command=decrypt).place(x=200, y=250)
    reset_button = Button(text="RESET", width=45, height=2, fg='white', bg='blue', bd=0, font=("Arial", 10), command=reset).place(x=10, y=300)
    
    # Button to set password
    set_password_button = Button(window, text="Set Password", width=20, height=2, fg="white", bg="purple", bd=0, font=("Arial", 10), command=set_password_screen)
    set_password_button.place(x=10, y=350)
    
    window.mainloop()

# Run the app
main_screen()
