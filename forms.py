from agrostar_app import *

class Admin_login(Form):
	e_mail_id=StringField('Emaill Id <color style="color:red;">*</color>',
		[validators.InputRequired(),validators.Email('Enter valid emaiil')])
	password=PasswordField('Password <color style="color:red;">*</color>',[
		validators.DataRequired(),
		validators.Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',message='please enter valid Password \n\n\n\n\n 1.At least one upper case English letter, (?=.*?[A-Z]) \n\n\n\n\n  2.At least one lower case English letter, (?=.*?[a-z]) \n\n\n\n\n 3.At least one digit, (?=.*?[0-9])\n\n\n\n\n4.At least one special character, (?=.*?[#?!@$%^&*-])\n\n\n\n\n 5.Minimum eight in length .{8,} (with the anchors)')])


	

class Signup(Form):
	"""docstring for Signup"""
  
	user_type=SelectField('User Type <color style="color:red;">*</color>',[validators.InputRequired()],
		choices=[('Farmer','Farmer'),('Agriculture Scientist','Agriculture Scientist')])

	user_full_name=StringField('Your Name <color style="color:red;">*</color>',
		[validators.InputRequired()])

	user_mobile_no=TelField('Mobile No <color style="color:red;">*</color>',
		[validators.InputRequired(),validators.length(min=10,max=10,message='mobile no. must in 10 digit.'),validators.Regexp('^([6789]{1})([0-9]{1})([0-9]{8})$',message='please enter valid mobile no.')])

	user_otp=IntegerField('Enter OTP <color style="color:red;">*</color>',
		[validators.InputRequired()], render_kw={'maxlength': 4,'size':4})

	user_city=SelectField('City <color style="color:red;">*</color>',
		[validators.InputRequired()],coerce=int)

	user_state=SelectField('State <color style="color:red;">*</color>',
		[validators.InputRequired()],coerce=int)

	user_address=TextAreaField('Address <color style="color:red;">*</color>',
		[validators.InputRequired()])
	user_password=PasswordField('Password <color style="color:red;">*</color>',[
		validators.DataRequired(),
		validators.Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',message='please enter valid Password \n\n\n\n\n 1.At least one upper case English letter, (?=.*?[A-Z])\n\n\n\n\n2.At least one lower case English letter, (?=.*?[a-z])\n\n\n\n\n3.At least one digit, (?=.*?[0-9])\n\n\n\n\n4.At least one special character, (?=.*?[#?!@$%^&*-])\n\n\n\n\n5.Minimum eight in length .{8,} (with the anchors)'),
		validators.EqualTo('user_confirm_password',message='Password do not match')])
	user_confirm_password = PasswordField('Confirm Password <color style="color:red;">*</color>',[validators.DataRequired()])
		



class LoginForm(Form):  # Create Login Form
	user_mobile_no=TelField('Mobile No <color style="color:red;">*</color>',
		[validators.InputRequired(),validators.length(min=10,max=10,message='mobile no must in 10 digit.'),validators.Regexp('^([6789]{1})([0-9]{1})([0-9]{8})$',message='please enter valid mobile no')])
	user_password=PasswordField('Password <color style="color:red;">*</color>',[
		validators.DataRequired(),
		validators.Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',message='please enter valid Password<br>1.At least one upper case English letter, (?=.*?[A-Z])<br>2.At least one lower case English letter, (?=.*?[a-z])<br>3.At least one digit, (?=.*?[0-9])<br>4.At least one special character, (?=.*?[#?!@$%^&*-])<br>5.Minimum eight in length .{8,} (with the anchors)')])


class Forgot_Password(Form):
	"""docstring for Forgot_Password"""
	user_password=PasswordField('Password ',
		[validators.DataRequired(),
		validators.Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',message='please enter valid Password<br>1.At least one upper case English letter, (?=.*?[A-Z])<br>2.At least one lower case English letter, (?=.*?[a-z])<br>3.At least one digit, (?=.*?[0-9])<br>4.At least one special character, (?=.*?[#?!@$%^&*-])<br>5.Minimum eight in length .{8,} (with the anchors)'),
		validators.EqualTo('user_confirm_password',message='Password do not match')])
	user_confirm_password = PasswordField('Confirm Password',[validators.DataRequired()])
	   
	
class Products(Form):
	product_category_name=SelectField('Product Category <color style="color:red;">*</color>',[validators.InputRequired()],coerce=int)
	product_name=StringField('Product Name <color style="color:red;">*</color>',[validators.InputRequired()])
	product_stock=IntegerField('Product Stock  <color style="color:red;">*</color>',[validators.InputRequired()])
	product_price=IntegerField('Product Price  <color style="color:red;">*</color>', [validators.InputRequired()])
	product_description=TextAreaField('Product Description  <color style="color:red;">*</color>',[validators.InputRequired()])
	related_crop=SelectMultipleField('Related Crop <color style="color:red;">*</color>',[validators.InputRequired()],coerce=int)
	brand_name=SelectField('Brand <color style="color:red;">*</color>',[validators.InputRequired()],coerce=int)

class Checkout_Form(Form):
	"""docstring for Checkout-Form"""
	name=StringField(' Name <color style="color:red;">*</color>',
		[validators.InputRequired()])

	order_alt_mobile_no=TelField('Mobile No <color style="color:red;">*</color>',
		[validators.InputRequired(),validators.length(min=10,max=10,message='mobile no must in 10 digit.'),validators.Regexp('^([6789]{1})([0-9]{1})([0-9]{8})$',message='please enter valid mobile no')])

	user_city=SelectField('City <color style="color:red;">*</color>',
		[validators.InputRequired()],coerce=int)

	user_state=SelectField('State <color style="color:red;">*</color>',
		[validators.InputRequired()],coerce=int)

	order_delivery_address=TextAreaField('Address <color style="color:red;">*</color>',
		[validators.InputRequired()])


class Userprofile(Form):
	"""docstring for Signup"""
  
	user_full_name=StringField('Your Name <color style="color:red;">*</color>',
		[validators.InputRequired()])

	user_mobile_no=TelField('Mobile No <color style="color:red;">*</color>',
		[validators.InputRequired(),validators.length(min=10,max=10,message='mobile no must in 10 digit.'),validators.Regexp('^([6789]{1})([0-9]{1})([0-9]{8})$',message='please enter valid mobile no')])


	user_city=SelectField('City <color style="color:red;">*</color>',
		[validators.InputRequired()],coerce=int)

	user_state=SelectField('State <color style="color:red;">*</color>',
		[validators.InputRequired()],coerce=int)

	user_address=TextAreaField('Address <color style="color:red;">*</color>',
		[validators.InputRequired()])
	user_old_password=PasswordField('Old Password <color style="color:red;">*</color>',[
		validators.Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',message='please enter valid Password<br>1.At least one upper case English letter, (?=.*?[A-Z])<br>2.At least one lower case English letter, (?=.*?[a-z])<br>3.At least one digit, (?=.*?[0-9])<br>4.At least one special character, (?=.*?[#?!@$%^&*-])<br>5.Minimum eight in length .{8,} (with the anchors)'),
		])
	user_new_password=PasswordField('New Password <color style="color:red;">*</color>',[
		validators.Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',message='please enter valid Password<br>1.At least one upper case English letter, (?=.*?[A-Z])<br>2.At least one lower case English letter, (?=.*?[a-z])<br>3.At least one digit, (?=.*?[0-9])<br>4.At least one special character, (?=.*?[#?!@$%^&*-])<br>5.Minimum eight in length .{8,} (with the anchors)'),
		])


class Contact_us(Form):
	contact_id=IntegerField()
	name= StringField('Name <color style="color:red;">*</color>',[validators.InputRequired()])
	mobile_no=IntegerField('Mobile no <color style="color:red;">*</color>',[validators.InputRequired()])
	question=TextAreaField('Question <color style="color:red;">*</color>',[validators.InputRequired()])
	answer = TextAreaField('Answer <color style="color:red;">*</color>')	





	
		
				
