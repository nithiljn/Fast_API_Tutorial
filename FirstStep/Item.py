from pydantic import BaseModel,Field
import logging
class Item(BaseModel):
    sid:str = Field(
        ...,description= "Need to know what screen this.."
    )
    Name : str = Field(
        ...,
        description="Need to get Data py employee Name"
    )
    user_id : str | None = None

logger = logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)