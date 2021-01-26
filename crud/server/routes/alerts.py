from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from crud.server.database import (
    add_alert,
    delete_alert,
    retrieve_alert,
    retrieve_alerts,
    update_alert,
)
from crud.server.models.alerts import (
    ErrorResponseModel,
    ResponseModel,
    AlertSchema,
    UpdateAlertModel,
)

router = APIRouter()


@router.post("/", response_description="Alert data added into the database")
async def add_alert_data(alert: AlertSchema = Body(...)):
    alert = jsonable_encoder(alert)
    new_alert = await add_alert(alert)
    return ResponseModel(new_alert, "Alert added successfully.")


@router.get("/", response_description="alerts retrieved")
async def get_alerts():
    alerts = await retrieve_alerts()
    if alerts:
        return ResponseModel(alerts, "alerts data retrieved successfully")
    return ResponseModel(alerts, "Empty list returned")


@router.get("/{id}", response_description="alert data retrieved")
async def get_alert_data(id):
    alert = await retrieve_alert(id)
    if alert:
        return ResponseModel(alert, "alert data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "alert doesn't exist.")


async def update_alert_data(id: str, req: UpdateAlertModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_alert = await update_alert(id, req)
    if updated_alert:
        return ResponseModel(
            "alert with ID: {} name update is successful".format(id),
            "alert name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the alert data.",
    )


@router.delete("/{id}", response_description="alert data deleted from the database")
async def delete_alert_data(id: str):
    deleted_alert = await delete_alert(id)
    if deleted_alert:
        return ResponseModel(
            "alert with ID: {} removed".format(id), "alert deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "alert with id {0} doesn't exist".format(id)
    )
