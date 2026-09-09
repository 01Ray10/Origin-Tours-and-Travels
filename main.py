import fastapi
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = fastapi.FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "http://127.0.0.1:5501",
        "http://localhost:5501",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type"],
)

class ContactForm(BaseModel):
    name: str
    email: str
    message: str


contacts = []


@app.post("/api/contact")
def receive_contact(data: ContactForm):
    # --- ADD THE PRINT STATEMENTS HERE ---
    print("=== NEW FORM SUBMISSION ===")
    print("Name:", data.name)
    print("Email:", data.email)
    print("Message:", data.message)
    print("===========================")

    contacts.append(data)

    return {"message": "Your message has been received"}


@app.get("/api/contact")
def get_contacts():
    return {"contacts": contacts}

@app.get("/")
def home():
    return {"message": "ORIGIN backend is running"}

@app.get("/api")
def api_home():
    return {"message": "ORIGIN API is running"}


@app.get("/api/tours")
@app.get("/tours")
def get_tours():
    return {
        "tours": [
            {"id": 1, "name": "Kashmir Escape", "duration": "5 days", "price": 850},
            {"id": 2, "name": "Dubai Discovery", "duration": "4 days", "price": 1200},
            {"id": 3, "name": "Umrah Package", "duration": "10 days", "price": 1800},
        ]
    }


@app.get("/destinations")
def get_destinations():
    return {
        "destinations": [
            {"id": 1, "name": "Kashmir", "country": "India"},
            {"id": 2, "name": "Dubai", "country": "United Arab Emirates"},
            {"id": 3, "name": "Makkah", "country": "Saudi Arabia"},
        ]
    }


@app.get("/services")
def get_services():
    return {
        "services": [
            "Flight booking",
            "Hotel reservations",
            "Airport transfers",
            "Tour planning",
        ]
    }


class ContactMessage(BaseModel):
    name: str
    email: str
    message: str


@app.get("/contact")
def get_contact_messages():
    return {"contacts": contacts}


@app.post("/contact")
def submit_contact_message(contact: ContactMessage):
    return {
        "message": "Your message has been received",
        "contact": contact,
    }
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MY Testing ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
User = ["Dave","John","Doe"]
print("Joe" in User)
print(User[1], User[-2])  
print(User [0:] )            # Shift alt down to copy multi-lines

print(len(User))

User.append("Ray")
print(User)
User += ["Jason"]  #to add merge multiple list into one
User.extend(["Robert", "Jimmy"]) #same as above
print(User)
