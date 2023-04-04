#create a list of AWS services using Python(S3, EC2, Lambda, etc). 
#The list should be empty initially.
aws_services = []


#Populate the list using append or insert.
aws_services = ["EC2", "Lambda", "Dynamodb", "S3"]

#print to check if the services are listed
print(aws_services)

#Append items to the end of the list with the append method.
aws_services.append("Cloudwatch")

#Insert an item at a specified index with the insert method.
aws_services.insert(1, "Cloudtrail")

#print the appended and inserted item services added
print(aws_services)

#Print the list and the length of the list.
print(aws_services)
print(len(aws_services))

#Remove two specific services from the list by name or by index.

#remove by service name
aws_services.remove("EC2")

#remove service by index
aws_services.pop(1)

#Print the new list and the new length of the list.
print(aws_services)
print(len(aws_services))

#Push your code to GitHub and include the link in your LinkedIn write up
