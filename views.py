from agrostar_app import *
from models import *
from forms import *
from Require_functions import *

@app.route('/signup',methods=['POST','GET'])
@not_logged_in
def signup():
	get_req_cookie()
	form=Signup(request.form)
	populate_city_state(form)
  
	if request.method == 'POST' and form.validate():
		u_mobile_no=int(form.user_mobile_no.data)
		otp_input=int(form.user_otp.data)
		u_type=form.user_type.data
		u_profile=str('Farmer.jpg')
		u_full_name=form.user_full_name.data
		u_password=sha256_crypt.hash(str(form.user_password.data))
		u_city_id=int(form.user_city.data)
		user_address=form.user_address.data
		user_reg_already_check=users.query.get(u_mobile_no)
		if user_reg_already_check is None:

			de_mo_bo,de_otp=Secure_Data.decrypt(str(request.cookies.get('otp_mo_no')),str(request.cookies.get('OTP'))) #have cookie ma store thayela mobile no and otp ne decrypt karse
			print(de_mo_bo)
			print(de_otp)

			if de_mo_bo and de_otp: # a check karse cookie mathi get karela mobile_no and otp none nthi ne

				if int(de_mo_bo) == u_mobile_no and int(de_otp) == otp_input: # check karse user e nakhel mobile_no and otp cookie mathi get karine decrypt karel mobile_no and otp match thai che 

					try:
						user_data=users(user_mobile_no=u_mobile_no,user_type=u_type,user_profile=u_profile,user_full_name=u_full_name,user_password=u_password,user_city_id=u_city_id,user_address=user_address)
						print(user_data)
						db.session.add(user_data)   
					except IntegrityError:  
						session.rollback()
					else:   
						db.session.commit()
					
					flash('Register successfully.Now you can Login','success')
					return redirect(url_for('login'))
				else: # jo nai to a part ma jase 
					flash('Invalid OTP ','danger')
					render_template('SignUp.html',form=form,cart_count=count_cart_product())
			else: # jo none hase to a else part ma jase
				flash('Your OTP is expired. please resend an OTP. ','danger')
				render_template('SignUp.html',form=form,cart_count=count_cart_product())
					
				
		else:
			flash( str(u_mobile_no) + ' mobile no. is already used please try another mobile no.','danger')
			render_template('SignUp.html',form=form,cart_count=count_cart_product())
	return render_template('SignUp.html',form=form,cart_count=count_cart_product())


URL = 'http://www.way2sms.com/api/v1/sendCampaign'

# post request
def sendPostRequest(reqUrl, apiKey, secretKey, useType,phoneNo, senderId,textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)

# get response

"""
  Note:-
	you must provide apikey, secretkey, usetype and senderid values
	and then requst to api
"""
# print response if you want






#a route ajax ni madad thi call thase pun hu tane html+ajax no part send nthi karto karan ke tare khali cookie+encrypt_otp ni jaroor che. 
@app.route('/signup/sendotp',methods=['GET','POST'])
@not_logged_in
def send_otp():

	u_mobile_no=request.form['user_mobile_no']

	if u_mobile_no:
		n_mo=u_mobile_no
		digits = "0123456789"
		OTP = "" 
		check_already_exist=users.query.get(int(n_mo))
		if check_already_exist is None:
			for i in range(4) :
				 OTP += digits[math.floor(random.random() * 10)]
	  
			message_user="your otp is :" + OTP + '\nCode Valid For 5 minutes \nby AG-STAR'
			response = sendPostRequest(URL, app.config['WAY2SMS_APIKEY'], app.config['WAY2SMS_SECRETKEY'], 'stage', u_mobile_no, 'AS-007',str(message_user))    
			print(response.text)
			# for set cookie

			res = make_response("Cookie is set") #create object for setcookie in make_response any name or any template you want to render
			en_mo_bo,en_OTP=Secure_Data.encrypt(u_mobile_no,OTP) #use for encrypt mobileno and otp
			print(en_mo_bo)
			print(en_OTP)
			res.set_cookie('otp_mo_no',en_mo_bo,max_age=300) #encrypted mobile no store in cookie
			res.set_cookie('OTP', en_OTP, max_age=300) #same as above
			return res #return cookie object 
			#over set cookie
		else:
			return jsonify({'error':'this number is already used please another use mobile no.'})

	return jsonify({'error':'missing data!!!'})
	
	










@app.route('/',methods=['GET','POST'])
def index():
	get_req_cookie()
	form=Contact_us(request.form)
	get_trending_products=db.session.query(products.product_id,products.product_img,products.product_name,products.product_price)\
	.join(orders_details.orders)\
	.filter(and_(orders_details.is_ordered == int(1),orders_details.is_cancelled == int(0) ,orders_details.product_id == products.product_id ,orders.order_status == 'Completed' ) )\
	.order_by(orders_details.product_id.desc()).distinct().all()



	if request.method == 'POST' and form.validate():
		c_name=str(form.name.data)
		c_mo_no=int(form.mobile_no.data)
		c_question=str(form.question.data)

		try:
			add_contact_data=contact_us(name=c_name,mobile_no=c_mo_no,question=c_question,answer=None)
			db.session.add(add_contact_data)
		except Exception as e:
			session.rollback()
		else:
			db.session.commit()
		flash('Request successfully send','success')
		return redirect(url_for('index'))	
		
	return render_template('new.html',cart_count=count_cart_product(),form=form,get_trending_products=get_trending_products) 

@app.route('/search',methods=['GET'])
def search():
	get_req_cookie()
	print(request.args.get('product-search'))
	product_search_data=db.session.query(products)\
	.join(products.product_category)\
	.filter(or_(products.product_name.like('%'+request.args.get('product-search')+'%'),product_category.product_category_name.like('%'+request.args.get('product-search')+'%'))).all()
  
	print(len(product_search_data))
	flash('Showing result for: ' + str(request.args.get('product-search')), 'success')
	return render_template('search.html',products=product_search_data,cart_count=count_cart_product())

@app.route('/show_all_products',methods=['GET','POST'])
def show_all_products():
	get_req_cookie()
	product_category_details=product_category().query.all();
	product_details=products().query.all()

	return render_template('Product_Grid.html',products=product_details,product_category=product_category_details,cart_count=count_cart_product())

@app.route('/products',methods=['GET'])
def Products():
	get_req_cookie()
	product_category_details=product_category().query.all();
	brands =brand().query.all();
	new_f_data = None
	count=0
	product_details=products().query.all() 
	if 'u_mb_no' in session:
		user_wishlists_details=user_wishlist.query.filter(user_wishlist.mobile_no == session['u_mb_no']).all()
	else:
		user_wishlists_details=None
		
	p_price_min_value=db.session.query(func.min(products.product_price)).scalar();
	p_price_max_value=db.session.query(func.max(products.product_price)).scalar();
 

	if  'filter_data' in request.args and 'p_sort' in request.args and 'p_cat' in request.args:
		p_c_id = request.args.get('p_cat')
		f_data=request.args.get('filter_data')
		new_f_data = list(f_data.split(","))
		if int(request.args.get('p_sort')) == 1:
			product_details=db.session.query(products)\
			.join(products.brand)\
			.filter(brand.brand_name.in_(new_f_data),products.product_category_id == p_c_id)\
			.order_by(products.product_price).all()
		else:

			product_details=db.session.query(products)\
			.join(products.brand)\
			.filter(brand.brand_name.in_(new_f_data),products.product_category_id == p_c_id)\
			.order_by(products.product_price.desc()).all()
			
		count=len(product_details)
		flash(' products found :' + str(count) ,'success')
		#return render_template('Product_Grid.html',products=product_details,product_category=product_category_details,cart_count=count_cart_product(),brand=brands,n_data=new_f_data)
	elif 'filter_data' in  request.args and 'p_sort' in request.args:
		f_data=request.args.get('filter_data')
		new_f_data = list(f_data.split(","))
		if int(request.args.get('p_sort')) == 1:

			product_details=db.session.query(products)\
			.join(products.brand)\
			.filter(brand.brand_name.in_(new_f_data))\
			.order_by(products.product_price).all()
		else:
			product_details=db.session.query(products)\
			.join(products.brand)\
			.filter(brand.brand_name.in_(new_f_data))\
			.order_by(products.product_price.desc()).all()

			
		count=len(product_details)
		flash(' products found :' + str(count) ,'success')
	   # return render_template('Product_Grid.html',products=product_details,product_category=product_category_details,cart_count=count_cart_product(),brand=brands,n_data=new_f_data)
	elif 'filter_data' in request.args and 'p_cat' in request.args:
		p_c_id = request.args.get('p_cat')
		f_data=request.args.get('filter_data')
		new_f_data = list(f_data.split(","))
		product_details=db.session.query(products)\
		.join(products.brand)\
		.filter(brand.brand_name.in_(new_f_data),products.product_category_id == p_c_id).all()
		count=len(product_details)
		flash(' products found :' + str(count) ,'success')
		#return render_template('Product_Grid.html',products=product_details,product_category=product_category_details,cart_count=count_cart_product(),brand=brands,n_data=new_f_data)
	elif 'p_sort' in request.args and 'p_cat' in request.args:
		p_c_id = request.args.get('p_cat')
		if int(request.args.get('p_sort'))==1:
			product_details=db.session.query(products)\
			.filter(products.product_category_id == p_c_id)\
			.order_by(products.product_price).all()
		else:
			product_details=db.session.query(products)\
			.filter(products.product_category_id == p_c_id)\
			.order_by(products.product_price.desc()).all()
			
		count=len(product_details)
		flash(' products found :' + str(count) ,'success')
	   # return render_template('Product_Grid.html',products=product_details,product_category=product_category_details,cart_count=count_cart_product(),brand=brands)
	elif 'filter_data' in request.args:
		f_data=request.args.get('filter_data')
		new_f_data = list(f_data.split(",")) 
		print(new_f_data)
		product_details=db.session.query(products)\
		.join(products.brand)\
		.filter(brand.brand_name.in_(new_f_data)).all()
		count=len(product_details)
		flash(' products found :' + str(count) ,'success')
	   # return render_template('Product_Grid.html',products=product_details,product_category=product_category_details,cart_count=count_cart_product(),brand=brands,n_data=new_f_data)
	elif 'p_sort' in request.args:
		if int(request.args.get('p_sort'))==1:
			product_details=products.query.order_by(products.product_price).all()
		else:
			product_details=products.query.order_by(products.product_price.desc()).all()

		count=len(product_details)
		flash(' products found :' + str(count) ,'success')
	   # return render_template('Product_Grid.html',products=product_details,product_category=product_category_details,cart_count=count_cart_product(),brand=brands)
	elif 'p_cat' in request.args:
		p_c_id = request.args.get('p_cat')
		product_details=products.query.filter( products.product_category_id == p_c_id).all()
		count=len(product_details)
		flash(' products found :' + str(count) ,'success')
	elif 'p_min' in request.args and 'p_max' in request.args:
		product_details=products.query.filter( products.product_price >= request.args.get('p_min'),products.product_price <= request.args.get('p_max')).all()
		count=len(product_details)
		flash(' products found :' + str(count) ,'success')
		
		#return render_template('Product_Grid.html',products=product_details,product_category=product_category_details,cart_count=count_cart_product(),brand=brands)
	return render_template('Product_Grid.html',products=product_details,product_category=product_category_details,cart_count=count_cart_product(),user_wishlists_details=user_wishlists_details,brand=brands,n_data=new_f_data, p_price_min_value=p_price_min_value,p_price_max_value=p_price_max_value)


@app.route('/products/<string:p_id>',methods=['GET','POST'])
def product_single_detail(p_id):
	get_req_cookie()
	print(p_id)
	enable_add_cart=0
	eligible_for_review = 0
	in_having_wishlist=False
	product_single_details=products.query.get(p_id)
	if 'u_mb_no' in session:
		user_wishlist_singal_detail=user_wishlist.query.filter(and_(user_wishlist.mobile_no==session['u_mb_no'],user_wishlist.product_id==p_id)).first()
		if user_wishlist_singal_detail:
			in_having_wishlist=True
		else:
			in_having_wishlist=False
	else:
		in_having_wishlist=False
	



	product_reviews=product_review.query.filter(product_review.product_id == product_single_details.product_id).all()
	if product_reviews:

		product_max_review=db.session.query(func.avg(product_review.rating)).filter(product_review.product_id == product_single_details.product_id).scalar()
		product_max_review=math.floor(product_max_review)
	else:
		product_max_review = 0

		
	recommend_product_list=products.query.filter(and_(products.product_category==product_single_details.product_category,products.product_id!=product_single_details.product_id)).all() 

	if 'logged_in' in session:
		check_already_exist=orders_details.query.filter(and_(orders_details.mobile_no == session['u_mb_no'],orders_details.product_id == p_id , orders_details.is_ordered == int(0))).first()

		if request.method == 'POST':
			p_rate=request.form['rate1'];
			p_review=request.form['product_review'];

			try:
				add_review=product_review(product_id=product_single_details.product_id,rating=int(p_rate),mobile_no=session['u_mb_no'],review_description=p_review)
				db.session.add(add_review)
			except IntegrityError:
				session.rollback
			else:
				db.session.commit()
			flash('Successfully Review Send','success')
			return redirect(url_for('product_single_detail',p_id=product_single_details.product_id)) 	
		if check_already_exist is None :
			enable_add_cart=0
			check_whether_eligible_for_review_or_not=db.session.query(orders_details).\
			join(orders_details.orders).\
			filter(and_(orders_details.mobile_no == session['u_mb_no'],orders_details.product_id == p_id , orders.order_status == 'Completed' )).first()
			if check_whether_eligible_for_review_or_not :
				eligible_for_review = 1
			else:
				eligible_for_review = 0			
		else:
			enable_add_cart=1			
	return render_template('View_Product.html',product=product_single_details,cart_count=count_cart_product(),in_having_wishlist=in_having_wishlist,recommend_product_list=recommend_product_list,enable_add_cart=enable_add_cart,eligible_for_review = eligible_for_review,product_reviews=product_reviews,product_max_review=product_max_review)    


@app.route('/cart/add',methods=['GET','POST'])
@is_logged_in
def add_to_cart():
	order_product_data=json.loads(request.data)
	if order_product_data:
		check_already_exist=orders_details.query.filter(orders_details.mobile_no == session['u_mb_no'],orders_details.product_id == order_product_data['product_id'] ,orders_details.is_ordered == int(0) ).first()
		print(check_already_exist)
		if check_already_exist is None : 
			try:
				order_product_data=orders_details(mobile_no=int(session['u_mb_no']) ,product_id= int(order_product_data['product_id']),quantity=int(order_product_data['order_product_qnt']))
				print(order_product_data)
				db.session.add(order_product_data)   
			except IntegrityError:  
				session.rollback()
			else:   
				db.session.commit() 
			return jsonify({'success_message':'product successfully added to cart'})

		return jsonify({'error_message':'product already having in cart'})
	else:
		return redirect(url_for('cart'))
		



@app.route('/cart/update',methods=['POST'])
@is_logged_in
def update_cart():
	cart_u_data_get= json.loads(request.data)
	orders_details.query.filter_by(order_product_id=cart_u_data_get['order_product_id']).update(dict(quantity=int(cart_u_data_get['product_quantity'])))
	db.session.commit()
	return jsonify({'success_message':'updation successfully done'})


@app.route('/cart/delete',methods=['POST'])
@is_logged_in
def delete_cart():
	cart_u_data_get= json.loads(request.data)
	#orders_details.query.filter_by(order_product_id=cart_u_data_get['order_product_id']).update(dict(quantity=int(cart_u_data_get['product_quantity'])))
	get_c_data=orders_details.query.get(cart_u_data_get['order_product_id'])
	db.session.delete(get_c_data)
	db.session.commit()
	return jsonify({'success_message':'deletion successfully done'})
	




@app.route('/cart',methods=['GET','POST'])
@is_logged_in
def cart():
	get_req_cookie()
	orders_data=orders_details.query.filter(and_(orders_details.mobile_no == session['u_mb_no'],orders_details.is_ordered==int(0))).all()
	total_cart_amt = 0
	for order_new_data in orders_data:
		total_cart_amt += (order_new_data.products.product_price * order_new_data.quantity)
	return render_template('Add_to_Cart.html',orders_details=orders_data,cart_count=count_cart_product(),t_c_amt=total_cart_amt)


@app.route('/checkout',methods=['GET','POST'])
@is_logged_in
def checkout():
	form=Checkout_Form(request.form)
	populate_city_state(form)
	orders_data=orders_details.query.filter(and_(orders_details.mobile_no == session['u_mb_no'],orders_details.is_ordered==int(0))).all()
	total_order_product=len(orders_data)
	total_cart_amt = 0
	for order_new_data in orders_data:
		total_cart_amt += (order_new_data.products.product_price * order_new_data.quantity)
	if request.method == 'POST' and form.validate():
		print('going here')
		name = form.name.data
		print("#####",name)
		mo_no = form.order_alt_mobile_no.data
		u_city_id=int(form.user_city.data)+1
		print(u_city_id)
		address=form.order_delivery_address.data
		delivery_date=(datetime.now() + timedelta(days=5) ).strftime('%Y-%m-%d')
		o_no=unique_order_no_generator()
		try:
			order_info=orders(order_no=o_no,order_total_amt = total_cart_amt ,\
				mobile_no=session['u_mb_no'],name=name,order_alt_mobile_no=int(mo_no),\
				city_id= u_city_id,order_delivery_address=address,\
				delivery_date=delivery_date,order_status=str('Ordered'))
			db.session.add(order_info)   
		except IntegrityError:
			session.rollback()
		else:
			db.session.commit()

		ordered_product_list=[]
		i=0
		while i< len(orders_data):
			ordered_product_list.append(orders_data[i].order_product_id)
			i+=1

		
		ordered_product_list = list(map(int,ordered_product_list))  
		up_qty = orders_details.query.filter(orders_details.order_product_id.in_(ordered_product_list)).update({orders_details.order_id:int(order_info.order_id),orders_details.is_ordered:int(1)},synchronize_session=False)
		db.session.commit()

		for orders_data in orders_data :
			products.query.filter(products.product_id == orders_data.product_id).\
			update({ products.product_stock :  products.product_stock - orders_data.quantity},synchronize_session = False)

		db.session.commit()

		payment_op = int(request.form['payment_options'])



		if payment_op == int(1):



			param_dict = {


				'MID': app.config['PAYTM_MERCHANT_ID'],
				'ORDER_ID': str(order_info.order_id),
				'TXN_AMOUNT': str(order_info.order_total_amt),
				'CUST_ID': 'cus'+str(order_info.mobile_no),
				'INDUSTRY_TYPE_ID': 'Retail',
				'WEBSITE': 'WEBSTAGING',
				'CHANNEL_ID': 'WEB',
				'PAYMENT_MODE_ONLY':'YES',
				'PAYMENT_TYPE_ID':'DC',
				'CALLBACK_URL':'http://localhost:2588/handlerequest/'+ str(order_info.order_id),
			}

			param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, app.config['PAYTM_API_KEY'])

			return render_template('/paytm.html',param_dict=param_dict)
		else:
			try:
				payment_info = payment(order_id = order_info.order_id,transaction_id = None,payment_method='Cash On Delivery',payment_date=None,payment_status='Pending')
				db.session.add(payment_info)
			except IntegrityError:
				session.rollback()
			else:
				db.session.commit()
			return redirect('/confirm-order/'+ str(o_no))

	return render_template('Checkout.html',orders_details=orders_data,cart_count=count_cart_product(),t_c_amt=total_cart_amt,total_order_product=total_order_product,form=form)



@app.route('/handlerequest/<string:orderid>',methods=['GET','POST'])
@csrf_exempt
@is_logged_in
def handlerequest(orderid):
	# paytm will send you post request here
	form = request.form
	response_dict = {}
	o_no=None
	o_no=orders.query.get(int(orderid)) 
	checksum="d"
	for i in form.keys():
		response_dict[i] = form[i]
		if i == 'CHECKSUMHASH':
			checksum = form[i]
			print(checksum)

	verify = Checksum.verify_checksum(response_dict,app.config['PAYTM_API_KEY'], checksum)
	if verify:
		if response_dict['RESPCODE'] == '01':
			print('order successful')
			try:
				payment_info = payment(order_id = int(orderid),transaction_id = response_dict['TXNID'],payment_method='Debit / ATM Card',payment_date=datetime.now().strftime('%Y-%m-%d'),payment_status='Paid')
				db.session.add(payment_info)
			except IntegrityError:
				session.rollback()
			else:
				db.session.commit()

			   
			return redirect('/confirm-order/'+ str(o_no.order_no))

		else:
			print('order was not successful because' + response_dict['RESPMSG'])

	return redirect('/confirm-order/'+ str(o_no.order_no))


@app.route('/verify_order_address',methods=['GET','POST'])
def verify_order_address():
	form = Checkout_Form(request.form)
	populate_city_state(form)
	if form.validate():
		
		print(form.name.data)

		#return render_template('Checkout.html',form=form)
		return jsonify(data={'message': 'hello {}'.format(form.data)})
	return jsonify(data=form.errors)


@app.route('/confirm-order/<string:token>',methods=['GET','POST'])
@is_logged_in
def confirm_order(token):

	order_info=db.session.query(orders).filter(orders.order_no == str(token)).first()

	confirm_order_info=db.session.query(orders_details).filter(orders_details.order_id == order_info.order_id).all()

	payment_info=db.session.query(payment)\
	.join(payment.orders)\
	.filter(orders.order_no == str(token)).first()

	return render_template('Confirmation.html',order_info=order_info,confirm_order_info=confirm_order_info,payment_info=payment_info)






@app.route('/compare_product',methods=['GET','POST'])
def compare_product():
	get_req_cookie()

	if request.args.get('product_id'):
		enable_add_cart=[]
		check_already_exist=[]
		get_p_ids=request.args.get('product_id')
		print(get_p_ids)
		new_p_ids=list(get_p_ids.split(","))

		product_details=db.session.query(products).filter(products.product_id.in_(new_p_ids)).all()
		if 'logged_in' in session:
			check_already_exist=orders_details.query.filter(orders_details.mobile_no == session['u_mb_no'],orders_details.product_id.in_(new_p_ids) ).all()
			print(len(check_already_exist))
			return render_template('Product_Compare.html',product_details=product_details,cart_count=count_cart_product(),check_already_exist=check_already_exist)
	else:
		return redirect(url_for('Products'))    
	return render_template('Product_Compare.html',product_details=product_details,cart_count=count_cart_product())






@app.route('/signin',methods=['GET','POST'])
@not_logged_in
def login():
	get_req_cookie()
	form=LoginForm(request.form)
	if request.method == 'POST' and form.validate():
		u_mobile_no=int(form.user_mobile_no.data)
		u_e_password=str(form.user_password.data)
		print(u_e_password)
		try:
			result=users.query.get(u_mobile_no)
			print(result)
			if result is None:
				flash('Mobile no and password is incorrect.', 'danger')
				return render_template('SignIn.html', form=form)
			else:   
				data_login=users.query.filter(users.user_mobile_no == u_mobile_no).first()
				password = data_login.user_password
				u_mb_no = data_login.user_mobile_no
				name = data_login.user_full_name

				print(password)
				if sha256_crypt.verify( u_e_password , password):
					 session['logged_in'] = True
					 session['u_mb_no'] = u_mb_no
					 session['s_name'] = name
					 session['s_type']=data_login.user_type

					 x = int(1)
					 users.query.filter_by(user_mobile_no=u_mobile_no).update(dict(user_status=x))
					 db.session.commit()

					 flash('Successfully Login', 'success')
					 expire_date = datetime.now()
					 expire_date = expire_date + timedelta(days=30)
					 #nexturl=session['nexturl']
					 #session.pop('nexturl',None)
					 #if nexturl:
					 #  resp=make_response(nexturl)
					 #else:
					 resp=make_response(redirect('/'))
					 resp.set_cookie('logged_in',str(session['logged_in']),expires=expire_date)
					 resp.set_cookie('mobile_no',str(session['u_mb_no']),expires=expire_date)
					 resp.set_cookie('name',str(session['s_name']),expires=expire_date)
					 resp.set_cookie('s_type',str(session['s_type']),expires=expire_date)
					 return resp

				else:
					 flash('Incorrect password', 'danger')
					 return render_template('SignIn.html', form=form,cart_count=count_cart_product())
		except IntegrityError:  
			session.rollback()
		else:
			db.session.commit()
	 
	return render_template('SignIn.html',form=form,cart_count=count_cart_product())


@app.route('/forgot_password/Enter-Mobileno',methods=['GET','POST'])
@not_logged_in
def forgot_password_mobo():
	
	if request.method == 'POST':
		if request.form['mobile_no']:


			u_mobile_no=request.form['mobile_no'] 
			result=users.query.get(u_mobile_no)
			if result is None:
				 flash('Incorrect mobile no.', 'danger')
				 return redirect(url_for('forgot_password_mobo'))
			else:


				u_mobile_no=request.form['mobile_no'] 
				digits = "0123456789"
				OTP = ""     
				for i in range(4):
					OTP += digits[math.floor(random.random() * 10)]
		  
				message_user="your otp is :" + OTP + '\nCode Valid For 5 minutes \nby AG-STAR'
				response = sendPostRequest(URL, app.config['WAY2SMS_APIKEY'], app.config['WAY2SMS_SECRETKEY'], 'stage', u_mobile_no, 'AS-007',str(message_user))    
				print(response.text)

				en_mo_bo,en_OTP=Secure_Data.encrypt(u_mobile_no,OTP)
				print(en_mo_bo)
				print(en_OTP)
				flash('Successfully message send to ' + str(u_mobile_no) + '\nnow see on your messages you got OTP \nenter in below. ' ,'success')
				res = make_response(redirect('/forgot_password/Enter-OTP'))  
				res.set_cookie('F_otp_mo_no',en_mo_bo,max_age=600)
				res.set_cookie('F_OTP', en_OTP, max_age=300)
				return res
	return render_template('Forgot.html')


@app.route('/forgot_password/Enter-OTP',methods=['GET','POST'])
@not_logged_in
def forgot_password_otp():
	if request.method == 'POST':
		if request.form['OTP']:
			otp=request.form['OTP']
			print("user side" + otp)
			de_mo_bo,de_otp=Secure_Data.decrypt(str(request.cookies.get('F_otp_mo_no')),str(request.cookies.get('F_OTP')))
			print(de_mo_bo)
			print(de_otp)
			if int(de_otp):
				if int(otp) == int(de_otp):
					flash('Successfully verified OTP \nnow you can change password','success')
					return redirect(url_for('forgot_password_pass'))
				else:
					flash('Invalid OTP','danger')
					return redirect(url_for('forgot_password_otp'))
			else:
				flash('OTP expired , send new otp','info')
				return render_template('Forgot.html')                   
	return render_template('OTP.html')


@app.route('/forgot_password/Enter-pass',methods=['GET','POST'])
@not_logged_in
def forgot_password_pass():
	form=Forgot_Password(request.form)
	if request.method == 'POST' and form.validate():
		u_password=sha256_crypt.hash(str(form.user_password.data))
		de_crypt_mo,de_crypt_otp=Secure_Data.decrypt(str(request.cookies.get('F_otp_mo_no')),'0224')
		user_data=users.query.filter_by(user_mobile_no=int(de_crypt_mo)).update(dict(user_password=u_password))
		db.session.commit()
		flash('Password Successfully change \nnow try to login with updated password','success')
		return redirect(url_for('login'))

	return render_template('Password.html',form=form)    


	


@app.route('/logout')
def logout():
	if 'u_mb_no' in session:
		# Create cursor
	   
		u_mb_no = session['u_mb_no']
		x = int(0)
		#cur.execute("UPDATE users SET online=%s WHERE id=%s", (x, uid))
		users.query.filter_by(user_mobile_no=u_mb_no).update(dict(user_status=x))
		db.session.commit()

		session.clear()

		flash('You are logged out', 'success')
		resp=make_response(redirect('/'))
		resp.set_cookie('logged_in', expires=0)
		resp.set_cookie('mobile_no', expires=0)
		resp.set_cookie('name', expires=0)
		resp.set_cookie('s_type', expires=0)
		return resp

	return redirect(url_for('login'))

@app.route('/user-profile',methods=['GET','POST'])
@is_logged_in
def user_profile():
	get_req_cookie()


	get_user_data=users.query.get(session['u_mb_no'])
	get_city_data=city.query.all()

	if request.method == 'POST':
		print("djdjdjdjjdjjdjjdjdjjdjjd");
		u_name=request.form['user_name']
		print(u_name)
		u_city=request.form['user_city']
		print(u_city)
		u_address=request.form['user_address']
		print(u_address)
		u_old_password=request.form['old_password']
		u_new_password=request.form['new_password']
			

			
		if u_name and u_city and u_address and u_old_password and u_new_password:
			if sha256_crypt.verify( u_old_password , get_user_data.user_password):
				if u_old_password == u_new_password:
					flash('New password cannot be old password.','danger')
					return redirect(url_for('user_profile'))
				else:
					enc_new_password=sha256_crypt.hash(str(u_new_password))
					users.query.filter(users.user_mobile_no == int(session['u_mb_no'])).\
					update({users.user_full_name:u_name,users.user_city_id:u_city,users.user_address:u_address,users.user_password:enc_new_password},synchronize_session=False)
					session['s_name'] = u_name
					db.session.commit()
					flash('Your profile successfully updated and password also updated','success')
					resp=make_response(redirect('/user-profile'))
					resp.set_cookie('name',str(session['s_name']), expires= datetime.now() + timedelta(days=30))
					return resp 
			else:
				flash('Your entered old password is incorrect , please enter valid old password','danger')
				return redirect(url_for('user_profile'))
		elif u_name and u_city and u_address and u_old_password  or u_new_password :
			flash('please fill all password field','danger')
			return redirect(url_for('user_profile'))
		elif u_name and u_city and u_address:
			users.query.filter(users.user_mobile_no == int(session['u_mb_no'])).\
			update({users.user_full_name:u_name,users.user_city_id:u_city,users.user_address:u_address},synchronize_session=False)
			session['s_name'] = u_name

			db.session.commit()
			flash('Your profile successfully updated','success')
			resp=make_response(redirect('/user-profile'))
			resp.set_cookie('name',str(session['s_name']), expires= datetime.now() + timedelta(days=30))
			return resp             
		else:
			flash('please fill out required field','info')
			return redirect(url_for('user_profile'))

	return render_template('My_account_myprofile.html',get_user_data=get_user_data,get_city_data=get_city_data,cart_count=count_cart_product())


@app.route('/user-wishlists/add',methods=['GET','POST'])
@is_logged_in
def add_to_wishlist():
	if 'add_wishlist_product_id' in request.args:
		check_already_exist=user_wishlist.query.filter(and_(user_wishlist.mobile_no == session['u_mb_no'],user_wishlist.product_id == int(request.args.get('add_wishlist_product_id'))) ).first()
		if check_already_exist is None:
			try:
				user_product_wishlist=user_wishlist(mobile_no=int(session['u_mb_no']),product_id=int(request.args.get('add_wishlist_product_id')))
				db.session.add(user_product_wishlist)
			except IntegrityError:
				session.rollback()
			else:
				db.session.commit()

			return jsonify({'data':'successfully added to wishlist'})					

	return jsonify({'error':'missing data!!!'})





@app.route('/user-wishlists',methods=['GET','POST'])
@is_logged_in
def user_wishlists():
	get_user_data=users.query.get(session['u_mb_no'])
	user_wishlist_data=user_wishlist.query.filter(user_wishlist.mobile_no == session['u_mb_no']).all()

	if 'delete_wishlist_id' in request.args:
		try:
			user_wishlist.query.filter(user_wishlist.wishlist_id == request.args.get('delete_wishlist_id')).delete()
		except IntegrityError:
			session.rollback()
		else:
			db.session.commit()

		return render_template('My_account_wishlists.html',get_user_data=get_user_data,user_wishlist_data=user_wishlist_data,cart_count=count_cart_product())
	elif 'move_wishlist_id' in request.args:
		#check whether this wish_list product already having in list or not
		get_wishlist_product_data=user_wishlist.query.get(request.args.get('move_wishlist_id'))
		check_order_exist_or_not=orders_details.query.filter(and_(orders_details.mobile_no == session['u_mb_no'],orders_details.is_ordered==int(0),orders_details.product_id == get_wishlist_product_data.product_id )).first()

		if check_order_exist_or_not is None:

			try:
				order_product_data=orders_details(mobile_no=int(session['u_mb_no']) ,product_id= int(get_wishlist_product_data.product_id),quantity=int(1))
				print(order_product_data)
				db.session.add(order_product_data)   
			except IntegrityError:  
				session.rollback()
			else:
				user_wishlist.query.filter(user_wishlist.wishlist_id == get_wishlist_product_data.wishlist_id).delete()   
				db.session.commit()

			return redirect(url_for('cart'))	
	return render_template('My_account_wishlists.html',get_user_data=get_user_data,user_wishlist_data=user_wishlist_data,cart_count=count_cart_product())


@app.route('/user-orders',methods=['GET','POST'])
@is_logged_in
def user_orders():
	get_user_data=users.query.get(session['u_mb_no'])
	user_orders=orders_details.query.filter(orders_details.mobile_no == session['u_mb_no'],orders_details.is_ordered == int(1)).all()
	if 'cancel_order_id' in request.args:

		try:
			order_cancel_data=orders_details.query.filter(orders_details.order_product_id == request.args.get('cancel_order_id')).\
			update({orders_details.is_cancelled:int(1)},synchronize_session=False)

		except IntegrityError:
			session.rollback()
		else:
			 db.session.commit()

		get_quantity_cancel_product=orders_details.query.get(request.args.get('cancel_order_id'))

		try:
			products.query.filter(products.product_id == request.args.get('cancel_order_id'))\
			.update({products.product_stock: products.product_stock + get_quantity_cancel_product.quantity },synchronize_session=False)
		except IntegrityError:
			session.rollback()
		else:
			db.session.commit()
			
			
		all_order_cancel_data = db.session.query(orders_details.order_product_id).\
		filter(orders_details.order_id == int(get_quantity_cancel_product.order_id)).all()

		get_cancel_order_result=orders_details.query.\
		filter(orders_details.order_product_id.in_(all_order_cancel_data),orders_details.is_cancelled == int(1)).all()



		if len(all_order_cancel_data) == len(get_cancel_order_result):
			try:
				orders.query.filter(orders.order_id == int(get_quantity_cancel_product.order_id)).\
				update({orders.order_status : str('Cancelled') },synchronize_session=False)
				payment.query.filter(payment.order_id == int(get_quantity_cancel_product.order_id)).\
				update({payment.payment_status : str('Cancelled') },synchronize_session=False)
			except IntegrityError:
				session.rollback()
			else:
				db.session.commit()         
				 
		render_template('My_account_orders.html',get_user_data=get_user_data,user_orders=user_orders,cart_count=count_cart_product()) 
	return render_template('My_account_orders.html',get_user_data=get_user_data,user_orders=user_orders,cart_count=count_cart_product())

@app.route('/weather',methods=['GET','POST'])
def weather():
	get_req_cookie()
	new_city=request.form.get('search_place')
	url='http://api.openweathermap.org/data/2.5/forecast?q={}&units=imperial&appid=0feff28e59f24064fe087c5cd9c3238d'
	if not new_city:
			new_city='Ahmedabad'

	city=new_city

	r = requests.get(url.format(city)).json()

	weathers=[]

	i=0
	while i<len(r['list']):

		#dictionary to store city and temprature
		wh={
			'city':city,
			'description': r['list'][i]['weather'][0]['description'],
			'temperature': r['list'][i]['main']['temp'],
			'icon':r['list'][i]['weather'][0]['icon'],
			'pressure':r['list'][i]['main']['pressure'],
			'humidity':r['list'][i]['main']['humidity'],
			'wind':r['list'][i]['wind']['speed'],
			'd_t': r['list'][i]['dt_txt']
		}

			
		weathers.append(wh)
		i+=1
		
	i=0

	date_values=''
	dates=''
	times=''
	ddate_values=''
	ddate=''
	dtime=''
	k=0
	init=True
	new_weather=[]
	while i<len(weathers):
		
		if  init==True:

				
			new_weather.append(weathers[i])
			date_values=new_weather[k]['d_t']
			dates,times=date_values.split(' ')
			k+=1
			init=False

		else:
			ddate_values=weathers[i]['d_t']
			ddate,dtime=ddate_values.split(' ')

			if ddate!=dates:

				if dtime==times:

						
					new_weather.append(weathers[i])
					date_values=new_weather[k]['d_t']
					dates,times=date_values.split(' ')
					k+=1
						

						
		i+=1        
		
	return render_template('Wheather_d.html',weather=new_weather,cart_count=count_cart_product())

@app.route('/weather_mesurement',methods=['GET','POST'])
def weather_mesurement():
	if 'chage_measuremnt' in request.args:
		get_req_cookie()
		new_city=request.form.get('search_place')
		url='http://api.openweathermap.org/data/2.5/forecast?q={}&units=imperial&appid=0feff28e59f24064fe087c5cd9c3238d'
		if not new_city:
			new_city='Ahmedabad'

		city=new_city

		get_mesauremnt = request.args.get('chage_measuremnt')
		city=new_city

		r = requests.get(url.format(city)).json()

		weathers=[]

		i=0

		if get_mesauremnt == 'c':


			while i<len(r['list']):

				#dictionary to store city and temprature
				wh={
					'city':city,
					'description': r['list'][i]['weather'][0]['description'],
					'temperature': math.floor((r['list'][i]['main']['temp']-32) * 5/9),
					'icon':r['list'][i]['weather'][0]['icon'],
					'pressure':r['list'][i]['main']['pressure'],
					'humidity':r['list'][i]['main']['humidity'],
					'wind':r['list'][i]['wind']['speed'],
					'd_t': r['list'][i]['dt_txt']
				}

				
				weathers.append(wh)
				i+=1
		else:
			while i<len(r['list']):

				#dictionary to store city and temprature
				wh={
					'city':city,
					'description': r['list'][i]['weather'][0]['description'],
					'temperature': r['list'][i]['main']['temp'],
					'icon':r['list'][i]['weather'][0]['icon'],
					'pressure':r['list'][i]['main']['pressure'],
					'humidity':r['list'][i]['main']['humidity'],
					'wind':r['list'][i]['wind']['speed'],
					'd_t': r['list'][i]['dt_txt']
				}

				
				weathers.append(wh)
				i+=1

				



		
		i=0

		date_values=''
		dates=''
		times=''
		ddate_values=''
		ddate=''
		dtime=''
		k=0
		init=True
		new_weather=[]
		while i<len(weathers):
		
			if  init==True:

				
				new_weather.append(weathers[i])
				date_values=new_weather[k]['d_t']
				dates,times=date_values.split(' ')
				k+=1
				init=False

			else:
				ddate_values=weathers[i]['d_t']
				ddate,dtime=ddate_values.split(' ')

				if ddate!=dates:
					if dtime==times:
						
						new_weather.append(weathers[i])
						date_values=new_weather[k]['d_t']
						dates,times=date_values.split(' ')
						k+=1
						

						
			i+=1        
		
		return render_template('Wheather_d.html',weather=new_weather,cart_count=count_cart_product())
	

		


@app.route("/Farming-info/")
def Research_info():
	get_req_cookie()
	global toggle
	toggle=int(0)
	#for fetching research-info data from database
	research_infos=research_info.query.all()
	if 'u_mb_no' in session:
		# Create cursor
	   
		u_type = session['s_type']
		if u_type=='Agriculture Scientist':
			 toggle=1
		else:
			 toggle=0   

		return render_template('Research_Info_Grid.html',toggle=toggle,research_infos=research_infos,cart_count=count_cart_product())
	else:
		return render_template('Research_Info_Grid.html',toggle=toggle,research_infos=research_infos,cart_count=count_cart_product())   

	return render_template('Research_Info_Grid.html',toggle=toggle,research_infos=research_infos,cart_count=count_cart_product())


@app.route('/Farming-info/<string:topic_id>')
def Research_info_detail(topic_id):
	global toggle
	toggle=int(0)
	#for fetching research-info data from database
	research_infos=research_info.query.get(topic_id)
	if research_infos is None:
		abort(404)
	else:
		 if 'u_mb_no' in session:
			# Create cursor
		   
			 u_type = session['s_type']
			 if u_type=='Agriculture Scientist':
				 toggle=1
			 else:
				 toggle=0   

			 return render_template('View_Research_Info.html',toggle=toggle,research_info=research_infos,cart_count=count_cart_product())
		 else:
			 return render_template('View_Research_Info.html',toggle=toggle,research_info=research_infos,cart_count=count_cart_product())    

	return render_template('View_Research_Info.html',toggle=toggle,research_info=research_infos,cart_count=count_cart_product())    



@app.route('/Upload-Farming-info',methods=['GET','POST'])
@app.route('/Upload_Farming_info',methods=['GET','POST'])
@is_logged_in
@is_agriculture_scientist
def Upload_Research_info():
	   #for fetching research-info data from database
	if request.method == 'POST':

		file_options = request.form['options'];
		topic_name=request.form['topic-name']
		topic_description=request.form['topic-description']
		if file_options=='opt_1':
			file_upload_image=request.files['file-upload-image']
			if file_upload_image:
				if file_upload_image and allowed_image_file(file_upload_image.filename):
					ext_file=file_upload_image.filename.rsplit('.',1)[1].lower()
					get_topic_max_id=db.session.query(func.max(research_info.topic_id)).scalar()
					if get_topic_max_id is None:
						file_upload_image.filename = 'topic' + str(1) + '.' + ext_file
					else:   
						file_upload_image.filename = 'topic' + str(get_topic_max_id+1) + '.' + ext_file
					filename_image = secure_filename(file_upload_image.filename)
					
					
					
					u_mb_no = session['u_mb_no']
					try:
						farming_info_data=research_info(topic_name=topic_name,topic_description=topic_description,topic_img=filename_image,topic_video=None,mobile_no=int(u_mb_no))
						db.session.add(farming_info_data)   
					except IntegrityError:  
						session.rollback()
					else:   
						db.session.commit()

						

	
					file_upload_image.save(os.path.join(app.config['UPLOAD_FOLDER'], 'farming-info/' + filename_image))    
			
					flash('New Farming-info Uploaded successfully','success')
					return redirect(url_for('Research_info'))
				else:
					flash('please select valid format of image','danger');
					return redirect(url_for('Upload_Research_info'))                    
			else:
				flash('please select image','danger');
				return redirect(url_for('Upload_Research_info'))
		else:
			file_upload_thumbnail=request.files['file-upload-thumbnail']
			file_upload_video=request.files['file-upload-video']

			if file_upload_thumbnail and file_upload_video:


				if file_upload_thumbnail and allowed_image_file(file_upload_thumbnail.filename):

					ext_file_tmb=file_upload_thumbnail.filename.rsplit('.',1)[1].lower()
					get_topic_max_id_tmb_video=db.session.query(func.max(research_info.topic_id)).scalar()
					if get_topic_max_id_tmb_video is None:
						file_upload_thumbnail.filename = 'topic' + str(1) + '.' + ext_file_tmb
					else:
						file_upload_thumbnail.filename = 'topic' + str(get_topic_max_id_tmb_video+1) + '.' + ext_file_tmb
							
					filename_image = secure_filename(file_upload_thumbnail.filename)
				

					if file_upload_video and allowed_video_file(file_upload_video.filename):
						ext_file_vid=file_upload_video.filename.rsplit('.',1)[1].lower()    
						if get_topic_max_id_tmb_video is None:
							file_upload_video.filename = 'topic' + str(1) + '.' + ext_file_vid
						else:
							file_upload_video.filename = 'topic' + str(get_topic_max_id_tmb_video+1) + '.' + ext_file_vid   
						filename_video = secure_filename(file_upload_video.filename)
						
						u_mb_no = session['u_mb_no']
						try:
							farming_info_data=research_info(topic_name=topic_name,topic_description=topic_description,topic_img=filename_image,topic_video=filename_video,mobile_no=int(u_mb_no))
							db.session.add(farming_info_data)   
						except IntegrityError:
							session.rollback()
						else:   
							db.session.commit()

						file_upload_thumbnail.save(os.path.join(app.config['UPLOAD_FOLDER'],'farming-info/' + filename_image))    
						file_upload_video.save(os.path.join(app.config['UPLOAD_FOLDER'],'farming-info/' + filename_video))    
						flash('New Farming-info Uploaded successfully','success')
						return redirect(url_for('Research_info'))     
							
					else:
						flash('please select only video','danger')
						return redirect(url_for('Upload_Research_info'))


					   
				else:
					flash('please select valid format of image','danger')
					return redirect(url_for('Upload_Research_info'))

			
			else:
				flash('please select thumbnail of video and video also.','danger')
				return redirect(url_for('Upload_Research_info'))
	else:
		return render_template('Upload_Research_Info.html',cart_count=count_cart_product())   




@app.route('/Crops/',methods=['GET','POST'])
def Crops():
	get_req_cookie()
	val=crop().query.all()
	print(val)
	return render_template('Crop_Grid.html',values=val,cart_count=count_cart_product())


@app.route('/Crops/<string:crop_id>/',methods=['GET','POST'])
def Crop_Details(crop_id):
		print(crop_id)
		crop_details = crop.query.get(crop_id)
		print(crop_details)
		return render_template('View_Crop_Detail.html' , crop_detail = crop_details,cart_count=count_cart_product())



@app.route('/E-learn/')
def E_learn_Grid():
		get_req_cookie()
		e_learns=e_learn().query.all()
		return render_template('E_learn_Grid.html',e_learns=e_learns)

@app.route('/E-learn/<string:e_learn_id>')
def E_learn(e_learn_id):
	e_learn_v1=e_learn.query.get(e_learn_id)
	e_learn_vs=e_learn.query.filter(e_learn.e_learn_id != e_learn_id ).all()
	return render_template('View_E-learn.html',e_learn_v1=e_learn_v1,e_learn_vs=e_learn_vs,cart_count=count_cart_product())     


@app.route('/ask-questions',methods=['GET','POST'])
def ask_questions():
	get_req_cookie()
	if 'msg' in request.args:
		user_text=request.args.get('msg')
		response_text=get_bot_response(user_text)
		return str(response_text)
	return render_template('Ask_Questions.html',cart_count=count_cart_product())
