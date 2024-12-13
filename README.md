# Django RestFramework Phonebook

 Simple API to add contacts to a contact list to perform CRUD operations.

 Every contact is tied to the user who added it.

 First name and phone number are required while last name can be left blank.
 Country code is set as default to Italy, so leaving it blank will add '+39' in the field.

 If not logged in ReadOnly mode is shown so only GET method is allowed.
 To log in I added two users:
	-admin0 psw=admin0
	-admin1 psw=admin1

 There's no duplicate control, yet.
