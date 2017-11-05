"""Seed some data."""

from models import db, Ticket

# full examples
t1 = Ticket(item='13 hats assorted colors', deliverer='Bonnie', gyfter='Ashika',
            pickup_address='smith memorial union',gyfter_phone='', pickup_time='11am',
            pickup_date='11/11/17',delivery_options='Needs picked up', requester='Jason',
            dropoff_address='pioneer courthouse square', requester_phone='',dropoff_time='11pm',
            dropoff_date='11/11/17',pickup_options='Needs delivered', comments='No comments', ticket_type='donation')

t2 = Ticket(item='11 coats assorted colors', deliverer='Michael',
            gyfter='Jason', pickup_address='pioneer courthouse square',gyfter_phone='',
            pickup_time='9am', pickup_date='11/12/17',delivery_options='Needs picked up', requester='Ashika',
            dropoff_address='smith memorial union',requester_phone='', dropoff_time='11am',
            dropoff_date='11/12/17',pickup_options='Needs delivered',comments='No comments', ticket_type='donation')

t3 = Ticket(item='3 pairs size 11 womens shoes', deliverer='Jason',
            gyfter='Michael',
            pickup_address='US Bank Tower, Southwest 4th Avenue, Portland, OR',gyfter_phone='',
            pickup_time='11am', pickup_date='11/11/17',delivery_options='Needs picked up', requester='Jason',
            dropoff_address='pioneer courthouse square',requester_phone='', dropoff_time='11pm',
            dropoff_date='11/11/17',pickup_options='Needs delivered',comments='No comments', ticket_type='request')

t4 = Ticket(item='a partridge in a pear tree', deliverer='Ashika',
            gyfter='Bonnie', pickup_address='The fields Park',gyfter_phone='',
            pickup_time='9am', pickup_date='11/12/17',delivery_options='Needs picked up', requester='Ashika',
            dropoff_address='Providence Park',requester_phone='', dropoff_time='11am',
            dropoff_date='11/12/17',pickup_options='Needs delivered', comments='No comments', ticket_type='request')

# examples with fields intentiallly left blank
t5 = Ticket(item='a nice warm L mens winter coat black', deliverer='',
            gyfter='Jason', pickup_address='Clinton Street Theater',gyfter_phone='',
            pickup_time='10pm', pickup_date='12/12/17',delivery_options='Can drop off', requester='',
            dropoff_address='',requester_phone='', dropoff_time='',
            dropoff_date='',pickup_options='Needs delivered',comments='No comments', ticket_type='donation')

t6 = Ticket(item='a blue L mens tucker hat', deliverer='',
            gyfter='', pickup_address='The fields Park',gyfter_phone='',
            pickup_time='', pickup_date='',delivery_options='', requester='Michael',
            dropoff_address='Providence Park',requester_phone='', dropoff_time='8pm',
            dropoff_date='1/11/18',pickup_options='',comments='No comments', ticket_type='donation')

db.session.add(t1)
db.session.add(t2)
db.session.add(t3)
db.session.add(t4)
db.session.add(t5)
db.session.add(t6)
db.session.commit()
tickets = Ticket.query.all()
donated_by_jason = Ticket.query.filter_by(gyfter='Jason').first()

print(tickets)
print(donated_by_jason)
