
I developed endpoint_query.py and it has no argument just to see each part, the system ask you to press enter.
Plus the stdout print , the log file “called log_endpoint_query.txt” will be created that save the tables in a text.

for the result of the query there is no filtering and all association scores are shown.

For this part I used REST API with request library.

Query the Open Targets associations data REST API endpoint (https://platform-api.opentargets.io/v3/platform/public/association/filter) to get target-disease association information. Use the parameter target to filter for association information for a target. i.e. use ENSG00000197386 as target id 
3.	From the returned JSON objects, parse each entry (association) and print to stdout the  combination of target_id, disease_id & association_score.overall 
4.	Repeat steps 2-3 above to get disease related information using the parameter disease to query for association information for a disease i.e. use Orphanet_399 as disease_id 
5.	At the end calculate and print to stdout the maximum, minimum and average and standard deviation values of association_score.overall for target & disease query 




