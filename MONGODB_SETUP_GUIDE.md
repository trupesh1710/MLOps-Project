# MongoDB Connection Setup Guide

This guide will help you resolve the MongoDB authentication error and properly configure your connection.

## 🔍 Problem Summary

The error you're seeing:
```
bad auth : Authentication failed.
```

This occurs because the `MONGODB_URL` environment variable is either:
- Not set
- Contains incorrect credentials
- Has an invalid connection string format

## ✅ Quick Fix Steps

### Step 1: Set Environment Variable

**Windows:**
1. Open Command Prompt as Administrator
2. Run:
```cmd
setx MONGODB_URL "mongodb+srv://dbuser:dbpassword123@cluster0.5svpxcq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
```
3. Restart your terminal/IDE

**Linux/Mac:**
```bash
export MONGODB_URL="mongodb+srv://dbuser:dbpassword123@cluster0.5svpxcq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
```

### Step 2: Using .env File (Recommended)

1. Create a `.env` file in your project root:
```bash
cp .env.example .env
```

2. Edit `.env` with your actual credentials:
```env
MONGODB_URL=mongodb+srv://your-username:your-password@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority&appName=YourClusterName
```

### Step 3: Test Connection

Run the validation script:
```bash
python setup_mongodb_connection.py
```

## 🔧 Connection String Format

Your MongoDB Atlas connection string should look like:
```
mongodb+srv://<username>:<password>@<cluster-url>/<database>?retryWrites=true&w=majority
```

### Example:
```
mongodb+srv://myuser:mypassword@cluster0.abc123.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
```

## 📋 MongoDB Atlas Setup Checklist

1. **Create Cluster**: Ensure your MongoDB Atlas cluster is created and running
2. **Create User**: Create a database user with appropriate permissions
3. **Whitelist IP**: Add your IP address to the IP whitelist
4. **Get Connection String**: Copy the connection string from Atlas dashboard

## 🐛 Troubleshooting

### Common Issues:

1. **"Authentication failed"**
   - Check username/password
   - Ensure user has correct database permissions

2. **"Server selection timeout"**
   - Check IP whitelist settings
   - Verify cluster is running

3. **"Invalid URI"**
   - Ensure special characters in password are URL-encoded
   - Check for typos in connection string

### URL Encoding Special Characters:
If your password contains special characters, encode them:
- `@` → `%40`
- `:` → `%3A`
- `/` → `%2F`
- `+` → `%2B`
- ` ` → `%20`

## 🧪 Testing Your Setup

After setting up, test with:

```python
from src.configuration.mongo_db_connection import MongoDBClient
client = MongoDBClient()
print("✅ Connection successful!")
```

## 📝 Environment Variables Summary

| Variable | Description | Example |
|----------|-------------|---------|
| `MONGODB_URL` | Full MongoDB connection string | `mongodb+srv://user:pass@cluster.mongodb.net/` |

## 🔄 Restart Required

After setting environment variables:
- **VS Code**: Restart the IDE
- **Terminal**: Close and reopen terminal
- **Jupyter**: Restart kernel
- **Docker**: Rebuild containers

## 🆘 Still Having Issues?

1. Run the diagnostic script: `python setup_mongodb_connection.py`
2. Check MongoDB Atlas logs for connection attempts
3. Verify network connectivity to MongoDB Atlas
4. Ensure firewall/antivirus isn't blocking connections
