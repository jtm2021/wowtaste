# WOW.taste blog

WOW.taste is a simple blog that features various exotic ingredients, spices and flavors all around the world. Each post in the blog features a certain food item or ingredient and highlights its description, characteristics and its uses. Users who are curious to read about each article can easily click on each post and they can opt to sign up and like any posts in the blog and they can leave a comment if they want to.

<img src="https://res.cloudinary.com/dborxc531/image/upload/v1665300300/README/mockup_fqy3bz.png">

## **CONTENTS**

<details>
<summary>
Table of Contents (click here to expand)
</summary>

- [Project Plan](#project-plan)
- [Features](#features)
- [Navigation](#navigation)
- [Footer Section](#footer-section)
- [Home Page](#home-page)
- [Register Page](#register-page)
- [Login/Logout Page](#loginlogout-page)
- [Likes/Comments](#likescomments)
- [Testing](#testing)
- [Agile Project Goals](#agile-project-goals)
- [Validator Testing](#validator-testing)
- [Deployment](#deployment)
- [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Content Information](#content-information)

</details>

<br>

## Project Plan ##

- ### User Stories ###
    - The User Stories of this project are divided into three categories depending on the site user: admin, unregistered (guest/visitor) or registered user. 
    - See the table below:
    <img src="https://res.cloudinary.com/dborxc531/image/upload/v1665229579/README/userstories_yun5ib.png">

- ### Wireframes ###
    - The wireframes for this project was made digitally using [**Figma**](https://www.figma.com/).

        <details><summary>Click here to see wireframes!</summary>
        <img src="https://res.cloudinary.com/dborxc531/image/upload/v1665083557/Wireframes/homepage_wnjiyz.png">
        <img src="https://res.cloudinary.com/dborxc531/image/upload/v1665083557/Wireframes/articlepage_fzi2ce.png">
        <img src="https://res.cloudinary.com/dborxc531/image/upload/v1665083557/Wireframes/register_xi7ahb.png">
        <img src="https://res.cloudinary.com/dborxc531/image/upload/v1665083557/Wireframes/login_woxmbv.png">
        </details>

- ### Database Structure ###
    - As seen on the diagram below, the tables show relationship between the site user, the post and the comments. 
      <img src="https://res.cloudinary.com/dborxc531/image/upload/v1665246146/README/databasestructure_cmncsh.png">
    
<br>


## Features ##
- ### The Header ###
    - The header of the page features the name of the blog.
    - This section is displayed on the left side of the page next to the navigation bar. 
    - The header is also clickable which redirects the user back to the main page.

    <img src="https://res.cloudinary.com/dborxc531/image/upload/v1665231097/README/header_kjidin.png">

<br>

- ### Navigation ###
    - The navigation bar is located next to the header. It is simple yet an effective feature of the website.
    - The navigation includes four links to different sections and these are accessible in each page.
    - This feature provides easy navigation for users from page to page across different devices.

    <img src="https://res.cloudinary.com/dborxc531/image/upload/v1665231201/README/nav_fspah1.png">

<br>


- ### Footer Section ###
    - The footer section of the blog is a simple section that provides a social media link to Facebook, YouTube and Twitter.
    
 
    <img src="https://res.cloudinary.com/dborxc531/image/upload/v1665247404/README/footer_sww6du.png">

<br>

- ### Home Page ###
    - The home page section features a welcome message of the blog with a button that redirect the users to the main articles.

    <img src="https://res.cloudinary.com/dborxc531/image/upload/v1665247818/README/home_pxz3kh.png">


<br>

- ### Register Page ###
    - This register page features a form for users to fill out if they want to sign up for the blog.
 
    <img src="https://res.cloudinary.com/dborxc531/image/upload/v1665247943/README/register_k4kefz.png">

<br>

- ### Login/Logout Page ###
    - This login page features a form for users to fill out if they want to log in. A message will also pop out to ask the users if they want to logout of the blog.
 
    <img src="https://res.cloudinary.com/dborxc531/image/upload/v1665248017/README/login_vd7wu1.png">
    <img src="https://res.cloudinary.com/dborxc531/image/upload/v1665248086/README/logout_p9swq1.png">

<br>

- ### Likes/Comments ###
    - This feature allows users to like and leave comments in each post.
    <img src="https://res.cloudinary.com/dborxc531/image/upload/v1665248204/README/likescomment_zuk83c.png">
    

<br>

## Testing ##

- I have tested this page in three different browsers including Chrome, Firefox and Microsoft Edge.
    - Firefox 

    <img src="https://res.cloudinary.com/dborxc531/image/upload/v1665248423/README/firefox_aylcku.png">

    - Microsoft Edge

    <img src="https://res.cloudinary.com/dborxc531/image/upload/v1665248337/README/edge_ptqw9v.png">

    - Google Chrome

    <img src="https://res.cloudinary.com/dborxc531/image/upload/v1665248267/README/chrome_tbeewg.png">

- I confirmed that the project is responsive and functions in various screen sizes using the devtools device toolbar.    
- I confirmed that the features of the website including the navigation bar, heading, contents and other sections are completely clear and easy to understand.
- I have confirmed that the signup form works.

<br>

## Agile Project Goals ##
- The project page was utilized in Github to serve as a guide in progressing through each stages of the project.

<img src="https://res.cloudinary.com/dborxc531/image/upload/v1665231296/README/agile_tdka0d.png">

<br>


### Validator Testing ###
- Javascript - The project only uses a small part of javascript and this was tested using [**JShint**](https://jshint.com/)
    <img src="https://res.cloudinary.com/dborxc531/image/upload/v1665231531/README/javascript_qusuyu.png">


- Python - There is ongoing issue with the official [**PEP8**](http://pep8online.com/) website to validate the Python code. So, as a workaround, PEP8 validator was added to my Gitpod workspace by these following steps:
    1. Run the command pip3 install pycodestyle.
    2. In the workspace, press Ctrl+Shift+P (or Cmd+Shift+P on Mac).
    3. Type the word linter into the search bar that appears, and click on Python: Select Linter from the filtered results.
    4. Select pycodestyle from the list.
    5. PEP8 errors will now be underlined in red, as well as being listed in the PROBLEMS tab beside your terminal.

    - As seen in the image below, there are no errors or problems detected in my workspace.
    
    <img src="https://res.cloudinary.com/dborxc531/image/upload/v1665240047/README/pythonvalidation_wstnkr.png">


<br>

## Deployment ##
This project was deployed initially to [**Heroku**](https://www.heroku.com/). However, due to the discontinuation of 
their free services, the data was eventually migrated using [**ElephantSQL**](https://www.elephantsql.com/) and the 
project was deployed to [**Render**](https://render.com/). Here are the steps below:

### I. DATABASE CREATION ###
- First, create the database with the following steps:
    1. Create an account in ElephantSQL.com to access your dashboard.
    2. Create new instance.
    3. Set up your plan by using Tiny Turtle (Free Plan) and leave the tags field blank.
    4. Select your region, then click "Review".
    5. Check your details are correct and then click "Create Instance".

### II. DATA MIGRATION ###
- Migration of data was achieved with a handy tool by Code Institute using the following steps:
    1. Navigate to the [** Postgres Migration Tool repo**](https://github.comCode-Institute-Orgpostgres-migration-tool) repo   on Github on a new browser.
    2. Click "Gitpod" buttton to open a new workspace.
    3. Run the script with the following command in the terminal: `python3 reel2reel.py`
    4. Open Heroku and navigate to your project's settings
    5. Click the "Reveal Config Vars" button.
    6. Copy the value in the DATABASE_URL Config Var. It will start with `postgres://`
    7. Return to Gitpod and paste in the URL you just copied into the terminal where prompted to provideyourDATABASE_URL and   click enter
    8. In your original browser tab, get your ElephantSQL database URL. Again, it will start with `postgres://`
    9. Return to Gitpod and paste in the URL where prompted. After hitting Enter, the data will now be downloadedfromHeroku    and uploaded to your ElephantSQL database.
    10. To test that your database has been moved successfully, return to ElephantSQL and select BROWSER
    11. Click the “Table queries” button. If you see any options in the dropdown, your tables have been created
    12. Select a table name you recognise, and then click “Execute”
    13. You should see your data displayed relating to the table you selected (You have successfully created a newdatabase   instance and migrated all your data)
    14. Now that your database is configured, you need to prepare your repository for deployment to Render. First,create a file     in the root directory of your repository called `build.sh`
    15. Paste in the following code to build.sh, then save the file.
        <img src="https://res.cloudinary.com/dborxc531/image/upload/v1668849009/README/build_sh_yzcyfb.png">
    16. In your settings.py file add the following code below the declaration of your ALLOWED_HOSTS variable
        <img src="https://res.cloudinary.com/dborxc531/image/upload/v1668849106/README/settings_py_sdiw4u.png">
    17. Unlike Heroku, Render does not require a Procfile - so you can delete this file.
    18. Add, commit and push your changes to GitHub.

### III. WEB SERVICE CREATION ###
- A web service allows a full stack application to be deployed. Connecting it to a repository on GitHub allows the repo to be built and deployed on Render’s hosting platform.
    1. Navigate to Render.com and log in.
    2. Click "New+".
    3. Click “Web Service”.
    4. Search for relevant repo and click “Connect. This will redirect to a new page with some fields to be completed. Ensure the following settings match.
    <img src="https://res.cloudinary.com/dborxc531/image/upload/v1668850241/README/deployment_settings_ddqblf.png">
    5. Set the BUILD COMMAND to:
        `./build.sh`
        <img src="https://res.cloudinary.com/dborxc531/image/upload/v1668850468/README/build_command_bozxpy.png">
    6. Set the BUILD COMMAND to:
        `gunicorn <PROJECT_NAME>.wsgi:application`
        <img src="https://res.cloudinary.com/dborxc531/image/upload/v1668850469/README/start_command_yqkz48.png">
    7. Ensure the Free plan $0/month is selected.
    

- The site was initially deployed to Heroku website. The steps to deploy are as follows done in the past:
    1. Open a web browser (like Chrome, Firefox or Edge)
    2. Login to Heroku and go to deploy tab.
    3. In the manual deploy section, choose main branch.
    4. Once the main branch has been selected, click the "Deploy Branch" button, wait for it to finish the process then a link will be provided for the completed website.

<br>

## Credits ##

### Content ###
- This project was inspired and based on Code Institute's `I Think Therefore I Blog` project.

### Media ###

- The images of the blog were taken from [**Pexels**](https://pexels.com/) and [**Wikipedia**](https://www.wikipedia.org/). The links are provided below:
    - https://www.pexels.com/photo/photo-of-truffles-on-the-plate-783153/
    - https://www.pexels.com/photo/food-vegetables-table-leaf-216368/
    - https://www.pexels.com/photo/black-caviar-and-cheese-on-crackers-4161713/
    - https://www.pexels.com/photo/coffee-beans-on-round-wok-2711959/
    - https://www.pexels.com/photo/close-up-of-abalone-rice-hot-pot-8896087/
    - https://www.pexels.com/photo/burger-and-smoothie-with-bowl-of-dried-bananas-and-dates-4553020/
    - https://www.pexels.com/photo/burger-and-smoothie-with-bowl-of-dried-bananas-and-dates-4553020/
    - https://www.pexels.com/photo/autumn-composition-with-assorted-pumpkins-and-bread-in-basket-placed-on-plaid-on-grassy-lawn-7245432/
    - https://www.pexels.com/photo/spoiled-orange-beside-cinnamon-3640474/
    - https://www.pexels.com/photo/lipstick-tree-with-seed-pods-in-garden-7498671/
    - https://en.wikipedia.org/wiki/Foie_gras#/media/File:Foie_gras_en_cocotte.jpg
    - https://en.wikipedia.org/wiki/Ghost_pepper#/media/File:Bhut-Jolokia-pc.jpg
    - https://www.pexels.com/photo/brown-wooden-chopping-board-with-meat-on-top-1314041/
    - https://en.wikipedia.org/wiki/Houttuynia_cordata#/media/File:Houttuynia_cordata.jpg
    - https://en.wikipedia.org/wiki/Asafoetida#/media/File:Asafoetida2.jpg

### Content Information ###

- The site content information are sourced from Wikipedia. See links below:
    - https://en.wikipedia.org/wiki/Tuber_melanosporum
    - https://en.wikipedia.org/wiki/Black_garlic#:~:text=Black%20garlic%20is%20a%20type,that%20results%20in%20black%20cloves.
    - https://en.wikipedia.org/wiki/Beluga_caviar
    - https://en.wikipedia.org/wiki/Abalone
    - https://en.wikipedia.org/wiki/Kopi_luwak
    - https://en.wikipedia.org/wiki/Bixa_orellana
    - https://en.wikipedia.org/wiki/Gochujang
    - https://en.wikipedia.org/wiki/Foie_gras
    - https://en.wikipedia.org/wiki/Ghost_pepper
    - https://en.wikipedia.org/wiki/Venison
    - https://en.wikipedia.org/wiki/Houttuynia_cordata
    - https://en.wikipedia.org/wiki/Asafoetida
