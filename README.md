
[![Build Status](https://travis-ci.com/dann254/city-temperature-api.svg?branch=master)](https://travis-ci.com/dann254/city-temperature-api)

# CITY TEMPERATURE - [API]

Know city temperature for a given city for a period of time.

## Relevant links

- [staging](https://city-temperature-api.herokuapp.com/locations/Herat/?days=1)

#Tade offs/ upgrades
- Api keys https://www.weatherapi.com/ don't work so I had to spend time finding another appropriate weather Api
- The weather API used requires city and country to be specified in request so a database of cities and their country was added.
- Some city names exist in multiple countries so users are directed to specify country i.e `/api/locations/London/?days=1&country=Canada`

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
- Create a **postgreSQL** database:
```bash
createdb city_temp_db
```
 *- follow appropriate tutorials for other DB managers*

- signup for an `API_KEY` here [https://www.weatherbit.io/](https://www.weatherbit.io/)

- Create a **.env** file in the project the directory (**city-temperature-api/api/**) with the following format.
```bash
  export CURRENT_ENV="development"
  export SECRET_KEY="your-secret-key"
  export API_KEY="weatherbit.io_api_key"
  export WEATHER_URL="https://api.weatherbit.io/v2.0/forecast/daily"
  export DB_URL="postgres:///cities"
```
- instructions for setting up `DB_URL` on other recomended DB managers are found [Here](https://github.com/jacobian/dj-database-url#url-schema).

- Run migrations from the project root directory to update the database
```bash
python manage.py migrate
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
