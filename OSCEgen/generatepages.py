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


def extractBySpeciality():
    oscelist = pd.read_csv("./src/osce_map.csv")
    gen = {}
    msk = {}
    resp = {}
    haem = {}
    cardio = {}
    neuro = {}
    renal = {}
    gastro = {}
    endo = {}
    onc = {}
    proc = {}
    gen['id'] = oscelist.query('speciality=="gen"')['OSCE_ID'].tolist()
    gen['title'] = oscelist.query('speciality=="gen"')['title'].tolist()
    msk['id'] = oscelist.query('speciality=="msk"')['OSCE_ID'].tolist()
    msk['title'] = oscelist.query('speciality=="msk"')['title'].tolist()
    resp['id'] = oscelist.query('speciality=="resp"')['OSCE_ID'].tolist()
    resp['title'] = oscelist.query('speciality=="resp"')['title'].tolist()
    haem['id'] = oscelist.query('speciality=="haem"')['OSCE_ID'].tolist()
    haem['title'] = oscelist.query('speciality=="haem"')['title'].tolist()
    cardio['id'] = oscelist.query('speciality=="cardio"')['OSCE_ID'].tolist()
    cardio['title'] = oscelist.query('speciality=="cardio"')['title'].tolist()
    neuro['id'] = oscelist.query('speciality=="neuro"')['OSCE_ID'].tolist()
    neuro['title'] = oscelist.query('speciality=="neuro"')['title'].tolist()
    renal['id'] = oscelist.query('speciality=="renal"')['OSCE_ID'].tolist()
    renal['title'] = oscelist.query('speciality=="renal"')['title'].tolist()
    gastro['id'] = oscelist.query('speciality=="gastro"')['OSCE_ID'].tolist()
    gastro['title'] = oscelist.query('speciality=="gastro"')['title'].tolist()
    endo['id'] = oscelist.query('speciality=="endo"')['OSCE_ID'].tolist()
    endo['title'] = oscelist.query('speciality=="endo"')['title'].tolist()
    onc['id'] = oscelist.query('speciality=="onc"')['OSCE_ID'].tolist()
    onc['title'] = oscelist.query('speciality=="onc"')['title'].tolist()
    proc['id'] = oscelist.query('speciality=="proc"')['OSCE_ID'].tolist()
    proc['title'] = oscelist.query('speciality=="proc"')['title'].tolist()

    return gen, msk, resp, haem, cardio, neuro, endo, renal, gastro, onc, proc

def generate_landing():
    gen, msk, resp, haem, cardio, neuro, endo, renal, gastro, onc, proc = extractBySpeciality()

    page = env.get_template('landing_template.html')
    htmlObj = page.render({'gen': gen, "msk": msk, "resp": resp, "haem": haem, "cardio": cardio, "neuro": neuro, "endo": endo, "renal": renal, "gastro": gastro, "onc": onc, "proc": proc })
    savePage(htmlObj, "./public/index.html")

    return

def generate_randomiser():


    return
