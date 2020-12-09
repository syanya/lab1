from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='111111', server='localhost', database='bank_test')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
## app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:111111@localhost:3306/LocalDB'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Customers(db.Model):
    __tablename__ = 'customers'
    Id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False )
    Login = db.Column(db.String(20), unique=True, nullable=False )
    FirstName = db.Column(db.String(120), unique=False, nullable=False)
    LastName = db.Column(db.String(120), unique=False, nullable=False)

    BankAccountIds = db.relationship("BankAccounts", secondary="bank_customers_match", backref="customers")
    session = db.relationship("Sessions", backref="customers")

class Sessions(db.Model):
    __tablename__ = 'sessions'
    Id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False )
    Login = db.Column(db.String(20), db.ForeignKey(Customers.Login), unique=True, nullable=False )
    CreateDate = db.Column(db.String(80), unique=False, nullable=False)
    ExpireDate = db.Column(db.String(120), unique=False, nullable=False)
    SecureToken = db.Column(db.String(40), unique=True, nullable=False)

class BankAccounts(db.Model):
    __tablename__ = 'bankaccounts'
    Id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    Type = db.Column(db.String(80), unique=False, nullable=False)
    Balance = db.Column(db.Float, unique=False, nullable=False)
    Currency = db.Column(db.String(120), unique=False, nullable=False)

    customerIds = db.relationship("Customers", secondary="bank_customers_match", backref="BankAccounts")

class BankCustomersMatch(db.Model):
    __tablename__ = 'bank_customers_match'
    Id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    BankAccountId = db.Column(db.Integer, db.ForeignKey(BankAccounts.Id), nullable=False)
    CustomerId = db.Column(db.Integer, db.ForeignKey(Customers.Id), nullable=False)

    # customers_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    # customers = db.relationship("Customers", backref=db.backref('bank_customers_match', lazy=True))

    # bankAccounts_id = db.Column(db.Integer, db.ForeignKey('bankAccounts.id'), nullable=False)
    # bankAccounts = db.relationship("BankAccounts", primaryjoin="(BankCustomersMatch.BankAccountId ==BankAccounts.Id)", backref="bank_customers_match")


class Transactions(db.Model):
    __tablename__ = 'transactions'
    Id = db.Column(db.Integer, primary_key=True, unique=True, nullable=True)
    Date = db.Column(db.DateTime, unique=False, nullable=False)
    Amount = db.Column(db.Float, unique=False, nullable=True)
    FromAccountId = db.Column(db.Integer, unique=False, nullable=False)
    ToAccountId = db.Column(db.Integer, unique=False, nullable=False)

db.create_all()

# Create a session
#jwk_trans = BankAccounts(Type='family', Balance='3000000.51', Currency='EUR')
# db.session.add(jwk_trans)
# db.session.commit()

@app.route("/api/v1/hello-world-29")
def hello():
    return "Hello World 29"

@app.route("/api/accountinfo/<int:id>")
def getAccountInfo(id):
    customer = db.session.query(Customers).get(id)

    return {
            'FirstName': customer.FirstName,
            'LastName': customer.LastName,
            'Balance': customer.BankAccounts[0].Balance,
            'Currency': customer.BankAccounts[0].Currency
        }

if __name__ == '__main__':
    app.run(debug=True)