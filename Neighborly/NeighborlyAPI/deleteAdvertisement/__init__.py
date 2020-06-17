import azure.functions as func
import pymongo
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "mongodb://ivanclare:Pr4kEjTLTyh6tXeL5AkQHwPeZOGcTpDRgPaQuXavL95h1tJCjI68vR4wGiALQVLcISP4g21GAXO5AC6mW9pL1A==@ivanclare.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@ivanclare@"  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['neighbourlydb']
            collection = database['advertisements']
            
            #query = {'_id': ObjectId(id)}
            query = {'_id': id}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
