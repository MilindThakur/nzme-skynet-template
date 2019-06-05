# **skynet-template - Template for test repository**

## **What is this repository for?**

    This project should be cloned to create a new emtpy project ready to write automated tests using 
    nzme-skynet automation package. Once cloned, push it to a new repo of your choice.

## **How do I setup?**

### **Install pip, web browsers, docker, docker-compose, emulators etc (as required)**
* [Follow these instructions](https://github.com/seleniumbase/SeleniumBase/blob/master/help_docs/requirements_installation.md) to install pip, git, virtualenv/virtualenvwrapper
* Download [Chrome browser](https://www.google.com/chrome/browser/desktop/index.html) and [Chrome Driver](https://sites.google.com/a/chromium.org/chromedriver/)
* Download Firefox. Firefox > v.47 requires [Marionette](https://developer.mozilla.org/en-US/docs/Mozilla/QA/Marionette) driver
* To verify drivers are working [check these instructions](https://github.com/seleniumbase/SeleniumBase/blob/master/help_docs/verify_webdriver.md)
* Install [mobile dependencies](docs/howto_mobile_tests.md) or docker solution e.g. [Selenoid Android](https://aerokube.com/selenoid/latest/#_android),
[docker-android](https://github.com/budtmo/docker-android)
* (optional) Install Selenium Grid of choice e.g. [Zalenium](https://github.com/zalando/zalenium),
[Selenoid](https://github.com/aerokube/selenoid), [docker-selenium](https://github.com/SeleniumHQ/docker-selenium) etc

### **Setup local test repo**
    git clone <this_repo>
    cd skynet-template
    mkvirtualenv skynet-template-env
    pip install -r requirements.txt

### **Setup test environment**
* If running web tests locally, make sure the browser and appropriate drivers are installed locally.
* If wish to run a local grid, you can use any grid setup of your choice, Examples of using grids like
Zalenium and Selenoid are provided below.


    # Zalenium
    docker-compose -f docker-compose-zalenium.yaml up -d
    
    # Selenoid
    docker-compose -f docker-compose-selenoid.yml up -d 

## **How do I run a web test?**
* Setup the test configuration of your choice in _testsetup.ini_ by specifying the appropriate
field values.

 For Local tests
 
    #------- Desktop Platforms -------#
    [BROWSER]
    #- Generic Selenium/Cloud capabilities -#
    capabilities =  {
                    "browserName": "chrome",
                    "version": "ANY"
                    }
    #- Framework specific capabilities -#
    highlight = true
    resolution = maximum
    headless = false
    mobileEmulation =
    
    #------- Environmental -------#
    #- Framework specific capabilities -#
    [ENVIRONMENT]
    testurl=https://www.google.co.nz/
    local=true
    selenium_grid_hub=http://127.0.0.1:4444/wd/hub
    zalenium=false
    
 For grid based tests (e.g. using Selenoid)
 
    #------- Desktop Platforms -------#
    [BROWSER]
    #- Generic Selenium/Cloud capabilities -#
    capabilities =  {
                    "browserName": "chrome",
                    "version": "73.0",
                    "enableVNC": True
                    }
    #- Framework specific capabilities -#
    highlight = true
    resolution = maximum
    headless = false
    mobileEmulation =
    
    #------- Environmental -------#
    #- Framework specific capabilities -#
    [ENVIRONMENT]
    testurl=https://www.google.co.nz/
    local=false
    selenium_grid_hub=http://127.0.0.1:4444/wd/hub
    zalenium=false   
     
* Select the scenario from the feature file _features/web/googlesearch.feature_ and run (using IDE)
* To tests from the command line


    behave features/web/googlesearch.feature # Run a feature file
    behave --tags=@google # Run only tagged tests
    behave --tags=~@manual # Dont run tagged tests
    behave --tags=@google -D local=true -D testurl=http://www.google.com  # Override testsetup fields in CLI
    behave --tags=@google --junit --junit-directory reports --no-skipped # generate junit reports
    behave --tags=@google -f allure_behave.formatter:AllureFormatter -o allure-results # Generate allure results
    nzme-behave-parallel -p 4 -t google # Run tests parallel

## **How do i run an api test?**
* Ensure that the feature file/scenario has been tagged with _**@api**_
* Select the scenario from the feature file _features/api/searchcountryapi.feature_ and run (using IDE)
* To tests from the command line


    behave features/api/searchcountryapi.feature # Run a feature file
    behave --tags=@api # Run only tagged tests
    behave --tags=~@api # Dont run tagged tests
    