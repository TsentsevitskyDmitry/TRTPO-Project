# Test Plan
 ### Content
  1. [Introduction](#1)
  2. [Test object](#2)
  3. [Risks](#3)
  4. [Aspects](#4)
  5. [Approaches](#5)
  6. [Results](#6)
  7. [Conclusion](#7)

<a name="1"></a>
 ## 1. Introduction
The plan is how we are going to test the python-bot "Mega Reminder"

<a name="2"></a>
 ## 2. Test object
### 1. Functional adequacy:
-   #### Сomprehensiveness.
    The functions of the "Mega Reminder" have to realize its full potential.
-   #### Correctness.
    The application, especially its functions, have to work correctly.
-   #### Reasonability.
    Every function in the "Mega Reminder" has to have a reason to be here.

<a name="3"></a>
## 3. Risks
- If telegram.org change its API or make it paid, we are not able to use the application.

<a name="4"></a>
## 4. Aspects
##### The list of function which we are testing:
1. Save, show, delete Notifications from db
2. Help echo
3. Show active notifications echo
4. Parsing relative timelable 
5. Parsing absolute timelable 
6. Executing payload from user messages

### Functional requirements
#### 1. Save, show, delete Notifications from db
We have to test this one before to start using the main functions of the application. User must be able to add new notification and delete it, when it appears. Also user must be able to see the list of all pending notifications.
#### 2. Help echo
User user must be able to find out how to use this bot.
#### 3. Show active notifications echo
User user must be able to see the list of all pending notifications.
#### 4. Parsing relative timelable
This function we are testing to understand bot's capabilities of undestending the human input in relative way.  
#### 5. Parsing absolute timelable 
This function we are testing to understand bot's capabilities of undestending the human input in absolute way. 
#### 6. Executing payload from user messages
We need to make sure the bot is able to separate user payload in message from a timelable.

### Nonfunctional requirements:
#### 1. Human-like interface
User messages to the bot shuold looks like a regular chat between two peoples to improve user expirence. 

#### 2. Performance
Bot must be able to maintain a large number of users.

<a name="5"></a>
## 5. Approaches
To test the application we need to write manually some messages and send them to the bot. 

<a name="6"></a>
## 6. Results
[Test result](TestResult.md)

<a name="7"></a>
## 7. Conclusion
Running the tests can help to find out bugs and architecture errors.