# cal2rednotebook

Were you using the built-in calendar.exe from Microsoft Windows 3.1 in to the old days? Maybe you wrote your diary or notes remember important events? If yes, you may noticed that there is no easy way to export your data due to proprietary binary file format of the software. Unfortunately there were no newer versions and the old calendar.exe is hard to run on the newest computers as it is a 16-bit software.

With this script you will be able to save your valuabel data and convert it to the open RedNotebook file format. [See more about Rednotebook here](https://rednotebook.sourceforge.io/). The result is in fact series of plain txt files which is easy to parse and import to other softwares.

# Usage

1. Install python 3.4 (or newer) if it is not installed yet.
2. Copy all the calendar files (\*.cal) you want to convert into a folder
3. Copy the convert.py script into the same folder.
4. Run the script. All cal files will be converted into txt files in the same folder. Check the script output if error happens.
5. Copy all the generated txt files into your Rednotebook calendar folder and restart Rednotebook.

# Known issues

- Only text is copied per day basis.
- Special charachters may cause issues when starting Rednotebook - in that case you have to replace them manually in the converted text.


