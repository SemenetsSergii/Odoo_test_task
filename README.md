# Odoo Persons Management Module

## Project Description

This project was created for a test task for the Odoo Fullstack Developer position. It includes the "Persons Management" module, which depends on the `website` module. The module has the following features:

- **Backend**: The `Persons` model stores information about first name, last name, age, gender, birthdate, and company. You can create and edit records using forms.
- **Frontend**: There is a controller that shows the 5 latest records from the `Persons` model on a webpage. The records are displayed as cards with full name, gender, age, and company.
- **Web Client**: A form is added to the website to create new records.

## Requirements

To run this project, you need the following:

- Odoo 16
- Python 3.8 or newer
- PostgreSQL
- Dependency management tools (pip)

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/persons_management.git
cd persons_management
```

## 2. Install dependencies
If you are using a virtual environment, activate it and install the dependencies:
```bash
pip install -r requirements.txt
```

## 3. Set up PostgreSQL using Docker

3.1 Pull the official PostgreSQL Docker image
If you haven't already pulled the PostgreSQL image, run:

```bash
docker pull postgres
```
3.2 Run the PostgreSQL container
Start a new PostgreSQL container with a specified database, user, and password:
Edit the odoo.conf file to add the database connection:
```bash
docker run --name odoo-postgres -e POSTGRES_DB=odoo_test -e POSTGRES_USER=odoo_user -e POSTGRES_PASSWORD=your_password -p 5432:5432 -d postgres
```
Explanation of the options:

- --name odoo-postgres: The name of your PostgreSQL container.
- -e POSTGRES_DB=odoo_test: The name of the database.
- -e POSTGRES_USER=odoo_user: The PostgreSQL username.
- -e POSTGRES_PASSWORD=your_password: The password for the PostgreSQL user.
- -p 5432:5432: This exposes the PostgreSQL port (5432) to your local machine.
- -d: Runs the container in detached mode (in the background).

3.3 Verify the running PostgreSQL container
To check if the container is running, use:

```bash
docker ps
```
You should see the odoo-postgres container listed.

3.4 Connect to the PostgreSQL container
If you need to manually access the PostgreSQL database inside the Docker container, run:
```bash
docker exec -it odoo-postgres psql -U odoo_user -d odoo_test.
```

## 4. Configure Odoo to connect to PostgreSQL
In your odoo.conf file, set the connection to the PostgreSQL database inside the Docker container:
```bash
[options]
addons_path = addons
db_host = localhost
db_port = 5432
db_user = odoo_user
db_password = your_password
db_name = odoo_test
```

## 5. Start Odoo
Once PostgreSQL is running in Docker and you've set up the connection in your odoo.conf, start Odoo by running:

```bash
./odoo-bin -c odoo.conf
```

Open your browser and go to http://localhost:8069. If necessary, create a new database.


## 6. Install the Module
- Log in to Odoo as an administrator.
- Go to the "Apps" menu and update the app list.
- Find the "Persons Management" module and install it.

## Usage
- **Backend**: A new menu item under "Website" will appear for managing persons (Persons). You can add, edit, and delete records.
- **Frontend**: Navigate to /persons to view the five latest records. You can also add new records using the form on the website.

## Additional Information
- Odoo Documentation: https://www.odoo.com/documentation/16.0/
- Odoo Official Repository: https://github.com/odoo/odoo

### If you have any questions or suggestions, feel free to contact me via GitHub or email.
