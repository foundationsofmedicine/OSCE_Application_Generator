from jinja2 import Environment, select_autoescape
from jinja2.loaders import FileSystemLoader
import pandas as pd

env = Environment(
    loader=FileSystemLoader('./src/'),
    autoescape=select_autoescape(['html', 'xml'])
)

def savePage(htmlObj, location):
    with open(location, "w") as f:
        f.write(htmlObj)

def loadOSCEdata(osce_id):
    osce_data = pd.read_csv("./src/osce/" + osce_id + ".csv")
    title = osce_data['title'].tolist()
    title = [i for i in title if str(i) != 'nan']
    prompt = osce_data['prompt'].tolist()
    prompt = [i for i in prompt if str(i) != 'nan']
    actor_prompt = osce_data['actor_prompt'].tolist()
    actor_prompt = [i for i in actor_prompt if str(i) != 'nan']
    examination_criteria = osce_data['examination_criteria'].tolist()
    examination_criteria = [i for i in examination_criteria if str(i) != 'nan']
    return osce_id, title, prompt, actor_prompt, examination_criteria

def generate_examiner_pages(item):
    osce_id, title, prompt, actor_prompt, examination_criteria = loadOSCEdata(item)
    page = env.get_template('examiner_template.html')
    htmlObj = page.render({'osce_id': osce_id, 'title': title, 'criteria': examination_criteria})
    savePage(htmlObj, "./public/" + item + "/index.html")
    return

def generate_prompt_pages(item):
    osce_id, title, prompt, actor_prompt, examination_criteria = loadOSCEdata(item)
    page = env.get_template('prompt_template.html')
    htmlObj = page.render({'osce_id': osce_id, 'user': "Examinee", 'prompt': prompt})
    savePage(htmlObj, "./public/" + item + "/prompt/index.html")
    return

def generate_actor_prompt_pages(item):
    osce_id, title, prompt, actor_prompt, examination_criteria = loadOSCEdata(item)
    page = env.get_template('prompt_template.html')
    htmlObj = page.render({'osce_id': osce_id, 'user': "Actor", 'prompt': actor_prompt})
    savePage(htmlObj, "./public/" + item + "/actor_prompt/index.html")
    return

def generate_landing():
    

    return

def generate_randomiser():


    return
