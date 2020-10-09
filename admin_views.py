from agrostar_app import *
from models import *
from forms import *
from Require_functions import *


@app.route("/admin/admin-login",methods=['GET','POST'])
@not_admin_logged_in
def admin_login():
	form=Admin_login(request.form)

	if request.method == 'POST' and form.validate():
		email_id=form.e_mail_id.data
		e_password=str(form.password.data)
		print(e_password)
		try:
			result=admin.query.get(email_id)
			print(result)
			if result is None:
				flash('Incorrect e-mail id and password', 'danger')
				return render_template('pages/login.html', form=form)
			else:   
				data_login=admin.query.filter(admin.e_mail_id == email_id).first()
				password = data_login.password      
				print(password)
				if sha256_crypt.verify( e_password , password):
					 session['admin_logged_in'] = True
					 session['email_id'] = email_id         

					 x = int(1)
					 admin.query.filter_by(e_mail_id=email_id).update(dict(status=x))
					 db.session.commit()

					 flash('Successfully Login', 'success')
					 return redirect(url_for('admin_dashboard'))    

				else:
					 flash('Incorrect password', 'danger')
					 return render_template('pages/login.html',form=form)
		except IntegrityError:  
			session.rollback()
		else:
			db.session.commit()
	return render_template('pages/login.html',form=form)


def send_reset_email(admin):
	token = admin.get_reset_token()
	msg = Message('Password Reset Request',
				  sender='dhruvsuthar715@gmail.com',
				  recipients=[admin.e_mail_id])
	msg.body = f'''To reset your password, visit the following link:
{url_for('admin_reset_password', token=token, _external=True)}.
'''
	mail.send(msg)




@app.route("/admin/admin-forgot-password",methods=['GET','POST'])
def admin_forgot_password():
	if request.method == 'POST':
		e_email=request.form['email']
		admin_data=admin.query.get(e_email)

		if admin_data:
			send_reset_email(admin_data)
			flash('successfully sended request','success')
			return redirect(url_for('admin_login'))
		else:
			flash('email id not found','danger')
			return redirect(url_for('admin_forgot_password'))       
	return render_template('pages/Forgot_Password1.html')


@app.route("/admin/admin-forgot-password/<token>/",methods=['GET','POST'])
def admin_reset_password(token):
	admin_data = admin.verify_reset_token(token)

	if admin_data is None:
		flash('That is an invalid or expired token', 'warning')
		return redirect(url_for('admin_forgot_password'))
	form=Forgot_Password(request.form)
	if request.method == 'POST' and form.validate():
		new_password=sha256_crypt.hash(form.user_password.data)
		admin.query.filter_by(e_mail_id = admin_data.e_mail_id).update(dict(password = new_password))
		db.session.commit()
		flash('Your password has been updated! You are now able to log in', 'success')
		return redirect(url_for('admin_login'))
			
	return render_template('pages/Forgot_Password3.html',form=form) 



@app.route("/admin/admin-logout",methods=['GET','POST'])
def admin_log_out():
	if 'email_id' in session:
		# Create cursor
	   
		email_id = session['email_id']
		x = int(0)
		#cur.execute("UPDATE users SET online=%s WHERE id=%s", (x, uid))
		admin.query.filter_by(e_mail_id=email_id).update(dict(status=x))
		db.session.commit()
		session.clear()
		flash('You are logged out', 'success')
		return redirect(url_for('admin_login'))
	return redirect(url_for('admin_login'))


@app.route("/admin/admin-dashboard")
@is_admin_logged_in
def admin_dashboard():
		get_total_user=db.session.query(func.count(users.user_mobile_no)).scalar()
		get_total_contact_us=contact_us.query.count()
		get_total_products=products.query.count()
		get_total_orders=orders.query.count()
		get_total_revenue=db.session.query(func.sum(orders.order_total_amt)).filter(orders.order_status == 'Completed').scalar()
		get_total_crops=crop.query.count()
		get_total_farming_info=research_info.query.count()
		get_total_e_learn=e_learn.query.count()
		
		total_upload_files=get_total_user+get_total_products+get_total_crops+get_total_farming_info+get_total_e_learn
		
		get_no_user = users.query.filter(extract('month', users.user_reg_date) == 3 ).count()
		get_no_user1 = users.query.filter(extract('month', users.user_reg_date) == 4 ).count()

		labels = ["January","February","March","April","May","June","July","August","September","October","November","December"]
		values = [0,0,get_no_user,get_no_user1,0,0,0,0,0,0,0,0]
		return render_template('pages/admin_dashboard.html',values=values,labels=labels,total_upload_files=total_upload_files,get_total_user=get_total_user,get_total_contact_us=get_total_contact_us,\
			get_total_products=get_total_products,get_total_orders=get_total_orders,get_total_revenue=get_total_revenue)

		

@app.route("/admin/product-mng/view-update-delete products" ,methods=['GET','POST'])
@is_admin_logged_in
def admin_product_mng():

		product_tb_details=products().query.all() 
		if 'product_id' in request.args:

			product_tb_details=products.query.get(int(request.args.get('product_id')))
			product_cat=product_category().query.all()
			brand_data=brand().query.all()
			return render_template('pages/Update-products.html',get_product_data=product_tb_details,product_category=product_cat,brand_data=brand_data) 
		elif 'delete_product_id' in request.args:
			p_del_id=request.args.get('delete_product_id')
			try:
				# order_detail_id=orders_details.query.filter(orders_details.product_id == int(p_del_id)).delete()
				
				get_p_data=db.session.query(products).get(int(p_del_id))
				product_del_img=get_p_data.product_img
				os.remove(os.path.join(app.config['UPLOAD_FOLDER'],'products/' + product_del_img))
				p_delete_details=products.query.filter(products.product_id == int(p_del_id)).delete()

				
			except IntegrityError:
				session.rollback()
			else:
				db.session.commit()
			return render_template('pages/admin_products_mng.html',product_tb_details=product_tb_details)   
		return render_template('pages/admin_products_mng.html',product_tb_details=product_tb_details)


@app.route("/admin/product-mng/add-product" ,methods=['GET','POST'])
@is_admin_logged_in
def admin_product_add():
	product_cat=product_category().query.all()
	brand_data=brand().query.all()

	if request.method == 'POST':

		p_img=request.files['file-upload-image']
		p_cat_name=request.form['product_category']

		p_name=request.form['product_name']
		p_stock=request.form['product_stock']
		p_price=request.form['product_price']
		p_description=request.form['product_description']
		p_related_crop=request.form['related_crop']
		p_brand_name=request.form['brand_name']

		print(p_cat_name)
		print(p_brand_name)

		if  p_img and p_cat_name and p_name and p_stock and p_price and p_description and p_related_crop and p_brand_name:


			if p_img and allowed_image_file(p_img.filename):


				# i=0
				# get_all_product_images=db.session.query(products).all()


				# if get_all_product_images:
				#     original=cv2.imread(p_img.filename)

				#     for get_all_product_image in get_all_product_images:
				#         p_file_name=str( app.config['UPLOAD_FOLDER'] + 'products/'+ get_all_product_image.product_img)
				#         print(p_file_name)
				#         duplicate_new=cv2.imread(p_file_name)
				#         if original.shape == duplicate_new.shape:
				#             difference = cv2.subtract(original, duplicate_new)
				#             b, g, r = cv2.split(difference)

				#             if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
				#                 print( "The images are completely Equal")
				#         else:
				#             flash('aleady this type image having in product list','success')
				#             return redirect('admin_product_add')
						
				ext_file=p_img.filename.rsplit('.',1)[1].lower()
				get_product_max_id=db.session.query(func.max(products.product_id)).scalar()
				if get_product_max_id is None:
					p_img.filename = p_img.filename + str(1) + '.' + ext_file
				else:
					p_img.filename = p_img.filename + str(get_product_max_id+1) + '.' + ext_file

					
				filename_image = secure_filename(p_img.filename)



				try:

					product_info_data=products(product_category_id=p_cat_name\
						,crop_related=p_related_crop\
						,product_brand_id=p_brand_name\
						,product_img=filename_image\
						,product_name=p_name\
						,product_stock=p_stock\
						,product_price=p_price,product_description=p_description)

					db.session.add(product_info_data)
					
				except IntegrityError:  
					session.rollback()
				else:   
					db.session.commit()

						
				p_img.save(os.path.join(app.config['UPLOAD_FOLDER'],'products/'+filename_image))    
			
				flash('New product added successfully','success')
				return redirect(url_for('admin_product_mng'))

			else:

				flash('please select valid format of image','danger');
				return redirect(url_for('admin_product_add'))

		else:
			flash('please fill all product related detail','danger');
			return redirect(url_for('admin_product_add'))
	else:
		return render_template('pages/admin_product_add.html',product_category=product_cat,brand_data=brand_data)

			
	return render_template('pages/admin_product_add.html',product_category=product_cat,brand_data=brand_data)


@app.route("/admin/product-mng/update_product",methods=['GET','POST'])
@is_admin_logged_in
def admin_product_up_data():


			if request.method == 'POST':           
				p_id=request.form['product_id']
				product_tb_details=products.query.get(int(p_id))
				product_cat=product_category().query.all()
				brand_data=brand().query.all() 
				p_img=request.files['file-upload-image']
				p_cat_name=request.form['product_category']
				p_name=request.form['product_name']
				p_stock=request.form['product_stock']
				p_price=request.form['product_price']
				p_description=request.form['product_description']
				p_related_crop=request.form['related_crop']
				p_brand_name=request.form['brand_name']
				print("true")

				if p_img and p_cat_name and p_name and p_stock and p_price and p_description and p_related_crop and p_brand_name:

					
						

					if p_img and allowed_image_file(p_img.filename):

						product_del_img=product_tb_details.product_img
						os.remove(os.path.join(app.config['UPLOAD_FOLDER'],'products/' + product_del_img))
						ext_file=p_img.filename.rsplit('.',1)[1].lower()
						p_img.filename = p_img.filename + str(p_id) + '.' + ext_file
						filename_image = secure_filename(p_img.filename)


						try:
							products.query.filter_by(product_id = p_id).\
							update(dict(product_category_id = p_cat_name,\
								crop_related=p_related_crop,product_brand_id=p_brand_name,product_img=filename_image,product_name=p_name,\
								product_stock=p_stock,product_price=p_price,product_description=p_description))
						except IntegrityError:
							session.rollback()
						else:
							db.session.commit()

						#products.edit_product(p_id,p_cat_name,p_related_crop,p_brand_name,filename_image,p_name,p_stock,p_price,p_description)
						p_img.save(os.path.join(app.config['UPLOAD_FOLDER'],'products/'+filename_image))
						flash('Successfully Updated product','success')
						return redirect(url_for('admin_product_mng'))       
					else:
							flash('please select valid format of image','danger')
							return render_template('pages/Update-products.html',get_product_data=product_tb_details,product_category=product_cat,brand_data=brand_data)
				else:
					flash('Fill all field', 'danger')
					return render_template('pages/Update-products.html',get_product_data=product_tb_details,product_category=product_cat,brand_data=brand_data)

			else:
				return redirect(url_for('admin_product_mng'))

@app.route('/admin/crop-mng/view-update-delete-crops',methods=['GET','POST'])
@is_admin_logged_in
def admin_crop_mng():
	crop_details=crop().query.all()
	if 'crop_id' in request.args:
		crop_details=crop.query.get(int(request.args.get('crop_id')))
		crop_cat=crop_category().query.all()
		return render_template('pages/Update-crops.html',crop_tb_details=crop_details,crop_category=crop_cat)
	elif 'delete_crop_id' in request.args:
		try:

			# order_detail_id=orders_details.query.filter(orders_details.product_id == int(p_del_id)).delete()
			get_c_data=db.session.query(crop).get(int(request.args.get('delete_crop_id')))
			crop_del_image=get_c_data.crop_image
			os.remove(os.path.join(app.config['UPLOAD_FOLDER'],'crops/' + crop_del_image))
			c_delete_details=crop.query.filter(crop.crop_id == int(request.args.get('delete_crop_id'))).delete()            
		except IntegrityError:
			session.rollback()
		else:
			db.session.commit()
		return render_template('pages/Crop_crop_mng.html',crop_tb_details=crop_details) 
	
	return render_template('pages/Crop_crop_mng.html',crop_tb_details=crop_details)

@app.route('/admin/crop-mng/add-crop',methods=['GET','POST'])
@is_admin_logged_in
def admin_crop_add():
	crop_category_data=crop_category.query.all()

	if request.method == 'POST':



		c_img=request.files['file-upload-image']

		c_cat_name=request.form['crop_category']
		c_name=request.form['crop_name']
		print(c_name)
		c_description=request.form['crop_description']
		print(c_description)
		print("true")

		if c_img and c_cat_name and c_name and  c_description :


	
			if c_img and allowed_image_file(c_img.filename):


				get_crop_max_id=db.session.query(func.max(crop.crop_id)).scalar()
				ext_file=c_img.filename.rsplit('.',1)[1].lower()
				if get_crop_max_id is None:

					c_img.filename = c_img.filename + str(1) + '.' + ext_file
				else:
					c_img.filename = c_img.filename + str(get_crop_max_id+1) + '.' + ext_file       
				filename_image = secure_filename(c_img.filename)




				try:

					add_crop_data=crop( crop_category_id = c_cat_name,crop_image=filename_image,\
								crop_name=str(c_name),crop_description=str(c_description))
					db.session.add(add_crop_data)
				except IntegrityError:
					session.rollback()
				else:

					db.session.commit()
					  
				c_img.save(os.path.join(app.config['UPLOAD_FOLDER'],'crops/'+ filename_image))
				flash('Successfully added crop detail','success')
				return redirect(url_for('admin_crop_mng'))      
			else:


				flash('please select valid format of image','danger')
				return redirect(url_for('admin_crop_add'))
		else:
			flash('Fill all field', 'danger')
			return redirect(url_for('admin_crop_add'))
	return render_template('pages/Crop_crop_add.html',crop_category_data=crop_category_data)

@app.route('/admin/crop-mng/update_crop',methods=['GET','POST'])
@is_admin_logged_in
def admin_crop_up_data():
	if request.method == 'POST':
				c_id=request.form['crop_id']
				crop_details=crop.query.get(int(c_id))
				crop_cat=crop_category().query.all()
				c_img=request.files['file-upload-image']
				c_cat_name=request.form['crop_category']
				c_name=request.form['crop_name']
				c_description=request.form['crop_description']
				print("true")

				if c_img and c_cat_name and c_name and  c_description :

	
					if c_img and allowed_image_file(c_img.filename):
						
						crop_del_image=crop_details.crop_image
						os.remove(os.path.join(app.config['UPLOAD_FOLDER'],'crops/' + crop_del_image))
						ext_file=c_img.filename.rsplit('.',1)[1].lower()
						c_img.filename = c_img.filename + str(c_id) + '.' + ext_file
						filename_image = secure_filename(c_img.filename)



						try:
							crop.query.filter_by(crop_id = c_id).\
							update(dict(crop_category_id=c_cat_name,crop_image=filename_image,\
								crop_name=c_name,crop_description=c_description))
						except IntegrityError:
							session.rollback()
						else:
							db.session.commit()

						#products.edit_product(p_id,p_cat_name,p_related_crop,p_brand_name,filename_image,p_name,p_stock,p_price,p_description)
						c_img.save(os.path.join(app.config['UPLOAD_FOLDER'],'crops/'+ filename_image))
						flash('Successfully Updated crop detail','success')
						return redirect(url_for('admin_crop_mng'))      
					else:
							flash('please select valid format of image','danger')
							return render_template('pages/Update-crops.html',crop_tb_details=crop_details,crop_category=crop_cat)
				else:
					flash('Fill all field', 'danger')
					return render_template('pages/Update-crops.html',crop_tb_details=crop_details,product_category=crop_cat)

	else:
				return redirect(url_for('admin_crop_mng'))




@app.route('/admin/user-mng/view-delete-users',methods=['GET','POST'])
@is_admin_logged_in
def admin_user_mng():
	user_tb_details=users().query.all()
	if 'user_mo_bo' in request.args:
		try:
			# order_detail_id=orders_details.query.filter(orders_details.product_id == int(p_del_id)).delete()
			get_u_data=db.session.query(users).get(int(request.args.get('user_mo_bo')))
			user_del_image=get_u_data.user_profile
			if user_del_image !='Farmer.jpg':
				os.remove(os.path.join(app.config['UPLOAD_FOLDER'],'users/' + user_del_image))
			u_delete_details=users.query.filter(users.user_mobile_no == int(request.args.get('user_mo_bo'))).delete()           
		except IntegrityError:
			session.rollback()
		else:
			db.session.commit()
			flash('Delete successfully','success')
		return render_template('pages/User_user_mng.html',user_tb_details=user_tb_details)  


	return render_template('pages/User_user_mng.html',user_tb_details=user_tb_details)

@app.route('/admin/user-mng/add-user',methods=['GET','POST'])
@is_admin_logged_in
def admin_user_add():
	form=Signup(request.form)
	populate_city_state(form)
  
	if request.method == 'POST' and form.validate():
		u_mobile_no=int(form.user_mobile_no.data)
		otp_input=int(form.user_otp.data)
		u_type=form.user_type.data
		if request.files['user_profile'] is None:
			u_profile=None
		else:
			u_profile=request.files['user_profile'] 
		u_full_name=form.user_full_name.data
		u_password=sha256_crypt.hash(str(form.user_password.data))
		u_city_id=int(form.user_city.data)
		user_address=form.user_address.data
		user_reg_already_check=users.query.get(u_mobile_no)
		if user_reg_already_check is None:
			if u_profile:
				if u_profile and allowed_image_file(u_profile.filename):
					ext_file=u_profile.filename.rsplit('.',1)[1].lower()
					u_profile.filename = u_profile.filename + str(u_mobile_no) + '.' + ext_file      
					filename_image = secure_filename(u_profile.filename)
					u_profile.save(os.path.join(app.config['UPLOAD_FOLDER'],'users/'+filename_image))

			try:
				user_data=users(user_mobile_no=u_mobile_no,user_type=u_type,user_profile=filename_image,user_full_name=u_full_name,user_password=u_password,user_city_id=u_city_id,user_address=user_address)
				print(user_data)
				db.session.add(user_data)   
			except IntegrityError:  
				session.rollback()
			else:   
				db.session.commit()
				
			flash('Successfully add new user','success')
			return redirect(url_for('admin_user_mng'))      
		else:
			flash( str(u_mobile_no) + ' mobile no. is already used please try another mobile no.','danger')
			render_template('pages/User_user_add.html',form=form)
	return render_template('pages/User_user_add.html',form=form)


@app.route('/admin/e-learn-mng/view-delete-video',methods=['GET','POST'])
@is_admin_logged_in
def admin_e_learn_mng():
	e_learn_details=e_learn().query.all()
	if 'e_learn_id' in request.args:
		try:
			# order_detail_id=orders_details.query.filter(orders_details.product_id == int(p_del_id)).delete()
			get_e_data=db.session.query(e_learn).get(int(request.args.get('e_learn_id')))
			e_del_image=get_e_data.e_learn_img_tmb
			e_del_video=get_e_data.e_learn_video
			os.remove(os.path.join(app.config['UPLOAD_FOLDER'],'video-tutorials/' + e_del_image))
			os.remove(os.path.join(app.config['UPLOAD_FOLDER'],'video-tutorials/' + e_del_video))
			e_delete_video=e_learn.query.filter(e_learn.e_learn_id == int(request.args.get('e_learn_id'))).delete()         
		except IntegrityError:
			session.rollback()
		else:
			db.session.commit()
			flash('Delete successfully','success')
		return render_template('pages/E-learn_e-learn_mng.html',e_learn_details=e_learn_details)

	return render_template('pages/E-learn_e-learn_mng.html',e_learn_details=e_learn_details)

@app.route('/admin/e-learn-mng/add-video',methods=['GET','POST'])
@is_admin_logged_in
def admin_add_e_learn_video():

	if request.method == 'POST':

		e_img=request.files['e_tmb']

		e_video=request.files['e_vid']


		e_name=request.form['e_learn_name']
		e_description=request.form['e_learn_description']
	

		if e_img and e_video and e_name and e_description:


			if e_img and allowed_image_file(e_img.filename):

				ext_file=e_img.filename.rsplit('.',1)[1].lower()
				e_learn_max_img_tmb=db.session.query(func.max(e_learn.e_learn_id)).scalar()
				if e_learn_max_img_tmb is None:
					e_img.filename = e_img.filename + str(1) + '.' + ext_file
				else:
					e_img.filename = e_img.filename + str(e_learn_max_img_tmb+1) + '.' + ext_file
					
				filename_image = secure_filename(e_img.filename)

				if e_video and allowed_video_file(e_video.filename):



						ext_file_vid=e_video.filename.rsplit('.',1)[1].lower()    
						if e_learn_max_img_tmb is None:
							e_video.filename = e_video.filename + str(1) + '.' + ext_file_vid
						else:
							e_video.filename = e_video.filename + str(e_learn_max_img_tmb+1) + '.' + ext_file_vid  
						filename_video = secure_filename(e_video.filename)





						try:
							e_learn_details=e_learn(e_learn_name=e_name,e_learn_description=e_description,\
								e_learn_img_tmb=filename_image,e_learn_video=filename_video)

							db.session.add(e_learn_details)
								
						except IntegrityError:  
							session.rollback()
						else:   
							db.session.commit()

									
						e_img.save(os.path.join(app.config['UPLOAD_FOLDER'],'video-tutorials/'+filename_image)) 
						e_video.save(os.path.join(app.config['UPLOAD_FOLDER'],'video-tutorials/'+filename_video))   
						
						flash('New video added successfully','success')
						return redirect(url_for('admin_e_learn_mng'))

				else:


					flash('please select validate format for video. ','danger')
					return redirect(url_for('admin_add_e_learn_video'))

			else:

				flash('please select valid format for image.','danger');
				return redirect(url_for('admin_add_e_learn_video'))

		else:
			flash('please fill all field to upload video','danger');
			return redirect(url_for('admin_add_e_learn_video'))
	else:
		return render_template('pages/E-learn_e-learn_add.html')

			
	return render_template('pages/E-learn_e-learn_add.html')


@app.route('/admin/product-mng/review-mng',methods=['GET','POST'])
@is_admin_logged_in
def admin_review_mng():
	review_tb_details=product_review().query.all()
	return render_template('pages/Review_Management.html',review_tb_details=review_tb_details)

@app.route('/admin/order-mng',methods=['GET','POST'])
@is_admin_logged_in
def admin_order_mng():
	#order_data=orders.query.all()
	#order_detail_data=orders_details.query.filter(orders_details.is_ordered==int(1)).all()
	payment_details=payment.query.all()
	if 'order_update_id' in request.args:
		try:
			orders.query.filter(orders.order_id == int(request.args.get('order_update_id')))\
			.update({orders.order_status:request.args.get('order_status')},synchronize_session = False)
			payment.query.filter(payment.order_id == int(request.args.get('order_update_id')))\
			.update({payment.payment_status:request.args.get('payment_status')},synchronize_session=False)
		except IntegrityError:
			session.rollback()
		else:
			db.session.commit()
			flash('Data updated successfully','success')
			return render_template('pages/Order_Management.html',payment_details=payment_details)      


	elif 'order_delete_id' in request.args:

		try:
			# order_detail_id=orders_details.query.filter(orders_details.product_id == int(p_del_id)).delete()
			orders.query.filter(orders.order_id == int(request.args.get('order_delete_id'))).delete()           
		except IntegrityError:
			session.rollback()
		else:
			db.session.commit()
			flash('Delete successfully','success')
		return render_template('pages/Order_Management.html',payment_details=payment_details)

	print(payment_details)
	return render_template('pages/Order_Management.html',payment_details=payment_details)


@app.route('/admin/order-mng/order-info/<string:orderid>',methods=['GET','POST'])
@is_admin_logged_in
def admin_order_mng_order_info(orderid):

	order_detail_data=orders_details.query.filter(orders_details.order_id == orderid).all()
   
	payment_details=payment.query.filter(payment.order_id == orderid).first()
  

	total_order_amt = 0
	for order_new_data in order_detail_data:
		total_order_amt += (order_new_data.products.product_price * order_new_data.quantity)


	if request.method == 'POST':
		o_status=request.form['order_status']
		p_status=request.form['payment_status']

		try:
			orders.query.filter(orders.order_id == orderid)\
			.update({orders.order_status:o_status},synchronize_session = False)
			payment.query.filter(payment.order_id == orderid)\
			.update({payment.payment_status:p_status},synchronize_session=False)
		except IntegrityError:
			session.rollback()
		else:
			db.session.commit()
			flash('Data updated successfully','success')
			return render_template('pages/Order_Management_order_info.html',payment_details=payment_details,order_detail_data=order_detail_data,t_o_amt=total_order_amt)      
			

	return render_template('pages/Order_Management_order_info.html',payment_details=payment_details,order_detail_data=order_detail_data,t_o_amt=total_order_amt)

@app.route('/admin/order-mng/order-invoice/<string:orderid>',methods=['GET','POST'])
@is_admin_logged_in
def admin_order_mng_order_invoice(orderid):
	
	order_detail_data=orders_details.query.filter(orders_details.order_id == orderid).all()
 
	payment_details=payment.query.filter(payment.order_id == orderid).first()
   

	total_order_amt = 0
	for order_new_data in order_detail_data:
		total_order_amt += (order_new_data.products.product_price * order_new_data.quantity)
	return render_template('pages/Order_Management_order_invoice.html',payment_details=payment_details,order_detail_data=order_detail_data,t_o_amt=total_order_amt)    

	


@app.route('/admin/contact-us-mng',methods=['GET','POST'])
@is_admin_logged_in
def admin_contact_us_mng():
	form = Contact_us(request.form)
	
	contact_us_data=contact_us().query.all()
	if request.method=="POST":
		 c_id=request.form['new_contact_id']
		 print(c_id)
		 c_a=str(form.answer.data)
		 print("*****",c_a)
		 contact_us.query.filter(contact_us.contact_id==c_id).update({contact_us.answer :c_a},synchronize_session=False)
		 db.session.commit()
		 flash('answer successfully sended','success')
		 return redirect(url_for('admin_contact_us_mng'))
	elif 'update_contact_id' in request.args:
		contactus_details = contact_us.query.filter(contact_us.contact_id == request.args.get('update_contact_id')).first()
		form.contact_id.data=contactus_details.contact_id
		form.question.data=contactus_details.question
		form.mobile_no.data=contactus_details.mobile_no
		form.name.data=contactus_details.name
		return render_template('pages/Contact_Us.html',contact_us_data=contact_us_data,form=form)
	elif 'delete_contact_id' in request.args:
		try:
			contact_us.query.filter(contact_us.contact_id == int(request.args.get('delete_contact_id'))).delete()
		except IntegrityError:
			session.rollback()
		else:
			db.session.commit()
		flash('data successfully deleted','success')	
		return redirect(url_for('admin_contact_us_mng'))	  
	return render_template('pages/Contact_Us.html',contact_us_data=contact_us_data,form=form)

@app.route("/admin/feedback-mng",methods=['GET','POST'])
def feeback_mng():
	feeback_data=feedback.query.all()
	return render_template('pages/Feedback_Management.html',feeback_data=feeback_data)

   











	

















