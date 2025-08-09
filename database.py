from pymongo import MongoClient
from datetime import datetime
import config

def get_mongo_client():
    """Get MongoDB client connection"""
    try:
        client = MongoClient(config.MONGO_URI)
        # Test the connection
        client.admin.command('ping')
        return client
    except Exception as e:
        return None

def log_query(case_type, case_number, filing_year, raw_response):
    """Log query to MongoDB database"""
    try:
        client = get_mongo_client()
        if not client:
            raise Exception("Failed to connect to MongoDB")
            
        db = client[config.MONGO_CONFIG['database']]
        collection = db.queries
        
        query_document = {
            "case_type": case_type,
            "case_number": case_number,
            "filing_year": filing_year,
            "raw_response": raw_response,
            "timestamp": datetime.now(),
            "created_at": datetime.now()
        }
        
        result = collection.insert_one(query_document)
        client.close()
        
        return result.inserted_id
        
    except Exception as e:
        return None

def get_all_queries():
    """Retrieve all queries from MongoDB"""
    try:
        client = get_mongo_client()
        if not client:
            raise Exception("Failed to connect to MongoDB")
            
        db = client[config.MONGO_CONFIG['database']]
        collection = db.queries
        
        queries = list(collection.find().sort("timestamp", -1))
        client.close()
        
        return queries
        
    except Exception as e:
        return []

def get_query_by_case(case_type, case_number, filing_year):
    """Retrieve specific query from MongoDB"""
    try:
        client = get_mongo_client()
        if not client:
            raise Exception("Failed to connect to MongoDB")
            
        db = client[config.MONGO_CONFIG['database']]
        collection = db.queries
        
        query = collection.find_one({
            "case_type": case_type,
            "case_number": case_number,
            "filing_year": filing_year
        })
        
        client.close()
        return query
        
    except Exception as e:
        return None
