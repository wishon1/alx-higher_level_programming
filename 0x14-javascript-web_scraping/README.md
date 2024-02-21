# Project: JavaScript Web Scraping

## RESOURCES:
- [Working with JSON data](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)
- [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://medium.com/@vietkieutie/the-workflow-of-accessing-the-attributes-of-a-simply-created-json-object-82a5b33e2319)
- [request module](https://github.com/request/request)
- [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

## Description

This project is a collection of JavaScript scripts designed to perform various tasks related to web scraping, API usage, and file manipulation. The tasks include reading and writing files, making HTTP GET requests, interacting with APIs, and processing JSON data.

## Usage

### Setup Environment

Ensure that you have Node.js version 14.x installed on your system. If not, follow the instructions below:

```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

Next, install the `semistandard` package globally:

```bash
$ sudo npm install semistandard --global
```

Then, install the `request` module and set the `NODE_PATH` environment variable:

```bash
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

### Task Execution

Each task is implemented as a separate JavaScript file and can be executed as follows:

#### Task 0: Readme

**Question:**
Write a script that reads and prints the content of a file.

```bash
$ ./0-readme.js <file_path>
```

#### Task 1: Write Me

**Question:**
Write a script that writes a string to a file.

```bash
$ ./1-writeme.js <file_path> "<string_to_write>"
```

#### Task 2: Status Code

**Question:**
Write a script that displays the status code of a GET request.

```bash
$ ./2-statuscode.js <URL>
```

#### Task 3: Star Wars Movie Title

**Question:**
Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

```bash
$ ./3-starwars_title.js <movie_id>
```

#### Task 4: Star Wars Wedge Antilles

**Question:**
Write a script that prints the number of movies where the character “Wedge Antilles” is present.

```bash
$ ./4-starwars_count.js <API_URL>
```

#### Task 5: Loripsum

**Question:**
Write a script that gets the contents of a webpage and stores it in a file.

```bash
$ ./5-request_store.js <URL> <file_path>
```

#### Task 6: How Many Completed?

**Question:**
Write a script that computes the number of tasks completed by user id.

```bash
$ ./6-completed_tasks.js <API_URL>
```
