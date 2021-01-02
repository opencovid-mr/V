import requests
import json
import csv
def get_region_microdata(session, region):
    payload = '{"version":"1.0.0","queries":[{"Query":{"Commands":[{"SemanticQueryDataShapeCommand":{"Query":{"Version":2,"From":[{"Name":"t","Entity":"TAB_MASTER_PIVOT","Type":0},{"Name":"t1","Entity":"TAB_REGIONI","Type":0}],"Select":[{"Column":{"Expression":{"SourceRef":{"Source":"t"}},"Property":"Valore"},"Name":"Sum(TAB_MASTER_PIVOT.Valore)"},{"Column":{"Expression":{"SourceRef":{"Source":"t1"}},"Property":"REGIONE"},"Name":"TAB_REGIONI.REGIONE"},{"Column":{"Expression":{"SourceRef":{"Source":"t"}},"Property":"Attributo"},"Name":"TAB_MASTER_PIVOT.Attributo"},{"Column":{"Expression":{"SourceRef":{"Source":"t"}},"Property":"KEY"},"Name":"TAB_MASTER_PIVOT.KEY"},{"Column":{"Expression":{"SourceRef":{"Source":"t"}},"Property":"Categoria Attributo"},"Name":"TAB_MASTER_PIVOT.Categoria Attributo"}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"t1"}},"Property":"REGIONE"}}],"Values":[[{"Literal":{"Value":"\'' + region + '\'"}}]]}}}],"GroupBy":[{"SourceRef":{"Source":"t"},"Name":"TAB_MASTER_PIVOT"}]},"Binding":{"Primary":{"Groupings":[{"Projections":[0,1,2,3,4],"GroupBy":[0]}]},"DataReduction":{"Primary":{"Top":{"Count":100000}}},"Version":1}}}]},"QueryId":"","ApplicationContext":{"DatasetId":"5bff6260-1025-49e0-8e9b-169ade7c07f9","Sources":[{"ReportId":"b548a77c-ab0a-4d7c-a457-2e38c2914fc6"}]}}],"cancelQueries":[],"modelId":4280811}'    microdata = session.post(url=url, headers=headers, params=params, data=payload).text
    return(microdata)

def write_raw_region(session, update,region):
    filename = 'data/raw/' + update + '_' + region +'.txt'
    file = open(filename, 'w')
    file.write(get_region_microdata(session, region))

def write_json_to_csv(update, filename, header, data):
    filename = "data/"+ update + "_" + filename + ".csv"
    f = csv.writer(open(filename, "w+"),lineterminator='\n')
    f.writerow(header)
    for row in data:    
        f.writerow(row['C'])

headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'RequestId': '265d8673-9d4b-ddd0-c0b7-2123e0198074',
    'X-PowerBI-ResourceKey': '388bb944-d39d-4e22-817c-90d1c8152a84',
    'Content-Type': 'application/json;charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'ActivityId': 'f143a185-340b-66aa-217e-b6464e44747a',
    'Origin': 'https://app.powerbi.com',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://app.powerbi.com/view?r=eyJrIjoiMzg4YmI5NDQtZDM5ZC00ZTIyLTgxN2MtOTBkMWM4MTUyYTg0IiwidCI6ImFmZDBhNzVjLTg2NzEtNGNjZS05MDYxLTJjYTBkOTJlNDIyZiIsImMiOjh9',
    'Accept-Language': 'en-US,en;q=0.9',
}

params = (
    ('synchronous', 'true'),
)

url = 'https://wabi-europe-north-b-api.analysis.windows.net/public/reports/querydata'

s = requests.Session() 

data = '{"version":"1.0.0","queries":[{"Query":{"Commands":[{"SemanticQueryDataShapeCommand":{"Query":{"Version":2,"From":[{"Name":"t","Entity":"TAB_MASTER","Type":0},{"Name":"t1","Entity":"TAB_MASTER_PIVOT","Type":0}],"Select":[{"Column":{"Expression":{"SourceRef":{"Source":"t"}},"Property":"TML_FASCIA_ETA"},"Name":"TAB_MASTER.TML_FASCIA_ETA"},{"Aggregation":{"Expression":{"Column":{"Expression":{"SourceRef":{"Source":"t1"}},"Property":"Valore"}},"Function":0},"Name":"Sum(TAB_MASTER_PIVOT.Valore)"}],"OrderBy":[{"Direction":1,"Expression":{"Column":{"Expression":{"SourceRef":{"Source":"t"}},"Property":"TML_FASCIA_ETA"}}}]},"Binding":{"Primary":{"Groupings":[{"Projections":[0,1]}]},"DataReduction":{"DataVolume":4,"Primary":{"Window":{"Count":1000}}},"Version":1}}}]},"CacheKey":"{\\"Commands\\":[{\\"SemanticQueryDataShapeCommand\\":{\\"Query\\":{\\"Version\\":2,\\"From\\":[{\\"Name\\":\\"t\\",\\"Entity\\":\\"TAB_MASTER\\",\\"Type\\":0},{\\"Name\\":\\"t1\\",\\"Entity\\":\\"TAB_MASTER_PIVOT\\",\\"Type\\":0}],\\"Select\\":[{\\"Column\\":{\\"Expression\\":{\\"SourceRef\\":{\\"Source\\":\\"t\\"}},\\"Property\\":\\"TML_FASCIA_ETA\\"},\\"Name\\":\\"TAB_MASTER.TML_FASCIA_ETA\\"},{\\"Aggregation\\":{\\"Expression\\":{\\"Column\\":{\\"Expression\\":{\\"SourceRef\\":{\\"Source\\":\\"t1\\"}},\\"Property\\":\\"Valore\\"}},\\"Function\\":0},\\"Name\\":\\"Sum(TAB_MASTER_PIVOT.Valore)\\"}],\\"OrderBy\\":[{\\"Direction\\":1,\\"Expression\\":{\\"Column\\":{\\"Expression\\":{\\"SourceRef\\":{\\"Source\\":\\"t\\"}},\\"Property\\":\\"TML_FASCIA_ETA\\"}}}]},\\"Binding\\":{\\"Primary\\":{\\"Groupings\\":[{\\"Projections\\":[0,1]}]},\\"DataReduction\\":{\\"DataVolume\\":4,\\"Primary\\":{\\"Window\\":{\\"Count\\":1000}}},\\"Version\\":1}}}]}","QueryId":"","ApplicationContext":{"DatasetId":"5bff6260-1025-49e0-8e9b-169ade7c07f9","Sources":[{"ReportId":"b548a77c-ab0a-4d7c-a457-2e38c2914fc6"}]}}],"cancelQueries":[],"modelId":4280811}'

FASCIA_ETA = json.loads(requests.post(url, headers=headers, params=params, data=data).text)

data = '{"version":"1.0.0","queries":[{"Query":{"Commands":[{"SemanticQueryDataShapeCommand":{"Query":{"Version":2,"From":[{"Name":"t2","Entity":"TAB_MASTER_PIVOT","Type":0}],"Select":[{"Column":{"Expression":{"SourceRef":{"Source":"t2"}},"Property":"Categoria Attributo"},"Name":"TAB_MASTER_PIVOT.Categoria Attributo"},{"Aggregation":{"Expression":{"Column":{"Expression":{"SourceRef":{"Source":"t2"}},"Property":"Valore"}},"Function":0},"Name":"Sum(TAB_MASTER_PIVOT.Valore)"}],"OrderBy":[{"Direction":1,"Expression":{"Column":{"Expression":{"SourceRef":{"Source":"t2"}},"Property":"Categoria Attributo"}}}]},"Binding":{"Primary":{"Groupings":[{"Projections":[0,1]}]},"DataReduction":{"DataVolume":4,"Primary":{"Window":{"Count":1000}}},"Version":1}}}]},"CacheKey":"{\\"Commands\\":[{\\"SemanticQueryDataShapeCommand\\":{\\"Query\\":{\\"Version\\":2,\\"From\\":[{\\"Name\\":\\"t2\\",\\"Entity\\":\\"TAB_MASTER_PIVOT\\",\\"Type\\":0}],\\"Select\\":[{\\"Column\\":{\\"Expression\\":{\\"SourceRef\\":{\\"Source\\":\\"t2\\"}},\\"Property\\":\\"Categoria Attributo\\"},\\"Name\\":\\"TAB_MASTER_PIVOT.Categoria Attributo\\"},{\\"Aggregation\\":{\\"Expression\\":{\\"Column\\":{\\"Expression\\":{\\"SourceRef\\":{\\"Source\\":\\"t2\\"}},\\"Property\\":\\"Valore\\"}},\\"Function\\":0},\\"Name\\":\\"Sum(TAB_MASTER_PIVOT.Valore)\\"}],\\"OrderBy\\":[{\\"Direction\\":1,\\"Expression\\":{\\"Column\\":{\\"Expression\\":{\\"SourceRef\\":{\\"Source\\":\\"t2\\"}},\\"Property\\":\\"Categoria Attributo\\"}}}]},\\"Binding\\":{\\"Primary\\":{\\"Groupings\\":[{\\"Projections\\":[0,1]}]},\\"DataReduction\\":{\\"DataVolume\\":4,\\"Primary\\":{\\"Window\\":{\\"Count\\":1000}}},\\"Version\\":1}}}]}","QueryId":"","ApplicationContext":{"DatasetId":"5bff6260-1025-49e0-8e9b-169ade7c07f9","Sources":[{"ReportId":"b548a77c-ab0a-4d7c-a457-2e38c2914fc6"}]}}],"cancelQueries":[],"modelId":4280811}'

CATEGORIA = json.loads(requests.post(url, headers=headers, params=params, data=data).text)

data = '{"version":"1.0.0","queries":[{"Query":{"Commands":[{"SemanticQueryDataShapeCommand":{"Query":{"Version":2,"From":[{"Name":"t2","Entity":"TAB_REGIONI","Type":0},{"Name":"t","Entity":"TAB_MASTER","Type":0}],"Select":[{"Column":{"Expression":{"SourceRef":{"Source":"t2"}},"Property":"AREA"},"Name":"TAB_REGIONI.AREA"},{"Aggregation":{"Expression":{"Column":{"Expression":{"SourceRef":{"Source":"t"}},"Property":"TOT_SOMM"}},"Function":0},"Name":"Sum(TAB_MASTER.TOT_SOMM)"},{"Measure":{"Expression":{"SourceRef":{"Source":"t"}},"Property":"TassoVaccinazione"},"Name":"TAB_MASTER.TassoVaccinazione"},{"Aggregation":{"Expression":{"Column":{"Expression":{"SourceRef":{"Source":"t"}},"Property":"DOSI_CONSEGNATE"}},"Function":4},"Name":"Sum(TAB_MASTER.DOSI_CONSEGNATE)"}],"OrderBy":[{"Direction":1,"Expression":{"Column":{"Expression":{"SourceRef":{"Source":"t2"}},"Property":"AREA"}}}]},"Binding":{"Primary":{"Groupings":[{"Projections":[0,1,2,3]}]},"DataReduction":{"DataVolume":3,"Primary":{"Window":{"Count":500}}},"Version":1}}}]},"CacheKey":"{\\"Commands\\":[{\\"SemanticQueryDataShapeCommand\\":{\\"Query\\":{\\"Version\\":2,\\"From\\":[{\\"Name\\":\\"t2\\",\\"Entity\\":\\"TAB_REGIONI\\",\\"Type\\":0},{\\"Name\\":\\"t\\",\\"Entity\\":\\"TAB_MASTER\\",\\"Type\\":0}],\\"Select\\":[{\\"Column\\":{\\"Expression\\":{\\"SourceRef\\":{\\"Source\\":\\"t2\\"}},\\"Property\\":\\"AREA\\"},\\"Name\\":\\"TAB_REGIONI.AREA\\"},{\\"Aggregation\\":{\\"Expression\\":{\\"Column\\":{\\"Expression\\":{\\"SourceRef\\":{\\"Source\\":\\"t\\"}},\\"Property\\":\\"TOT_SOMM\\"}},\\"Function\\":0},\\"Name\\":\\"Sum(TAB_MASTER.TOT_SOMM)\\"},{\\"Measure\\":{\\"Expression\\":{\\"SourceRef\\":{\\"Source\\":\\"t\\"}},\\"Property\\":\\"TassoVaccinazione\\"},\\"Name\\":\\"TAB_MASTER.TassoVaccinazione\\"},{\\"Aggregation\\":{\\"Expression\\":{\\"Column\\":{\\"Expression\\":{\\"SourceRef\\":{\\"Source\\":\\"t\\"}},\\"Property\\":\\"DOSI_CONSEGNATE\\"}},\\"Function\\":4},\\"Name\\":\\"Sum(TAB_MASTER.DOSI_CONSEGNATE)\\"}],\\"OrderBy\\":[{\\"Direction\\":1,\\"Expression\\":{\\"Column\\":{\\"Expression\\":{\\"SourceRef\\":{\\"Source\\":\\"t2\\"}},\\"Property\\":\\"AREA\\"}}}]},\\"Binding\\":{\\"Primary\\":{\\"Groupings\\":[{\\"Projections\\":[0,1,2,3]}]},\\"DataReduction\\":{\\"DataVolume\\":3,\\"Primary\\":{\\"Window\\":{\\"Count\\":500}}},\\"Version\\":1}}}]}","QueryId":"","ApplicationContext":{"DatasetId":"5bff6260-1025-49e0-8e9b-169ade7c07f9","Sources":[{"ReportId":"b548a77c-ab0a-4d7c-a457-2e38c2914fc6"}]}}],"cancelQueries":[],"modelId":4280811}'

REGIONI =  json.loads(requests.post(url, headers=headers, params=params, data=data).text)


data_reg=REGIONI["results"][0]["result"]['data']['dsr']['DS'][0]['PH'][0]['DM0']

data_cat=CATEGORIA["results"][0]["result"]['data']['dsr']['DS'][0]['PH'][0]['DM0']

data_eta=FASCIA_ETA["results"][0]["result"]['data']['dsr']['DS'][0]['PH'][0]['DM0']

update=FASCIA_ETA["results"][0]["result"]['data']['timestamp']

update=update.replace(':', '_').replace('.', '_')

write_json_to_csv(update, "regioni", ["Regione", "somministrazioni", "percentuale", "dosi_consegnate"],  data_reg)
write_json_to_csv(update, "categoria", ["Categoria", "somministrazioni"],  data_cat)
write_json_to_csv(update, "eta", ["Classe", "somministrazioni"],  data_eta)

write_raw_region(s, update, "Valle d'Aosta")
write_raw_region(s, update, "Piemonte")
write_raw_region(s, update, "Lombardia")
write_raw_region(s, update, "Liguria")

write_raw_region(s, update, "Veneto")
write_raw_region(s, update, "Trentino-Alto Adige")
write_raw_region(s, update, "Friuli-Venezia Giulia")
write_raw_region(s, update, "Emilia-Romagna")

write_raw_region(s, update, "Toscana")
write_raw_region(s, update, "Umbria")
write_raw_region(s, update, "Marche")
write_raw_region(s, update, "Lazio")

write_raw_region(s, update, "Basilicata")
write_raw_region(s, update, "Molise")
write_raw_region(s, update, "Abruzzo")
write_raw_region(s, update, "Calabria")
write_raw_region(s, update, "Puglia")
write_raw_region(s, update, "Campania")

write_raw_region(s, update, "Sicilia")
write_raw_region(s, update, "Sardegna")
