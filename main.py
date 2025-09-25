from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LeaveRequest(BaseModel):
    requested_days: int

@app.post("/check-leave")
def check_leave(data: LeaveRequest):
    if data.requested_days <= 12:
        return {"result": f"✅ Approved for {data.requested_days} days off."}
    else:
        return {"result": f"❌ Rejected. You only have 12 days left."}
