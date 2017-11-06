"""Main Free Hot Soup logic and point that is used to start the app."""
from flask import render_template, request, redirect, Response
# from models import app, db, User, Ticket, Place
from models import app, db, User, Ticket
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib import sqla
from forms import AddressForm
from flask_basicauth import BasicAuth
from werkzeug.exceptions import HTTPException
from flask.ext.admin.base import MenuLink, Admin, BaseView, expose

basic_auth = BasicAuth(app)
app.config['BASIC_AUTH_USERNAME'] = 'freehotsoup'
app.config['BASIC_AUTH_PASSWORD'] = 'SoupProvides123'

class ModelView(sqla.ModelView):
    def is_accessible(self):
        if not basic_auth.authenticate():
            raise AuthException('Not authenticated.')
        else:
            return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(basic_auth.challenge())

class AuthException(HTTPException):
    def __init__(self, message):
        super().__init__(message, Response(
            "You could not be authenticated. Please refresh the page.", 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}
        ))



# @app.route("/newrequest", methods=['POST', 'GET'])
# def newrequest():
#     """Create and show only request fields."""
#     if request.method == 'GET':
#         return render_template('new_request.html', title="New Ticket")
#     if request.method == 'POST':
#         item = request.form['item']
#         deliverer = ''

#         requester = request.form['requester']
#         dropoff_address = request.form['dropoff_address']
#         dropoff_time = request.form['dropoff_time']
#         dropoff_date = request.form['dropoff_date']

#         gyfter = ''
#         pickup_address = ''
#         pickup_time = ''
#         pickup_date = ''

#         ticket = Ticket(item, deliverer, gyfter, pickup_address,
#                         pickup_time, pickup_date, requester,
#                         dropoff_address, dropoff_time, dropoff_date)

#         db.session.add(ticket)
#         db.session.commit()
#         return render_template('show_request.html', ticket=ticket)


# @app.route("/newoffer", methods=['POST', 'GET'])
# def newoffer():
#     """Create and show only offer fields."""
#     if request.method == 'GET':
#         return render_template('new_offer.html', title="New Ticket")
#     if request.method == 'POST':
#         item = request.form['item']
#         deliverer = ''

#         gyfter = request.form['gyfter']
#         pickup_address = request.form['pickup_address']
#         pickup_time = request.form['pickup_time']
#         pickup_date = request.form['pickup_date']

#         requester = ''
#         dropoff_address = ''
#         dropoff_time = ''
#         dropoff_date = ''

#         ticket = Ticket(item, deliverer, gyfter, pickup_address,
#                         pickup_time, pickup_date, requester,
#                         dropoff_address, dropoff_time, dropoff_date)
#         db.session.add(ticket)
#         db.session.commit()
#         return render_template('show_offer.html', ticket=ticket)


# @app.route("/newticket", methods=['POST', 'GET'])
# def newticket(item='', deliverer='',
#               gyfter='', pickup_address='', pickup_time='', pickup_date='',
#               requester='', dropoff_address='', dropoff_time='',
#               dropoff_date=''):
#     """Render ticket form."""
#     if request.method == 'GET':
#         return render_template('new_ticket.html', title="New Ticket")
#     if request.method == 'POST':
#         # alternative store form fields in varibles & create new ticket object
#         item = request.form['item']
#         deliverer = request.form['deliverer']

#         gyfter = request.form['gyfter']
#         pickup_address = request.form['pickup_address']
#         pickup_time = request.form['pickup_time']
#         pickup_date = request.form['pickup_date']

#         requester = request.form['requester']
#         dropoff_address = request.form['dropoff_address']
#         dropoff_time = request.form['dropoff_time']
#         dropoff_date = request.form['dropoff_date']

#         ticket = Ticket(item, deliverer, gyfter, pickup_address,
#                         pickup_time, pickup_date, requester,
#                         dropoff_address, dropoff_time, dropoff_date)

#         db.session.add(ticket)
#         db.session.commit()

#         # map2 show
#         pickup_ll = geocoder.google(pickup_address)
#         dropoff_ll = geocoder.google(dropoff_address)

#         pickup_geoj = pickup_ll.geojson
#         dropoff_geoj = dropoff_ll.geojson

#         # complete address
#         pickup_address = pickup_geoj['properties']['address']
#         dropoff_address = dropoff_geoj['properties']['address']

#         p_lat, p_lng = pickup_ll.lat, pickup_ll.lng
#         d_lat, d_lng = dropoff_ll.lat, dropoff_ll.lng

#         coords_1 = (p_lat, p_lng)
#         coords_2 = (d_lat, d_lng)

#         dist = geopy.distance.vincenty(coords_1, coords_2).mi
#         dist = round(dist, 2)
#         dist = str(dist) + ' mi'

#         return render_template('map2.html',
#                                ticket=ticket,
#                                p_lat=p_lat, p_lng=p_lng,
#                                d_lat=d_lat, d_lng=d_lng,
#                                pickup_geoj=pickup_geoj,
#                                dropoff_geoj=dropoff_geoj, dist=dist)


@app.route("/addticket", methods=['POST', 'GET'])
def addticket(item='', deliverer='',
              gyfter='', pickup_address='',gyfter_phone='', pickup_time='', pickup_date='',delivery_options='',gyfter_comments='',
              requester='', dropoff_address='',requester_phone='', dropoff_time='',
              dropoff_date='',pickup_options='',requester_comments='', exchange_time='', exchange_date='', ticket_type = ''):
    """Stubbed out map and list view."""
    if request.method == 'GET':
        return render_template('addticket.html', title="New Ticket")  # , title=title)
    if request.method == 'POST':
        if request.form['formtype'] == "donation":
            print(request.form['formtype'])
            item = request.form['item']
            gyfter = request.form['name']
            # email = request.form['contactemail']
            pickup_address = request.form['location']
            gyfter_phone = request.form['phone']
            #pickup_time = request.form['time']
            #pickup_date = request.form['expiration']
            gyfter_comments = request.form['comments']
            ticket_type = request.form['formtype']
            delivery_options = request.form['delivery']
            if request.form['delivery'] == 'Can drop off':
                deliverer = gyfter
                dropoff_time = pickup_time
                dropoff_date = pickup_date
                pickup_time = ""
                pickup_date = ""

        elif request.form['formtype'] == "request":
            print(request.form['formtype'])
            item = request.form['item']
            requester = request.form['name']
            # email = request.form['contactemail']
            dropoff_address = request.form['location']
            requester_phone = request.form['phone']
            #dropoff_time = request.form['time']
            #dropoff_date = request.form['expiration']
            requester_comments = request.form['comments']
            ticket_type = request.form['formtype']
            pickup_options = request.form['pickup']
            if request.form['pickup'] == 'Can pick up':
                deliverer = requester
                pickup_time = dropoff_time
                pickup_date = dropoff_date
                dropoff_time = ""
                dropoff_date = ""

    ticket = Ticket(item, deliverer, gyfter, pickup_address,gyfter_phone,
                    pickup_time, pickup_date,delivery_options, gyfter_comments, requester,
                    dropoff_address,requester_phone, dropoff_time, dropoff_date,pickup_options, requester_comments, exchange_time, exchange_date, ticket_type)

    db.session.add(ticket)
    db.session.commit()
    # return render_template('show.html', ticket=ticket)
    
    ticket_id = str(ticket.tid)
    return redirect("view?tid=" + ticket_id)


# @app.route('/point_2_geojson', methods=['GET', 'POST'])
# def point_2_geojson():
#     """Return a string of the Point from geojson. Must be string returned."""
#     return str(Point((-122.67752, 45.51862))["coordinates"])
#     # >> [-122.67752, 45.51862]


# @app.route('/map2/<int:tid>', methods=['GET', 'POST'])
# def map2(tid):
#     """Map, list and sentence view for tickets using tid.

#     Get ticket id from url, use that to find the ticket
#     convert ticket addresses to geolocation and show them
#     and finally provide distance calulations.
#     """
#     tid = tid
#     ticket = Ticket.query.get(tid)
#     pickup_address = ticket.pickup_address
#     dropoff_address = ticket.dropoff_address

#     pickup_ll = geocoder.google(pickup_address)
#     dropoff_ll = geocoder.google(dropoff_address)

#     pickup_geoj = pickup_ll.geojson
#     dropoff_geoj = dropoff_ll.geojson

#     # complete address
#     pickup_address = pickup_geoj['properties']['address']
#     dropoff_address = dropoff_geoj['properties']['address']

#     p_lat, p_lng = pickup_ll.lat, pickup_ll.lng
#     d_lat, d_lng = dropoff_ll.lat, dropoff_ll.lng

#     coords_1 = (p_lat, p_lng)
#     coords_2 = (d_lat, d_lng)

#     dist = geopy.distance.vincenty(coords_1, coords_2).mi
#     dist = round(dist, 2)
#     dist = str(dist) + ' mi'

#     return render_template('map2.html',
#                            ticket=ticket,
#                            p_lat=p_lat, p_lng=p_lng,
#                            d_lat=d_lat, d_lng=d_lng,
#                            pickup_geoj=pickup_geoj,
#                            dropoff_geoj=dropoff_geoj, dist=dist)


# @app.route("/nearby/<int:tid>", methods=["GET", "POST"])
# def nearby(tid):
#     """Nearby uses flask_wtform and wikipedia apis.

#     Get the address, query for places around it
#     (currently wikipedia, may become locations of tickets),
#     return results.
#     """
#     tid = tid
#     ticket = Ticket.query.get(tid)
#     pickup_address = ticket.pickup_address
#     pickup_ll = geocoder.google(pickup_address)
#     p_lat, p_lng = pickup_ll.lat, pickup_ll.lng
#     form = AddressForm()
#     places = []
#     my_coordinates = (p_lat, p_lng)
#     lat_lng = (p_lat, p_lng)

#     if request.method == 'POST':
#         if form.validate() is False:
#             return render_template('nearby.html', form=form, tid=tid,
#                                    ticket=ticket)
#         else:
#             address = form.address.data
#             p = Place()
#             my_coordinates = p.address_to_latlng(address)
#             places = p.main(address)

#             return render_template('nearby.html', form=form, places=places,
#                                    my_coordinates=my_coordinates, tid=tid,
#                                    lat_lng=lat_lng, ticket=ticket)

#     elif request.method == 'GET':
#         return render_template("nearby.html", form=form, places=places,
#                                my_coordinates=my_coordinates, tid=tid,
#                                lat_lng=lat_lng, ticket=ticket)


@app.route("/")
def index():
    """Splash screen."""
    return render_template("index.html", title="Home")


@app.route("/about")
def about():
    """Mission statement."""
    return render_template("about.html", title="About")


# @app.route("/map")
# def map():
#     """Stubbed out map and list view."""
#     return render_template("map.html", title="Offerings")


# @app.route("/map")
# def map():
#     """Dynamic list view with stubbed out map and list view."""
#     if request.method == 'GET':
#         all_tickets = Ticket.query.all()
#         return render_template('map.html', all_tickets=all_tickets,
#                                title="Offerings")
#     if request.method == 'POST':
#         all_tickets = Ticket.query.all()
#         # ticket = Ticket.query.get(ticket_id)
#         return render_template('map.html', all_tickets=all_tickets,
#                                title="Offerings")


# @app.route("/all_requests", methods=['GET', 'POST'])
# def all_requests():
#     """Dynamic list view with stubbed out map and list view."""
#     if request.method == 'GET':
#         search_term = request.args.get('search_term')

#         all_tickets = Ticket.query.all()
#         if search_term:
#             # hard coded works if exact string
#             # filtered_tickets = Ticket.query
#             # .filter_by(item="11 coats assorted colors").all()

#             # general # must be exact string
#             filtered_tickets = Ticket.query.filter_by(item=search_term).all()

#             # TODO: impliment fuzzy search
#             return render_template('all_requests.html',
#                                    all_tickets=all_tickets,
#                                    title="Requests",
#                                    search_term=search_term,
#                                    filtered_tickets=filtered_tickets)
#         else:
#             all_tickets = Ticket.query.all()
#             return render_template('all_requests.html',
#                                    all_tickets=all_tickets,
#                                    title="Requests")

#     if request.method == 'POST':
#         all_tickets = Ticket.query.all()
#         # get query param and return...
#         search_term = request.args.get('search_term')
#         # return search_term
#         return render_template('all_requests.html', all_tickets=all_tickets,
#                                title="Requests", search_term=search_term)


# @app.route("/all_offers")
# def all_offers():
#     """Dynamic list view with stubbed out map and list view."""
#     if request.method == 'GET':
#         all_tickets = Ticket.query.all()
#         return render_template('all_offers.html', all_tickets=all_tickets,
#                                title="Offerings")
#     if request.method == 'POST':
#         # get query param and return...
#         search_term = request.args.get('search_term')
#         return render_template('all_offers.html', all_tickets=all_tickets,
#                                title="Offerings", search_term=search_term)
      

# @app.route('/clients/')
# @app.route('/clients')
# def clients():
#     """Client who use the Gyfted Platform."""
#     return render_template('clients.html', title="Clients")


@app.route("/show_all", methods=['GET', 'POST'])
def show_all():
    """Stubbed out show and list users view."""
    all_tickets = Ticket.query.all()
    return render_template('show_all.html', all_tickets=all_tickets, title="Tickets")


@app.route("/view", methods=['GET', 'POST'])
def status():
    """Stubbed out show and list users view."""
    ticket_id = request.args.get('tid')
    ticket_status = request.args.get('status.name')

    ticket = Ticket.query.get(ticket_id)
    ticket_action = request.args.get('action')
    # print("id: ", ticket_id, "status: ", ticket_status, "action: ", ticket_action)
    ticket = Ticket.query.get(ticket_id)

    # view ticket
    if ticket_id and not(ticket_status):
        return render_template("showticket.html", title="View Ticket", ticket=ticket)

    # display potential matchfound form
    if ticket_status.name == "New" and ticket_action:
        return render_template("status_change_matchfound.html", title="Edit Ticket", ticket=ticket)

    # change status from new to matchfound
    if ticket_status.name == "Match Found" and not ticket_action: 
        # retrieve form data
        if ticket.ticket_type == "donation":
            requester = request.form['requester']
            requester_phone = request.form['phone']
            pickup_address = request.form['location']
            pickup_options = request.form['pickup']
            requester_comments = request.form['response_comments']

        else:
            gyfter = request.form['gyfter']
            gyfter_phone = request.form['phone']
            delivery_address = request.form['location']
            delivery_options = request.form['delivery']
            gyfter_comments = request.form['response_comments']

        # update ticket in db
        if ticket.ticket_type == "donation":
            ticket.requester = requester
            ticket.requester_phone = requester_phone
            ticket.pickup_address = pickup_address
            ticket.pickup_options = pickup_options
            ticket.requester_comments = requester_comments

        else:
            ticket.gyfter = gyfter
            ticket.gyfter_phone = gyfter_phone
            ticket.delivery_address = delivery_address
            ticket.delivery_options = delivery_options
            ticket.gyfter_comments = gyfter_comments

        ticket.status = ticket_status
        db.session.commit()
        return redirect("view?tid=" + ticket_id)

    # # display add delivery instructions form
    # if ticket_status == "new" and ticket_action:
    #     return render_template("status_change_inprogress.html", title="Edit Ticket", ticket=ticket)

    # # change status from new to ready
    # if ticket_status == "ready" and not ticket_action: 

    #     # retrieve form data
    #     deliverer = request.form['deliverer']
    #     comments = request.form['comments']

    #     # update ticket in db
    #     ticket.deliverer = deliverer
    #     ticket.comments = comments

    #     if ticket.ticket_type == "donation" and ticket.delivery_options == "Needs picked up":

    #         # dropoff_address = request.form['dropoff_address']
    #         # dropoff_time = request.form['dropoff_time']
    #         # dropoff_date = request.form['dropoff_date']
    #         pickup_address = request.form['pickup_address']
    #         pickup_time = request.form['pickup_time']
    #         pickup_date = request.form['pickup_date']
    #         # update ticket in db
    #         # ticket.dropoff_address = dropoff_address
    #         # ticket.dropoff_time = dropoff_time
    #         # ticket.dropoff_date = dropoff_date
    #         ticket.pickup_address = pickup_address
    #         ticket.pickup_time = pickup_time
    #         ticket.pickup_date = pickup_date

    #     elif ticket_status == "ready" and not(ticket_action) and ticket.ticket_type == "donation" and ticket.delivery_options == "Can drop off":

    #         # retrieve form data
    #         dropoff_address = request.form['dropoff_address']
    #         dropoff_time = request.form['dropoff_time']
    #         dropoff_date = request.form['dropoff_date']
    #         # pickup_address = request.form['pickup_address']
    #         # pickup_time = request.form['pickup_time']
    #         # pickup_date = request.form['pickup_date']

    #         # update ticket in db
    #         ticket.dropoff_address = dropoff_address
    #         ticket.dropoff_time = dropoff_time
    #         ticket.dropoff_date = dropoff_date
    #         # ticket.pickup_address = pickup_address
    #         # ticket.pickup_time = pickup_time
    #         # ticket.pickup_date = pickup_date

    #     elif ticket_status == "ready" and not(ticket_action) and ticket.ticket_type == "request" and ticket.pickup_options == "Needs delivered":

    #         # retrieve form data
    #         dropoff_address = request.form['dropoff_address']
    #         dropoff_time = request.form['dropoff_time']
    #         dropoff_date = request.form['dropoff_date']
    #         # pickup_address = request.form['pickup_address']
    #         # pickup_time = request.form['pickup_time']
    #         # pickup_date = request.form['pickup_date']

    #         # update ticket in db
    #         ticket.dropoff_address = dropoff_address
    #         ticket.dropoff_time = dropoff_time
    #         ticket.dropoff_date = dropoff_date
    #         # ticket.pickup_address = pickup_address
    #         # ticket.pickup_time = pickup_time
    #         # ticket.pickup_date = pickup_date

    #     elif ticket_status == "ready" and not(ticket_action) and ticket.ticket_type == "request" and ticket.pickup_options == "Can pick up":

    #         # retrieve form data
    #         # dropoff_address = request.form['dropoff_address']
    #         # dropoff_time = request.form['dropoff_time']
    #         # dropoff_date = request.form['dropoff_date']
    #         pickup_address = request.form['pickup_address']
    #         pickup_time = request.form['pickup_time']
    #         pickup_date = request.form['pickup_date']

    #         # update ticket in db
    #         # ticket.dropoff_address = dropoff_address
    #         # ticket.dropoff_time = dropoff_time
    #         # ticket.dropoff_date = dropoff_date
    #         ticket.pickup_address = pickup_address
    #         ticket.pickup_time = pickup_time
    #         ticket.pickup_date = pickup_date

    #     ticket.status = ticket_status
    #     db.session.commit()
    #     return redirect("view?tid=" + ticket_id)

    # # display add delivery or pickup form
    # if ticket_status == "ready" and ticket_action:
    #     return render_template("status_closed.html", title="Edit Ticket", ticket=ticket)

    # # change status from ready to closed
    # if ticket_status == "closed":

    #     # # retrieve form data
    #     comments = request.form['comments']
    #     closed_details = request.form['closed_details']

    #     # # update ticket in db
    #     ticket.comments = comments
    #     ticket.closed_details = closed_details
    #     ticket.status = ticket_status
    #     db.session.commit()
    #     return redirect("view?tid=" + ticket_id)


# @app.route('/delete_ticket', methods=['GET', 'POST'])
# def delete_ticket():
#     """Hide ticket instead of removing from db.

#     grabs hidden ticket id from form, queries it and 'deletes' by hiding.
#     """
#     ticket_id = request.form['tid']  # WIP
#     hide_ticket = Ticket.query.get(ticket_id)

#     if not hide_ticket:
#         return redirect("/?error=Attempt to watch a ticket unknown to db")

#     hide_ticket.hidden = True
#     db.session.commit()
#     return redirect('/show_all')  # currently only


# disable browser caching
@app.after_request
def add_header(response):
    """Add headers to both force latest IE rendering engine or Chrome Frame.

    Also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


if __name__ == "__main__":
    # admin.add_view(ModelView(User, db.session))
    admin = Admin(app, name='Free Hot Soup', template_mode='bootstrap3')
    admin.add_view(ModelView(Ticket, db.session))
    admin.add_link(MenuLink(name='Back to Main Site', url='/'))
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
    app.debug = True
