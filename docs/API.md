# 📡 API Documentation

## Elysia Concierge REST API

Complete API reference for the Elysia Concierge system.

## 🌐 Base URL

- **Development**: `http://localhost:8000`
- **Production**: `https://your-domain.vercel.app`

## 🔐 Authentication

Currently, the API uses basic authentication. Future versions will include JWT tokens.

```bash
# Include in headers (if authentication is enabled)
Authorization: Bearer your-token-here
```

## 📋 Common Headers

```bash
Content-Type: application/json
Accept: application/json
```

## 🏥 Health & Status

### GET /health

Check system health and status.

**Response:**
```json
{
  "status": "healthy",
  "service": "Elysia Concierge Lite",
  "property": "The Avant",
  "version": "1.0.0-lite",
  "mode": "intelligent_mock",
  "timestamp": "2024-12-28T10:30:00.000Z"
}
```

**Status Codes:**
- `200`: Service is healthy
- `503`: Service unavailable

### GET /

Service information and available endpoints.

**Response:**
```json
{
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
```

## 🤖 Elysia AI Endpoints

### POST /api/elysia/request

Submit a resident request to the AI concierge.

**Request Body:**
```json
{
  "resident_id": "AVT-RES-304-001",
  "unit_number": "304",
  "request_type": "maintenance",
  "message": "My kitchen faucet is leaking",
  "priority": "medium",
  "contact_method": "email",
  "phone": "+1-555-0123",
  "email": "resident@example.com"
}
```

**Parameters:**
- `resident_id` (string, required): Unique resident identifier
- `unit_number` (string, required): Apartment unit number
- `request_type` (string, required): Type of request
  - `maintenance` - Maintenance and repair requests
  - `amenity_booking` - Amenity reservations
  - `package_inquiry` - Package delivery questions
  - `community_info` - Community events and information
  - `guest_access` - Guest access requests
  - `general` - General inquiries
- `message` (string, required): Detailed request description
- `priority` (string, optional): Request priority
  - `low` - Non-urgent, can wait several days
  - `medium` - Standard priority (default)
  - `high` - Urgent, needs attention within 24 hours
  - `emergency` - Immediate attention required
- `contact_method` (string, optional): Preferred contact method
- `phone` (string, optional): Contact phone number
- `email` (string, optional): Contact email address

**Response:**
```json
{
  "request_id": "REQ-20241228-001",
  "status": "received",
  "response": "Hello! I'm Elysia, your concierge at The Avant. I understand you have a leaking kitchen faucet in unit 304. I've created a maintenance request (ID: MAINT-20241228-001) and notified our maintenance team. They'll contact you within 2-4 hours to schedule a repair. Is there anything else I can help you with today?",
  "estimated_resolution": "2-4 hours",
  "follow_up_needed": false,
  "next_steps": [
    "Maintenance team will contact you within 2-4 hours",
    "Repair will be scheduled at your convenience",
    "You'll receive updates via your preferred contact method"
  ],
  "timestamp": "2024-12-28T10:30:00.000Z"
}
```

**Status Codes:**
- `200`: Request processed successfully
- `400`: Invalid request data
- `422`: Validation error
- `500`: Internal server error

**Example cURL:**
```bash
curl -X POST http://localhost:8000/api/elysia/request \
  -H "Content-Type: application/json" \
  -d '{
    "resident_id": "AVT-RES-304-001",
    "unit_number": "304",
    "request_type": "maintenance",
    "message": "My kitchen faucet is leaking",
    "priority": "medium"
  }'
```

### GET /api/elysia/amenities

Get information about available amenities and their booking status.

**Query Parameters:**
- `date` (string, optional): Date to check availability (YYYY-MM-DD)
- `amenity_type` (string, optional): Filter by amenity type

**Response:**
```json
{
  "amenities": [
    {
      "id": "fitness-center",
      "name": "Fitness Center",
      "description": "24/7 access fitness facility with cardio and weight equipment",
      "location": "Ground Floor",
      "hours": "24/7",
      "booking_required": true,
      "capacity": 15,
      "current_availability": "available",
      "next_available_slot": "2024-12-28T14:00:00.000Z",
      "amenities": [
        "Cardio equipment",
        "Free weights",
        "Cable machines",
        "Yoga mats"
      ]
    },
    {
      "id": "pool",
      "name": "Swimming Pool",
      "description": "Heated indoor pool with adjacent hot tub",
      "location": "Ground Floor",
      "hours": "6:00 AM - 10:00 PM",
      "booking_required": false,
      "capacity": 20,
      "current_availability": "available",
      "temperature": "82°F",
      "amenities": [
        "25-meter lap pool",
        "Hot tub",
        "Pool furniture",
        "Towel service"
      ]
    },
    {
      "id": "clubhouse",
      "name": "Clubhouse",
      "description": "Community gathering space for events and meetings",
      "location": "Second Floor",
      "hours": "8:00 AM - 11:00 PM",
      "booking_required": true,
      "capacity": 50,
      "current_availability": "booked",
      "next_available_slot": "2024-12-29T10:00:00.000Z",
      "amenities": [
        "Meeting rooms",
        "Kitchen facility",
        "Audio/visual equipment",
        "WiFi"
      ]
    }
  ],
  "booking_info": {
    "advance_booking_days": 14,
    "cancellation_policy": "24 hours advance notice",
    "contact": "concierge@theavant.com"
  }
}
```

**Status Codes:**
- `200`: Amenities retrieved successfully
- `400`: Invalid query parameters

### GET /api/elysia/community

Get community information, events, and announcements.

**Query Parameters:**
- `type` (string, optional): Filter by content type
  - `events` - Upcoming events
  - `announcements` - Building announcements
  - `alerts` - Important alerts
- `limit` (integer, optional): Number of items to return (default: 10)

**Response:**
```json
{
  "community_info": [
    {
      "id": "event-holiday-party-2024",
      "type": "event",
      "title": "Holiday Party 2024",
      "description": "Join us for our annual holiday celebration in the clubhouse!",
      "date": "2024-12-31T19:00:00.000Z",
      "location": "Clubhouse",
      "rsvp_required": true,
      "rsvp_deadline": "2024-12-28T23:59:59.000Z",
      "contact": "events@theavant.com",
      "details": {
        "dress_code": "cocktail attire",
        "food": "catered dinner and appetizers",
        "entertainment": "live DJ",
        "age_restriction": "21+"
      }
    },
    {
      "id": "announcement-maintenance-2024-12-30",
      "type": "announcement",
      "title": "Scheduled Maintenance - Elevator B",
      "description": "Elevator B will be out of service for routine maintenance.",
      "date": "2024-12-30T09:00:00.000Z",
      "priority": "medium",
      "affected_areas": ["Elevator B", "Units 201-280"],
      "duration": "4 hours",
      "alternative": "Please use Elevator A or the stairwell"
    },
    {
      "id": "alert-weather-2024-12-28",
      "type": "alert",
      "title": "Winter Weather Advisory",
      "description": "Snow expected tonight. Please move vehicles from fire lanes.",
      "date": "2024-12-28T20:00:00.000Z",
      "priority": "high",
      "expiry": "2024-12-29T12:00:00.000Z",
      "action_required": "Move vehicles from fire lanes and main driveways"
    }
  ],
  "quick_links": {
    "resident_portal": "https://portal.theavant.com",
    "maintenance_requests": "https://portal.theavant.com/maintenance",
    "amenity_booking": "https://portal.theavant.com/amenities",
    "community_calendar": "https://portal.theavant.com/calendar"
  }
}
```

**Status Codes:**
- `200`: Community information retrieved successfully
- `400`: Invalid query parameters

## 📋 Request Types & Examples

### Maintenance Requests

```json
{
  "request_type": "maintenance",
  "message": "My dishwasher is not draining properly",
  "priority": "medium"
}
```

**Common maintenance requests:**
- Plumbing issues
- Electrical problems
- Appliance malfunctions
- HVAC concerns
- Lock/key issues
- General repairs

### Amenity Booking

```json
{
  "request_type": "amenity_booking",
  "message": "I'd like to book the fitness center for tomorrow at 7 AM",
  "priority": "low"
}
```

**Bookable amenities:**
- Fitness center
- Clubhouse
- Conference rooms
- Guest parking spaces

### Package Inquiries

```json
{
  "request_type": "package_inquiry",
  "message": "Has my Amazon package arrived today?",
  "priority": "low"
}
```

### Guest Access

```json
{
  "request_type": "guest_access",
  "message": "Please add guest access for John Smith visiting tomorrow from 2-6 PM",
  "priority": "medium"
}
```

### Community Information

```json
{
  "request_type": "community_info",
  "message": "What events are happening this weekend?",
  "priority": "low"
}
```

## ⚠️ Error Responses

### Error Format

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid request data",
    "details": {
      "field": "unit_number",
      "issue": "Unit number is required"
    }
  },
  "timestamp": "2024-12-28T10:30:00.000Z"
}
```

### Error Codes

- `VALIDATION_ERROR` (400): Invalid or missing required fields
- `AUTHENTICATION_ERROR` (401): Invalid or missing authentication
- `AUTHORIZATION_ERROR` (403): Insufficient permissions
- `NOT_FOUND` (404): Resource not found
- `RATE_LIMIT_EXCEEDED` (429): Too many requests
- `INTERNAL_ERROR` (500): Server error
- `SERVICE_UNAVAILABLE` (503): Service temporarily unavailable

## 📊 Rate Limiting

- **Requests per minute**: 60
- **Requests per hour**: 1000
- **Headers included in response**:
  - `X-RateLimit-Limit`: Request limit
  - `X-RateLimit-Remaining`: Remaining requests
  - `X-RateLimit-Reset`: Reset time (Unix timestamp)

## 🔄 API Versioning

Currently using v1. Future versions will be available at:
- `/api/v1/` - Current version
- `/api/v2/` - Future version

## 📱 Mobile App Integration

### Recommended Headers

```bash
User-Agent: ElysiaConciergeMobile/1.0 (iOS/Android)
X-App-Version: 1.0.0
X-Platform: ios/android
```

### Push Notifications

The API supports webhook endpoints for push notifications:

```json
{
  "webhook_url": "https://your-app.com/webhook",
  "events": ["request_update", "community_alert", "maintenance_complete"]
}
```

## 🧪 Testing

### Interactive Documentation

Visit `/docs` for Swagger UI interactive documentation:
- **Development**: http://localhost:8000/docs
- **Production**: https://your-domain.vercel.app/docs

### Postman Collection

Import the API into Postman:
```bash
# Download collection
curl -o elysia-api.json https://raw.githubusercontent.com/Spectral-Flow/ELSZYIAH/main/docs/postman_collection.json
```

### Example Test Suite

```bash
# Health check
curl -f http://localhost:8000/health

# Submit test request
curl -X POST http://localhost:8000/api/elysia/request \
  -H "Content-Type: application/json" \
  -d '{
    "resident_id": "TEST-001",
    "unit_number": "101",
    "request_type": "maintenance",
    "message": "Test maintenance request",
    "priority": "low"
  }'

# Get amenities
curl http://localhost:8000/api/elysia/amenities

# Get community info
curl http://localhost:8000/api/elysia/community?type=events&limit=5
```

## 📞 Support

- **API Issues**: [GitHub Issues](https://github.com/Spectral-Flow/ELSZYIAH/issues)
- **Documentation**: [GitHub Wiki](https://github.com/Spectral-Flow/ELSZYIAH/wiki)
- **Community**: [Discussions](https://github.com/Spectral-Flow/ELSZYIAH/discussions)