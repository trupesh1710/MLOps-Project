#!/usr/bin/env python3
"""
MongoDB Connection Setup and Validation Script
This script helps validate your MongoDB connection and provides setup instructions.
"""

import os
import sys
from src.configuration.mongo_db_connection import MongoDBClient
from src.constants import DATABASE_NAME

def test_mongodb_connection():
    """Test MongoDB connection and provide detailed feedback."""
    print("🔍 Testing MongoDB Connection...")
    print("=" * 50)
    
    # Check if MONGODB_URL environment variable is set
    mongodb_url = os.getenv("MONGODB_URL")
    
    if not mongodb_url:
        print("❌ ERROR: MONGODB_URL environment variable is not set!")
        print("\n📋 To fix this:")
        print("1. Create a .env file in your project root")
        print("2. Add your MongoDB connection string:")
        print("   MONGODB_URL=mongodb+srv://username:password@cluster.mongodb.net/")
        print("\n📝 Example .env file:")
        print("MONGODB_URL=mongodb+srv://dbuser:dbpassword123@cluster0.5svpxcq.mongodb.net/?retryWrites=true&w=majority")
        return False
    
    print(f"✅ MONGODB_URL found: {mongodb_url[:50]}...")
    
    try:
        # Test the connection
        print("\n🔄 Testing connection...")
        client = MongoDBClient(database_name=DATABASE_NAME)
        
        # Get database info
        db = client.database
        collections = db.list_collection_names()
        
        print(f"✅ Successfully connected to MongoDB!")
        print(f"📊 Database: {DATABASE_NAME}")
        print(f"📁 Collections found: {len(collections)}")
        if collections:
            print(f"   - {', '.join(collections[:5])}")
            if len(collections) > 5:
                print(f"   - ... and {len(collections) - 5} more")
        
        return True
        
    except Exception as e:
        print(f"❌ Connection failed: {str(e)}")
        print("\n🔧 Troubleshooting tips:")
        print("1. Check your username and password in the connection string")
        print("2. Ensure your IP address is whitelisted in MongoDB Atlas")
        print("3. Verify the cluster URL is correct")
        print("4. Check if your MongoDB Atlas cluster is running")
        return False

def setup_windows_environment():
    """Provide Windows-specific setup instructions."""
    print("\n🪟 Windows Environment Setup Instructions:")
    print("=" * 50)
    print("Method 1: Using System Environment Variables")
    print("1. Press Windows + R, type 'sysdm.cpl' and press Enter")
    print("2. Click 'Environment Variables'")
    print("3. Under 'User variables', click 'New'")
    print("4. Variable name: MONGODB_URL")
    print("5. Variable value: your-mongodb-connection-string")
    print("6. Click OK and restart your terminal/IDE")
    
    print("\nMethod 2: Using .env file (Recommended)")
    print("1. Create a file named '.env' in your project root")
    print("2. Add your connection string:")
    print("   MONGODB_URL=mongodb+srv://username:password@cluster.mongodb.net/")
    print("3. Install python-dotenv: pip install python-dotenv")
    print("4. The project should automatically load .env file")

def setup_linux_mac_environment():
    """Provide Linux/Mac-specific setup instructions."""
    print("\n🐧 Linux/Mac Environment Setup Instructions:")
    print("=" * 50)
    print("Method 1: Using .env file (Recommended)")
    print("1. Create a file named '.env' in your project root")
    print("2. Add your connection string:")
    print("   MONGODB_URL=mongodb+srv://username:password@cluster.mongodb.net/")
    
    print("\nMethod 2: Using shell environment")
    print("1. Add to ~/.bashrc or ~/.zshrc:")
    print("   export MONGODB_URL='mongodb+srv://username:password@cluster.mongodb.net/'")
    print("2. Run: source ~/.bashrc")

if __name__ == "__main__":
    print("🚀 MongoDB Connection Setup and Validation")
    print("=" * 50)
    
    # Test connection
    success = test_mongodb_connection()
    
    if not success:
        # Detect OS and provide appropriate setup instructions
        if os.name == 'nt':  # Windows
            setup_windows_environment()
        else:  # Linux/Mac
            setup_linux_mac_environment()
    
    print("\n✨ For more help, check the .env.example file!")
