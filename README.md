# GESAM Website
This is a website for campus church that relays sermons and teachings to its members. It takes feedback from its contact section and keeps track of cheuch members.Members can pay for offering through the offering section using PAystack's API. 

This is was built with Python, Django, HTML5, CSS3, PostgreSQL, PaystackAPI

## Installation

Clone the repository, run the virtual environment and install all requirements.
```bash
git clone https://github.com/Ceasar15/finances.git
pip install virtualenv
virtualenv venv
source venv/Scripts/activate
pip install requirements.txt
```
Run migrations commands and manage.py to start the development server.

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```


## Preview
You can access the live application here.
[Live Preview](http://gesam.herokuapp.com/)

## Visuals

```image 1
![Screenshot](screenshot.png)
![plot](./directory_1/directory_2/.../directory_n/plot.png)
![Alt text](relative/path/to/img.jpg?raw=true "Title")
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Project status
This project is not under development anymore. 
## License
[MIT](https://choosealicense.com/licenses/mit/)