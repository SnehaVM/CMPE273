# -*- coding: utf-8 -*-
import boto3
print "loading function..."

def handler(event, context):
    client = boto3.client('dynamodb',region_name='us-west-2', aws_access_key_id='AKIAJOJEQQFYFHORKZEQ', aws_secret_access_key='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')
    store_hours={}
    for item in event["store_hours"]:
        shDict=dict()
        shDict["S"] = event["store_hours"][item]
        store_hours[item] = shDict
    item ={"menu_id":{"S":event["menu_id"]},
         "store_name": {"S":event["store_name"]},
         "selection":{"SS":event["selection"]}, 
         "Size":{"SS":event["size"]},
         "price":{"NS":event["price"]},
         "store_hours":{"M":store_hours}}  
    client.put_item(TableName="Pizza_Menu", Item= item)
    return "ok"
   
