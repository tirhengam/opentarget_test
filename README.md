# opentarget_test
The goal of this test is to assess the ability to query a remote documented REST API, fetch and analyse the data, and test the code to specifications.

QUESTION 1:
We would like you to build a program (in Python preferably) that can query the Open Targets REST API (https://docs.targetvalidation.org/programmati c-access/rest-api) to get a data value labelled as association_score.overall for a given target or disease id. You are required to parse the output and print a simple analysis to the stdout. 
1.	Parse the arguments from command line, where: 
[your_code] –t ENSG00000197386 
will run analysis for a target 
[your_code] –d Orphanet_399 
will run analysis for a disease 

ANSWER 1:
For this part I developed opentarget_query.py that accept two arguments from command line after –t you can use any other target name 
Just in Terminal command line type: 
python opentarget_query.py -t ENSG00000197386

after –d you can use use any other disease id
python opentarget_query.py -d Orphanet_399

the application create a log file called: log_opentarget_query.txt to check the output carefully with date and time
as simple analysis I just filet the association score overall summary higher than 0.2 and “direct” association.

opentargetclient library is used for implementation.



QUESTIO2-5
2.	Query the Open Targets associations data REST API endpoint (https://platform-api.opentargets.io/v3/platform/public/association/filter) to get target-disease association information. Use the parameter target to filter for association information for a target. i.e. use ENSG00000197386 as target id 
3.	From the returned JSON objects, parse each entry (association) and print to stdout the  combination of target_id, disease_id & association_score.overall 
4.	Repeat steps 2-3 above to get disease related information using the parameter disease to query for association information for a disease i.e. use Orphanet_399 as disease_id 
5.	At the end calculate and print to stdout the maximum, minimum and average and standard deviation values of association_score.overall for target & disease query 


ANSWER 2-5:
For this part I developed endpoint_query.py and it has no argument just to see each part, the system ask you to press enter.
Plus the stdout print , the log file “called log_endpoint_query.txt” will be created that save the tables in a text.

for the result of the query there is no filtering and all association scores are shown.

For this part I used REST API with request library.


