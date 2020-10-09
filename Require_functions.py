from agrostar_app import *
from models import *
from forms import *

ALLOWED_IMAGE_EXTENSIONS =  set(['jpg','png','jpeg'])
ALLOWED_VIDEO_EXTENSIONS = set(['mp4','gif','webm'])


##need to change
def count_cart_product():
	if 'logged_in' in session:
		return orders_details.query.filter(and_(orders_details.mobile_no==session['u_mb_no'],orders_details.is_ordered == int(0))).count()
	else:
		return None
		



def get_req_cookie():

	if request.cookies.get('logged_in') and request.cookies.get('mobile_no') and request.cookies.get('name') and request.cookies.get('s_type'):
		session['logged_in']=bool(request.cookies.get('logged_in'))
		session['u_mb_no']=request.cookies.get('mobile_no')
		session['s_name']=request.cookies.get('name')
		session['s_type']=request.cookies.get('s_type')

#for check whether file extensions allowed or not
def allowed_image_file(filename):
	return '.' in filename and \
	filename.rsplit('.',1)[1].lower() in ALLOWED_IMAGE_EXTENSIONS

#for check whether file extensions allowed or not
def allowed_video_file(filename):
	return '.' in filename and \
	filename.rsplit('.',1)[1].lower() in ALLOWED_VIDEO_EXTENSIONS

#for usertype to show/hide farming-info module
toggle=0

def is_logged_in(f):
	@wraps(f)
	def wrap(*args,**kwargs):
		if 'logged_in' in session:
			return f(*args,**kwargs)
		else:
			return redirect(url_for('login'))
	return wrap         

def not_logged_in(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return redirect(url_for('index'))
		else:

			return f(*args, **kwargs)
	return wrap



def is_agriculture_scientist(f):
	@wraps(f)
	def wrap(*args,**kwargs):
		if  session['s_type']=='Agriculture Scientist':

			return f(*args,**kwargs)
		else:
			flash('you are not authenticated user for use Upload-Research-info service','danger')
			return redirect(url_for('index'))   
	return wrap
	

def is_admin_logged_in(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'admin_logged_in' in session:
			return f(*args, **kwargs)
		else:
			return redirect(url_for('admin_login'))

	return wrap


def not_admin_logged_in(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'admin_logged_in' in session:
			return redirect(url_for('admin_dashboard'))
		else:
			return f(*args, **kwargs)

	return wrap


	


@app.context_processor
def override_url_for():
	return dict(url_for=dated_url_for)

def dated_url_for(endpoint,**values):
	if endpoint == 'static':
		filename=values.get('filename',None)
		if filename:
			file_path=os.path.join(app.root_path,endpoint,filename)
			values['q']=int(os.stat(file_path).st_mtime)

	return url_for(endpoint,**values)    


def populate_city_state(form):

	#queury for all city
	cities=city.query.all()
	states=state.query.all()
	city_names=[]

	for city_s in cities:
		city_names.append(city_s.city_name)

	city_choices = list(enumerate(city_names))  

	state_names=[]

	for state_s in states:
		state_names.append(state_s.state_name)

	state_choices = list(enumerate(state_names))

	form.user_city.choices=city_choices 
	form.user_state.choices=state_choices


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))


def unique_order_no_generator(instance=5):

	order_new_no= random_string_generator()
	order_no_exist = orders.query.filter(orders.order_no == order_new_no).first()
	if order_no_exist:
		return unique_order_no_generator()
	return order_new_no


def get_bot_response(usrText):
    bot = ChatBot('Bot',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        }
     

    ],
    trainer='chatterbot.trainers.ListTrainer')
    bot.set_trainer(ListTrainer)
    while True:
        if usrText.strip()!= 'Bye':
            result = bot.get_response(usrText)                        
            reply = str(result)
            return(reply)
        if usrText.strip() == 'Bye':
            return('Bye')
            break	
