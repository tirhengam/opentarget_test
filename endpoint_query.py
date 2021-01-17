import requests
import sys
import statistics as st

def print_json(response):
    i = 0
    association_array=[]
    print("%6s | %32s | %15s" % ('index', 'target-disease', 'overall association'))
    log.write("\n%6s | %32s | %15s" % ('index', 'target-disease', 'overall association'))
    for e in response.json()['data']:
        i += 1
        overall = round(e['association_score']['overall'], 4)
        print("%6d |%33s | %11s" % (i, e['id'], overall))

        log.write("\n%6d |%33s | %11s" % (i, e['id'], overall))
        association_array.append(overall)



    mean = st.mean(association_array)
    sd = st.stdev(association_array)

    print("\n---------------------------OVERAL SUMMARY---------------------------")
    print("Maximum: %5f  | Minimum: %5f | Mean: %5f | SD: %5f " %( max(association_array) , min(association_array) , mean , sd ))
    log.write("\n---------------------------OVERAL SUMMARY---------------------------")
    log.write("\nMaximum: %5f  | Minimum: %5f | Mean: %5f | SD: %5f " %( max(association_array) , min(association_array) , mean , sd ))

def query_target():
    target_response = requests.get('https://platform-api.opentargets.io/v3/platform/public/association/filter?size=1330&target=ENSG00000197386')
    print_json(target_response)

def query_disease():
    print("strp2: Query  –d Orphanet_399")
    disease_response = requests.get('https://platform-api.opentargets.io/v3/platform/public/association/filter?size=758&disease=Orphanet_399')
    print_json(disease_response)


#Start point
log = open("log_endpoint_query.txt", "w")
log.write("<target ENSG00000197386>")
print("*********  First Part of Quesion  **************\n"
      "We will query opentargets for <<target ENSG00000197386>>\n"
      "The output will be a table of  target-disease  and overall association plus summary statistics"
      )
input("PRESS ENTER ...")
query_target()
input("PRESS ENTER ...")
print("*********  Second Part of Quesion  **************\n"
      "We will query opentargets for <<disease Orphanet_399>>\n"
      "The Out put will be a table of target-disease and overall association plus summary statistics"
      )
input("PRESS ENTER ...")
log.write("\n<disease Orphanet_399>")
query_disease()



