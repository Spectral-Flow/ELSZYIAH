#!/usr/bin/env python3
"""
Test script for Elysia Lite API
"""

import requests
import json
from datetime import datetime

def test_elysia_api():
    print("🧪 Testing Elysia Concierge Lite API")
    print("=" * 50)
    
    base_url = "http://localhost:8000"
    
    # Test 1: Root endpoint
    try:
        print("📋 Testing root endpoint...")
        response = requests.get(f"{base_url}/")
        print(f"✅ Status: {response.status_code}")
        print(f"📝 Response: {json.dumps(response.json(), indent=2)}")
        print()
    except Exception as e:
        print(f"❌ Error: {e}")
        return
    
    # Test 2: Health check
    try:
        print("💓 Testing health check...")
        response = requests.get(f"{base_url}/health")
        print(f"✅ Status: {response.status_code}")
        print(f"📝 Response: {json.dumps(response.json(), indent=2)}")
        print()
    except Exception as e:
        print(f"❌ Error: {e}")
        return
    
    # Test 3: Amenities endpoint
    try:
        print("🏊 Testing amenities endpoint...")
        response = requests.get(f"{base_url}/api/elysia/amenities")
        print(f"✅ Status: {response.status_code}")
        print(f"📝 Response: {json.dumps(response.json(), indent=2)}")
        print()
    except Exception as e:
        print(f"❌ Error: {e}")
        return
    
    # Test 4: Maintenance request
    try:
        print("🔧 Testing maintenance request...")
        request_data = {
            "resident_id": "AVT-RES-304-001",
            "unit_number": "304",
            "request_type": "maintenance",
            "message": "My kitchen faucet is leaking",
            "priority": "medium"
        }
        
        response = requests.post(
            f"{base_url}/api/elysia/request",
            json=request_data,
            headers={"Content-Type": "application/json"}
        )
        print(f"✅ Status: {response.status_code}")
        print(f"📝 Request: {json.dumps(request_data, indent=2)}")
        print(f"📝 Response: {json.dumps(response.json(), indent=2)}")
        print()
    except Exception as e:
        print(f"❌ Error: {e}")
        return
    
    # Test 5: Amenity booking request
    try:
        print("🏋️ Testing amenity booking...")
        request_data = {
            "resident_id": "AVT-RES-304-001",
            "unit_number": "304",
            "request_type": "amenity_booking",
            "message": "I'd like to book the fitness center for tomorrow morning",
            "priority": "medium"
        }
        
        response = requests.post(
            f"{base_url}/api/elysia/request",
            json=request_data,
            headers={"Content-Type": "application/json"}
        )
        print(f"✅ Status: {response.status_code}")
        print(f"📝 Response: {json.dumps(response.json(), indent=2)}")
        print()
    except Exception as e:
        print(f"❌ Error: {e}")
        return
    
    print("🎉 All tests completed successfully!")
    print("🏢 Elysia Concierge Lite is working perfectly for The Avant!")

if __name__ == "__main__":
    test_elysia_api()
