# """
# Basic Calculator Router

# Purpose:
# ------------
# Is file ka sirf ek kaam hai:

# Basic Calculator ke tamam API Endpoints
# isi file me honge.

# Yahan calculation nahi hogi.

# Yahan sirf:

# Receive Request
# ↓

# Service Call

# ↓

# Return Response
# """

from fastapi import APIRouter

router = APIRouter(
    prefix="/calculator",
    tags=["Basic Calculator"]
)
@router.get("/")
def BasicCalculator():
    return {
        "message": "Basic Calculator API"
    }
