## End_to_end_ML_Project

### Software and account Requirements:

1. [Github Account](https://github.com/syedshahlal/End_to_end_ML_Project)
2. [Azure Account](https://portal.azure.com/#home)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)


Creating conda virtual environment
```
conda create -p venv python==3.11 -y
```
```
conda activate venv/
```

Create a ```requirements.txt``` file and add all the libraries required and install them
```
pip install -r requirements.txt
```

Now, we create the flask app file as ```app.py``` and write our code in it and then run the app
```
python app.py
```

To add file in the git repo
```
git add <filename>
```
or 
```
git add .
```
> Note: If there are some file in our folder that we do not want to track or do versioning then we add them to the ```.gitignore``` file

To check the git status
```
git status
```
To check all the versions maintained by git
```
git log
```

To create a new version/commit all the changes by git
```
git commit -m "your comment/message"
```