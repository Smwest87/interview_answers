<h1> Steven's Interview Answers</h1>


<h2> Feature Testing and Defects</h2>

<ol>
<li>Navigate to www.shipt.com. Choose a feature of the site and write a description or test case to describe how to test the feature.</li>
        Add Address Auto Complete
        Log into Shipt.com and navigate to Account>Addresses
        Select `Add Address`
        Input test address into `Start typing an address field` - attempt to use the autocomplete option
        Assert - Street Address, Unit/APT, City, State, Zip Code match test address
        Select Save
        Assert Address has been added to list of address
        Select test address 
        Assert selection of retailers display

<li>Locate one bug or bad workflow within the app.</li>
<ol>
<li>Explain the behavior you are seeing</li>

                        Very small User Experience issue but one that annoys me. Navigate to Account > Orders
                        Under the Past tab attempt to click on any of the elements above View Details but still in that specific order
                        Expected Result: User should be navigated to the Order Details Screen
                        Actual Result: No navigation occurrs - User must click the View Details to navigate to the Details Page

<li>Include any useful errors or screenshots</li>

                        [![Click Area](https://raw.githubusercontent.com/Smwest87/interview_answers/master/screenshot.png)]]

<li>Explain why and how it needs to be corrected</li>

                        The mobile app allows the user to select anywhere inside of the order element and be navigated to the details page. This feels natural to me
                        I would expect the same kind of functionality on Segway pages.
                        Make any area within the order div clickable to take the user to the details page.

<li>What are the steps you would take to report the issue?</li>

                        Build a clubhouse card for the Segway Team. I tested on Mobile Member App and the functionality was as expected.
                        Include the steps to reproduce, browser and my expected result

<li>What priority would you give this bug (Scale of 1-5, 1 being highest) and why?</li>

                        Priority would be a 5. This isn't going to prevent any kind of functionality and is just a mere annoyance. 
</ol>
<li>What are the possible reasons for the following defect? How would you go about debugging the problem and gathering more information?</li>
        On a web application, a user adds a phone number to their account. The user
        then changes the phone number. Upon trying to re-enter the first phone number,
        the user is allowed to click Save, and it seems to work, but the saved number
        remains the second number rather than updating to the more recently entered
        number. A page refresh does not change the result.

        My first thought is there is some check to see if the phone number exists in the phone_numbers table. If it does, maybe no other profile can have that phone number.
        So to confirm, open my console, reload the page. Select the Edit button and change the phone number to the original number.
        If an error appears in the console it will hopefully give me some information on where to look next. 
        I can also look at the database itself. Does the original phone number still exist in the database? Was it soft deleted?
        Ultimately there is some validation preventing the original phone number from being used on the back end. Otherwise we would see a error message on the front end. 
</ol>

<h2>SQL Questions - Answers</h2>

<ol>

<li>List me the stores allowed to sell alcohol</li>

        'SELECT id, name FROM interview.stores
        WHERE allowed_alcohol = True;'

<li>Give the product name of the 2 most expensive items based on their price at store id 1</li>

        SELECT p.name FROM interview.products p
        JOIN interview.store_prices sp on sp.product_id = p.id 
        WHERE sp.store_id = 1
        ORDER BY sp.price DESC
        LIMIT 2;

<li>List the products that are not sold in the store id 2</li>

        SELECT p.id, p.name FROM interview.products p
        JOIN interview.store_prices sp on sp.product_id = p.id
        WHERE store_id != 2 ;

<li>What is the most popular item sold?</li>

        SELECT ol.product_id, p.name,  sum(qty) as total_ordered FROM interview.order_lines ol
        JOIN interview.products p ON ol.product_id = p.id
        GROUP BY 1,2
        order by 3 desc
        LIMIT 1;

<li>Write a SQL statement to update the line_total field</li>

    UPDATE interview.order_lines ol
    SET line_total = subquery.line_total
    FROM (SELECT ol.id, ol.product_id, sp.price, ol.store_id, ol.qty, ol.qty * sp.price as line_total FROM interview.store_prices sp
		JOIN interview.order_lines ol on sp.product_id = ol.id) AS subquery
    WHERE subquery.id = ol.id;
</ol>


<h2>Automation Assessments</h2>
We recommend you choose from the following languages/tools. Feel free to use other tools if
you feel they lend better to this type of testing. Please try to do both automation assessments
listed below. Partial completion still counts for something, so please do what you can for both
parts.
<h3>UI Automation</h3>
Write an automated test which accomplishes the following
<ol>
<li>Access www.shipt.com in the browser</li>
<li>Using the feature you chose for step 1, write an automated test</li>
<li>The test should validate the feature works as expected</li>
</ol>
We recommend you choose from the following languages/tools. Feel free to use other tools if
you feel they lend better to this type of testing.
<ul>
<li>Selenium</li>
<li>Calabash</li>
<li>Typescript/Javascript</li>
<li>Ruby</li>
</ul>
<h3>API Automation</h3>
<strong>This has been completed in the api_automation folder.</strong>


        $pip install venv

        $python -m venv interview

        $source interview/bin/activate

        $pip install -r requirements.txt

        $cd api_automation

        $pytest



Using the Star Wars API https://swapi.co/documentation write a test that does the following:
<ul>
<li>Assert that Obi-Wan Kenobi was in the film A New Hope</li>
<li>Assert that the Enterprise is a starship (yes, this should fail)</li>
<li>Assert that Chewbacca is a Wookie</li>
<li>Assert that the /starships endpoint returns the fields below:</li>
<ul>
<li>name</li>
<li>model</li>
<li>crew</li>
<li>hyperdrive_rating</li>
<li>pilots</li>
<li>films</li>
<li>Assert that the /starships count returned is correct by paging through the results</li>
</ul>
</ul>

Feel free to use any language or helper package, but refrain from using tools such as Postman.
Please provide documentation on executing your automation and setting up any dependencies.
Recommended languages we use are below:
<ul>
<li>Python/Pytest</li>
<li>Ruby/Rspec</li>
<li>Go/Testify</li>
</ul>
<h3>Good assessments will have:</h3>
<ul>
<li>Dependency management</li>
<li>How to run documented in a readme</li>
<li>Clear test failure messages</li>
<li>Some reusable code on common actions (ex, logging or sending the HTTP request, interacting with browser)</li>
<li>A GitHub repo</li>
</ul>
<h3>Above and Beyond for API:</h3>
- Setup a mock server that uses the same request/response schemas as the real API and
run the same tests
<h2>Automation Assessment Follow Up Questions:</h2>
<ol>
<li>How did you go about locating the elements for your tests?</li>
<ol>
<li>Navigate to the page in my browser and select the element with element inspector</li>
<li>If the element has a unique id, name, class or other attribute and I use that to build my xpath</li>
<li>Otherwise I navigate to the partent div and look for unique identifiers and then follow that to the correct child</li>
</ol>
<li>What do you believe are the most common causes for instability in UI automation?</li>
<ol>
<li>time.sleep(n) versus using implicit waits. Sometimes pages take longer/shorter to load and either cause failures or extends the length of the test</li>
<li>Using xpaths that begin at the root of the page. Common with right click copy xpath instead of building your own xpath as close as you can to the desired element</li>
<li>Forgetting to maximise the browser window in the options parameter, especially in headless mode. This can result in the incorrect element receiving the click </li>
</ol>
<li>How do you make your tests consistent and easy to debug?</li>
<ol>
<li>Funcitons and classes. If all of my functions are defined in a single location I don't have to go back to multiple locations in the code and update/fix in the future</li>
<li>Comments. Comments in your code allow others to follow your train of thought and what you intended with the code. It also forces you to explain your code and can result in you finding your own mistakes</li>
<li>Just like functions and classes, define your xpaths/selectors in a different file/class. If all the xpaths/selectors are in one place you don't have to hunt through your code to find each xpath to update. </li>
</ol>
</ol>