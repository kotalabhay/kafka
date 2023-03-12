import pymongo
client = pymongo.MongoClient("mongodb+srv://kafka_user:Kafka%40123@cluster-kafka.0uk5opz.mongodb.net/?retryWrites=true&w=majority")
collection = client['sample_mflix']['comments']
print(collection)
cursor = collection.find({})
counter=0
for document in cursor:
          print(document)
          counter = counter+1
          if counter>10:
            break