"""Seed some data."""

from models import db, Ticket, Status

#4 statuses
new_status = Status(name='New')
match_found_status = Status(name='Match Found')
in_progress_status = Status(name='In Progress')
closed_status = Status(name='Closed')



# full examples

t1 = Ticket(item='5 gallons of vegetable soup', deliverer='Bonnie', gyfter='Ashika',
            pickup_address='smith memorial union',gyfter_phone='1234567890', delivery_options='Needs picked up', requester='Eric',
            dropoff_address='pioneer courthouse square', requester_phone='0987654321',pickup_options='Needs delivered', gyfter_comments='New ticket comments...', requester_comments='Match Found ticket comments...', exchange_time='9am', exchange_date='11/12/17', ticket_type='donation')
t1.status = new_status

t2 = Ticket(item='11 coats assorted colors', deliverer='Michael',
            gyfter='Harrison', pickup_address='pioneer courthouse square',gyfter_phone='1234567890',
            delivery_options='Needs picked up', requester='Bonnie',
            dropoff_address='smith memorial union',requester_phone='0987654321', pickup_options='Needs delivered',gyfter_comments='New ticket comments...', requester_comments='Match Found ticket comments...', exchange_time='9am', exchange_date='11/12/17', ticket_type='donation')
t2.status = new_status

t3 = Ticket(item='3 pairs size 11 womens shoes', deliverer='Mary',
            gyfter='Michael',
            pickup_address='US Bank Tower, Southwest 4th Avenue, Portland, OR',gyfter_phone='1234567890',
            delivery_options='Needs picked up', requester='Melvin',
            dropoff_address='pioneer courthouse square',requester_phone='0987654321', pickup_options='Needs delivered', requester_comments='New ticket comments...', gyfter_comments='Match Found ticket comments...', exchange_time='9am', exchange_date='11/12/17', ticket_type='request')
t3.status = new_status

t4 = Ticket(item='Winter Hat', deliverer='Ashika',
            gyfter='Bonnie', pickup_address='The fields Park',gyfter_phone='1234567890',
            delivery_options='Needs picked up', requester='Ashika',
            dropoff_address='Providence Park',requester_phone='0987654321', pickup_options='Needs delivered', requester_comments='New ticket comments...', gyfter_comments='Match Found ticket comments...', exchange_time='9am', exchange_date='11/12/17', ticket_type='request')
t4.status = new_status

# examples with fields intentiallly left blank
t5 = Ticket(item='a nice warm mens winter coat black size large', deliverer='Sarah',
            gyfter='Pritiv', pickup_address='Clinton Street Theater',gyfter_phone='1234567890',
            delivery_options='Can drop off', requester='Elizabeth',
            dropoff_address='Smith Memorial Hall',requester_phone='0987654321', pickup_options='Needs delivered',gyfter_comments='New ticket comments...', requester_comments='Match Found ticket comments...', exchange_time='9am', exchange_date='11/12/17', ticket_type='donation')
t5.status = new_status

t6 = Ticket(item='a blue womens summer hat size medium', deliverer='Monica',
            gyfter='Mr. Harrison', pickup_address='The fields Park',gyfter_phone='1234567890',
            delivery_options='Can drop off', requester='Michael',
            dropoff_address='Providence Park',requester_phone='0987654321', pickup_options='Can pick up',gyfter_comments='New ticket comments...', requester_comments='Match Found ticket comments...', exchange_time='9am', exchange_date='11/12/17', ticket_type='donation')
t6.status = new_status

db.session.add(t1)
db.session.add(t2)
db.session.add(t3)
db.session.add(t4)
db.session.add(t5)
db.session.add(t6)
db.session.add(new_status)
db.session.add(match_found_status)
db.session.add(in_progress_status)
db.session.add(closed_status)

db.session.commit()
tickets = Ticket.query.all()
print(tickets)
