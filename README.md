# Google-Form-Management
SSL PROJECT

Clone the repository on the machine using git clone or download ZIP
Inside the directory created, open a terminal and run the following command:
$ python manage.py runserver

The URL generated will be the link to the product. You can sign up/login and then create your own forms/change password/edit profile/
create questions of modular kind in your form.

The link generated for forms can be shared by you for people to fill in. And the responses will be stored and you can click on 
"Export CSV" to see them in a csv file (view responses) or also see the data in form of pie chart/bar graphs.

You can add collabarators to your form(s) as well.

The feature of conditional forms has been provided there, using which you can ask for options in form, only if some options have been selected in a particular way.

Form Validation allows you to be specific about the responses required, for example:
- Numeric
- EMail
- .pdf extension
- Alphanumeric

For database details, you can go to db.sqlite3 and see relevant the tables.

We have two tables:
1. One with Form ID and User ID
2. One with Form ID and Questions with all its information (Necessity, Visiblilty, Text, Type, Choice)

If you want to run it on another system, connected to the same ip address,
then you can add it's ip address to ALLOWED_HOSTS in settings.py 
