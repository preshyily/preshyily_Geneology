

#### Task: Environment Setup
1. **Install Python 3.7.9 [done]:**
    
    - Download Python 3.7.9 from the official website: [Python 3.7.9 Download](https://www.python.org/downloads/release/python-379/) [done]
    - Follow the installation instructions for your operating system. [done]
    - Verify installation by running `python --version` in your terminal. [done]
		Check:
			C:\Windows\system32>python --version
			Python 3.7.9

1. **Install VSCode and Necessary Extensions:** [done]
    
    - Download and install Visual Studio Code from the official website: [VSCode Download](https://code.visualstudio.com/)
    - Install essential extensions:
        - Python by Microsoft [done]
        - Pylance by Microsoft [done]
        - GitLens — Git supercharged by GitKraken [done]

1. **Install Uncompyle6:**
    
    - Open a terminal and run: `pip install uncompyle6`
    - Verify installation by running `uncompyle6 --version`

1. **Configure VSCode Settings for The Sims 4 Modding:**
    
    - Open VSCode, press CTRL + Shift + P and search: 'python: Select Interpreter'.
    - Create a new virtual env named after mod
    - Configure Python path to point to newly created virtual env.
    - Adjust other settings as needed for a comfortable development environment.


#### Task: Mod Initialization
1. **Download Mod Folder Structure:[done]**
- Create a new folder for your mod project.
-  Download the [mod template](https://github.com/LuquanLi/TheSims4ScriptModBuilder) by Luquan Li
- Inside the [TheSims4ScriptModBuilder](https://github.com/LuquanLi/TheSims4ScriptModBuilder) folder, copy all subfolders and files: `src`, `util`, `.gitignore`, `LICENSE`, `README.md`, `compile.py`, `config.ini`, `decompile.py`.
- Paste in created Mod Folder.
2. **Add Configuration Files & Update The Sims 4  (`settings.py`):[done]**
- Create a `settings.py` file in the `src` folder to manage settings programmatically.
- Update The Sims 4 to latest version.
3. **Initialize a Git Repository for Version Control:**
- Download Git for Windows
- Open Git Bash and enter the following:
    ```bash
    $ git config --global user.name "username"
    $ git config --global user.email email@domain.com

    #verify changes
    $ git config --list
    ```
    
    **Option 1:**
    - Open a terminal in your mod project folder.
    - Run `git init` to initialize a Git repository.
    - Verify the `.gitignore` file was updated so that it can exclude unnecessary files from version control.
    - Commit the initial project structure.
    - Push initial changes.
    
    **Option 2:**
    - Open VSCode and click `Source Control` in left hand tab
    - Commit the initial project structure.
    - Enter Message in textbox above `Commit` button
    - Push initial changes. 

#### Task: Configuration Settings
1. **Set Up Paths in `config.ini`:[done]**
   - Define paths for the Sims 4 mod directory, game content directory, project directory, and Uncompyle directory. **Pay attention to the direction of the slashes**. 
    Config.ini:
     ```ini
        [Directory]
        #Default path for windows
        Sims4ModDir = C:\Users\msjac\OneDrive\Documents\Electronic Arts\The Sims 4\Mods
        Sims4GameContentDir = C:\Program Files (x86)\Steam\steamapps\common\The Sims 4
        ProjectDir = C:\Users\msjac\OneDrive\Documents\preshyily_Geneology
        GameContentPython = /Game/Bin/Python
        [Dependency]
        # For windows: where uncompyle6
        Uncompyle6Path = C:\Program Files\Python37\Scripts\uncompyle6.exe
        # Number of worker processes
        workers = 10
        # For windows: where uncompyle6
        Uncompyle6Path = C:\Program Files\Python37\Scripts\uncompyle6.exe
        # Number of worker processes
        workers = 10
     ```
   - Update the following lines in the constants.py file.
    Constants.py:
     ```python
     game_content_gameplay = game_content_dir + '\\Data\\Simulation\\Gameplay'

     project_game_zip_dir = project_dir + '\\game\\zip'
     project_game_unzip_dir = project_dir + '\\game\\unzip'
     project_game_decompile_dir = project_dir + '\\game\\decompile'
     project_game_python = '\\python'
     project_game_gameplay = '\\gameplay'
     project_build_dir = project_dir + '\\build'
     project_build_compile_dir = project_build_dir + '\\compile'
     project_src_dir = project_dir + '\\src'
     
     ```
   - Update the following lines in the decompile.py file. Do NOT select all, copy and paste this. Find the lines in the decompile.py file and change.
    decompile.py:
     ```python
        def unzip(src: string, dest: string):
            for file in os.listdir(src):
                if file.endswith('.zip'):
                    PyZipFile(src + '/' + file).extractall(dest + '\\' + file.title().split('.')[0].lower())




        def decompile_worker(args):
            dest_path, src_file = args

            dest_dir = os.path.dirname(dest_path)
            # Create the destination directory if it does not exist
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            print("Decompiling %s" % src_file)
            rv = run([uncompyle6, "-o", dest_dir, src_file], text=True,
                    capture_output=True)

            # Move the decompiled file to the correct location
            src_filename = os.path.basename(src_file).replace('.pyc', '.py')
            dest_file = os.path.join(dest_dir, src_filename)
            if os.path.exists(dest_file):
                shutil.move(os.path.join(dest_dir, src_filename), dest_path)


        def run_decompile():
            for folder in [project_game_unzip_dir + '\\' + x for x in os.listdir(project_game_unzip_dir)]:
                decompile(folder)




        src_file_path = str(os.path.join(root, filename))
        relative_path = str(Path(root).relative_to(project_game_unzip_dir))
        desc_path = project_game_decompile_dir + '\\' + relative_path



        target_file_name = filename.replace('.pyc', '.py')
        todo.append([desc_path + "\\" + target_file_name, src_file_path])

     ```


2. **Configure Mod-Specific Settings:[done]**
   - Add settings for mod name, version, author, etc., in `config.ini`.
   - Example:
     ```ini
     [User]
     UserName = username
     [Mod]
     Name = MySims4Mod
     Version = 1.0
     ```


3. **Decompile The SIms 4 python files via `config.ini`:[done]**
   - In VSCode right-click and run `decompile.py` or open cmd terminal in VSCode and type `python decompile.py`
   - Verify `game` folder has generated in Mod folder. 