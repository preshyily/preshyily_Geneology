

#### Task: Environment Setup

**Priority:** P1  
**Sprint:** 1  
**Due Date:** [Insert Due Date]

**Description:** Set up the development environment using VSCode and install necessary tools.

**Requirements:**

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
    
    - Open a terminal and run `pip install uncompyle6`
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
- Open Git Bash and enter the followig:
    ``` 
    $ git config --global user.name "username"
    $ git config --global user.email email@domain.com

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
