import sys
from opentargets import OpenTargetsClient
import datetime

def print_score_overal(message):
    print("%6s | %40s | %15s" % ('index', 'target-disease', 'overall association'))
    log.write("\n%6s | %40s | %15s" % ('index', 'target-disease', 'overall association'))
    for i, r in enumerate(message):
        print("%6d | %40s | %11s" % (i, r['id'], round(r['association_score']['overall'] , 3)))
        log.write("\n%6d | %40s | %11s " % (i, r['id'], round(r['association_score']['overall'] , 3)))

def command_parser():
   client = OpenTargetsClient()
   response = client.filter_associations()

   # first Argument of command line determine if we query target or disease
   if(sys.argv[1] == '-t'):
       print("query target")
       log.write( "%s , query target\n" %(datetime.datetime.now()))

       #the second argument is gene id
       text = "%s" % (sys.argv[2])
       target = response.filter(target = text)
       print(target)

       #simple data filtering
       target.filter(direct=True)
       target.filter(scorevalue_min=0.2)


       print_score_overal(target)



   elif(sys.argv[1] == '-d'):
       print("Query Disease")
       log.write("%s , Query Disease\n" %(datetime.datetime.now()))

       # the second argument is disease id
       text = "%s" % (sys.argv[2])
       disease = response.filter(disease = text)
       print(disease)

       # simple data filtering
       disease.filter(direct=True)
       disease.filter(scorevalue_min=0.2)


       print_score_overal(disease)

   else:
       print("Unresolved Command\n "
             "A correct command should look like this:\n "
             "-d disease_nam or-t target_name for example:\n"
             "–t ENSG00000197386"
        )

#Start point
log = open("log_opentarget_query.txt", "w")
command_parser()