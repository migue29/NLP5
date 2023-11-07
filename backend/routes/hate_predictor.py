from fastapi import APIRouter, Response, status
from controllers import hate_predictor

predictor = APIRouter(prefix="/predict",tags=["ML Predictor"])

@predictor.get(
    "/message",
    summary="Enviamos el mensaje que viene por el campo de texto de streamlit",
    response_description="Muestra el mensaje de la predicción",
    status_code=status.HTTP_200_OK,
)
async def receive_message(response: Response):
    return await hate_predictor.receive_message(response)