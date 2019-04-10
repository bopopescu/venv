#!/usr/bin/python3.6
import boto3


ec2 = boto3.resource('ec2')





for instance in ec2.instances.all():



   if(instance.tags == None):
       if (instance.state['Name'] == 'terminated'):
           print(instance.id, instance.state['Name'], instance.launch_time, instance.tags)
       elif(instance.state['Name'] == 'starting'):
           print(instance.id, instance.state['Name']+" ", instance.launch_time, instance.tags)
       elif(instance.state['Name'] == 'running'):
           print(instance.id, instance.state['Name']+"   ", instance.launch_time, instance.tags)
       elif (instance.state['Name'] == 'stopping'):
           print(instance.id, instance.state['Name'] + "  ", instance.launch_time, instance.tags)
 #          print(instance.get(u'PublicIpAddress'))
       else:
           print(instance.id, instance.state['Name'] + "   ", instance.launch_time, instance.tags)


   else:
       for d in instance.tags:

           if (instance.state['Name'] == 'terminated'):
               print(instance.id, instance.state['Name'], instance.launch_time, d['Value']),
           elif (instance.state['Name'] == 'starting'):
               print(instance.id, instance.state['Name'] + " ", instance.launch_time, d['Value']),
           elif (instance.state['Name'] == 'running'):
               print(instance.id, instance.state['Name'] + "   ", instance.launch_time, d['Value'] , end = ' '),
               ec2_2 = boto3.client('ec2')                                  
               response = ec2_2.describe_instances().get('Reservations')    
               #print(response)                                             
               for instance in response:                                    
                   find_ipaddrs = instance.get('Instances')                 
                   for key in find_ipaddrs:                                 
                       ipad = key.get('PublicIpAddress')                    
                       print(ipad),  


           elif (instance.state['Name'] == 'stopping'):
               print(instance.id, instance.state['Name'] + "  ", instance.launch_time, d['Value']),
           else:
               print(instance.id, instance.state['Name'] + "   ", instance.launch_time, d['Value'])


#ec2_2 = boto3.client('ec2')
#response = ec2_2.describe_instances().get('Reservations')
##print(response)
####for instance in response:
####    find_ipaddrs = instance.get('Instances')
###    for key in find_ipaddrs:
##        ipad = key.get('PublicIpAddress')
#        print(ipad),

#for i in response:
 #   for n in Reservations:
                                                                                                              
##instance_dict = response.describe_instances().get('Reservations')
##for i in instance_dict:
#    print(i)
