
### Documentation pour l'installation et l'utilisation

----------

#### Partie 1 : Utilisation de l'EXE (pour les utilisateurs)

Si vous êtes un utilisateur final et souhaitez simplement exécuter l'application sans avoir besoin de gérer Python ou ses dépendances, vous pouvez télécharger l'EXE du projet et l'utiliser directement.

#### Prérequis

-   **Système d'exploitation :** Windows
-   **EXE :** Téléchargez simplement le fichier `.exe` qui a été compilé à partir du projet Python.

#### Étapes :

1.  **Téléchargez l'EXE** : Le fichier exécutable (`permission_scan.exe`) peut être téléchargé depuis le dépôt ou un lien fourni par le développeur.
    
2.  **Exécution de l'EXE** :
    
    -   Une fois le fichier téléchargé, vous pouvez simplement double-cliquer sur le fichier `permission_scan.exe` pour l'exécuter.
    -   L'interface graphique (GUI) de l'application s'ouvrira.
3.  **Sélectionner un répertoire à analyser** :
    
    -   L'application vous demandera de choisir un répertoire que vous souhaitez analyser pour ses permissions.
    -   Vous pouvez parcourir vos répertoires et sélectionner celui à analyser.
4.  **Sélectionner un fichier de sortie** :
    
    -   Après avoir choisi le répertoire, vous devrez sélectionner l'emplacement où vous souhaitez enregistrer le fichier CSV contenant les résultats du scan des permissions.
5.  **Lancer l'analyse** :
    
    -   Cliquez sur le bouton pour démarrer le scan. L'application analysera les permissions de chaque fichier et répertoire dans le dossier sélectionné.
    -   Une barre de progression vous indiquera l'état de l'analyse.
6.  **Obtenir les résultats** :
    
    -   Une fois l'analyse terminée, un message s'affichera pour vous indiquer que les résultats ont été enregistrés dans le fichier CSV sélectionné.

----------

#### Partie 2 : Pour les Développeurs (Installation et Compilation)

Si vous souhaitez développer, personnaliser ou compiler le projet vous-même, vous pouvez suivre ces étapes.

##### 1. **Installation des Dépendances Python**

Avant de pouvoir exécuter le script Python ou compiler l'application, vous devez installer les bibliothèques nécessaires.

Voici les étapes :

-   **Téléchargez ou clonez le projet** : Téléchargez les fichiers du projet dans un répertoire de votre choix.
    
-   **Installez les dépendances** : Ouvrez votre terminal (ou invite de commande) et installez les bibliothèques nécessaires en utilisant `pip`.

    `pip install pywin32`
   `pip install tk`
    
    Ces bibliothèques sont utilisées pour la gestion des permissions de fichiers sous Windows (`pywin32`) et pour l'interface graphique (`tkinter`).
    

##### 2. **Exécution du Script Python**

Une fois les dépendances installées, vous pouvez exécuter le script Python directement. Voici comment procéder :

1.  Ouvrez un terminal ou invite de commandes.
    
2.  Naviguez vers le répertoire contenant le fichier Python principal (par exemple, `test.py`).
    
3.  Exécutez le script avec la commande suivante :
    

    
    `python test.py` 
    

Cela ouvrira l'interface graphique du projet où vous pourrez choisir un répertoire à analyser et un fichier de sortie pour les résultats.

##### 3. **Compilation du Script en EXE**

Si vous souhaitez compiler le projet en un fichier exécutable `.exe` afin de le distribuer sans avoir besoin d'une installation Python, vous pouvez utiliser `PyInstaller`.

Voici les étapes pour compiler le projet en EXE :

1.  **Installez `PyInstaller`** :
  
    
    `pip install pyinstaller` 
    
2.  **Compilez le fichier Python** :
    
    Ouvrez un terminal ou une invite de commande, puis naviguez jusqu'au répertoire contenant le fichier Python (par exemple, `test.py`). Exécutez la commande suivante pour générer l'EXE :
    
    `pyinstaller --onefile --windowed --icon="logo.ico" --add-data="logo.ico;." test.py` 
    
    -   **`--onefile`** : Génère un fichier EXE unique.
    -   **`--windowed`** : Empêche l'ouverture d'une fenêtre de terminal lors de l'exécution de l'EXE.
    -   **`--icon="logo.ico"`** : Définit l'icône de l'application.
    -   **`--add-data="logo.ico;."`** : Ajoute le fichier `logo.ico` dans l'EXE.
3.  **Récupérer l'EXE** :
    
    Une fois la compilation terminée, vous trouverez le fichier `.exe` dans le dossier `dist` à l'intérieur de votre répertoire de travail. Ce fichier peut être exécuté directement sans avoir besoin de Python.
    

----------

#### 4. **Dépannage**

-   **Problèmes d'installation des dépendances** :
    
    -   Assurez-vous que vous avez une version de Python compatible (Python 3.6 ou supérieure).
        
    -   Si l'installation échoue, vérifiez que `pip` est à jour avec la commande suivante :
        

        
        `python -m pip install --upgrade pip` 
        
-   **Problèmes d'exécution de l'EXE** :
    
    -   Si l'EXE ne fonctionne pas, assurez-vous que les dépendances sont correctement incluses lors de la compilation avec `PyInstaller`.
    -   Vérifiez également que l'icône `logo.ico` est bien présente dans le répertoire du projet ou est incluse dans la compilation.







## 1. Importation des Modules

### Code :

    python
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

### Explication :

-   **`os`** : Ce module permet d'interagir avec le système de fichiers, ce qui inclut la navigation dans les répertoires et la gestion des chemins de fichiers (par exemple, créer, supprimer ou renommer des fichiers).
    
-   **`csv`** : Utilisé pour lire et écrire des fichiers CSV. Ici, il est utilisé pour générer un fichier de sortie contenant les informations sur les permissions des fichiers et répertoires analysés.
    
-   **`win32security` et `win32con`** : Ce module fait partie de la bibliothèque `pywin32`, permettant de manipuler la sécurité des fichiers sous Windows. `win32security` permet d'obtenir des informations de sécurité sur les fichiers, telles que les permissions d'accès, et `win32con` contient des constantes associées aux permissions de fichiers.
    
-   **`tkinter`** : Ce module est la bibliothèque standard pour créer des interfaces graphiques en Python. Il est utilisé pour afficher des fenêtres, des boutons, des champs de texte, des barres de progression, etc.
    
-   **`threading`** : Ce module permet de travailler avec des threads, permettant d'exécuter plusieurs tâches simultanément. Dans ce cas, il est utilisé pour effectuer l'analyse des fichiers dans un thread séparé, ce qui permet à l'interface graphique de rester réactive pendant l'exécution.
    
-   **`sys`** : Ce module permet d'interagir avec le système Python. Ici, il est utilisé pour gérer le chemin d'accès des ressources lorsque l'application est convertie en fichier EXE avec `PyInstaller` (par exemple, pour inclure des icônes ou des fichiers de ressources).
    

----------

## 2. Fonction `resource_path`

### Code :

python

CopierModifier

`def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)` 

### Explication :

Cette fonction permet d'obtenir le chemin absolu du fichier `logo.ico` (l'icône de l'application). Lorsque l'application est convertie en EXE avec `PyInstaller`, les ressources comme les icônes sont extraites dans un dossier temporaire (`_MEIPASS`). Cette fonction permet de trouver correctement les ressources, que le programme soit exécuté directement depuis le code source ou depuis l'exécutable compilé.

-   **`sys._MEIPASS`** : Cet attribut est spécifique à `PyInstaller` et représente le chemin temporaire où les fichiers sont extraits lors de l'exécution de l'EXE.
    
-   **`os.path.abspath(".")`** : Si le script n'a pas été compilé, cette ligne retourne le chemin actuel du répertoire du script.
    

----------

## 3. Fonction `get_permissions`

### Code :

python

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

### Explication :

Cette fonction prend en entrée un chemin de fichier ou de répertoire (`path`) et retourne une liste des permissions associées à ce fichier ou répertoire.

1.  **`win32security.GetFileSecurity()`** : Cette fonction récupère un objet de sécurité (`SD`) qui contient des informations sur les ACL (Access Control Lists - listes de contrôle d'accès).
    
2.  **`sd.GetSecurityDescriptorDacl()`** : Récupère la DACL (Discretionary Access Control List) associée au fichier ou répertoire. La DACL contient des ACE (Access Control Entries), qui définissent les permissions pour chaque utilisateur ou groupe.
    
3.  **Boucle `for` sur les ACE** : Pour chaque ACE, les permissions (masquées par des bits) sont extraites et ajoutées à la liste des permissions.
    
4.  **Vérification des permissions** : Chaque permission est vérifiée par des masques d'accès (par exemple, `win32con.DELETE`, `win32con.GENERIC_READ`, etc.). Si la permission est présente dans le masque, elle est ajoutée à la liste des droits de l'utilisateur.
    
5.  **Gestion des erreurs** : En cas d'erreur lors de l'extraction des permissions d'un ACE, un message d'erreur est ajouté.
    

----------

## 4. Fonction `list_files_and_folders`

### Code :

python

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

### Explication :

Cette fonction parcourt un répertoire donné et obtient les permissions de tous les fichiers et sous-répertoires.

1.  **`os.walk(directory)`** : Cette fonction permet de parcourir récursivement tous les fichiers et répertoires dans le répertoire spécifié.
    
2.  **Calcul du nombre total de fichiers** : Avant de commencer l'analyse, on calcule le nombre total de fichiers et répertoires dans le répertoire afin de mettre à jour la barre de progression.
    
3.  **Mise à jour de la barre de progression** : À chaque fichier ou répertoire scanné, la barre de progression est mise à jour pour informer l'utilisateur de l'état de l'analyse.
    
4.  **Gestion de l'annulation** : Si l'événement `stop_event` est activé (par exemple, si l'utilisateur annule l'analyse), l'analyse est arrêtée prématurément.
    
5.  **Ajout des informations** : Pour chaque fichier ou répertoire, le nom, le chemin complet et les permissions sont ajoutés à la liste `file_info`.
    

----------

## 5. Fonction `save_to_csv`

### Code :

python

    def save_to_csv(directory, output_file, progress_label, progress_bar, root, stop_event):
        file_info = list_files_and_folders(directory, progress_label, progress_bar, root, stop_event)
    
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(["Nom", "Chemin", "Permissions"])
            writer.writerows(file_info)
    
        messagebox.showinfo("Succès", f"Les informations ont été enregistrées dans {output_file}")

` 

### Explication :

Cette fonction enregistre les informations de fichiers et leurs permissions dans un fichier CSV.

1.  **Appel à `list_files_and_folders()`** : Cette fonction est appelée pour obtenir la liste des fichiers et leurs permissions avant de les écrire dans un fichier CSV.
    
2.  **Écriture dans un fichier CSV** : Le fichier de sortie est ouvert en mode écriture (`'w'`), et un objet `csv.writer` est utilisé pour écrire les lignes. Les données sont séparées par un point-virgule (`;`).
    
3.  **Message de confirmation** : Après l'enregistrement des informations, un message de succès est affiché pour informer l'utilisateur.
    

----------

## 6. Fonction `select_directory` et `select_output_file`

Ces fonctions permettent à l'utilisateur de sélectionner un répertoire à analyser et un fichier CSV de sortie via une interface graphique, en utilisant la bibliothèque `tkinter`.

----------

## 7. Fonction `start_scan_thread` et `scan_task`

Ces fonctions permettent de lancer le processus d'analyse dans un thread séparé, afin que l'interface graphique reste réactive pendant l'exécution.

----------

## 8. Interface Graphique (`Tkinter`)

Les lignes suivantes du code créent l'interface utilisateur avec `tkinter` :

### Code :

python


    root = tk.Tk()
    icon_path = resource_path("logo.ico")
    root.iconbitmap(icon_path)
    root.title("Scanner de permissions de fichiers")
    root.geometry("750x320")
    root.configure(bg="#f7f7f7")

### Explication :

-   **`tk.Tk()`** : Crée la fenêtre principale de l'application.
    
-   **`root.iconbitmap(icon_path)`** : Définit l'icône de l'application en utilisant le fichier `logo.ico`.
    
-   **`root.title()`** : Définit le titre de la fenêtre principale.
    
-   **`root.geometry()`** : Définit la taille de la fenêtre principale (750x320 pixels).
    
-   **`root.configure(bg="#f7f7f7")`** : Définit le fond de la fenêtre principale en utilisant une couleur grise claire (`#f7f7f7`).
