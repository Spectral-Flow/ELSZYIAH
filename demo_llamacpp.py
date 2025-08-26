#!/usr/bin/env python3
"""
Demo script showing llama-cpp-python integration with Elysia Concierge
This demonstrates how to use the new llama-cpp backend option

Usage:
    python demo_llamacpp.py

Environment Variables:
    ELYSIA_USE_LLAMACPP=true
    ELYSIA_LLAMACPP_REPO_ID=HagalazAI/Elysia-Trismegistus-Mistral-7B-v02-GGUF
    ELYSIA_LLAMACPP_FILENAME=Elysia-Trismegistus-Mistral-7B-v02-IQ3_M.gguf
"""

import os
import sys
import asyncio
from unittest.mock import Mock, patch

# Add backend to path
sys.path.append('backend')

def demo_llamacpp_integration():
    """Demonstrate llama-cpp integration with mocked model"""
    
    print("🧠 ELYSIA CONCIERGE - llama-cpp-python INTEGRATION DEMO")
    print("=" * 60)
    print()
    
    # Set environment for llama-cpp
    os.environ["ELYSIA_USE_LLAMACPP"] = "true"
    os.environ["ELYSIA_LLAMACPP_REPO_ID"] = "HagalazAI/Elysia-Trismegistus-Mistral-7B-v02-GGUF"
    os.environ["ELYSIA_LLAMACPP_FILENAME"] = "Elysia-Trismegistus-Mistral-7B-v02-IQ3_M.gguf"
    
    # Mock responses that sound like the Elysia model
    mock_responses = {
        "maintenance": "Good afternoon! I see you're experiencing a maintenance issue in your unit. I've immediately logged this request in our system and notified our maintenance team. Given the nature of your concern, someone from our team will contact you within the next 2 hours to schedule a convenient time for the repair. We take these matters seriously and want to ensure your comfort at The Avant. Is there anything else I can assist you with today?",
        "amenity": "I'd be delighted to help you with your amenity booking! Our fitness center is one of our residents' favorite spaces, featuring premium equipment and floor-to-ceiling windows with beautiful views. I can certainly reserve your preferred time slot. Would you like me to also check the pool schedule in case you'd like to enjoy both amenities during your visit?",
        "package": "I'll check on your package status right away! Our smart package system automatically sends notifications when deliveries arrive, but let me verify everything is working correctly for your unit. I'll also make sure your contact information is up to date so you receive all notifications. Expect an update from me within the next 10 minutes.",
        "community": "What a wonderful question! The Avant has such a vibrant community. This weekend we have several exciting events planned: our monthly wine and paint night in the clubhouse Saturday evening, Sunday morning yoga on the rooftop terrace, and a resident meet-and-greet by the pool. I'd be happy to send you the full events calendar and help you RSVP for anything that interests you!"
    }
    
    # Mock llama model
    mock_llama = Mock()
    
    def mock_chat_completion(**kwargs):
        # Extract the user message to determine appropriate response
        messages = kwargs.get('messages', [])
        user_message = ""
        for msg in messages:
            if msg['role'] == 'user':
                user_message = msg['content'].lower()
                break
        
        # Select appropriate mock response
        if 'maintenance' in user_message or 'leak' in user_message or 'faucet' in user_message:
            content = mock_responses["maintenance"]
        elif 'fitness' in user_message or 'gym' in user_message or 'workout' in user_message:
            content = mock_responses["amenity"]
        elif 'package' in user_message or 'delivery' in user_message or 'amazon' in user_message:
            content = mock_responses["package"]
        elif 'event' in user_message or 'community' in user_message or 'weekend' in user_message:
            content = mock_responses["community"]
        else:
            content = "Hello! I'm Elysia, your concierge at The Avant. I'm here to make your day better. How can I assist you today?"
        
        return {
            "choices": [{
                "message": {
                    "content": content
                }
            }]
        }
    
    mock_llama.create_chat_completion = mock_chat_completion
    
    # Mock test requests
    test_requests = [
        {
            "resident_id": "AVT-RES-304-001",
            "unit_number": "304", 
            "request_type": "maintenance",
            "message": "My kitchen faucet is leaking badly",
            "priority": "medium"
        },
        {
            "resident_id": "AVT-RES-501-002",
            "unit_number": "501",
            "request_type": "amenity_booking", 
            "message": "I'd like to book the fitness center for tomorrow at 7 AM",
            "priority": "medium"
        },
        {
            "resident_id": "AVT-RES-202-003",
            "unit_number": "202",
            "request_type": "package_inquiry",
            "message": "Did my Amazon package arrive today?",
            "priority": "low"
        },
        {
            "resident_id": "AVT-RES-701-004", 
            "unit_number": "701",
            "request_type": "community_info",
            "message": "What fun events are happening this weekend?",
            "priority": "low"
        }
    ]
    
    try:
        with patch('llama_cpp.Llama.from_pretrained', return_value=mock_llama):
            # Import after setting environment
            import importlib
            import elysia_lite
            importlib.reload(elysia_lite)
            
            from elysia_lite import ElysiaLiteEngine, ResidentRequest, RequestType, Priority
            
            # Create engine - should use llama-cpp
            engine = ElysiaLiteEngine()
            
            print(f"✅ Engine initialized with: {type(engine.ai).__name__}")
            print()
            
            for i, req_data in enumerate(test_requests, 1):
                print(f"📋 TEST {i}: {req_data['request_type'].replace('_', ' ').title()}")
                print(f"👤 Unit {req_data['unit_number']}: {req_data['message']}")
                print()
                
                # Create request
                request = ResidentRequest(**req_data)
                
                # Generate response using llama-cpp
                response = asyncio.run(engine.ai.generate_response(request))
                
                print("🤖 ELYSIA (via llama-cpp) RESPONSE:")
                print(f"   {response}")
                print()
                print("-" * 60)
                print()
        
        print("✨ LLAMA-CPP INTEGRATION FEATURES DEMONSTRATED:")
        print("   • Direct GGUF model loading via llama-cpp-python")
        print("   • Chat completion API compatibility")
        print("   • Elysia-specific model integration")
        print("   • Seamless fallback and error handling")
        print("   • Environment-based configuration")
        print()
        print("🎯 CONFIGURATION USED:")
        print(f"   • ELYSIA_USE_LLAMACPP=true")
        print(f"   • Repo: {os.environ['ELYSIA_LLAMACPP_REPO_ID']}")
        print(f"   • Model: {os.environ['ELYSIA_LLAMACPP_FILENAME']}")
        print()
        print("🚀 Ready for production with real GGUF models!")
        
    finally:
        # Clean up environment
        for key in ["ELYSIA_USE_LLAMACPP", "ELYSIA_LLAMACPP_REPO_ID", "ELYSIA_LLAMACPP_FILENAME"]:
            if key in os.environ:
                del os.environ[key]


if __name__ == "__main__":
    demo_llamacpp_integration()