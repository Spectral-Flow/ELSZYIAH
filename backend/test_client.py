#!/usr/bin/env python3
"""
Simple test client for Elysia Concierge API
Tests The Avant concierge functionality
"""

import requests
import json
import time

def test_elysia_api():
    """Test the Elysia Concierge API"""
    base_url = "http://localhost:8000"
    
    print("🏢 Testing Elysia Concierge for The Avant")
    print("=" * 50)
    
    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/health")
        print(f"✅ Health check: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        return
    
    # Test amenities endpoint
    try:
        response = requests.get(f"{base_url}/api/elysia/amenities")
        print(f"✅ Amenities: {response.status_code}")
        amenities = response.json()
        print(f"   Available amenities: {len(amenities.get('amenities', []))}")
    except Exception as e:
        print(f"❌ Amenities test failed: {e}")
    
    # Test community info
    try:
        response = requests.get(f"{base_url}/api/elysia/community")
        print(f"✅ Community info: {response.status_code}")
        community = response.json()
        print(f"   Property: {community.get('property_name', 'Unknown')}")
    except Exception as e:
        print(f"❌ Community test failed: {e}")
    
    # Test concierge request
    test_requests = [
        {
            "resident_id": "AVT-RES-304-001",
            "unit_number": "304",
            "request_type": "general_inquiry",
            "message": "Hello Elysia, how are you today?",
            "priority": "medium"
        },
        {
            "resident_id": "AVT-RES-205-001", 
            "unit_number": "205",
            "request_type": "maintenance",
            "message": "My kitchen faucet is leaking",
            "priority": "high"
        },
        {
            "resident_id": "AVT-RES-101-001",
            "unit_number": "101", 
            "request_type": "amenity_booking",
            "message": "I'd like to book the fitness center for tomorrow morning",
            "priority": "medium"
        }
    ]
    
    print("\n🎯 Testing Concierge Requests")
    print("-" * 30)
    
    for i, request_data in enumerate(test_requests, 1):
        try:
            response = requests.post(
                f"{base_url}/api/elysia/request",
                headers={"Content-Type": "application/json"},
                json=request_data
            )
            
            print(f"\n{i}. Unit {request_data['unit_number']} - {request_data['request_type']}")
            print(f"   Request: \"{request_data['message']}\"")
            print(f"   Status: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                print(f"   ✅ Request ID: {result.get('request_id', 'N/A')}")
                print(f"   🤖 Elysia: \"{result.get('response', 'No response')[:100]}...\"")
                print(f"   ⏱️  ETA: {result.get('estimated_resolution_time', 'Unknown')}")
                
                if result.get('follow_up_needed'):
                    print(f"   📋 Follow-up required")
                if result.get('escalation_required'):
                    print(f"   🚨 Escalation required")
            else:
                print(f"   ❌ Error: {response.text}")
                
        except Exception as e:
            print(f"   ❌ Request failed: {e}")
        
        time.sleep(0.5)  # Small delay between requests
    
    print("\n" + "=" * 50)
    print("✨ Elysia Concierge testing complete!")

if __name__ == "__main__":
    test_elysia_api()
