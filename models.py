from agrostar_app import *
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

class crop_category(db.Model):
    """docstring for crop_category"""
    __tablename__='crop_category'
    crop_category_id=db.Column(db.Integer,primary_key=True)
    crop_category_name=db.Column(db.String(20),nullable=False)
    

    def __repr__(self):
        return f"crop_category('{self.crop_category_name}')"


class crop(db.Model):
    __tablename__='crop'
    crop_id = db.Column(db.Integer, primary_key=True)
    crop_category_id=db.Column(db.Integer,db.ForeignKey('crop_category.crop_category_id'), nullable=False)
    crop_category = db.relationship('crop_category', backref='crop_category', lazy=True)
    crop_image=db.Column(db.String(50),nullable=False)
    crop_name=db.Column(db.String(25),nullable=False)
    crop_description=db.Column(db.Text,nullable=False)

    def __repr__(self):
        return f"crop('{self.crop_name}','{self.crop_image}','{self.crop_description}')"
    


class e_learn(db.Model):
            """docstring for e_learn"""
            __tablename__='e_learn'
            e_learn_id=db.Column(db.Integer,primary_key=True)
            e_learn_name=db.Column(db.String(25),nullable=False)
            e_learn_description=db.Column(db.Text,nullable=False)
            e_learn_img_tmb=db.Column(db.String(50),nullable=False)
            e_learn_video=db.Column(db.String(50),nullable=False)

            def __repr__(self):
                return f"e_learn('{self.e_learn_name}','{self.e_learn_description}','{self.e_learn_img_tmb}','{self.e_learn_video}')"
                    

class state(db.Model):
    """docstring for state"""
    __tablename__='state'
    state_id=db.Column(db.Integer,primary_key=True)
    state_name=db.Column(db.String(20),nullable=False)

    def __init__(self,state_name):
        self.state_name=state_name
        

class city(db.Model):
    """docstring for city"""
    __tablename__='city'
    city_id=db.Column(db.Integer,primary_key=True)
    state_id=db.Column(db.Integer,db.ForeignKey('state.state_id'),nullable=False)
    state=db.relationship('state',backref='state',lazy=True)
    city_name=db.Column(db.String(15),nullable=False)

    def __init__(self,state_id,city_name):
        self.state_id=state_id
        self.city_name=city_name
    
class users(db.Model):
    """docstring for users"""
    __tablename__='users'
    user_mobile_no=db.Column(db.Integer,primary_key=True)
    user_type=db.Column(db.String(25),nullable=False)
    user_profile=db.Column(db.String(50),nullable=False)
    user_full_name=db.Column(db.String(25),nullable=False)
    user_password=db.Column(db.String(80),nullable=False)
    user_city_id=db.Column(db.Integer,db.ForeignKey('city.city_id'),nullable=False)
    city=db.relationship('city',backref='city',lazy=True)
    user_address=db.Column(db.String(80),nullable=False)
    user_reg_date=db.Column(db.DateTime,nullable=False,default=datetime.utcnow())
    user_status=db.Column(db.Integer,nullable=True,default=int(0))

    # def __init__(self,user_mobile_no,user_type,user_profile,user_full_name,user_password,user_city_id,user_address,user_reg_date=None,user_status=0):
    #     self.user_mobile_no=user_mobile_no
    #     self.user_type=user_type
    #     self.user_profile=user_profile
    #     self.user_full_name=user_full_name
    #     self.user_password=user_password
    #     self.user_city_id=user_city_id
    #     self.user_address=user_address
    #     self.user_reg_date=datetime.utcnow()
    #     self.user_status=user_status


class research_info(db.Model):
    """docstring for research_info"""
    __tablename__='research_info'
    topic_id=db.Column(db.Integer,primary_key=True)
    topic_name=db.Column(db.String(50),nullable=False)
    topic_description=db.Column(db.Text,nullable=False)
    topic_img=db.Column(db.String(50),nullable=False)
    topic_video=db.Column(db.String(50),nullable=True)
    mobile_no=db.Column(db.Integer,db.ForeignKey('users.user_mobile_no'),nullable=False)
    users=db.relationship('users',backref='users',lazy=True)
    topic_upload_date=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

    def __init__(self,topic_name,topic_description,topic_img,topic_video,mobile_no,topic_upload_date=None):
        self.topic_name=topic_name
        self.topic_description=topic_description
        self.topic_img=topic_img
        self.topic_video=topic_video
        self.mobile_no=mobile_no
        self.topic_upload_date=datetime.utcnow()
        
        
class brand(db.Model):
    """docstring for brand"""
    __tablename__='brand'
    brand_id=db.Column(db.Integer,primary_key=True)
    brand_name=db.Column(db.String(25),nullable=False)

    #def __init__(self, brand_name):
     #   self.brand_name = brand_name

class product_category(db.Model):
    """docstring for product_category"""
    __tablename__='product_category'
    product_category_id=db.Column(db.Integer,primary_key=True)
    product_category_name=db.Column(db.String(25),nullable=False)

    def __repr__(self):
        return f"product_category('{self.product_category_name}')"    


class products(db.Model):
    """docstring for products"""
    __tablename__='products'
   

    product_id=db.Column(db.Integer,primary_key=True)
    product_category_id=db.Column(db.Integer,db.ForeignKey('product_category.product_category_id'),nullable=False)
    product_category=db.relationship('product_category',backref='product_category',lazy=True)
    crop_related=db.Column(db.String(50),nullable=True)
    product_brand_id=db.Column(db.Integer,db.ForeignKey('brand.brand_id'),nullable=False)
    brand=db.relationship('brand',backref='brand',lazy=True)
    product_img=db.Column(db.String(50),nullable=False)
    product_name=db.Column(db.String(50),nullable=False)
    product_stock=db.Column(db.Integer,nullable=False)
    product_price=db.Column(db.Float,nullable=False)
    product_description=db.Column(db.String(400),nullable=False)

    # def __init__(self, product_category_id,crop_related,product_brand_id,product_img,product_name,product_stock,product_price,product_description):
    #     self.product_category_id=product_category_id
    #     self.crop_related=crop_related
    #     self.product_brand_id=product_brand_id
    #     self.product_img=product_img
    #     self.product_name=product_name
    #     self.product_stock=product_stock
    #     self.product_price=product_price
    #     self.product_description=product_description

    @staticmethod   
    def edit_product(p_id,p_cat_id,c_related,p_b_id,p_img,p_name,p_stock,p_price,p_description):
        try:
            products.query.filter_by(product_id = p_cat_id).\
            update(dict(product_category_id = p_id,\
                crop_related=c_related,product_brand_id=p_b_id,product_img=p_img,product_name=p_name,\
                product_stock=p_stock,product_price=p_price,product_description=p_description))
        except IntegrityError:
            session.rollback()
        else:
            db.session.commit()

       

class orders(db.Model):
    """docstring for orders"""
    __tablename__='orders'
    order_id=db.Column(db.Integer,primary_key=True)
    order_no=db.Column(db.String(25),nullable=False)
    order_total_amt=db.Column(db.Float,nullable=False)
    mobile_no=db.Column(db.Integer,db.ForeignKey('users.user_mobile_no'),nullable=False)
    users=db.relationship('users',backref='order_user',lazy=True)
    name=db.Column(db.String(25),nullable=False)
    order_alt_mobile_no=db.Column(db.Integer,nullable=False)
    city_id=db.Column(db.Integer,db.ForeignKey('city.city_id'),nullable=False)
    city=db.relationship('city',backref='order_city',lazy=True)
    order_delivery_address=db.Column(db.String(80),nullable=False)
    order_date=db.Column(db.DateTime,nullable=False,default=datetime.utcnow())
    delivery_date=db.Column(db.DateTime,nullable=False)
    order_status=db.Column(db.String(25),nullable=False)
    #paid=db.Column(db.Integer,nullable=False)

class payment(db.Model):
    """docstring for payment"""
    __tablename__='payment'
    payment_id=db.Column(db.Integer,primary_key=True)
    order_id=db.Column(db.Integer,db.ForeignKey('orders.order_id'),nullable=False)
    orders=db.relationship('orders',backref='order_payment',lazy=True)
    transaction_id=db.Column(db.String(30),nullable=True)
    payment_method=db.Column(db.String(15),nullable=False)
    payment_date=db.Column(db.DateTime,nullable=False)
    payment_status=db.Column(db.String(25),nullable=False)  


class orders_details(db.Model):
    """docstring for order_details"""
    __tablename__='orders_details'
    order_product_id=db.Column(db.Integer,primary_key=True)
    mobile_no=db.Column(db.Integer,db.ForeignKey('users.user_mobile_no'),nullable=False)
    users=db.relationship('users',backref='orders_details_user',lazy=True)
    order_id=db.Column(db.Integer,db.ForeignKey('orders.order_id'),nullable=True)
    orders=db.relationship('orders',backref='orders',lazy=True)
    product_id=db.Column(db.Integer,db.ForeignKey('products.product_id',ondelete='CASCADE'),nullable=False)
    products=db.relationship('products',backref='products',lazy=True)
    quantity=db.Column(db.Integer,nullable=False)
    is_ordered=db.Column(db.Integer,default=0)
    is_cancelled=db.Column(db.Integer,default=0)


class user_wishlist(db.Model):
       """docstring for user_wishlist"""
       __tablename__='user_wishlist'
       wishlist_id=db.Column(db.Integer,primary_key=True)
       mobile_no=db.Column(db.Integer,db.ForeignKey('users.user_mobile_no'),nullable=False)
       users=db.relationship('users',backref='user_data_wishlist',lazy=True)
       product_id=db.Column(db.Integer,db.ForeignKey('products.product_id',ondelete='CASCADE'),nullable=False)
       products=db.relationship('products',backref='wishlist_product',lazy=True)    

class product_review(db.Model):

    """docstring for product_review"""
    __tablename__='product_review'
    review_id=db.Column(db.Integer,primary_key=True)
    product_id=db.Column(db.Integer,db.ForeignKey('products.product_id',ondelete='CASCADE'),nullable=False)
    products=db.relationship('products',backref='user_product_review',lazy=True)
    rating=db.Column(db.Integer,nullable=False)
    mobile_no=db.Column(db.Integer,db.ForeignKey('users.user_mobile_no',ondelete='CASCADE'),nullable=False)
    users=db.relationship('users',backref='user_review',lazy=True)
    review_description=db.Column(db.Text,nullable=False)

class feedback(db.Model):
    __tablename__='feedback'
    feedback_id=db.Column(db.Integer,primary_key=True)
    feedback_description=db.Column(db.String(40),nullable=False)
    mobile_no=db.Column(db.Integer,db.ForeignKey('users.user_mobile_no',ondelete='CASCADE'),nullable=False)
    users=db.relationship('users',backref='user_feedback',lazy=True)


class contact_us(db.Model):
    __tablename__='contact_us'
    contact_id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(25),nullable=False)
    mobile_no=db.Column(db.Integer,nullable=False)
    question=db.Column(db.Text,nullable=False)
    answer=db.Column(db.Text,nullable=False)




class admin(db.Model):
    __tablename__='admin'
    e_mail_id=db.Column(db.String(30),primary_key=True)
    password=db.Column(db.String(80),nullable=False)
    status=db.Column(db.Integer,nullable=False)

    def get_reset_token(self, expires_sec=300):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'admin_email_id': self.e_mail_id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            e_mail_id = s.loads(token)['admin_email_id']
        except:
            return None
        return admin.query.get(e_mail_id)    



       
                



       
                




       
                
