# -*- coding: utf-8 -*-
import boto3
import json
import time
print "loading function..."
def handler(event, context):
    count = 0
    temp = ''
    choiceDict = {}
    #dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    client = boto3.client('dynamodb',region_name='us-west-2', aws_access_key_id='AKIAJOJEQQFYFHORKZEQ', aws_secret_access_key='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')
    #client = boto3.client('dynamodb',region_name='us-west-2')
    #get items from event
    menuId = event.get("menu_id")
    order_id = event.get("order_id")
    customer_name = event.get("customer_name")
    customer_email = event.get("customer_email")
    #insert order into table
    item = {
        'order_id': {"S":order_id},
        'customer_name':{"S": customer_name},
        'customer_email':{"S": customer_email},
        'menu_id': {"S":menuId}
    }
    res = client.put_item(TableName= 'pizza_order', Item = item)
    #get 'selection' from Pizza_Menu table for given menu id
    data =  client.get_item(TableName='Pizza_Menu', Key={'menu_id':{'S':menuId}})['Item']
    choice = data[u'selection']
    choiceList = choice[u'SS']
    for item in choiceList:
        count = count + 1
        temp = temp + str(count) + ". " + item + " "
        choiceDict[str(count)]=str(item).strip('')
   
    userChoice = "Hi " +customer_name + ", please choose one of these selections: " + temp    
    return userChoice

