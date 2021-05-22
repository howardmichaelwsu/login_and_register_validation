from django.db import models
import re
import bcrypt
EMAIL_REGEX =re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
	def validate(self, form):
		errors = {}
		if len(form['first_name']) < 2:
			errors['first_name'] = 'First name must be at least 2 characters'
		if len(form['last_name']) < 2:
			errors['last_name'] = 'Last name must be at least 2 characters'
		if not EMAIL_REGEX.match(form['email']):
			errors['email'] = 'Invaild email'
		email_check = self.filter(email.form['email'])
		if email_check:
			errors['email'] ='Email already in use'
		if len(form['password']) < 8:
			errors['password'] 'Password must be 8 characters or longer'
		if form['password'] != form['confirm']:
			errors['password'] = 'Passwords do not match bro'
		return errors

def authenticate(self, email, password):
		users = self.filter(email=email)
		if not users:
			return False

		user = users[0]
		return bcrypt.checkpw(password.encode(), user.password.encode())

def register(self, form):
	pw = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt()).decode()
	return self.create(
		first_name = form['first_name'],
		last_name = form['last_name'],
		email = form['email'],
		password = pw,
	)

class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=255)

	objects = UserManager()



# Create your models here.
