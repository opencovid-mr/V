import requests
import json
import csv

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

data = '{"version":"1.0.0","queries":[{"Query":{"Commands":[{"SemanticQueryDataShapeCommand":{"Query":{"Version":2,"From":[{"Name":"t","Entity":"TAB_MASTER","Type":0},{"Name":"t1","Entity":"TAB_MASTER_PIVOT","Type":0}],"Select":[{"Column":{"Expression":{"SourceRef":{"Source":"t"}},"Property":"TML_FASCIA_ETA"},"Name":"TAB_MASTER.TML_FASCIA_ETA"},{"Aggregation":{"Expression":{"Column":{"Expression":{"SourceRef":{"Source":"t1"}},"Property":"Valore"}},"Function":0},"Name":"Sum(TAB_MASTER_PIVOT.Valore)"}],"OrderBy":[{"Direction":1,"Expression":{"Column":{"Expression":{"SourceRef":{"Source":"t"}},"Property":"TML_FASCIA_ETA"}}}]},"Binding":{"Primary":{"Groupings":[{"Projections":[0,1]}]},"DataReduction":{"DataVolume":4,"Primary":{"Window":{"Count":1000}}},"Version":1}}}]},"CacheKey":"{\\"Commands\\":[{\\"SemanticQueryDataShapeCommand\\":{\\"Query\\":{\\"Version\\":2,\\"From\\":[{\\"Name\\":\\"t\\",\\"Entity\\":\\"TAB_MASTER\\",\\"Type\\":0},{\\"Name\\":\\"t1\\",\\"Entity\\":\\"TAB_MASTER_PIVOT\\",\\"Type\\":0}],\\"Select\\":[{\\"Column\\":{\\"Expression\\":{\\"SourceRef\\":{\\"Source\\":\\"t\\"}},\\"Property\\":\\"TML_FASCIA_ETA\\"},\\"Name\\":\\"TAB_MASTER.TML_FASCIA_ETA\\"},{\\"Aggregation\\":{\\"Expression\\":{\\"Column\\":{\\"Expression\\":{\\"SourceRef\\":{\\"Source\\":\\"t1\\"}},\\"Property\\":\\"Valore\\"}},\\"Function\\":0},\\"Name\\":\\"Sum(TAB_MASTER_PIVOT.Valore)\\"}],\\"OrderBy\\":[{\\"Direction\\":1,\\"Expression\\":{\\"Column\\":{\\"Expression\\":{\\"SourceRef\\":{\\"Source\\":\\"t\\"}},\\"Property\\":\\"TML_FASCIA_ETA\\"}}}]},\\"Binding\\":{\\"Primary\\":{\\"Groupings\\":[{\\"Projections\\":[0,1]}]},\\"DataReduction\\":{\\"DataVolume\\":4,\\"Primary\\":{\\"Window\\":{\\"Count\\":1000}}},\\"Version\\":1}}}]}","QueryId":"","ApplicationContext":{"DatasetId":"5bff6260-1025-49e0-8e9b-169ade7c07f9","Sources":[{"ReportId":"b548a77c-ab0a-4d7c-a457-2e38c2914fc6"}]}}],"cancelQueries":[],"modelId":4280811}'

FASCIA_ETA = json.loads(requests.post('https://wabi-europe-north-b-api.analysis.windows.net/public/reports/querydata', headers=headers, params=params, data=data).text)

data = '{"version":"1.0.0","queries":[{"Query":{"Commands":[{"SemanticQueryDataShapeCommand":{"Query":{"Version":2,"From":[{"Name":"t2","Entity":"TAB_MASTER_PIVOT","Type":0}],"Select":[{"Column":{"Expression":{"SourceRef":{"Source":"t2"}},"Property":"Categoria Attributo"},"Name":"TAB_MASTER_PIVOT.Categoria Attributo"},{"Aggregation":{"Expression":{"Column":{"Expression":{"SourceRef":{"Source":"t2"}},"Property":"Valore"}},"Function":0},"Name":"Sum(TAB_MASTER_PIVOT.Valore)"}],"OrderBy":[{"Direction":1,"Expression":{"Column":{"Expression":{"SourceRef":{"Source":"t2"}},"Property":"Categoria Attributo"}}}]},"Binding":{"Primary":{"Groupings":[{"Projections":[0,1]}]},"DataReduction":{"DataVolume":4,"Primary":{"Window":{"Count":1000}}},"Version":1}}}]},"CacheKey":"{\\"Commands\\":[{\\"SemanticQueryDataShapeCommand\\":{\\"Query\\":{\\"Version\\":2,\\"From\\":[{\\"Name\\":\\"t2\\",\\"Entity\\":\\"TAB_MASTER_PIVOT\\",\\"Type\\":0}],\\"Select\\":[{\\"Column\\":{\\"Expression\\":{\\"SourceRef\\":{\\"Source\\":\\"t2\\"}},\\"Property\\":\\"Categoria Attributo\\"},\\"Name\\":\\"TAB_MASTER_PIVOT.Categoria Attributo\\"},{\\"Aggregation\\":{\\"Expression\\":{\\"Column\\":{\\"Expression\\":{\\"SourceRef\\":{\\"Source\\":\\"t2\\"}},\\"Property\\":\\"Valore\\"}},\\"Function\\":0},\\"Name\\":\\"Sum(TAB_MASTER_PIVOT.Valore)\\"}],\\"OrderBy\\":[{\\"Direction\\":1,\\"Expression\\":{\\"Column\\":{\\"Expression\\":{\\"SourceRef\\":{\\"Source\\":\\"t2\\"}},\\"Property\\":\\"Categoria Attributo\\"}}}]},\\"Binding\\":{\\"Primary\\":{\\"Groupings\\":[{\\"Projections\\":[0,1]}]},\\"DataReduction\\":{\\"DataVolume\\":4,\\"Primary\\":{\\"Window\\":{\\"Count\\":1000}}},\\"Version\\":1}}}]}","QueryId":"","ApplicationContext":{"DatasetId":"5bff6260-1025-49e0-8e9b-169ade7c07f9","Sources":[{"ReportId":"b548a77c-ab0a-4d7c-a457-2e38c2914fc6"}]}}],"cancelQueries":[],"modelId":4280811}'

CATEGORIA = json.loads(requests.post('https://wabi-europe-north-b-api.analysis.windows.net/public/reports/querydata', headers=headers, params=params, data=data).text)

data = '{"version":"1.0.0","queries":[{"Query":{"Commands":[{"SemanticQueryDataShapeCommand":{"Query":{"Version":2,"From":[{"Name":"t2","Entity":"TAB_REGIONI","Type":0},{"Name":"t","Entity":"TAB_MASTER","Type":0}],"Select":[{"Column":{"Expression":{"SourceRef":{"Source":"t2"}},"Property":"AREA"},"Name":"TAB_REGIONI.AREA"},{"Aggregation":{"Expression":{"Column":{"Expression":{"SourceRef":{"Source":"t"}},"Property":"TOT_SOMM"}},"Function":0},"Name":"Sum(TAB_MASTER.TOT_SOMM)"},{"Measure":{"Expression":{"SourceRef":{"Source":"t"}},"Property":"TassoVaccinazione"},"Name":"TAB_MASTER.TassoVaccinazione"},{"Aggregation":{"Expression":{"Column":{"Expression":{"SourceRef":{"Source":"t"}},"Property":"DOSI_CONSEGNATE"}},"Function":4},"Name":"Sum(TAB_MASTER.DOSI_CONSEGNATE)"}],"OrderBy":[{"Direction":1,"Expression":{"Column":{"Expression":{"SourceRef":{"Source":"t2"}},"Property":"AREA"}}}]},"Binding":{"Primary":{"Groupings":[{"Projections":[0,1,2,3]}]},"DataReduction":{"DataVolume":3,"Primary":{"Window":{"Count":500}}},"Version":1}}}]},"CacheKey":"{\\"Commands\\":[{\\"SemanticQueryDataShapeCommand\\":{\\"Query\\":{\\"Version\\":2,\\"From\\":[{\\"Name\\":\\"t2\\",\\"Entity\\":\\"TAB_REGIONI\\",\\"Type\\":0},{\\"Name\\":\\"t\\",\\"Entity\\":\\"TAB_MASTER\\",\\"Type\\":0}],\\"Select\\":[{\\"Column\\":{\\"Expression\\":{\\"SourceRef\\":{\\"Source\\":\\"t2\\"}},\\"Property\\":\\"AREA\\"},\\"Name\\":\\"TAB_REGIONI.AREA\\"},{\\"Aggregation\\":{\\"Expression\\":{\\"Column\\":{\\"Expression\\":{\\"SourceRef\\":{\\"Source\\":\\"t\\"}},\\"Property\\":\\"TOT_SOMM\\"}},\\"Function\\":0},\\"Name\\":\\"Sum(TAB_MASTER.TOT_SOMM)\\"},{\\"Measure\\":{\\"Expression\\":{\\"SourceRef\\":{\\"Source\\":\\"t\\"}},\\"Property\\":\\"TassoVaccinazione\\"},\\"Name\\":\\"TAB_MASTER.TassoVaccinazione\\"},{\\"Aggregation\\":{\\"Expression\\":{\\"Column\\":{\\"Expression\\":{\\"SourceRef\\":{\\"Source\\":\\"t\\"}},\\"Property\\":\\"DOSI_CONSEGNATE\\"}},\\"Function\\":4},\\"Name\\":\\"Sum(TAB_MASTER.DOSI_CONSEGNATE)\\"}],\\"OrderBy\\":[{\\"Direction\\":1,\\"Expression\\":{\\"Column\\":{\\"Expression\\":{\\"SourceRef\\":{\\"Source\\":\\"t2\\"}},\\"Property\\":\\"AREA\\"}}}]},\\"Binding\\":{\\"Primary\\":{\\"Groupings\\":[{\\"Projections\\":[0,1,2,3]}]},\\"DataReduction\\":{\\"DataVolume\\":3,\\"Primary\\":{\\"Window\\":{\\"Count\\":500}}},\\"Version\\":1}}}]}","QueryId":"","ApplicationContext":{"DatasetId":"5bff6260-1025-49e0-8e9b-169ade7c07f9","Sources":[{"ReportId":"b548a77c-ab0a-4d7c-a457-2e38c2914fc6"}]}}],"cancelQueries":[],"modelId":4280811}'

REGIONI =  json.loads(requests.post('https://wabi-europe-north-b-api.analysis.windows.net/public/reports/querydata', headers=headers, params=params, data=data).text)


data_reg=REGIONI["results"][0]["result"]['data']['dsr']['DS'][0]['PH'][0]['DM0']

data_cat=CATEGORIA["results"][0]["result"]['data']['dsr']['DS'][0]['PH'][0]['DM0']

data_eta=FASCIA_ETA["results"][0]["result"]['data']['dsr']['DS'][0]['PH'][0]['DM0']

update=FASCIA_ETA["results"][0]["result"]['data']['timestamp']

update=update.replace(':', '_').replace('.', '_')


f_r = csv.writer(open("regioni"+update+".csv", "w+"),lineterminator='\n')

f_r.writerow(["Regione", "somministrazioni", "percentuale", "dosi_consegnate"])

for row in data_reg:
    f_r.writerow(row['C'])

f_c = csv.writer(open("categorie"+update+".csv", "w+"),lineterminator='\n')

f_c.writerow(["Categoria", "somministrazioni"])

for row in data_cat:
    f_c.writerow(row['C'])

f_e = csv.writer(open("eta"+update+".csv", "w+"),lineterminator='\n')

f_e.writerow(["Classe", "somministrazioni"])

for row in data_eta:
    f_e.writerow(row['C'])
