from google.appengine.ext import ndb
###############################################################################################################
#
# DATASTORE - Kind classes
#
###############################################################################################################

# define an employee class
class Employee(ndb.Model):
	# Cloud Datastore assign a numeric ID automatically, omit the key_name argument:
	fname = ndb.StringProperty()
	lname = ndb.StringProperty()
	employee_creation_date = ndb.DateTimeProperty(auto_now_add=True)

# define an opportunity class
class Opportunity(ndb.Model):
	entity_creation_date = ndb.DateTimeProperty(auto_now_add=True)
	opp_start_date = ndb.StringProperty()
	company_name = ndb.StringProperty()
	unit_name = ndb.StringProperty()
	num_units = ndb.IntegerProperty()
	existing_customer = ndb.StringProperty()
	notes = ndb.TextProperty()


###############################################################################################################
#
# DATASTORE - Entity creation
#
###############################################################################################################


# <---------------EMPLOYEES------------------------------>

# create an employee
def create_employee(fname, lname):
	employee = Employee()
	# Cloud Datastore assign a numeric ID automatically since the keyword is omitted, omit the key_name argument:
	employee.fname = fname
	employee.lname = lname
	employee.put()



# <---------------OPPORTUNITIES-------------------------------------->

def create_opportunity_key(nickname):
    return ndb.Key('Employee', nickname)

# create an opportunity
def create_opportunity(nickname, company_name, opp_start_date, unit_name, num_units, existing_customer, notes):
	opportunity = Opportunity(parent = create_opportunity_key(nickname))
	# Cloud Datastore assign a numeric ID automatically since the keyword is omitted, omit the key_name argument:
	opportunity.company_name = company_name
	opportunity.opp_start_date = opp_start_date
	opportunity.unit_name = unit_name
	opportunity.num_units = num_units
	opportunity.existing_customer = existing_customer
	opportunity.notes = notes
	opportunity.put()


# edit an opportunity
def edit_opportunity(opp_id, nickname, company_name, opp_start_date, unit_name, num_units, existing_customer, notes):
	# get the key
	opp_key = ndb.Key('Opportunity', opp_id)
	# get the entry from the datastore
	opportunity = opp_key.get()
	# alter the parameters
	opportunity.company_name = company_name
	opportunity.opp_start_date = opp_start_date
	opportunity.unit_name = unit_name
	opportunity.num_units = num_units
	opportunity.existing_customer = existing_customer
	opportunity.notes = notes
	# save edits back to datastore
	opportunity.put()

