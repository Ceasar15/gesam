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
![Home Page ](https://user-images.githubusercontent.com/42820626/156568578-a082c746-bdec-4d55-bdc0-98a7181b9561.png)
![Sermons Page](https://user-images.githubusercontent.com/42820626/156568622-77aad14e-857b-4f0d-bc00-81f19901ef38.png)
![Beliefs Page](https://user-images.githubusercontent.com/42820626/156568648-fc89ccce-f16d-4fdd-a662-16a6b55165d2.png)
![Payment Page ](https://user-images.githubusercontent.com/42820626/156568669-d900b9fd-d190-49bb-ba84-43712a0aad89.png)
![ContactUs Page](https://user-images.githubusercontent.com/42820626/156568697-78e184cb-dbce-4234-a449-15f56d83ff4c.png)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Project status
This project is not under development anymore. 
## License
[MIT](https://choosealicense.com/licenses/mit/)