from flask_script import Manager
from resume import app, db, Professor, Course

manager = Manager(app)


# reset the database and create two artists
@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    hartono = Professor(name='Edward Hartono', dept='MIS')
    dragone = Professor(name='Debra Dragone', dept='Accounting')
    fang = Professor(name='Xiao Fang', dept='MIS')
    wang = Professor(name='Harry Wang', dept='MIS')
    MISY330 = Course(number='MISY330', title='Database Design and Implementation', desc='Covers the design and implementation of enterprise databases in the business environment. A networked setting and its effect on database management will be emphasized.', professor=fang)
    MISY350 = Course(number='MISY350', title='Business Application Development II', desc='Covers concepts related to client side development, including cascading style sheets and JavaScript.', professor=wang)
    MISY160 = Course(number='MISY160', title='Business Computing: Tools and Concepts', desc='Introduction to coputers" components and operations', professor=hartono)
    ACCT208 = Course(number='ACCT208', title='Accounting II', desc='Introduction to Managerial Accounting', professor=dragone)
    db.session.add(hartono)
    db.session.add(dragone)
    db.session.add(fang)
    db.session.add(wang)
    db.session.add(MISY330)
    db.session.add(MISY350)
    db.session.add(MISY160)
    db.session.add(ACCT208)
    db.session.commit()


@manager.command
def hello():
    print "hello"


if __name__ == "__main__":
    manager.run()
