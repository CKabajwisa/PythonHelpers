# PythonHelpers

**Convert all PDF files in a specific location to CSV format using Tabula-py library using Python and creating an exe**
1.Install the tabula-py library using pip install tabula-py
2.tabula.convert_into() function and saves the output in the same directory with the same base name but a .csv extension
3.The output_format="csv" parameter specifies that the output should be in CSV format. The pages='all' parameter indicates that all pages of the PDF should be converted to CSV. The parameter can be modified to specific requirements g.g if 1-2 pages.

**step-by-step guide to creating an executable program with a configuration file using PyInstaller**
1.Install PyInstaller using pip install pyinstaller.
2. Create your Python script with the configuration file logic. For example,I have a script named convert_all.py
3. Create a configuration file (config.ini) in the same directory as your script.
4. Open a command prompt or terminal and navigate to the directory containing your script.
5. Use PyInstaller to create the executable by running the following command: pyinstaller --onefile convert_all.py
6. This command creates a single executable file (convert_all.exe on Windows) in the dist directory.
7.Copy the config.ini file to the dist directory, alongside the executable file.
8.Run the executable file, and it will use the configuration file in the same directory.

