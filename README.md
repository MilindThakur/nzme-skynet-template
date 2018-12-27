# skynet-template

This is a work in progress
What is this repository for?

    This project should be cloned to create a new emtpy project ready to write automated tests.
    Once cloned, push it to a new repo of your choice.

How do I get set up?

    Install google chrome.

    open a terminal window in the project root and run

    . installdriversLinux.sh

    Mac install script is here

    Ensure xcode has been installed and license accepted.
    . installdriversmac.sh

    Windows.... Tough, install a virtual machine of linux mint.

    Create a python virtualenv

    mkvirtualenv skynettemplate

    Install all python requirements

    pip install -r requirements.txt

How do i run a web test?

    Select the run configuration for webTests
    Click run or debug.
    This is just magic and will run with chrome as default. Firefox is available but updating the testsetup.ini

    To tests from the command line

    behave features/web/googlesearch.feature # Run a feature file
    behave --tags=@google # Run only tagged tests
    behave --tags=~@manual # Dont run tagged tests
    behave --tags=@google -D type=firefox -D baseurl=http://www.google.com  # Override testsetup fields in CLI
    nzme-behave-parallel -p 4 -t google -D type=firefox -D baseurl=http://www.google.com # Run tests parallel

How do i run a api test?

    Select the run configuration for apiTests
    Click run or debug.

    To tests from the command line

    behave features/api/searchcountryapi.feature # Run a feature file
    behave --tags=@api # Run only tagged tests
    behave --tags=~@api # Dont run tagged tests
    
Contribution guidelines

    This should be a static repo. If you have any improvements please communicate them to us.

Who do I talk to?

    Milind Thakur or Kumar Karthikeyan
