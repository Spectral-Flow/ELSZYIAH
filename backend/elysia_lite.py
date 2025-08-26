"""
Elysia Concierge - Ultra Lightweight Version
For immediate testing without heavy model downloads
Mobile/Vercel optimized with intelligent mock responses
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Dict, Any, List, Optional
from enum import Enum
import os
import json
import logging

# Request types for The Avant
class RequestType(str, Enum):
    MAINTENANCE = "maintenance"
    AMENITY_BOOKING = "amenity_booking"
    PACKAGE_INQUIRY = "package_inquiry"
    GUEST_ACCESS = "guest_access"
    COMMUNITY_INFO = "community_info"
    GENERAL_INQUIRY = "general_inquiry"
    EMERGENCY = "emergency"

class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"
    EMERGENCY = "emergency"

class ResidentRequest(BaseModel):
    resident_id: str
    unit_number: str
    request_type: RequestType
    message: str
    priority: Priority = Priority.MEDIUM
    preferred_contact: str = "app"
    timestamp: datetime = Field(default_factory=datetime.now)

class ConciergeResponse(BaseModel):
    response: str
    request_id: str
    estimated_resolution_time: str
    follow_up_needed: bool
    escalation_required: bool
    satisfaction_prompt: bool = True

class IntelligentMockAI:
    """Intelligent mock AI that provides contextual responses"""
    
    def __init__(self):
        self.the_avant_knowledge = {
            "amenities": [
                "Fitness Center (24/7)",
                "Swimming Pool (6 AM - 10 PM)",
                "Clubhouse (6 AM - 11 PM)", 
                "Coworking Spaces (24/7)",
                "Rooftop Terrace (6 AM - 11 PM)",
                "Pet Park (24/7)",
                "Package Room (24/7)",
                "EV Charging Stations"
            ],
            "local_area": {
                "parks": "Cherry Creek State Park (5 min), Centennial Center Park (2 min)",
                "shopping": "Cherry Creek Mall (15 min), Centennial Promenade (5 min)",
                "transit": "Cherry Creek Light Rail Station (10 min)",
                "dining": "Centennial Promenade restaurants, local cafes"
            },
            "building_info": {
                "total_units": 280,
                "floors": 12,
                "built": 2023,
                "style": "Luxury modern apartments"
            }
        }
    
    async def generate_response(self, request: ResidentRequest) -> str:
        """Generate contextual response based on request type and content"""
        
        message_lower = request.message.lower()
        request_type = request.request_type
        
        # Maintenance requests
        if request_type == RequestType.MAINTENANCE:
            if any(word in message_lower for word in ["leak", "water", "faucet", "toilet"]):
                return f"I understand you're experiencing a water-related issue in Unit {request.unit_number}. I've immediately notified our maintenance team, and someone will contact you within 2 hours to schedule a repair. For urgent water issues, we have emergency maintenance available 24/7. Is this causing any immediate damage that needs emergency attention?"
            
            elif any(word in message_lower for word in ["heat", "cold", "hvac", "temperature", "air"]):
                return f"I see you're having HVAC concerns in Unit {request.unit_number}. Our climate control systems are monitored 24/7. I've logged your request and our maintenance team will investigate within 24 hours. In the meantime, you can adjust settings on your smart thermostat. Would you like me to walk you through the controls?"
            
            elif any(word in message_lower for word in ["electric", "power", "outlet", "light"]):
                return f"I've received your electrical issue report for Unit {request.unit_number}. For safety, I'm prioritizing this request. Our certified electrician will be notified immediately and should contact you within 4 hours. Please avoid using the affected outlets until it's resolved. If you're experiencing a complete power outage, please let me know immediately."
            
            else:
                return f"Thank you for reporting this maintenance issue in Unit {request.unit_number}. I've created a work order and our team will assess the situation within 24 hours. You'll receive updates via the app as we progress. Is there anything else about this issue I should know?"
        
        # Amenity bookings
        elif request_type == RequestType.AMENITY_BOOKING:
            if any(word in message_lower for word in ["gym", "fitness", "workout"]):
                return f"I'd be happy to help you book the fitness center! Our 24/7 fitness center features state-of-the-art equipment. Peak hours are 6-9 AM and 5-8 PM. Would you prefer a time outside peak hours for a less crowded experience? I can also set up recurring bookings if you have a regular workout schedule."
            
            elif any(word in message_lower for word in ["pool", "swim", "lap"]):
                return f"Perfect timing for pool season! Our pool is open 6 AM to 10 PM daily. I can book you a lane for lap swimming or reserve poolside seating. We also have pool towels available. What time works best for you? I'll send you the pool rules and current temperature in the app."
            
            elif any(word in message_lower for word in ["clubhouse", "event", "party"]):
                return f"The clubhouse is perfect for gatherings! It accommodates up to 50 people and includes a full kitchen, AV system, and beautiful views. I can check availability and send you the booking details. Are you planning a private event? I can also recommend local catering services that other residents love."
            
            else:
                available_amenities = ", ".join(self.the_avant_knowledge["amenities"])
                return f"I can help you book any of our premium amenities: {available_amenities}. Which one interests you? I'll check availability and get you all set up!"
        
        # Package inquiries
        elif request_type == RequestType.PACKAGE_INQUIRY:
            return f"Let me check on your packages for Unit {request.unit_number}. Our secure package room uses smart lockers with automatic notifications. You should receive an app notification when packages arrive. I'll verify the current status and send you an update within 15 minutes. If you're expecting something specific, I can track it with the carrier."
        
        # Guest access
        elif request_type == RequestType.GUEST_ACCESS:
            return f"I'll be glad to set up guest access! I can create temporary access codes for the main entrance and garage. Your guests will receive instructions via text. How many guests and what dates? I can also provide them with visitor parking information and a brief welcome guide to The Avant's amenities."
        
        # Community info
        elif request_type == RequestType.COMMUNITY_INFO:
            if any(word in message_lower for word in ["event", "social", "community"]):
                return f"We have wonderful community events at The Avant! This month features rooftop yoga sessions, wine tastings in the clubhouse, and our monthly resident mixer. I'll send you the full calendar. We also have a resident WhatsApp group for informal meetups. Would you like to join?"
            
            elif any(word in message_lower for word in ["restaurant", "food", "dining", "eat"]):
                local_dining = self.the_avant_knowledge["local_area"]["dining"]
                return f"Great dining options near The Avant! {local_dining}. I can recommend specific restaurants based on your preferences - Italian, sushi, casual dining, or fine dining. Would you like me to make a reservation somewhere special?"
            
            else:
                return f"The Avant community offers so much! We're perfectly located in Centennial with easy access to Cherry Creek State Park, premium shopping, and the light rail. What specific information can I help you with? I know all the best local spots!"
        
        # General inquiries
        else:
            return f"Hello! I'm Elysia, your personal concierge at The Avant. I'm here 24/7 to help with maintenance requests, amenity bookings, package tracking, guest access, local recommendations, and anything else you need. How can I make your day at The Avant better?"

class ElysiaLiteEngine:
    """Lightweight Elysia engine with intelligent responses"""
    
    def __init__(self):
        self.ai = IntelligentMockAI()
        self.active_requests = {}
        
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("elysia-lite")
    
    async def process_request(self, request: ResidentRequest) -> ConciergeResponse:
        """Process resident request with intelligent mock AI"""
        
        # Generate request ID
        request_id = f"AVT-{datetime.now().strftime('%Y%m%d')}-{len(self.active_requests) + 1:04d}"
        
        # Log request
        self.logger.info(f"Request {request_id}: Unit {request.unit_number} - {request.request_type}")
        
        # Generate intelligent response
        response_text = await self.ai.generate_response(request)
        
        # Determine response characteristics
        eta_mapping = {
            RequestType.MAINTENANCE: "24-48 hours for standard requests",
            RequestType.AMENITY_BOOKING: "Immediate confirmation",
            RequestType.PACKAGE_INQUIRY: "Real-time status update",
            RequestType.GUEST_ACCESS: "Immediate setup",
            RequestType.COMMUNITY_INFO: "Immediate response",
            RequestType.GENERAL_INQUIRY: "Immediate response",
            RequestType.EMERGENCY: "Immediate response"
        }
        
        escalation_needed = request.priority in [Priority.URGENT, Priority.EMERGENCY]
        follow_up_needed = request.request_type in [RequestType.MAINTENANCE, RequestType.GUEST_ACCESS]
        
        response = ConciergeResponse(
            response=response_text,
            request_id=request_id,
            estimated_resolution_time=eta_mapping.get(request.request_type, "Within 24 hours"),
            follow_up_needed=follow_up_needed,
            escalation_required=escalation_needed
        )
        
        # Store request
        self.active_requests[request_id] = {
            "request": request,
            "response": response,
            "timestamp": datetime.now(),
            "status": "active"
        }
        
        return response

# Initialize Elysia Lite
elysia_engine = ElysiaLiteEngine()

# FastAPI app
app = FastAPI(
    title="Elysia Concierge Lite",
    description="Lightweight AI concierge for The Avant luxury apartments",
    version="1.0.0-lite"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Endpoints
@app.post("/api/elysia/request")
async def submit_request(data: ResidentRequest) -> ConciergeResponse:
    """Submit request to Elysia Lite"""
    return await elysia_engine.process_request(data)

@app.get("/api/elysia/amenities")
async def get_amenities() -> Dict[str, Any]:
    """Get The Avant amenities"""
    return {
        "amenities": elysia_engine.ai.the_avant_knowledge["amenities"],
        "operating_hours": {
            "fitness_center": "24/7",
            "pool": "6 AM - 10 PM",
            "clubhouse": "6 AM - 11 PM",
            "coworking": "24/7",
            "rooftop": "6 AM - 11 PM"
        },
        "booking_available": True
    }

@app.get("/api/elysia/community")
async def get_community_info() -> Dict[str, Any]:
    """Get The Avant community info"""
    return {
        "property_name": "The Avant",
        "location": "Centennial, Colorado",
        "local_highlights": [
            "Cherry Creek State Park - 5 minutes",
            "Centennial Center Park - 2 minutes",
            "Light Rail Access - Cherry Creek Station",
            "Premium Shopping - Cherry Creek Mall",
            "Dining - Centennial Promenade"
        ],
        "building_info": elysia_engine.ai.the_avant_knowledge["building_info"]
    }

@app.get("/health")
async def health_check():
    """Health check"""
    return {
        "status": "healthy",
        "service": "Elysia Concierge Lite",
        "property": "The Avant",
        "version": "1.0.0-lite",
        "mode": "intelligent_mock",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/")
async def root():
    """API info"""
    return {
        "service": "Elysia Concierge Lite API",
        "property": "The Avant - Centennial, Colorado",
        "description": "Lightweight AI concierge with intelligent responses",
        "version": "1.0.0-lite",
        "endpoints": {
            "chat": "/api/elysia/request",
            "amenities": "/api/elysia/amenities",
            "community": "/api/elysia/community",
            "health": "/health",
            "docs": "/docs"
        }
    }

# Server can be started with: python -m uvicorn elysia_lite:app --host 0.0.0.0 --port 8000 --reload
