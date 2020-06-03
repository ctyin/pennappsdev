# Pennapps Dev Technical Challenge
Wrote a small Django app that authenticates users and allows them to post content to the feed.

## Structure
Created a custom model form for posts that saves them to the SQLite db whenever it's submitted. There is a single app called 'main' in the project which contains the templates, forms, models, and views. Boilerplate code is from https://pythonprogramming.net/django-web-development-python-tutorial/

## Known bugs
I had significant trouble with saving the provided User class as a foreign key in the Post. I ended up changing it so that posts just save the username field (so validity of a user is not checked by the database, only by the authentication form). You can view my attempt in the migration I believe

Another known 'bug' is just something I wasn't able to implement: post deletion. This gets fairly annoying when the db gets cluttered.
