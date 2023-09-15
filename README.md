## End_to_end_ML_Project

### Software and account Requirements:

1. [Github Account](https://github.com/syedshahlal/End_to_end_ML_Project)
2. [Azure Account](https://portal.azure.com/#home)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/git)


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
To send version/changes to the github
```
git push origin main
```

To check remote URl from where the files will be pushed or pulled
```
git remote -v
```

To setup CI/CD pipeline in Heroku we need 3 informations:

1. HEROKU_EMAIL = sr.shahlal@gmail.com
2. HEROKU_API_Key = <>
3. HEROKU_APP_Name = ml-ete-app

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase

To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 b3bb833287a8
```

To check running container in docker
```
docker ps
```

To stop docker container
```
docker stop <container_id>
```
