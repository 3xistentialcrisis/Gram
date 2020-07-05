# Insta Clone
## Author  
  
>[Wanjiku Karanja](https://github.com/3xistentialcrisis)  
  
# Description  
This is a Django clone of the photo-sharing application instagram. 
  
##  Live Link  
 Click [View Site](https://anothergram.herokuapp.com/)  to visit the site
  
## Screenshots 
###### Home page
 
<img src="https://raw.githubusercontent.com/3xistentialcrisis/Gram/master/static/images/landingpage.png" width="900px" height="440px">
 

 ###### Images
 <img src="https://raw.githubusercontent.com/3xistentialcrisis/Gram/master/static/images/gallery.png" width="900px" height="440px">

  ###### Image Details
 <img src="https://raw.githubusercontent.com/3xistentialcrisis/Gram/master/static/images/imagedetails.png" width="900px" height="440px">
 
## User Story  
This app enables user to:

* Sign in to the application to start using.
* Upload their pictures to the application.
* See their profile with all their pictures.
* Follow other users and see their pictures on their timeline.
* Like a picture and leave a comment on it. 

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/3xistentialcrisis/Gram/.git 
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Gram pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
python3 -m venv virtual 
```  
```bash 
source virtual/bin/activate 
```

##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrations 
 ```bash 
python manage.py makemigrations instagram
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python3 manage.py runserver 
``` 

##### Testing the application  
 ```bash 
 python3 manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python 3.8](https://www.python.org/)  
* [Django 1.11.17](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
* [Postgres](https://www.postgresql.org/)
* [Pip](https://pypi.org/project/pip/)
* Html and CSS (Bootstrap)
  
## Known Bugs  
There are no known bugs at the time of deployment of this application 
  
## CodeBeat
[![codebeat badge](https://codebeat.co/badges/61881488-2da3-4522-be01-0226f8d1a6c6)](https://codebeat.co/projects/github-com-3xistentialcrisis-gram-master) 

## License 
[![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/3xistentialcrisis/gram/blob/master/LICENSE)

## Contact Information   
If you have any question or contributions, please email the administrator at [administrator@gramclone.com] 
