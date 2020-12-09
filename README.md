Install Python:
1. Download https://github.com/pyenv-win/pyenv-win/archive/master.zip
2. Open archive and copy pyenv-win folder to path: C:\Users\CurrentUser\.pyenv\
 >> Ensure you see bin folder under C:\Users\CurrentUser\.pyenv\pyenv-win
3. Add PYENV to your Environment Variables using PowerShell: 
	[System.Environment]::SetEnvironmentVariable('PYENV',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
4. Add the following paths to your USER PATH variable in order to access the pyenv command
	[System.Environment]::SetEnvironmentVariable('path', $HOME + "\.pyenv\pyenv-win\bin;" + $HOME + "\.pyenv\pyenv-win\shims;" + $env:Path,"User")
5. Close and reopen your terminal app and run pyenv --version
6. Install python : 
	pyenv install 3.7.0
7. Set a python version as the global version: 
	pyenv global 3.7.0	
	
Local configuration and use:
1. Clone git repository and copy path (e.g. C:\Desktop\git)
2. In Command Promptrun command: cd C:\Desktop\git
3. Create "myenv" directory: mkdir myenv
4. Run command to create virtual environment in directory "myenv": python -m venv myenv
5. Activate virtual env: myenv\Scripts\activate.bat
6. Install packages using command: pip install -r requirements.txt
7. Check if Flask was installed: pip list
8. Run: python hw.py
9. Open url in browser: http://localhost:5000/api/v1/hello-world-29