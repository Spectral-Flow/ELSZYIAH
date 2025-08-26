"""
Quick Test & Demo Script for Elysia Concierge
Tests the API with mock data - no heavy models required
"""

import asyncio
import requests
import json
import time

# Test data for The Avant
test_requests = [
    {
        "resident_id": "AVT-RES-304-001",
        "unit_number": "304",
        "request_type": "maintenance",
        "message": "My kitchen faucet is leaking. Can someone fix it?",
        "priority": "medium"
    },
    {
        "resident_id": "AVT-RES-205-002", 
        "unit_number": "205",
        "request_type": "amenity_booking",
        "message": "I'd like to book the fitness center for tomorrow at 7 AM",
        "priority": "low"
    },
    {
        "resident_id": "AVT-RES-101-003",
        "unit_number": "101", 
        "request_type": "package_inquiry",
        "message": "Is my Amazon package ready for pickup?",
        "priority": "low"
    },
    {
        "resident_id": "AVT-RES-420-004",
        "unit_number": "420",
        "request_type": "guest_access", 
        "message": "Can you set up guest access for my friend visiting this weekend?",
        "priority": "medium"
    }
]

def test_api_endpoint(url: str, timeout: int = 30):
    """Test if API endpoint is responding"""
    try:
        response = requests.get(url, timeout=timeout)
        return response.status_code == 200
    except:
        return False

def test_elysia_chat():
    """Test Elysia concierge chat functionality"""
    
    base_url = "http://localhost:8000"
    
    print("🏢 Testing Elysia Concierge for The Avant")
    print("=" * 50)
    
    # Test health endpoint
    print("🔍 Checking health endpoint...")
    if test_api_endpoint(f"{base_url}/health"):
        print("✅ Health check passed")
    else:
        print("❌ Health check failed - is server running?")
        return
    
    # Test each request type
    for i, test_req in enumerate(test_requests, 1):
        print(f"\n🧪 Test {i}: {test_req['request_type'].title()} Request")
        print(f"👤 Unit {test_req['unit_number']}: {test_req['message']}")
        
        try:
            response = requests.post(
                f"{base_url}/api/elysia/request",
                json=test_req,
                headers={"Content-Type": "application/json"},
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                print(f"✅ Request ID: {result['request_id']}")
                print(f"🤖 Elysia: {result['response'][:200]}...")
                print(f"⏱️  ETA: {result['estimated_resolution_time']}")
            else:
                print(f"❌ Error: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Request failed: {e}")
        
        time.sleep(1)  # Small delay between requests
    
    # Test amenities endpoint
    print(f"\n🏊 Testing amenities endpoint...")
    try:
        response = requests.get(f"{base_url}/api/elysia/amenities")
        if response.status_code == 200:
            amenities = response.json()
            print("✅ Available amenities:")
            for amenity in amenities.get('amenities', []):
                print(f"   • {amenity}")
        else:
            print(f"❌ Amenities request failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Amenities request error: {e}")

if __name__ == "__main__":
    print("🚀 Starting Elysia Concierge Test Suite")
    print("Make sure the server is running: python backend/elysia_concierge.py")
    print("")
    
    # Wait for server to be ready
    print("⏳ Waiting for server to start...")
    for i in range(10):
        if test_api_endpoint("http://localhost:8000/health"):
            print("✅ Server is ready!")
            break
        time.sleep(2)
        print(f"   Checking... ({i+1}/10)")
    else:
        print("❌ Server not responding. Please start manually.")
        exit(1)
    
    # Run tests
    test_elysia_chat()
    
    print("\n🎉 Test suite completed!")
    print("Visit http://localhost:8000 to see the API documentation")
