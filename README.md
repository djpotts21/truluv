![TruLuv Logo](/static/images/truluvlogo.png)
# TruLuv Dating
## Purpose:
At TruLove, we're all about bringing people together, no matter who they are or who they love. Our goal is simple: to create a dating app where everyone feels welcome and accepted. We want to give you a place to explore connections without worrying about being judged for who you are. TruLove is here to help you find your perfect match, whatever that looks like for you. So whether you're straight, gay, bi, trans, or anywhere in between, we've got your back. Let's make finding love easy and fun for everyone.

## Overview:
TruLove, our cutting-edge dating application, is built upon a sophisticated technical stack to provide users with a seamless and inclusive experience. TruLove utilises Heroku as its hosting platform, ensuring scalability, reliability, and effortless deployment. We rely on PostgreSQL (Postgres SQL) for its robust data storage, retrieval, and management features, ensuring data integrity and optimal performance.

Powering the backend infrastructure is Python Django, a high-level web framework renowned for its rapid development capabilities and security features. With Django, we effortlessly handle user authentication, data modelling through ORM (Object-Relational Mapping), routing, and templating, enabling us to focus on delivering a consistent and responsive user experience.

TruLove uses Bootstrap as its core on the front end, a leading front-end framework known for its mobile-first approach and extensive set of UI components and styles. We craft a visually appealing and intuitive user interface that seamlessly adapts to different devices and screen sizes by leveraging Bootstrap's grid system, typography, and CSS utilities.


## Wireframe
### Desktop Views
- [Home](/GitMedia/WireFrames/Desktop%20Wireframes/Home.png)
- [Liked You](/GitMedia/WireFrames/Desktop%20Wireframes/Liked%20You.png)
- [Login / Registration](/GitMedia/WireFrames/Desktop%20Wireframes/Login.png)
- [Messages](/GitMedia/WireFrames/Desktop%20Wireframes/Messages.png)
- [Profile Editor](/GitMedia/WireFrames/Desktop%20Wireframes/Profile%20Editor.png)
- [Settings](/GitMedia/WireFrames/Desktop%20Wireframes/Settings.png)
- [User Grid](/GitMedia/WireFrames/Desktop%20Wireframes/User%20Grid.png)
- [Profile](/GitMedia/WireFrames/Desktop%20Wireframes/Profile.png)
### Tablet Views
- [Home](/GitMedia/WireFrames/Tablet%20View/Home.png)
- [Liked You](/GitMedia/WireFrames/Tablet%20View/Liked%20You.png)
- [Login / Registration](/GitMedia/WireFrames/Tablet%20View/Login.png)
- [Messages](/GitMedia/WireFrames/Tablet%20View/Messages.png)
- [Profile Editor](/GitMedia/WireFrames/Tablet%20View/Profile%20Editor.png)
- [Settings](/GitMedia/WireFrames/Tablet%20View/Settings.png)
- [User Grid](/GitMedia/WireFrames/Tablet%20View/User%20Grid.png)
- [Profile](/GitMedia/WireFrames/Tablet%20View/Profile.png)
### Mobile Views
- [Home](/GitMedia/WireFrames/Mobile%20View/Home.png)
- [Liked You](/GitMedia/WireFrames/Mobile%20View/Liked%20You.png)
- [Login / Registration](/GitMedia/WireFrames/Mobile%20View/Home.png)
- [Messages](/GitMedia/WireFrames/Mobile%20View/Messages.png)
- [Profile Editor](/GitMedia/WireFrames/Mobile%20View/Profile%20Editor.png)
- [Settings](/GitMedia/WireFrames/Mobile%20View/Settings.png)
- [User Grid](/GitMedia/WireFrames/Mobile%20View/User%20Grid.png)
- [Profile](/GitMedia/WireFrames/Mobile%20View/Profile.png)

## User Stories
- [Link to User Stories PDF](/GitMedia/TruLuv%20User%20Stories.pdf)
- [Link to User Stories - Complete PDF](/GitMedia/TruLuv%20User%20Stories%20-%20Complete.pdf)

## Scope of Work
[Link to Scope of Work PDF](/GitMedia/Project%20Scope%20of%20Work%20-%20TruLuv.pdf)

## Live Link
[Visit the site live on Heroku](https://truluv-23cf9458fd34.herokuapp.com/)


## Final Screenshots
### Desktop Views
- [Home](/GitMedia/Live%20Screenshots/Desktop/home.png)
- [Login](/GitMedia/Live%20Screenshots/Desktop/accounts-login.png)
- [Log Out](/GitMedia/Live%20Screenshots/Desktop/accounts-logout.png)
- [Sign Up](/GitMedia/Live%20Screenshots/Desktop/accounts-signup.png)
- [Chats / Messages](/GitMedia/Live%20Screenshots/Desktop/chat.png)
- [Chats / Messages User to User](/GitMedia/Live%20Screenshots/Desktop/chat-user-2.png)
- [Likes](/GitMedia/Live%20Screenshots/Desktop/likes.png)
- [My Profile](/GitMedia/Live%20Screenshots/Desktop/myprofile.png)
- [Upgrade Account](/GitMedia/Live%20Screenshots/Desktop/upgradeaccount.png)
- [User Grid](/GitMedia/Live%20Screenshots/Desktop/usergrid.png)
- [View User Profile](/GitMedia/Live%20Screenshots/Desktop/viewuser-2.png)
### Tablet Views
- [Home](/GitMedia/Live%20Screenshots/Tablet/home.png)
- [Login](/GitMedia/Live%20Screenshots/Tablet/accounts-login.png)
- [Sign Up](/GitMedia/Live%20Screenshots/Tablet/accounts-signup.png)
- [Chats / Messages](/GitMedia/Live%20Screenshots/Tablet/chat.png)
- [Likes](/GitMedia/Live%20Screenshots/Tablet/likes.png)
- [My Profile](/GitMedia/Live%20Screenshots/Tablet/myprofile.png)
- [Upgrade Account](/GitMedia/Live%20Screenshots/Tablet/upgradeaccount.png)
- [User Grid](/GitMedia/Live%20Screenshots/Tablet/usergrid.png)
- [View User Profile](/GitMedia/Live%20Screenshots/Tablet/viewuser-3.png)
### Mobile Views
- [Home](/GitMedia/Live%20Screenshots/Mobile/home.png)
- [Login](/GitMedia/Live%20Screenshots/Mobile/accounts-login.png)
- [Sign Up](/GitMedia/Live%20Screenshots/Mobile/accounts-signup.png)
- [Chats / Messages](/GitMedia/Live%20Screenshots/Mobile/chat.png)
- [Likes](/GitMedia/Live%20Screenshots/Mobile/likes.png)
- [My Profile](/GitMedia/Live%20Screenshots/Mobile/myprofile.png)
- [Upgrade Account](/GitMedia/Live%20Screenshots/Mobile/upgradeaccount.png)
- [User Grid](/GitMedia/Live%20Screenshots/Mobile/usergrid.png)
- [View User Profile](/GitMedia/Live%20Screenshots/Mobile/viewuser-3.png)
- [Menu Mobile](/GitMedia/Live%20Screenshots/Mobile/menu.png)
## User Goals:
- Setup a dating profile
- View users based on distance from location
- Make secure payments using Stripe.

## Features:
- Responsive website design.
- Secure user authentication and authorization.
- E-commerce functionality for added features.
- Admin dashboard for managing users.
- Integration with Stripe for payment processing.

## Getting Started:
- Clone the repository to your local machine.
- Install dependencies with pip install -r requirements.txt.
- Set up a Stripe account and configure API keys.
- Setup AWS S3 Bucket
- Setup AWS RDS 
- Setup Fixie Proxy (https://usefixie.com/)
- Configure the Environment Variables as detailed in [Environment Variables.txt](/Environment%20Variables.txt)
### For Development
- Run migrations with python manage.py migrate.
- Start the Django development server with python manage.py runserver.
### For Production
- Start the Heroku server/dyno and the site will boot automatically.

## Automated Testing
There is a series of built-in testing in all major apps, please follow the guide below to run the tests. Note: This will fail if you do not disable RDS and AWS.

- Clone the repository to your local machine.
- Install dependencies with pip install -r requirements.txt.
- Set up a Stripe account and configure API keys.
- Setup AWS S3 Bucket
- Setup AWS RDS 
- Setup Fixie Proxy (https://usefixie.com/)
- Configure the Environment Variables as detailed in [Environment Variables.txt](/Environment%20Variables.txt)
- Remove USE_RDS and USE_AWS from the Environment Variables
- Run migrations with python manage.py migrate.
- Run Run migrations with python manage.py test.

## Acknowledgments / Attributes:

- [Brian Burns - JS Load Image Preview - Stackoverflow](https://stackoverflow.com/a/27165977)

