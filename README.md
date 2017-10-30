# Gyfted
(pronounced gift-ed)

![Alt text](/static/images/G.jpg?raw=true "Gyfted")

### Setup
1. Mkdir Gyfted
2. CD into Gyfted
3. git init
4. git remote add origin https://github.com/freehotsoup/gyfted.git
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
We connect people needing items

With those who have them

And no longer need them.

For instance, If you need a coat or shoes

You request for them.

Please include your size/measurements whenever possible.

If both the item and a person are currently available

Our platform may fullfill your request.

Then you become gyfted.



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


And when you receive

You are Gyfted.

You now possess the knowledge

Someone loves you

Someone cares

That part of humanity

That tethers us

That believe that we will prevail

That part should not be in shorter supply

Than the demand demands.


So I ask:

Can we?

Yes.

Should we?

Yes.

Then all that is left is how.

We decided to call those who participate

“Requesters” and “Gyfters”

Once a request has been fulfilled

Requesters become “Gyfted”.

Service is the message loud and clear.

And I believe it will be

Felt stronger by this name.

One can carry with them

All throughout their days

That which they are Gyfted.

### Wireframes

__Wireframe 1__<br>
<img src="/docs/wireframes/20171004_192940.jpg" width="350" alt="wireframe1"><br>
__Wireframe 2__<br>
<img src="/docs/wireframes/discussion_02oct17.jpg" width="350" alt="wireframe2"><br>
__Wireframe 3__<br>
<img src="/docs/wireframes/sketch_08oct17 6.13.28 PM.jpg" width="350" alt="wireframe3"><br>
__Wireframe 4__<br>
PDF [Click to View](/docs/wireframes/donations_walkthrough.pdf)

