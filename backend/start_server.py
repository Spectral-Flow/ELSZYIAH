#!/usr/bin/env python3
"""
Elysia Concierge Lite - Startup Script
Simple startup without uvicorn complications
"""

from elysia_lite import app
import uvicorn

if __name__ == "__main__":
    print("🏢 Elysia Concierge Lite for The Avant")
    print("✨ Starting lightweight server...")
    print("🚀 Server will run on http://localhost:8000")
    print("📱 Mobile/Vercel optimized")
    print("=" * 50)
    
    try:
        uvicorn.run(
            app,
            host="0.0.0.0",
            port=8000,
            log_level="info"
        )
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except Exception as e:
        print(f"❌ Server error: {e}")
