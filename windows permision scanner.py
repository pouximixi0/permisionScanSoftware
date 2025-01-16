import os
import csv
import win32security
import win32con
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import threading
import sys 

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def get_permissions(path):
    try:
        sd = win32security.GetFileSecurity(path, win32security.DACL_SECURITY_INFORMATION)
        dacl = sd.GetSecurityDescriptorDacl()

        permissions = []
        for i in range(dacl.GetAceCount()):
            ace = dacl.GetAce(i)
            try:
                trustee = ace[2]
                access_mask = ace[1]
                user, domain, _ = win32security.LookupAccountSid(None, trustee)

                rights = []
                if access_mask & win32con.DELETE:
                    rights.append("DELETE")
                if access_mask & win32con.READ_CONTROL:
                    rights.append("READ_CONTROL")
                if access_mask & win32con.WRITE_DAC:
                    rights.append("WRITE_DAC")
                if access_mask & win32con.WRITE_OWNER:
                    rights.append("WRITE_OWNER")
                if access_mask & win32con.SYNCHRONIZE:
                    rights.append("SYNCHRONIZE")
                if access_mask & win32con.GENERIC_READ:
                    rights.append("GENERIC_READ")
                if access_mask & win32con.GENERIC_WRITE:
                    rights.append("GENERIC_WRITE")
                if access_mask & win32con.GENERIC_EXECUTE:
                    rights.append("GENERIC_EXECUTE")
                if access_mask & win32con.GENERIC_ALL:
                    rights.append("GENERIC_ALL")

                permissions.append(f"{domain}\\{user}: {' '.join(rights)}")
            except Exception as e:
                permissions.append(f"Erreur de permission pour l'ACE {i}: {str(e)}")

        if not permissions:
            permissions.append("Aucune permission disponible")
        return permissions
    except Exception as e:
        return [f"Erreur: {str(e)}"]

def list_files_and_folders(directory, progress_label, progress_bar, root, stop_event):
    file_info = []
    total_files = 0

    for root_dir, dirs, files in os.walk(directory):
        total_files += len(dirs) + len(files)

    progress_bar['maximum'] = total_files

    current_file = 0
    for root_dir, dirs, files in os.walk(directory):
        if stop_event.is_set():
            break

        for name in dirs + files:
            full_path = os.path.join(root_dir, name)
            permissions = get_permissions(full_path)
            current_file += 1

            progress_label.config(text=f"Scanning {current_file}/{total_files}")
            progress_bar['value'] = current_file
            root.update_idletasks()

            file_info.append([name, full_path, '; '.join(permissions)])

    return file_info

def save_to_csv(directory, output_file, progress_label, progress_bar, root, stop_event):
    file_info = list_files_and_folders(directory, progress_label, progress_bar, root, stop_event)

    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["Nom", "Chemin", "Permissions"])
        writer.writerows(file_info)

    messagebox.showinfo("Succès", f"Les informations ont été enregistrées dans {output_file}")

def select_directory():
    folder_selected = filedialog.askdirectory(title="Sélectionner un dossier à scanner")
    if folder_selected:
        entry_directory.delete(0, tk.END)
        entry_directory.insert(0, folder_selected)

def select_output_file():
    file_selected = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Fichiers CSV", "*.csv")])
    if file_selected:
        entry_output.delete(0, tk.END)
        entry_output.insert(0, file_selected)

def start_scan_thread():
    progress_label.config(text=f"Chargement ...")
    directory = entry_directory.get()
    output_file = entry_output.get()

    if not directory or not output_file:
        messagebox.showerror("Erreur", "Veuillez sélectionner un répertoire et un fichier de sortie.")
        return

    stop_event.clear()
    scan_thread = threading.Thread(target=scan_task, args=(directory, output_file))
    scan_thread.start()

def scan_task(directory, output_file):
    try:
        save_to_csv(directory, output_file, progress_label, progress_bar, root, stop_event)
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue : {str(e)}")

def stop_scan():
    stop_event.set()

root = tk.Tk()
icon_path = resource_path("logo.ico")
root.iconbitmap(icon_path)
root.title("Scanner de permissions de fichiers")
root.geometry("750x320")
root.configure(bg="#f7f7f7")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 12), background="#f7f7f7")
style.configure("TButton", font=("Arial", 12), padding=6)
style.configure("TEntry", font=("Arial", 12))
style.configure("TProgressbar", thickness=20)

label_directory = ttk.Label(root, text="Sélectionner un répertoire à scanner:")
label_directory.grid(row=0, column=0, padx=10, pady=10, sticky="w")

entry_directory = ttk.Entry(root, width=50)
entry_directory.grid(row=0, column=1, padx=10, pady=10)

button_directory = ttk.Button(root, text="Parcourir", command=select_directory)
button_directory.grid(row=0, column=2, padx=10, pady=10)

label_output = ttk.Label(root, text="Sélectionner un fichier CSV de sortie:")
label_output.grid(row=1, column=0, padx=10, pady=10, sticky="w")

entry_output = ttk.Entry(root, width=50)
entry_output.grid(row=1, column=1, padx=10, pady=10)

button_output = ttk.Button(root, text="Parcourir", command=select_output_file)
button_output.grid(row=1, column=2, padx=10, pady=10)

progress_label = ttk.Label(root, text="En attente...")
progress_label.grid(row=2, column=0, columnspan=3, pady=10)

progress_bar = ttk.Progressbar(root, orient='horizontal', length=400, mode='determinate')
progress_bar.grid(row=3, column=0, columnspan=3, pady=10)

button_start = ttk.Button(root, text="Démarrer le scan", command=start_scan_thread)
button_start.grid(row=4, column=0, columnspan=3, pady=10)

button_stop = ttk.Button(root, text="Arrêter le scan", command=stop_scan)
button_stop.grid(row=5, column=0, columnspan=3, pady=10)

stop_event = threading.Event()

root.mainloop()
