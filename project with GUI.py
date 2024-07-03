from tkinter import*
from tkinter import messagebox, simpledialog, ttk

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
        result_window = Tk.Toplevel()
        result_window.title("Search Results")
        text = Tk.Text(result_window)
        text.insert(Tk.END, result)
        text.pack(expand=True, fill=Tk.BOTH)
        button = Tk.Button(result_window, text="Close", command=result_window.destroy)
        button.pack()

class RegistrationApp(Tk.Tk):
    def __init__(self, registration):
        super().__init__()
        self.registration = registration
        self.title("Debre Birhan University PC Registration")
        self.geometry("600x400")

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

        self.notebook.pack(expand=True, fill=Tk.BOTH)

    def create_register_tab(self):
        Tk.Label(self.register_frame, text="Student Name:").grid(row=0, column=0, padx=10, pady=5)
        self.student_name_entry = Tk.Entry(self.register_frame)
        self.student_name_entry.grid(row=0, column=1, padx=10, pady=5)

        Tk.Label(self.register_frame, text="Student ID:").grid(row=1, column=0, padx=10, pady=5)
        self.student_Id_entry = Tk.Entry(self.register_frame)
        self.student_Id_entry.grid(row=1, column=1, padx=10, pady=5)

        Tk.Label(self.register_frame, text="Phone Number:").grid(row=2, column=0, padx=10, pady=5)
        self.student_phonenumber_entry = Tk.Entry(self.register_frame)
        self.student_phonenumber_entry.grid(row=2, column=1, padx=10, pady=5)

        Tk.Label(self.register_frame, text="PC Name:").grid(row=3, column=0, padx=10, pady=5)
        self.pc_name_entry = Tk.Entry(self.register_frame)
        self.pc_name_entry.grid(row=3, column=1, padx=10, pady=5)

        Tk.Label(self.register_frame, text="PC Model:").grid(row=4, column=0, padx=10, pady=5)
        self.pc_model_entry = Tk.Entry(self.register_frame)
        self.pc_model_entry.grid(row=4, column=1, padx=10, pady=5)

        Tk.Label(self.register_frame, text="Serial Number:").grid(row=5, column=0, padx=10, pady=5)
        self.pc_serial_entry = Tk.Entry(self.register_frame)
        self.pc_serial_entry.grid(row=5, column=1, padx=10, pady=5)

        self.register_button = Tk.Button(self.register_frame, text="Register", command=self.register_pc)
        self.register_button.grid(row=6, columnspan=2, pady=10)

    def create_display_tab(self):
        self.display_button = Tk.Button(self.display_frame, text="Display All PCs", command=self.registration.display_registered_pcs)
        self.display_button.pack(pady=10)

    def create_search_tab(self):
        Tk.Label(self.search_frame, text="Search by:").grid(row=0, columnspan=2, pady=10)
        
        self.search_by_model_button = Tk.Button(self.search_frame, text="PC Model", command=self.search_by_model)
        self.search_by_model_button.grid(row=1, column=0, padx=10, pady=5)

        self.search_by_serial_button = Tk.Button(self.search_frame, text="PC Serial", command=self.search_by_serial)
        self.search_by_serial_button.grid(row=1, column=1, padx=10, pady=5)

        self.search_by_student_id_button = Tk.Button(self.search_frame, text="Student ID", command=self.search_by_student_id)
        self.search_by_student_id_button.grid(row=2, column=0, columnspan=2, pady=5)

    def create_delete_tab(self):
        Tk.Label(self.delete_frame, text="Delete by:").grid(row=0, columnspan=2, pady=10)

        self.delete_by_serial_button = Tk.Button(self.delete_frame, text="PC Serial", command=self.delete_by_serial)
        self.delete_by_serial_button.grid(row=1, column=0, padx=10, pady=5)

        self.delete_by_model_button = Tk.Button(self.delete_frame, text="PC Model", command=self.delete_by_model)
        self.delete_by_model_button.grid(row=1, column=1, padx=10, pady=5)

        self.delete_by_student_id_button = Tk.Button(self.delete_frame, text="Student ID", command=self.delete_by_student_id)
        self.delete_by_student_id_button.grid(row=2, column=0, columnspan=2, pady=5)

    def register_pc(self):
        student_name = self.student_name_entry.get()
        student_Id = self.student_Id_entry.get()
        student_phonenumber = self.student_phonenumber_entry.get()
        pc_name = self.pc_name_entry.get()
        pc_model = self.pc_model_entry.get()
        pc_serial = self.pc_serial_entry.get()

        if student_name and student_Id and student_phonenumber and pc_name and pc_model and pc_serial:
            pc = Pc(student_name, student_Id, student_phonenumber, pc_name, pc_model, pc_serial)
            self.registration.register_pc(pc)
            self.clear_entries()
        else:
            messagebox.showerror("Error", "All fields are required.")

    def search_by_model(self):
        pc_model = simpledialog.askstring("Search by PC Model", "Enter PC Model:")
        if pc_model:
            self.registration.search_by_model(pc_model)

    def search_by_serial(self):
        pc_serial = simpledialog.askstring("Search by PC Serial", "Enter PC Serial Number:")
        if pc_serial:
            self.registration.search_by_serial(pc_serial)

    def search_by_student_id(self):
        student_Id = simpledialog.askstring("Search by Student ID", "Enter Student ID:")
        if student_Id:
            self.registration.search_by_student_Id(student_Id)

    def delete_by_serial(self):
        pc_serial = simpledialog.askstring("Delete by PC Serial", "Enter PC Serial Number:")
        if pc_serial:
            self.registration.delete_by_serial(pc_serial)

    def delete_by_model(self):
        pc_model = simpledialog.askstring("Delete by PC Model", "Enter PC Model:")
        if pc_model:
            self.registration.delete_by_model(pc_model)

    def delete_by_student_id(self):
        student_Id = simpledialog.askstring("Delete by Student ID", "Enter Student ID:")
        if student_Id:
            self.registration.delete_by_student_Id(student_Id)

    def clear_entries(self):
        self.student_name_entry.delete(0, Tk.END)
        self.student_Id_entry.delete(0, Tk.END)
        self.student_phonenumber_entry.delete(0, Tk.END)
        self.pc_name_entry.delete(0, Tk.END)
        self.pc_model_entry.delete(0, Tk.END)
        self.pc_serial_entry.delete(0, Tk.END)

def main():
    registration = Registration()
    app = RegistrationApp(registration)
    app.mainloop()

if __name__ == "__main__":
    main()