
# CITY TEMPERATURE - [API]

Know city temperature for a given city for a period of time.

## How to set up
- Make sure you have **python3** installed.
- Install **virtualenv** and **virtualenvwrapper** or use suitable alternatives to create a virtual environment.
 - using virtualenvwrapper:
```
$ mkvirtualenv city-temp
$ workon city-temp
```
- Clone this repository:
```bash
git clone git@github.com:dann254/city-temperature-api.git
```
- switch to the project folder:
```bash
cd city-temperature-api
```
- install requirements:
```bash
pip install -r requirements.txt
```


- Create a **.env** file in the project the directory (**city-temperature-api/api/**) with the following format.
```bash
  export CURRENT_ENV="development"
  export SECRET_KEY="your-secret-key"
```

- To start the app, run:
```bash
python manage.py runserver
```
- All set up, you can now use the url  **http://127.0.0.1:8000/** to access the app from your development server. 🤗

- The API docs and relevant endpoints will be availabe in GIU by accessing the URL on a browser.


- #### running tests
  After setting up your development environment
  - run tests using the following command:
  ```bash
  ./manage.py test
  ```
