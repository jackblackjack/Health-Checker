import ast
import urllib
import fetchSymptoms

text = ''''''
with open('example.txt') as f:
    for line in f:
        text += line

text = text.lower()
print(text)

for symptom in fetchSymptoms.symptoms:
    if symptom in text:
        symptomMC = str(fetchSymptoms.symptomDict[symptom])
        print(symptomMC)
        gender = 'male'
        year_of_birth = '1996'
        urlMedicalCondition = "https://healthservice.priaid.ch/diagnosis?symptoms=[" + symptomMC + "]&gender=" + gender + "&year_of_birth=" + year_of_birth + "&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImtyaWFnYTNAZ21haWwuY29tIiwicm9sZSI6IlVzZXIiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9zaWQiOiIxMjUwIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy92ZXJzaW9uIjoiMTA4IiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9saW1pdCI6IjEwMCIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcCI6IkJhc2ljIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9sYW5ndWFnZSI6ImVuLWdiIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9leHBpcmF0aW9uIjoiMjA5OS0xMi0zMSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcHN0YXJ0IjoiMjAxOC0xMC0wNyIsImlzcyI6Imh0dHBzOi8vYXV0aHNlcnZpY2UucHJpYWlkLmNoIiwiYXVkIjoiaHR0cHM6Ly9oZWFsdGhzZXJ2aWNlLnByaWFpZC5jaCIsImV4cCI6MTUzOTI2Nzc5NiwibmJmIjoxNTM5MjYwNTk2fQ.yrYLIbaJB6GQImHxXTqLsf0AmTdH_8Aslm_FEVpFUIg&format=json&language=en-gb"
        resultsMC = urllib.request.urlopen(urlMedicalCondition).read()
        medicalConditions = ast.literal_eval(resultsMC.decode("utf-8"))
        for issue in medicalConditions:
            print(issue['Issue']['Name'])
