from flask import Flask, request, redirect
import twilio.twiml
import data
from services import *

app = Flask(__name__)

## the sublist of commands that contain the given tag
def filter(tag,cmds=data.box):
    return [cmd for cmd in cmds if tag in cmd['tags']]

## evaluates a given command to a string by delegating to the proper service
def eval(cmd, input=None):
    s = ""
        if cmd['service'] == 'C': ## Coupon
        return coupon.eval(cmd['args'])
    else:
        return "ERROR 42: service not recognized"

## list of services that need the user's input to work, not a command
#### We will likely need this section, since we need the user to input a location (for coupon stuff)
def needsInput(cmd):
    return cmd['service'] in ['C']

"""
Again, I deleted anything that was not the first service since we will only have one (with the
exception of DEMO in the event that we wish to keep the demo stuff in here
"""
def special(incoming):
    body = ''
    if incoming.upper() == "SHUTTLE" :
        body = shuttle.special
    elif incoming.upper() == "DEMO": ## We are going to need to adjust this later
        ## welcome/instructions
        body = 'Thanks for using Harvard Now!\n'
        body += 'A list of restaurants with coupons right now is accessed by sending what you\'re in the mood for right now\n'
        body += 'e.g. Chinese\n'
     return body

## main function
@app.route("/", methods=['GET', 'POST'])
def response():
    resp = twilio.twiml.Response()
    incoming = request.values.get('Body',None)

    ## first check if the query is a special case
    #### I bet we could modify this a bit, if we have time
    #### This error section doesn't seem to need much in terms of editing to function though
    body = special(incoming.replace(' ',''))
    if body != '':
        resp.message(body)
        return str(resp)
    ## if not, continue with command filtering
    words = set(incoming.upper().split(" "))
    started = False
    results = data.box
    for word in words:
        r = filter(word,results)
        if r == []:
            continue
        else:
            started = True
            results = r
    if not started:
        body = "Sorry, I don't know what that is."
    elif len(results) > 12:
        body = "Sorry, that's too many requests."
    else:
        if any(needsInput(cmd) for cmd in results):
            body = "\n".join(['\n'+eval(cmd, words) for cmd in results])
        else:
            body = "\n".join(['\n'+eval(cmd) for cmd in results])

    resp.message(body)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
