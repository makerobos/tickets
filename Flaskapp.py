from flask import Flask, jsonify, request, Response
import requests
import json
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


url = 'https://<subdomain>.zendesk.com/api/v2/tickets.json'
user = '<useremail>/token'
pwd = 'sfd6aTgkX94Cq7HxB9wczYMjl5XB5nncNZ9LjH8J'
# define app using Flask
app = Flask(__name__)


@app.route('/getticket/', methods=['GET'])
def get():
    id = request.args.get('TicketID')
    email = request.args.get('Email')
    particular_Problem = request.args.get('particular_Problem')
    if id:
        url = 'https://puneetmakerobos.zendesk.com/api/v2/tickets/' + id + '.json'
        response = requests.get(url, auth=(user, pwd))
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
                  "message": '''<table border=1 style="text-align:center;"><tr><td>Problem</td><td>''' + particular_Problem + '''</td></tr><tr><td>Status</td><td>''' + _map[a]["status"] + '''</td></tr></table>'''
                }
              ]
            })

    elif email:
        url = 'https://puneetmakerobos.zendesk.com/api/v2/tickets.jsonn?external_id=' + email + ''
        response = requests.get(url, auth=(user, pwd))
        open_List = []
        pending_List = []
        solved_List = []
        for a in response.json()['tickets']:
            if a["status"] == 'open':
                open_List.append('open')
            if a["status"] == 'pending':
                pending_List.append('pending')
            if a["status"] == 'solved':
                solved_List.append('solved')
        total_Open = len(open_List)
        total_pending = len(pending_List)
        total_solved = len(solved_List)
        if len(response.json()['tickets']):
            return jsonify({
                "entries": [
                    {
                        "template_type": "message",
                        "message": '''<table border=1 style="text-align:center;"><tr><td>Submit as Open</td><td>''' + str(
                            total_Open) + '''</td></tr><tr><td>Submit as Pending</td><td>''' + str(total_pending) + '''</td></tr><tr><td>Submit as Solved</td><td>''' + str(total_solved) + '''</td></tr></table>
                                    '''
                    }
                ]
            })
        else:
            return jsonify({
                "entries": [
                    {
                        "template_type": "message",
                        "message": "Nothing Found"
                    }
                ]
            })

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
# run app on Port No 8000 in debug mode
if __name__ == '__main__':
    app.run(debug=True, port=8000)
