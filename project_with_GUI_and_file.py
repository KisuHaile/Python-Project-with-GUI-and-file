from tkinter import *
from tkinter import messagebox, simpledialog, ttk
import json

class Pc:
    def __init__(self, student_name, student_Id, student_phonenumber, pc_name, pc_model, pc_serial):
        self.student_name = student_name
        self.student_Id = student_Id
        self.student_phonenumber = student_phonenumber
        self.pc_name = pc_name
        self.pc_model = pc_model
        self.pc_serial = pc_serial

class Registration:
    def __init__(self):
        self.registered_pcs = {}

    def register_pc(self, pc):
        if pc.pc_serial not in self.registered_pcs:
            self.registered_pcs[pc.pc_serial] = pc
            messagebox.showinfo("Success", "PC registered successfully!")
        else:
            messagebox.showerror("Error", "PC with this serial number is already registered.")
    
    def search_by_model(self, pc_model):
        matching_pcs = [pc for pc in self.registered_pcs.values() if pc.pc_model == pc_model]
        if matching_pcs:
            results = ""
            for pc in matching_pcs:
                results += (f"Student Name: {pc.student_name}\n"
                            f"Student ID: {pc.student_Id}\n"
                            f"Student Phone number: {pc.student_phonenumber}\n"
                            f"Serial: {pc.pc_serial}\n"
                            f"PC Name: {pc.pc_name}\n"
                            f"PC Model: {pc.pc_model}\n\n")
            self.show_result(results)
        else:
            messagebox.showerror("Error", "PC with this model is not registered.")

    def search_by_serial(self, pc_serial):
        if pc_serial in self.registered_pcs:
            pc = self.registered_pcs[pc_serial]
            results = (f"Student Name: {pc.student_name}\n"
                       f"Student ID: {pc.student_Id}\n"
                       f"Student Phone number: {pc.student_phonenumber}\n"
                       f"Serial: {pc.pc_serial}\n"
                       f"PC Name: {pc.pc_name}\n"
                       f"PC Model: {pc.pc_model}\n")
            self.show_result(results)
        else:
            messagebox.showerror("Error", "PC with this serial number is not registered.")

    def search_by_student_Id(self, student_Id):
        matching_pcs = [pc for pc in self.registered_pcs.values() if pc.student_Id == student_Id]
        if matching_pcs:
            results = ""
            for pc in matching_pcs:
                results += (f"Student Name: {pc.student_name}\n"
                            f"Student ID: {pc.student_Id}\n"
                            f"Student Phone number: {pc.student_phonenumber}\n"
                            f"Serial: {pc.pc_serial}\n"
                            f"PC Name: {pc.pc_name}\n"
                            f"PC Model: {pc.pc_model}\n\n")
            self.show_result(results)
        else:
            messagebox.showerror("Error", "PC with this student ID is not registered.")

    def display_registered_pcs(self):
        if self.registered_pcs:
            results = "All registered PCs:\n\n"
            for pc in self.registered_pcs.values():
                results += (f"Student Name: {pc.student_name}\n"
                            f"Student ID: {pc.student_Id}\n"
                            f"Student Phone number: {pc.student_phonenumber}\n"
                            f"Serial: {pc.pc_serial}\n"
                            f"PC Name: {pc.pc_name}\n"
                            f"PC Model: {pc.pc_model}\n\n")
            self.show_result(results)
        else:
            messagebox.showinfo("Info", "No PCs are currently registered.")

    def delete_by_student_Id(self, student_Id):
        matching_pcs = [pc_serial for pc_serial, pc in self.registered_pcs.items() if pc.student_Id == student_Id]
        if matching_pcs:
            for pc_serial in matching_pcs:
                pc = self.registered_pcs[pc_serial]
                del self.registered_pcs[pc_serial]
                messagebox.showinfo("Deleted", f"PC {pc.pc_name} (Serial: {pc.pc_serial}) has been removed.")
        else:
            messagebox.showerror("Error", "No PC found with this student ID.")

    def delete_by_model(self, pc_model):
        matching_pcs = [pc_serial for pc_serial, pc in self.registered_pcs.items() if pc.pc_model == pc_model]
        if matching_pcs:
            for pc_serial in matching_pcs:
                pc = self.registered_pcs[pc_serial]
                del self.registered_pcs[pc_serial]
                messagebox.showinfo("Deleted", f"PC {pc.pc_name} (Serial: {pc.pc_serial}) has been removed.")
        else:
            messagebox.showerror("Error", "No PC found with this model.")

    def delete_by_serial(self, pc_serial):
        if pc_serial in self.registered_pcs:
            pc = self.registered_pcs[pc_serial]
            del self.registered_pcs[pc_serial]
            messagebox.showinfo("Deleted", f"PC {pc.pc_name} (Serial: {pc.pc_serial}) has been removed.")
        else:
            messagebox.showerror("Error", "No PC found with this serial number.")

    def show_result(self, result):
        result_window = Toplevel()
        result_window.title("Search Results")
        text = Text(result_window)
        text.insert(END, result)
        text.pack(expand=True, fill=BOTH)
        button = Button(result_window, text="Close", command=result_window.destroy)
        button.pack()

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump([pc.__dict__ for pc in self.registered_pcs.values()], f)
        messagebox.showinfo("Saved", f"Registered PCs have been saved to {filename}")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.registered_pcs = {pc_data['pc_serial']: Pc(**pc_data) for pc_data in data}
            messagebox.showinfo("Loaded", f"Registered PCs have been loaded from {filename}")
        except FileNotFoundError:
            messagebox.showerror("File Not Found", f"File {filename} not found.")

class RegistrationApp(Tk):
    def __init__(self, registration):
        super().__init__()
        self.registration = registration
        self.title("Debre Birhan University PC Registration")
        self.geometry("500x250")

        self.create_widgets()

    def create_widgets(self):
        self.notebook = ttk.Notebook(self)
        
        self.register_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.register_frame, text="Register PC")
        self.create_register_tab()

        self.display_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.display_frame, text="Display PCs")
        self.create_display_tab()

        self.search_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.search_frame, text="Search PC")
        self.create_search_tab()

        self.delete_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.delete_frame, text="Delete PC")
        self.create_delete_tab()

        self.notebook.pack(expand=True, fill=BOTH)

        self.create_menu()

    def create_menu(self):
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save", command=self.save_to_file)
        filemenu.add_command(label="Load", command=self.load_from_file)
        menubar.add_cascade(label="File", menu=filemenu)
        self.config(menu=menubar)

    def save_to_file(self):
        filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if filename:
            self.registration.save_to_file(filename)

    def load_from_file(self):
        filename = filedialog.askopenfilename(filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if filename:
            self.registration.load_from_file(filename)

    def create_register_tab(self):
        Label(self.register_frame, text="Student Name:").grid(row=0, column=0, padx=10, pady=5)
        self.student_name_entry = Entry(self.register_frame)
        self.student_name_entry.grid(row=0, column=1, padx=10, pady=5)

        Label(self.register_frame, text="Student ID:").grid(row=1, column=0, padx=10, pady=5)
        self.student_Id_entry = Entry(self.register_frame)
        self.student_Id_entry.grid(row=1, column=1, padx=10, pady=5)

        Label(self.register_frame, text="Phone Number:").grid(row=2, column=0, padx=10, pady=5)
        self.student_phonenumber_entry = Entry(self.register_frame)
        self.student_phonenumber_entry.grid(row=2, column=1, padx=10, pady=5)

        Label(self.register_frame, text="PC Name:").grid(row=3, column=0, padx=10, pady=5)  # Corrected column from 1 to 0
        self.pc_name_entry = Entry(self.register_frame)
        self.pc_name_entry.grid(row=3, column=1, padx=10, pady=5)

        Label(self.register_frame, text="PC Model:").grid(row=4, column=0, padx=10, pady=5)
        self.pc_model_entry = Entry(self.register_frame)
        self.pc_model_entry.grid(row=4, column=1, padx=10, pady=5)

        Label(self.register_frame, text="PC Serial:").grid(row=5, column=0, padx=10, pady=5)
        self.pc_serial_entry = Entry(self.register_frame)
        self.pc_serial_entry.grid(row=5, column=1, padx=10, pady=5)

        register_button = Button(self.register_frame, text="Register PC", command=self.register_pc)
        register_button.grid(row=6, column=0, columnspan=2, pady=10)


    def register_pc(self):
        student_name = self.student_name_entry.get()
        student_Id = self.student_Id_entry.get()
        student_phonenumber = self.student_phonenumber_entry.get()
        pc_name = self.pc_name_entry.get()
        pc_model = self.pc_model_entry.get()
        pc_serial = self.pc_serial_entry.get()

        pc = Pc(student_name, student_Id, student_phonenumber, pc_name, pc_model, pc_serial)
        self.registration.register_pc(pc)

    def create_display_tab(self):
        display_all_button = Button(self.display_frame, text="Display All PCs", command=self.display_all_pcs)
        display_all_button.pack(pady=20)

    def display_all_pcs(self):
        self.registration.display_registered_pcs()

    def create_search_tab(self):
        Label(self.search_frame, text="Search by PC Model:").grid(row=0, column=0, padx=10, pady=5)
        self.search_model_entry = Entry(self.search_frame)
        self.search_model_entry.grid(row=0, column=1, padx=10, pady=5)
        search_model_button = Button(self.search_frame, text="Search", command=self.search_by_model)
        search_model_button.grid(row=0, column=2, padx=10, pady=5)

        Label(self.search_frame, text="Search by PC Serial:").grid(row=1, column=0, padx=10, pady=5)
        self.search_serial_entry = Entry(self.search_frame)
        self.search_serial_entry.grid(row=1, column=1, padx=10, pady=5)
        search_serial_button = Button(self.search_frame, text="Search", command=self.search_by_serial)
        search_serial_button.grid(row=1, column=2, padx=10, pady=5)

        Label(self.search_frame, text="Search by Student ID:").grid(row=2, column=0, padx=10, pady=5)
        self.search_student_Id_entry = Entry(self.search_frame)
        self.search_student_Id_entry.grid(row=2, column=1, padx=10, pady=5)
        search_student_Id_button = Button(self.search_frame, text="Search", command=self.search_by_student_Id)
        search_student_Id_button.grid(row=2, column=2, padx=10, pady=5)

    def search_by_model(self):
        pc_model = self.search_model_entry.get()
        self.registration.search_by_model(pc_model)

    def search_by_serial(self):
        pc_serial = self.search_serial_entry.get()
        self.registration.search_by_serial(pc_serial)

    def search_by_student_Id(self):
        student_Id = self.search_student_Id_entry.get()
        self.registration.search_by_student_Id(student_Id)

    def create_delete_tab(self):
        Label(self.delete_frame, text="Delete by PC Model:").grid(row=0, column=0, padx=10, pady=5)
        self.delete_model_entry = Entry(self.delete_frame)
        self.delete_model_entry.grid(row=0, column=1, padx=10, pady=5)
        delete_model_button = Button(self.delete_frame, text="Delete", command=self.delete_by_model)
        delete_model_button.grid(row=0, column=2, padx=10, pady=5)

        Label(self.delete_frame, text="Delete by PC Serial:").grid(row=1, column=0, padx=10, pady=5)
        self.delete_serial_entry = Entry(self.delete_frame)
        self.delete_serial_entry.grid(row=1, column=1, padx=10, pady=5)
        delete_serial_button = Button(self.delete_frame, text="Delete", command=self.delete_by_serial)
        delete_serial_button.grid(row=1, column=2, padx=10, pady=5)

        Label(self.delete_frame, text="Delete by Student ID:").grid(row=2, column=0, padx=10, pady=5)
        self.delete_student_Id_entry = Entry(self.delete_frame)
        self.delete_student_Id_entry.grid(row=2, column=1, padx=10, pady=5)
        delete_student_Id_button = Button(self.delete_frame, text="Delete", command=self.delete_by_student_Id)
        delete_student_Id_button.grid(row=2, column=2, padx=10, pady=5)

    def delete_by_model(self):
        pc_model = self.delete_model_entry.get()
        self.registration.delete_by_model(pc_model)

    def delete_by_serial(self):
        pc_serial = self.delete_serial_entry.get()
        self.registration.delete_by_serial(pc_serial)

    def delete_by_student_Id(self):
        student_Id = self.delete_student_Id_entry.get()
        self.registration.delete_by_student_Id(student_Id)
            
    def save_to_file(self):
        filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if filename:
            self.registration.save_to_file(filename)

    def load_from_file(self):
        filename = filedialog.askopenfilename(filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if filename:
            self.registration.load_from_file(filename)

if __name__ == "__main__":
    registration = Registration()
    app = RegistrationApp(registration)
    app.mainloop()

