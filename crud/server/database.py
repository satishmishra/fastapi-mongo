from bson.objectid import ObjectId

import motor.motor_asyncio

MONGO_DETAILS = "mongodb://dev.cyops.cyber:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.alerts

alerts_collection = database.get_collection("alerts_collection")


# Alerts helper
def alerts_helper(alerts) -> dict:
    return {
        "id": str(alerts["_id"]),
        "name": alerts["name"],
        "description": alerts["description"],
        "email": alerts["email"],
        "status": alerts["status"],
        "severity": alerts["severity"]
    }


# Retrieve all alerts present in the database
async def retrieve_alerts():
    alerts = []
    async for alert in alerts_collection.find():
        alerts.append(alerts_helper(alert))
    return alerts


# Add a new alert into to the database
async def add_alert(alert_data: dict) -> dict:
    alert = await alerts_collection.insert_one(alert_data)
    new_alert = await alerts_collection.find_one({"_id": alert.inserted_id})
    return alerts_helper(new_alert)


# Retrieve a alert with a matching ID
async def retrieve_alert(id: str) -> dict:
    alert = await alerts_collection.find_one({"_id": ObjectId(id)})
    if alert:
        return alerts_helper(alert)


# Update a alert with a matching ID
async def update_alert(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    alert = await alerts_collection.find_one({"_id": ObjectId(id)})
    if alert:
        updated_alert = await alerts_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_alert:
            return True
        return False


# Delete a alert from the database
async def delete_alert(id: str):
    alert = await alerts_collection.find_one({"_id": ObjectId(id)})
    if alert:
        await alerts_collection.delete_one({"_id": ObjectId(id)})
        return True
