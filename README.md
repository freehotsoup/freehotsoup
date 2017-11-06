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

## FHS Mission Statement
Our goal is simple: to provide food to those who need it within the Portland metro area. For some, we exist as an alternative welcoming food resource to those who choose not to be affiliated with other existing resources for a variety of personal reasons. These are the suggested guidelines to make it easier for new participants to engage in the FHS mission. Service is generally provided near 9th & SW Salmon (in the NW corner of Director Park), however; some evenings FHS may serve as a mobile unit to address emergency needs during inclement weather. This is dependent upon the availability and resources of FHS volunteers and the larger FHS network. FHS members appreciate and recognize that people do what they can.

### Wireframes
__Wireframe 1__<br>
<img src="/docs/wireframes/20171004_192940.jpg" width="350" alt="wireframe1"><br>
__Wireframe 2__<br>
<img src="/docs/wireframes/discussion_02oct17.jpg" width="350" alt="wireframe2"><br>
__Wireframe 3__<br>
<img src="/docs/wireframes/sketch_08oct17 6.13.28 PM.jpg" width="350" alt="wireframe3"><br>
__Wireframe 4__<br>
PDF [Click to View](/docs/wireframes/donations_walkthrough.pdf)

