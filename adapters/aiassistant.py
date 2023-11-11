import json
import re
from openai import OpenAI
client = OpenAI()

ASSISTANT_ID = "asst_q0z52SFDJFVnq9OWZMIiIPmT"

MDCODE = re.compile("^\s*```(.*)```$")

def sendMessage(message):
    thread = client.beta.threads.create()
    omessage = client.beta.threads.messages.create(thread_id=thread.id, role="user", content=message)
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=ASSISTANT_ID
    )
    while(run.status != "completed"):
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        print(run.status)
    messages = list(client.beta.threads.messages.list(thread_id=thread.id, before=omessage.id))
    responsetext = _remove_markdown(messages[0].content[0].text.value)
    print(responsetext)
    responsejson = json.loads(responsetext)
    print(responsejson)
    return {
        "message": responsejson.get("message"),
        "action": responsejson.get("action")
    }

def _remove_markdown(s):
    m = MDCODE.match(s)
    if m:
        return m.groups()[0]
    else:
        return s
    