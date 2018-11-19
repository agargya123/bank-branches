from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)

#from database import db
#from database import pass_param

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:hello@localhost:5432/bank_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


db = SQLAlchemy()

#pass_param(db)

#from Branch import Branch
#from bank import bank

class bank(db.Model):
    __tablename__='banks'
    name = db.Column('name',db.String(49)) #Unicode for varchar
    id = db.Column('id',db.Integer,nullable=False,primary_key=True)
    bank_branches = db.relationship( 'Branch',backref = 'bank',lazy='dynamic')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')  # Unicode for varchar
        self.id = kwargs.get('id')

class Branch(db.Model):
    __tablename__='branches'
    ifsc = db.Column('ifsc',db.String(11),primary_key=True) #Unicode for varchar
    bank_id = db.Column('bank_id',db.Integer,db.ForeignKey(bank.id),nullable=False)
    branch=db.Column('branch',db.String(174))
    address=db.Column('address',db.String(300))
    city = db.Column('city', db.String(50))
    district = db.Column('district', db.String(50))
    state = db.Column('state', db.String(26))

    def __init__(self,**kwargs):
        self.ifsc = kwargs.get('ifsc')
        self.bank_id = kwargs.get('bank_id')
        self.branch = kwargs.get('branch')
        self.address = kwargs.get('address')
        self.city = kwargs.get('city')
        self.district = kwargs.get('district')
        self.state = kwargs.get('state')

#db.create_all()
#db.session.commit()

@app.route('/',methods=['GET'])
def test():
    return jsonify({'m2':'For searching branch details via IFSC Code, go to /find_using_ifsc/IFSC no \n For searching branch details using Bank And City name, go to /find_using_city/bank,city'})

global branchinfo
@app.route('/find_using_ifsc/<string:ifsc>',methods=['GET'])
def branch_ifsc(ifsc):
    branchinfo = { }
    branchinfo = db.session.query(Branch).join(bank, bank.id == Branch.bank_id).add_columns(bank.name).filter(Branch.ifsc == ifsc).all()
    #branchinfo = db.session.query(branches).join(banks,banks.id==branches.bank_id).add_columns(banks.name).filter(branches.ifsc==ifsc).all()
    return jsonify (branchinfo)
    #db.session.query(bank).\join

@app.route('/find_using_city/<string:name>,<string:city>',methods=['GET'])
def branch_city(name,city):
    branchinfo = { }
    branchinfo = branches.query.join(banks,banks.id==branches.id).add_column(banks.name).filter(banks.name==name).filter(branches.city==city).all()
    return jsonify(branchinfo)




if __name__=='__main__':
    db.init_app(app)
    app.run(debug=True, port=8080)



'''
@app.route('/',methods=['GET'])
def test():
    return jsonify({'message':'It works!'})

@app.route('/lang',methods=['GET'])
def ret():
    return jsonify({'languages':languages}) #wrap languages in aonther dict

@app.route('/lang/<string:name>',methods=['GET'])
def returnname(name):
    langs=[language for language in languages if language['name']==name]
    return jsonify({'language':langs})'''