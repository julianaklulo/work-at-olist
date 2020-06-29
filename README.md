# Work at Olist

This repository contains an application for a library to store authors and book data. It's a REST API that can also be accessed through a web browseable API, developed using Python, Django and Django REST Framework.

The project is hosted on Heroku and available at: https://olist-teste.herokuapp.com

### Setup Instructions
1. Clone this repository
```bash
$ git clone https://github.com/julianaklulo/work-at-olist.git
```
2. Move into the folder
```bash
$ cd work-at-olist
```
3. Create .env file with SECRET_KEY
```bash
$ echo "SECRET_KEY='random_string'" > .env
```
4. Add connection string to a PostgreSQL database (local or web hosted) to .env file:
```bash
$ echo "DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME" >> .env
```
5. Create the virtualenv and install the dependencies
```bash
$ pipenv install
```
6. Activate the created virtualenv
```bash
$ pipenv shell
```
7. Migrate the database
```bash
$ python manage.py migrate
```
8. Start the server
```bash
$ python manage.py runserver
```

### Testing Instructions
The tests were written using `pytest`. To run, type
```bash
$ pytest
```

### API Documentation
Each book has a name, publication year, edition and a list of authors, and each author has a name.

The authors' data can also be imported into the database using a CSV file.

To import from file, create a .csv formatted as:
```
name
good_author
very_good_author
another_good_author

```

Then, run
```bash
$ python manage.py import_authors authors.csv
```

#### Endpoints for Authors

Method |  Endpoint  | Description
-------|------------|------------
POST | **/authors/** | Create an author on database. 
GET | **/authors/** | Return a list containing all authors' information (paginated, 10 authors per page).
GET | **/authors/?name=[** name_to_search **]** | Search for authors whose name contains the "name_to_search" string.
GET | **/authors/[** id **]/** | Retrieve information of the author with the specified id.
PATCH, PUT | **/authors/[** id **]/** | Update the author information with the specified id.
DELETE |  **/authors/[** id **]/** | Delete the author with the specified id.

Payload for POST:
```
{
    "name": // name of the author
}
```

#### Endpoints for Books

Method |  Endpoint  | Description
-------|------------|------------
POST | **/books/** | Create a book on database. 
GET | **/books/** | Return a list containing all books' information (paginated, 10 books per page).
GET | **/books/?name=[** name **]&publication_year=[** year **]&edition=[** edition **]&authors__name=[** author_name **]** | Search for books that match the query params.
GET | **/authors/[** id **]/** | Retrieve information of the author with the specified id.
PATCH, PUT |  **/books/[** id **]/** | Update the book information with the specified id.
DELETE |  **/books/[** id **]/** | Delete the book with the specified id.

Payload for POST:
```
 {
    "name": // Name of the book
    "edition": // Edition number
    "publication_year": // Publication year of the book
    "authors": // List of author ids
}
```


### Work environment
**Operating system:** Arch Linux

**IDE:** Visual Studio Code

**Python version:** 3.8.3

**Virtual environmnet:** pipenv

**Libraries:**
* Django
* Django REST Framework
* Pytest to write tests
* dj-database-url *to read database URL from env var*
* python-dotenv *to load env vars from .env file*

**DBMS:** PostgreSQL 12.3
