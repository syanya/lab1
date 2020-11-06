1. Clone git repository and copy path (e.g. C:\Desktop\git)
2. In Command Promptrun command: cd C:\Desktop\git
3. Create "myenv" directory: mkdir myenv
4. Run command to create virtual environment in directory "myenv": python -m venv myenv
5. Activate virtual env: myenv\Scripts\activate.bat
6. Install packages using command: pip install -r requirements.txt
7. Check if Flask was installed: pip list
8. Run: python hw.py
9. Open url in browser: http://localhost:5000/api/v1/hello-world-29