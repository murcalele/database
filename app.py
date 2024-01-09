from flask import *
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, LoginManager, login_user, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database4.db'
app.config['SECRET_KEY'] = 'secret_key_goes_here'
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.login_view = 'login_post'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Goods(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    good = db.Column(db.String(50), nullable=False)
    information = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    cost = db.Column(db.Integer(), nullable=False)
    
    
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    adress = db.Column(db.String(50), nullable=False)


class ShopList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    item = db.Column(db.Integer, db.ForeignKey(Goods.id), nullable=False)
    count = db.Column(db.Integer(), nullable=False)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", current_user=current_user.is_authenticated)


@app.route('/store')
def store():
    items = Goods.query.all()
    return render_template("store.html", items=items, current_user=current_user.is_authenticated)


@app.route('/furniture')
def furniture():
    furnitures = Goods.query.filter(Goods.type == "furniture").all()
    return render_template("furniture.html", furnitures=furnitures, current_user=current_user.is_authenticated)


@app.route('/furniture/<int:id>', methods=['POST', 'GET'])
def furniture_detail(id):
    furnit = Goods.query.get(id)
    if request.method == 'POST':
        current_order = ShopList.query.filter_by(user=current_user.id, item=furnit.id).first()
        
        if current_order:
            count = current_order.count + 1
            
            try:
                db.session.query(ShopList).filter(ShopList.id == current_order.id).update({ShopList.count: count}, synchronize_session=False)
                db.session.commit()
                return(redirect('/shopList'))
            except:
                return(redirect(url_for('furniture/<int:id>')))
        
        else:
            new_order = ShopList(user=current_user.id, item=furnit.id, count=1)
            
            try:
                db.session.add(new_order)
                db.session.commit()
                return(redirect('/shopList'))
            except:
                return(redirect('/furniture/<int:id>'))
                
    return render_template("furniture-detail.html", furnit=furnit, current_user=current_user.is_authenticated)


@app.route('/accessories')
def accessories():
    accs = Goods.query.filter(Goods.type == "accessories").all()
    return render_template("accessories.html", accs=accs, current_user=current_user.is_authenticated)


@app.route('/accessories/<int:id>', methods=['POST', 'GET'])
def accessorie_detail(id):
    acc = Goods.query.get(id)
    if request.method == 'POST':
        current_order = ShopList.query.filter_by(user=current_user.id, item=acc.id).first()

        if current_order:
            count = current_order.count + 1

            try:
                db.session.query(ShopList).filter(ShopList.id == current_order.id).update({ShopList.count: count}, synchronize_session=False)
                db.session.commit()
                return(redirect('/shopList'))
            except:
                return(redirect(url_for('accessories/<int:id>')))

        else:
            new_order = ShopList(user=current_user.id, item=acc.id, count=1)

            try:
                db.session.add(new_order)
                db.session.commit()
                return(redirect('/shopList'))
            except:
                return(redirect('/accessories/<int:id>'))
    return render_template("accessorie-detail.html", acc=acc, current_user=current_user.is_authenticated)


@app.route('/electronics')
def electronics():
    elecs = Goods.query.filter(Goods.type == "electronics").all()
    return render_template("electronics.html", elecs=elecs, current_user=current_user.is_authenticated)


@app.route('/electronics/<int:id>', methods=['POST', 'GET'])
def electronic_detail(id):
    elec = Goods.query.get(id)
    if request.method == 'POST':
        current_order = ShopList.query.filter_by(user=current_user.id, item=elec.id).first()

        if current_order:
            count = current_order.count + 1

            try:
                db.session.query(ShopList).filter(ShopList.id == current_order.id).update({ShopList.count: count}, synchronize_session=False)
                db.session.commit()
                return(redirect('/shopList'))
            except:
                return(redirect(url_for('electronics/<int:id>')))

        else:
            new_order = ShopList(user=current_user.id, item=elec.id, count=1)

            try:
                db.session.add(new_order)
                db.session.commit()
                return(redirect('/shopList'))
            except:
                return(redirect('/electronics/<int:id>'))
    return render_template("electronic-detail.html", elec=elec, current_user=current_user.is_authenticated)


@app.route('/information')
def information():
    return render_template("information.html", current_user=current_user.is_authenticated)


@app.route('/siteMap')
def sitemap():
    return render_template("siteMap.html", current_user=current_user.is_authenticated)


@app.route('/siteNews')
def sitenews():
    return render_template('siteNews.html', current_user=current_user.is_authenticated)


@app.route('/shopList', methods=['POST', 'GET'])
@login_required
def shoplist():
    id = current_user.id
    orders = ShopList.query.filter_by(user=id).all()
    items = Goods.query.order_by(Goods.id.desc()).all()
    
    if request.method == 'POST':
        current_order = ShopList.query.filter_by(user=id).first()
        while current_order:
            try:
                db.session.delete(current_order)
                db.session.commit()
                current_order = ShopList.query.filter_by(user=id).first()
            except:
                return(redirect('/shopList'))
        return(redirect('/shopList'))
    
    return render_template('shopList.html', orders=orders, items=items)


@app.route('/signup', methods=['POST', 'GET'])
def signup_post():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['mail']
        password = request.form['pass']
        adress = request.form['adress']

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Пользователь с таким e-mail уже зарегистрирован')
            return redirect('/signup')

        new_user = User(email=email, password=generate_password_hash(password), surname=surname, name=name, adress=adress)

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect('/')
        except:
            return redirect(url_for('signup_post'))
    else:
        return render_template("signup.html")


@app.route('/login', methods=['POST', 'GET'])
def login_post():
    if request.method == 'POST':
        email = request.form['mail']
        password = request.form['pass']
        remember = True if request.form['remember'] else False

        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            flash('Проверьте введённые данные')
            return redirect('/login')

        login_user(user, remember=remember)
        return redirect('/')

    else:
        return render_template("login.html")
    
    
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/index')