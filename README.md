# Tickets                                Zendesk is a Customer Support Ticket System 



=> Firstly You Will Create Your Zendesk Account Throughout That You Can Access The APIs

=> then Login thorugh this Url: https://www.zendesk.com/login/
![](https://github.com/makerobos/tickets/blob/master/ZendeskLogin.PNG)

=> After Login You Will Redirected To Your Dashbaord From Where You Can See Your Tickets Details. 
![](https://github.com/makerobos/tickets/blob/master/DashboardLogin.PNG)

=> Now Here Comes The Steps To Create the API 
=> If You Stuck in Any Of The Steps than You Will Go throughout The (Zendesk API Documentation Support for Developers)
=> Here is the Url To Go Through The (Zendesk API Documentation for Developers) https://developer.zendesk.com/rest_api/docs/support/introduction

![](https://github.com/makerobos/tickets/blob/master/SupportApi.PNG)
  To Get Access To The APIs Three Things Must Require:-
    1. Url 
    2. User
    3. Password 
  
=> We Can Get All Ticket Json Response Through this Url  https://puneetmakerobos.zendesk.com/api/v2/tickets.json
You Will Replace This Url According To Your Login Credential 

* Now User Credential: puneetmakerobos4@gmail.com/token
Change It Also According To Your Businees Email Credential

* Password: To Create This Password Read Zendesk API Authentication and Authorization 
It Will Generate Like This: sfd6aTgkX94Cq7HxB0wczYMjl5XB3nncNZ9LjH8J

## Now We Will Start To Create The Ticket.
 	1. First We Will Go To The Makerobos Plaform.
  2. Then Create the block With The name of Ticket
  3. In Which We Will Take Total 3 Cards (See Structure Below)
  4. ![](https://github.com/makerobos/tickets/blob/master/CreateTicketChatFirst.PNG)
  5. Then Create a block With New Ticket
  6. ![](https://github.com/makerobos/tickets/blob/master/CreateTicketChatSecond.PNG)
  7. ![](https://github.com/makerobos/tickets/blob/master/CreateTicketChatThird.PNG)

* Now We Have To Write The code For Json Api In This Documentation I Have Created This API In Flask which is a Python Framework.
```
@app.route('/postticket/', methods=['POST'])
def post():
    problem = request.form.get('Problem')
    Name = request.form.get('Name')
    mail = request.form.get('Mail')
    final_subject = Name +' Having an Issue'
    data = {"ticket": {"subject": final_subject, "comment": {"body": problem}, "external_id": mail}}
    response = requests.post(url, auth=(user, pwd), headers={"Content-Type": "application/json"}, data=json.dumps(data))
    return jsonify({
        "entries": [
            {
                "template_type": "message",
                "message": '''<table border=1 style="text-align:center;"><tr><td colspan="2">Note This Id For Future Reference</td></tr><tr><td>Ticket ID
                           </td><td>'''+format((response.json()["ticket"]["id"]))+'''</td></tr><tr><td>Your Email</td><td>'''+mail+'''</td></tr><tr><td>Pro
                           blem</td><td>'''+problem+'''</td></tr><tr><td>Created At</td><td>'''+format((response.json()["ticket"]["created_at"]))+'''</td>
                           </tr><td>Assignee Id</td><td>'''+format((response.json()["ticket"]["assignee_id"]))+'''</td></table>'''
            }
        ]
    })

```
* Through This We get a Ticket Id as a Response in The Table Format 
* See Below The Overall ChatBot Response

  ![](https://github.com/makerobos/tickets/blob/master/CreateTicketChatBot.jpeg)
 
## Now We Will Get The Status of the Ticket By Using Ticket ID
  1. Go To The Makerobos Platform.
  2. In Our Ticket Block
      * Hello Greetings Of the Day 
      * Are You Facing Some Problem 
      * If Client Say No Then 
    






  
  

