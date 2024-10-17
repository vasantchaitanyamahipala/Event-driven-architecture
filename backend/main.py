from fastapi import FastAPI, HTTPException
from models import User, Ticket
from events import trigger_event, process_events
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI()

# CORS middleware to allow frontend requests (adjust for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development. Replace '*' with frontend domain in production.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage for simplicity
users = {}
tickets = {}

# Root route to confirm the backend is running
@app.get("/")
def read_root():
    return {"message": "Welcome to the Event-Driven Architecture Backend!"}

# Signup endpoint
@app.post("/signup")
def signup(user: User):
    if user.id in users:
        raise HTTPException(status_code=400, detail="User already exists.")
    users[user.id] = user
    return {"message": "User signed up successfully."}

# Update user endpoint
@app.put("/user/{user_id}")
def update_user(user_id: int, user: User):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found.")
    users[user_id] = user
    trigger_event("user_updated", user.dict())  # Trigger event
    process_events()  # Process events immediately for demo
    return {"message": "User updated successfully."}

# Create ticket endpoint
@app.post("/ticket")
def create_ticket(ticket: Ticket):
    if ticket.id in tickets:
        raise HTTPException(status_code=400, detail="Ticket already exists.")
    if ticket.user_id not in users:
        raise HTTPException(status_code=404, detail="User not found.")
    
    tickets[ticket.id] = ticket
    trigger_event("ticket_created", ticket.dict())  # Trigger event
    process_events()  # Process events immediately for demo
    return {"message": "Ticket created successfully."}

# Get user-specific tickets
@app.get("/tickets/{user_id}")
def get_user_tickets(user_id: int):
    user_tickets = [ticket for ticket in tickets.values() if ticket.user_id == user_id]
    if not user_tickets:
        raise HTTPException(status_code=404, detail="No tickets found for the user.")
    return {"tickets": user_tickets}
