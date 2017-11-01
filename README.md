# Free Hot Soup


### Setup
1. Mkdir Free Hot Soup
2. CD into Free Hot Soup
3. git init
4. git remote add origin https://github.com/freehotsoup/freehotsoup.git
5. git pull origin master
6. source activate flask-env
7. Download Postgres 10, installed with default options
http://postgresapp.com/
8. source activate flask-env
9. pip install -r requirements.txt
10. first run export DATABASE_URL=“postgresql://localhost/gyfted_dev”, afterwards DATABASE_URL=“postgresql://localhost/gyfted_dev”

### Setup in Windows/MySQL
1. Install MAMP for Windows
2. Open MAMP and click on Start servers
3. Open start page and go to Tools->phpMyAdmin
4. Create a new user and database with name gifted_dev and password gifted_password
5. In models.py, replace the database url to app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://gyfted_dev:gifted_password@localhost:8889/gyfted_dev'
6. In terminal, run
   python db_create.py
   python seed.py

### Brief
Free Hot Soup is a group that seeks to provide food to those who need it within the Portland metro area. The Free Hot app, which is coded in Python, will help the group manage food donations and requests. 


## Mission Statement

People need things.

Others have things

That they don’t want.

If someone needs a coat to stay alive

And to thrive

To improve their situation

And another happily offers it

How best to connect the two?


How do we exchange goods and services

Peer-to-peer while preserving

Safety, Anonymity and Integrity?

Provide a forum and create a space.

Should we use traditional methods

To solve these problems?

Only when they work best.


They already exist

And if they have not fulfilled the need

We must stretch ourselves

To accommodate the rest.

### Wireframes

__Wireframe 1__<br>
<img src="/docs/wireframes/20171004_192940.jpg" width="350" alt="wireframe1"><br>
__Wireframe 2__<br>
<img src="/docs/wireframes/discussion_02oct17.jpg" width="350" alt="wireframe2"><br>
__Wireframe 3__<br>
<img src="/docs/wireframes/sketch_08oct17 6.13.28 PM.jpg" width="350" alt="wireframe3"><br>
__Wireframe 4__<br>
PDF [Click to View](/docs/wireframes/donations_walkthrough.pdf)

