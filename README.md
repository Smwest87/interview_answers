# interview_answers

<h1> Automation Installation and Execution</h1>

<h2> UI Automation</h2> 
I'm not satisfied with everything in the UI automation with Selenium but I've unfrotunately run out of time. 

I've chosen to use Selenium and Python and I'm attempting to test the autocomplete address in the account section. 

<h3>Steps to install: </h3>

<ol>
<li>Create a virtual environment for python </li>

        $pip install venv

        $python -m venv interview

        $source interview/bin/activate

        $pip install -r requirements.txt

This will cover all requirements for both the UI automation and the API automation

<li>cd to UI Automation folder in terminal</li>
<li>Create credentials.py file and add login credentials in a creds dictionary</li>
    creds = {
        'username' : 'username',
        'password' : 'password'
    }
<li>Run app.py</li>
        $python app.py
</ol>

This should log into shipt.com, navigate to addresses and add a new address. I ran into some problems with assertions but I'm on the path to debugging it. For some reason get_attribute isn't actually giving a string back.

<h2> API Automation</h2>

Installation has already been complete when we first created the virtual environment earlier. Just make sure you are still referencing that environment as your source 

<ol>
<li> cd to api_automation folder</li>
<li> run pytest</li>
        $pytest
</ol>

This will run 5 tests, where the Enterprise test will fail. I need to make better error messages for the failing test or for potential failures.
