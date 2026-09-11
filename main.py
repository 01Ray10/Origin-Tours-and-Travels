import fastapi
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

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
def submit_contact_message(data: ContactForm):
    print("=== NEW FORM SUBMISSION ===")
    print("Name:", data.name)
    print("Email:", data.email)
    print("Message:", data.message)
    print("===========================")

    contacts.append(data)

    return {
        "message": "Your message has been received",
        "contact": data,
    }

@app.get("/api/contact")
def get_contact_messages():
    return {"contacts": contacts}

@app.get("/")
def home():
    return {"message": "ORIGIN backend is running"}

@app.get("/api")
def api_home():
    return {"message": "ORIGIN API is running"}


class Destination(BaseModel):
    name: str
    country: str
    duration: str
    price: int
    image: str
    description: str
    link: str


class DestinationUpdate(BaseModel):
    country: Optional[str] = None
    duration: Optional[str] = None
    price: Optional[int] = None
    image: Optional[str] = None
    description: Optional[str] = None
    link: Optional[str] = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "price": 50000,
            }
        }
    }


destinations = [
    {
        "name": "Dubai",
        "country": "United Arab Emirates",
        "duration": "4 Days",
        "price": 45000,
        "image": "New folder/Dubai.jpg",
        "description": "Experience desert adventures, city lights, and modern luxury.",
        "link": "Internationaltours.html",
    },
    {
        "name": "Istanbul",
        "country": "Turkey",
        "duration": "5 Days",
        "price": 55000,
        "image": "New folder/attractions-in-istanbul.png",
        "description": "Discover Istanbul's historic landmarks, markets, and culture.",
        "link": "Internationaltours.html",
    },
    {
        "name": "Kashmir",
        "country": "India",
        "duration": "5 Days",
        "price": 25000,
        "image": "New folder/kashmir.png",
        "description": "Explore Kashmir's valleys, lakes, and mountain landscapes.",
        "link": "Domestictours.html",
    },
    {
        "name": "Switzerland",
        "country": "Switzerland",
        "duration": "7 Days",
        "price": 95000,
        "image": "New folder/switzerland1.png",
        "description": "Travel through alpine villages, lakes, and breathtaking mountain views.",
        "link": "Internationaltours.html",
    },
    {
        "name": "Goa",
        "country": "India",
        "duration": "4 Days",
        "price": 22000,
        "image": "New folder/Goa.png",
        "description": "Enjoy Goa's beaches, coastal scenery, and vibrant local life.",
        "link": "Domestictours.html",
    },
    {
        "name": "Maldives",
        "country": "India",
        "duration": "5 Days",
        "price": 65000,
        "image": "New folder/banner_themaldives_01.jpg",
        "description": "Relax among turquoise waters, beaches, and island resorts.",
        "link": "Internationaltours.html",

    },
    {
        "name": "Hyderabad",
        "country": "India",
        "duration": "11 Days",
        "price" : 55000,
        "image" : "New folder\Hyd.jpg",
        "description": "Enjoy Hyderabad's culture and its culinary",
        "link": "Domestictours.html",
    },
]


@app.get("/api/tours")
def get_tours():
    return {"tours": []}


@app.get(
    "/api/destinations",
    tags=["Destinations"],
    summary="List all destinations",
)
def get_destinations():
    return {"destinations": destinations}


@app.post(
    "/api/destinations",
    tags=["Destinations"],
    summary="Create a destination",
)
def create_destination(destination: Destination):
    destination_data = destination.model_dump()
    destinations.append(destination_data)
    return {
        "message": "Destination created successfully",
        "destination": destination_data,
    }


@app.put(
    "/api/destinations/{destination_name}",
    tags=["Destinations"],
    summary="Update a destination in memory",
)
def update_destination(destination_name: str, updates: DestinationUpdate):
    for destination in destinations:
        if destination["name"].casefold() == destination_name.casefold():
            submitted_updates = updates.model_dump(
                exclude_unset=True,
                exclude_none=True,
            )
            valid_updates = {
                key: value
                for key, value in submitted_updates.items()
                if not (
                    isinstance(value, str)
                    and value.strip().lower() in {"", "string"}
                )
            }
            destination.update(valid_updates)
            return {
                "message": "Destination updated successfully",
                "destination": destination,
            }
    raise fastapi.HTTPException(status_code=404, detail="Destination not found")


@app.get("/api/services")
def get_services():
    return {
"services": [
"Flight booking",
"Hotel reservations",
"Airport transfers",
"Tour planning",
]
}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MY Testing ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

User = ["Dave", "John", "Doe"]

print("Joe" in User)
print(User[1], User[-2])
print(User[0:])

print(len(User))

User.append("Ray")
print(User)

User += ["Jason"]  # to add merge multiple lists into one
User.extend(["Robert", "Jimmy"])  # same as above
print(User)