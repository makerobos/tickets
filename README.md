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

  ![](https://github.com/makerobos/tickets/blob/master/create_ticket_chatbot.jpeg)
  
  
## Now We Will Get The Status of the Ticket By Using Ticket ID
  1. Go To The Makerobos Platform.
  2. In Our Ticket Block
      * Hello Greetings Of the Day 
      * Are You Facing Some Problem 
      * If User Say No, Then
      
       ![](https://github.com/makerobos/tickets/blob/master/StatusByTicketIdfirst.PNG)
       
      * Do You Want To Check The Status 
      * If Client Say Yes 
      * Then Redirected it to the Our New Block which is Get Ticket 
  3. In Our Get Ticket Block
      
      ![](https://github.com/makerobos/tickets/blob/master/status_by_ticketid_getticblock.PNG)
      
      ![](https://github.com/makerobos/tickets/blob/master/gotoblock_getticketbyid.PNG)
      
  4. Check Your Status Using:- We Have Two Options for that
       * Do You Have Ticket Id
       * Without Having Ticket Id 
       
        Their Value Stored in the {{HasTicketId}} attribute i.e If the User Will CHoose Do You Have Ticket Id or Without Having Ticket         Id Their Chosen Vaue Will will Be Stored In The Attribute. And The Attribute is Nothing But {{HasTicketId}} You Can Give any of
        name. This is Not A Fixed Name. But Give Some meaningful Name. Which Make Less Chance Of Creating Error When You Will use this 
        attribute in the future. 
  
  5. In This Case We Will learn How To get the Status By Using Ticket Id. So We Will Choose Do You Have Ticket Id
  6. Now in Next Run If Card we will check the condition (HasTicketId contains Do You Have) and If This Condition is True Than we Will s
     select for the Next Card which is Nothing But a Go To Card Which Will Redirected It To the GetTicketById Block.
     Make Sure You Will Tick Mark To the Next Card. If This Condition is True then Only Go To Block perform Redirection
  7. Now GetTicketById   Block
  
     ![](https://github.com/makerobos/tickets/blob/master/getticketbyid_block.PNG)
  
  9. Now in this First Card is User Input in which Bot Says to User. Ok Give me Your Ticket Id and Then User Will Provide Their Ticket 
     Id and The Id Will Be Stored in the {{TicketID}} attribute 
  
  10. Our Next Card is Json Api In Which We Pass the Url Along With the Parameter TicketID. To get The TicketID in Our API To Process         our Request.
  
      ```
      @app.route('/getticket/', methods=['GET'])
      def get():
          id = request.args.get('TicketID')
          if id:
              print(id)
              url = 'https://puneetmakerobos.zendesk.com/api/v2/tickets/' + id + '.json'
              response = requests.get(url, auth=(user, pwd))
              print(response.json()["ticket"]["status"])
              if response.status_code == 404:
                  return jsonify({
                      "entries": [
                          {
                              "template_type": "message",
                              "message": "This is Not A Registered ID "
                          }
                      ]
                  })
              if response:
                  return jsonify({
                      "entries": [
                          {
                              "template_type": "message",
                              "message": '''<table border=1 style="text-align:center;"><tr><td colspan="2">Details:-</td></tr><tr><td>Your Problem</td><td style="padding:5px";>''' + (response.json()["ticket"]["description"]) + '''</td></tr><tr><td>Status is</td><td style="padding:5px";>''' + (response.json()["ticket"]["status"]) + '''</td></tr></table>'''
                          }
                      ]
                  })
        ```
   11. See Below The Overall ChatBot Response 
   
       ![](https://github.com/makerobos/tickets/blob/master/get_ticketbyid_chatbot.jpeg)      
      
      
## Now We Will Get The Status of the Ticket through the Problem (Without Using Ticket Id)
  1. Go To The Makerobos Platform.
  2. In Our Ticket Block
      * Hello Greetings Of the Day 
      * Are You Facing Some Problem 
      * If User Say No, Then
      
       ![](https://github.com/makerobos/tickets/blob/master/StatusByTicketIdfirst.PNG)
       
      * Do You Want To Check The Status 
      * If Client Say Yes 
      * Then Redirected it to the Our New Block which is Get Ticket 
  3. In Our Get Ticket Block
      
      ![](https://github.com/makerobos/tickets/blob/master/status_by_ticketid_getticblock.PNG)
      
      ![](https://github.com/makerobos/tickets/blob/master/gotoblock_getticketbyid.PNG)
      
  4. Check Your Status Using:- We Have Two Options for that
       * Do You Have Ticket Id
       * Without Having Ticket Id
       
        Now In This Case We Will learn If User Will Press Without Using Ticket Id
          * In This We Have Two More Cases
          4.1 Looking For A Particular Problem Status 
          4.2 All Problem Status 
        
        4.1 Looking For a Particular Problem Status
          1. This Below Diagram is Nothing But The Continuation of GetTicket Block
          
        ![](https://github.com/makerobos/tickets/blob/master/look_a_single_probFirst.PNG)
        
        ![](https://github.com/makerobos/tickets/blob/master/look_a_single_probSecond.PNG)
        
        ![](https://github.com/makerobos/tickets/blob/master/look_a_single_probThird.PNG)
        
        2. HasTicketId contains Without Having Ticket Id At This Time If This Condition is True Than Our Next 2 Card Will Be Process.              Than Our Next Card Process Start In Which Bot Will take The Email Id From The User And Stored in The {{Email}} Attribute
           And Says OK According To The Next Card Situation. Than Ask For A Looking For a Paticular Problem Status and All Problem                  Status. In This case We Will Choose Looking For a Particular Problem Status And Particluar Choosed Section Value Stored in 
           Attribute {{problem_Status}}. Than Next Card Condition If The {{problem_Status}} contains Looking Foa a Partcular. If This 
           Condition Is True Than Next 2 Card Will Came in The Picture. According To Next Card Situation Bot Will Ask To The User Tell 
           Me The Problem Once Again. So I can Check The Status For that Problem and their Value Which is Given By The User Will Store 
           in the Attribute {{particular_Problem}} And In The Next Card Our Json APi Card Will COme in The Picture in Which We Will PAss            the particular_Problem, and Email as A Parameter Throughout Which We Can Search For The Status.
        3. Now We Will See The Flask Api Code 
           Note In This Flask API Code Compulsory You Will get the particular_Problem and email Which You Will Pass In The Json Api Card
           ```
           email = request.args.get('Email')
           particular_Problem = request.args.get('particular_Problem')
           ```
        4. Flask API Code   
           ```
           elif particular_Problem and email:
               query = particular_Problem
               url = 'https://puneetmakerobos.zendesk.com/api/v2/tickets.jsonn?external_id=' + email + ''
               response = requests.get(url, auth=(user, pwd))
               final_list = []
               _map = {}
               for ticket in response.json()['tickets']:
                    _map[ticket['description']] = ticket
                    final_list.append(ticket["description"])
               a = process.extractOne(query, final_list)[0]
               return jsonify({
                      "entries":[
                        {
                          "template_type": "message",
                          "message": '''<table border=1 style="text-align:center;"><tr><td>Problem</td><td>''' + particular_Problem +                                        '''</td></tr><tr><td>Status</td><td>''' + _map[a]["status"] + '''</td></tr></table>'''
                        }
                      ]
                    })
             ```
        
        
        
        
          
        
            

      
  
        
        
      
      
    






  
  

