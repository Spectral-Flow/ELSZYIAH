"""
Test for llama-cpp-python integration with Elysia Concierge
"""

import os
import asyncio
from unittest.mock import Mock, patch
import pytest
import sys

sys.path.append('backend')


def test_llamacpp_adapter_monkeypatch():
    """Test llama-cpp adapter with mocked model to avoid downloads"""
    
    # Set environment for llama-cpp
    os.environ["ELYSIA_USE_LLAMACPP"] = "true"
    
    # Mock the response structure
    mock_response = {
        "choices": [{
            "message": {
                "content": "I understand your maintenance concern. I'll get our team to address this right away."
            }
        }]
    }
    
    # Mock llama model
    mock_llama = Mock()
    mock_llama.create_chat_completion.return_value = mock_response
    
    try:
        with patch('llama_cpp.Llama.from_pretrained', return_value=mock_llama):
            # Import and reload to pick up environment variable
            import importlib
            import elysia_lite
            importlib.reload(elysia_lite)
            
            from elysia_lite import LlamaCppAI, ResidentRequest, RequestType, Priority
            
            # Create adapter directly
            adapter = LlamaCppAI(mock_llama)
            
            # Create test request
            req = ResidentRequest(
                resident_id="TEST-001",
                unit_number="304",
                request_type=RequestType.MAINTENANCE,
                message="My sink is clogged",
                priority=Priority.MEDIUM
            )
            
            # Test the adapter
            result = asyncio.get_event_loop().run_until_complete(adapter.generate_response(req))
            
            # Verify response
            assert "maintenance concern" in result
            
            # Verify mock was called with correct structure
            mock_llama.create_chat_completion.assert_called_once()
            call_args = mock_llama.create_chat_completion.call_args
            
            # Check that proper parameters were passed
            assert 'messages' in call_args[1]
            assert 'max_tokens' in call_args[1]
            assert 'temperature' in call_args[1]
            
            messages = call_args[1]['messages']
            assert len(messages) == 2
            assert messages[0]['role'] == 'system'
            assert messages[1]['role'] == 'user'
            assert 'Unit 304' in messages[1]['content']
            
    finally:
        # Clean up environment
        if "ELYSIA_USE_LLAMACPP" in os.environ:
            del os.environ["ELYSIA_USE_LLAMACPP"]


def test_llamacpp_error_handling():
    """Test that llama-cpp errors are handled gracefully"""
    
    # Mock a failing model
    mock_llama = Mock()
    mock_llama.create_chat_completion.side_effect = Exception("Model loading failed")
    
    from elysia_lite import LlamaCppAI, ResidentRequest, RequestType, Priority
    
    adapter = LlamaCppAI(mock_llama)
    
    req = ResidentRequest(
        resident_id="TEST-002",
        unit_number="101",
        request_type=RequestType.GENERAL_INQUIRY,
        message="Hello",
        priority=Priority.LOW
    )
    
    # Test error handling
    result = asyncio.get_event_loop().run_until_complete(adapter.generate_response(req))
    
    # Should contain error message but still be helpful
    assert "technical difficulties" in result.lower()
    assert "management office" in result.lower()
    assert "[LlamaCpp error:" in result


def test_llamacpp_engine_selection():
    """Test that engine properly selects llama-cpp when configured"""
    
    # Clean environment first
    for key in ["ELYSIA_USE_LLAMACPP", "ELYSIA_USE_BLOOM", "ELYSIA_USE_HOSTED"]:
        os.environ.pop(key, None)
    
    try:
        # Test llama-cpp selection
        os.environ["ELYSIA_USE_LLAMACPP"] = "true"
        
        mock_llama = Mock()
        with patch('llama_cpp.Llama.from_pretrained', return_value=mock_llama):
            import importlib
            import elysia_lite
            importlib.reload(elysia_lite)
            
            from elysia_lite import ElysiaLiteEngine
            
            engine = ElysiaLiteEngine()
            
            # Should be using LlamaCppAI
            assert hasattr(engine.ai, 'model')
            assert engine.ai.model == mock_llama
            
    finally:
        # Clean up
        for key in ["ELYSIA_USE_LLAMACPP", "ELYSIA_USE_BLOOM", "ELYSIA_USE_HOSTED"]:
            os.environ.pop(key, None)


if __name__ == "__main__":
    test_llamacpp_adapter_monkeypatch()
    test_llamacpp_error_handling()
    test_llamacpp_engine_selection()
    print("✅ All llama-cpp tests passed!")