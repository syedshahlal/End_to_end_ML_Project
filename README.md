## End_to_end_ML_Project

### 1. Software and account Requirements:

1. [Github Account](https://github.com/syedshahlal/End_to_end_ML_Project)
2. [Azure Account](https://portal.azure.com/#home)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/git)


### 2. Creating conda virtual environment
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

### 3. Github connections for push and pull
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

### 4. Setting up CI/CD Pipelines
To setup CI/CD pipeline in Heroku we need 3 informations:

1. HEROKU_EMAIL = sr.shahlal@gmail.com
2. HEROKU_API_Key = <>
3. HEROKU_APP_Name = ml-ete-app

#### BUILD DOCKER IMAGE
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

### 5. Building CI/CD Pipelines in Heroku APP

1. Create a ```.github``` folder and inside the folder add another folder ```workflows``` in this workflows folder create a file ```main.yaml```
2. ```main.yaml``` file write the github action flow
3. push the change to the git repo
4. open the repo in github and go to setting/secrets/actions and create New repository secret for all the secrets that has been mentioned in the ```main.yaml``` file and save them
    > Note: That the ```Name*``` and ```Secret*``` is same as mentioned
5. once this is done our deployment will take place automatically which we can see in the actions tab in github repo

Now whenever there is any push to the repo it will automatically tigger the deployment in the heroku web app

### 6. Files and Folder creation for structuring the project 
Moving ahead we will add a ```setup.py``` file and a folder ```housing``` that we'll contain a file inside it which has to be created as ```__init__.py```

Now we will write the setup coed in our ```setup.py``` file and run it 
```
python setup.py install
```
 >Note: this will generate ```build``` , ```dist``` and ```housing_predictor.egg-info``` based on what values we have passed in the ```setup.py```

I have created a ```create_folders.py``` file which has a list of folder we want to create once we run that file it will automatically created all the folders that we want to create under ```housing``` folder.