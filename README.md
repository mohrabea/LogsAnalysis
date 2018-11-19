# Logs Analysis Project

### About logs analysis
#### Why this project?

In this project, you will stretch your SQL database skills. You will get practice interacting with a live database both from the command line and from your code. You will explore a large database with over a million rows. And you will build and refine complex queries and use them to draw business conclusions from data.

#### Report generation

Building an informative summary from logs is a real task that comes up very often in software engineering. For instance, at Udacity we collect logs to help us measure student progress and the success of our courses. The reporting tools we use to analyze those logs involve hundreds of lines of SQL.

#### Database as shared resource

In this project, you'll work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.

This shows one of the valuable roles of a database server in a real-world application: it's a point where different pieces of software (a web app and a reporting tool, for instance) can share data.

#### So what are we reporting, anyway?

Here are the questions the reporting tool should answer. The example answers given aren't the right ones, though!

1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)

### Functions in LogsAnalysis.py:
* **main():** To show a list of 4 options on the Home screen.
* **get_data(query):** connect to database and Return Query results.
* **report(p_sn):** Select the Query and sending to get_data() function to get results and printing.


### Views Made:

* <h4>popular_articles</h4>
```sql
SELECT a.title ,COUNT(log.path) AS views_count 
FROM articles AS a 
INNER JOIN log ON a.slug = reverse(split_part"(reverse( log.path ),'/',1)) "
GROUP BY a.title "
ORDER BY views_count desc Limit 3;
```
* <h4>popular_authors</h4>
```sql
SELECT au.name ,COUNT(log.path) AS views_count
FROM authors AS au 
INNER JOIN articles AS a ON  a.author = au.id
INNER JOIN log ON a.slug = reverse(split_part(reverse( log.path ),'/',1)) "
GROUP BY au.name 
ORDER BY views_count DESC LIMIT 3;
```

* <h4>log_status</h4>
```sql
SELECT req_err.day_dd , ROUND((req_err.errors_count::numeric /req_ok.ok_count::numeric)*100,1) AS per 
FROM 

(SELECT to_char(time,'Mon DD YYYY') AS day_dd , COUNT(*) AS errors_count 
FROM log 
WHERE status = '404 NOT FOUND' GROUP BY day_dd
) AS req_err,

(SELECT to_char(time,'Mon DD YYYY') AS day_dd , COUNT(*) AS ok_count 
FROM log 
GROUP BY day_dd
) AS req_ok 

WHERE req_err.day_dd = req_ok.day_dd AND (req_err.errors_count::numeric"/req_ok.ok_count::numeric) *100 >= 1 
ORDER BY req_err.day_dd ;"
```


## Getting Started

These instructions will get you a copy of the project up and running on your local machine. See deployment for notes on how to deploy the project on a live system.

### PreRequisites:

* Operating system (Linux / Windows)
* [Python 3.x](https://www.python.org/)
* [VirtualBox](https://www.virtualbox.org/)
* [Vagrant](https://www.vagrantup.com/)
* [PostgreSQL](https://www.postgresql.org/)
* [psycopg2](https://pypi.org/project/psycopg2/)


### Installation and Configuration Steps

* <h4>Install Python</h4>

  ```
  $ sudo apt-get install python3.7
  ```

  You can run the following command to verify whether Python 3.7 is working:

  ```
  $ python3.7 --version
  ```

  As you can see, it’s working.

* <h4>Install VirtualBox</h4>

  VirtualBox is the software that actually runs the virtual machine. [You can download it from  virtualbox.org, here.](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

  Currently (October 2017), the supported version of VirtualBox to install is version 5.1. Newer  versions do not work with the current release of Vagrant.

  Ubuntu users: If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.

* <h4>Install Vagrant</h4>

  Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. [Download it from vagrantup.com.](https://www.vagrantup.com/downloads.html) Install the version for your operating system.

  **Windows users:** The Installer may ask you to grant network permissions to Vagrant or make a   firewall exception. Be sure to allow this.
If Vagrant is successfully installed, you will be able to run `vagrant --version` in your terminal to see the version number.

  If Vagrant is successfully installed, you will be able to run vagrant --version
  in your terminal to see the version number. 
  The shell prompt in your terminal may differ. Here, the $ sign is the shell prompt.

  ```
  $ vagrant --version
  Vagrant 1.8.5
  $
  ```

  If Vagrant successfully installed, you will be able to run `vagrant --version` in your terminal number.
  The shellprompt in your terminal may differ. Hear, the `$` signis the shell prompet.

* <h4>Download the VM configuration</h4>

  There are a couple of different ways you can download the VM configuration.

  You can download and unzip this file: [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/  video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip)   This will give you a directory called **FSND-Virtual-Machine.** It may be located inside your   **Downloads** folder.

  Alternately, you can use Github to fork and clone the repository [https://github.com/udacity/ fullstack-nanodegree-vm.](https://github.com/udacity/fullstack-nanodegree-vm)

   Either way, you will end up with a new directory containing the VM files. Change to this directory in your terminal with `cd`. Inside, you will find another directory called **vagrant**. Change directory to the **vagrant** directory:

  ![screen-shot-2016-12-07-at-13.28.31.png](https://d17h27t6h515a5.cloudfront.net/topher/2016/ December/58487f12_screen-shot-2016-12-07-at-13.28.31/screen-shot-2016-12-07-at-13.28.31.png)

* <h4>Start the virtual machine</h4>

  From your terminal, inside the vagrant subdirectory, run the command `vagrant up`. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.

  ![screen-shot-2016-12-07-at-13.57.50.png](https://d17h27t6h515a5.cloudfront.net/topher/2016/December/58488603_screen-shot-2016-12-07-at-13.57.50/screen-shot-2016-12-07-at-13.57.50.png)

  When `vagrant up` is finished running, you will get your shell prompt back. At this point, you   can run `vagrant ssh` to log in to your newly installed Linux VM!

  ![screen-shot-2016-12-07-at-14.12.29.png](https://d17h27t6h515a5.cloudfront.net/topher/2016/December/58488962_screen-shot-2016-12-07-at-14.12.29/screen-shot-2016-12-07-at-14.12.29.png)

  Inside the VM, change directory to /vagrant and look around with ls.

  The files you see here are the same as the ones in the vagrant subdirectory on your computer (where you started Vagrant from). Any file you create in one will be automatically shared to the other. This means that you can edit code in your favorite text editor, and run it inside the VM.

  Files in the VM's `/vagrant` directory are shared with the `vagrant` folder on your computer. But other data inside the VM is not. For instance, the PostgreSQL database itself lives only inside the VM.


* <h4>Running the PostgreSQL database</h4>

  The PostgreSQL database server will automatically be started inside the VM. You can use the `psql` command-line tool to access it and run SQL statements:

  ![screen-shot-2016-12-07-at-14.46.25.png](https://d17h27t6h515a5.cloudfront.net/topher/2016/December/58489186_screen-shot-2016-12-07-at-14.46.25/screen-shot-2016-12-07-at-14.46.25.png)


* <h4>Download the data</h4>

  Next, [download the data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called `newsdata.sql`. Put this file into the `vagrant` directory, which is shared with your virtual machine.
  To load the data, `cd` into the `vagrant` directory and use the command `psql -d news -f newsdata.sql`.



```
As you can see, it’s working
https://github.com/mohrabea/logs-analysis.git
```

### Running program

```
$ python3 LogsAnalysis.py
```
## Authors

* **Mohammed Rabea** - *Email: moh.rabea@gmail.com* 


