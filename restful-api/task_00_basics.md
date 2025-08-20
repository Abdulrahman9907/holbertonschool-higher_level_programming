# Task 0: Basics of HTTP/HTTPS

## HTTP vs HTTPS

### HTTP (Hypertext Transfer Protocol)
- Unsecured protocol for data transfer
- Data transmitted in plain text
- Vulnerable to eavesdropping and tampering
- Uses port 80 by default

### HTTPS (HTTP Secure)
- Secured version of HTTP with SSL/TLS encryption
- Data encrypted during transmission
- Protects against eavesdropping and man-in-the-middle attacks
- Uses port 443 by default
- Essential for sensitive data like banking and authentication

## HTTP Request/Response Structure

### HTTP Request Structure
```
METHOD /path HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Content-Type: application/json

{request body}
```

### HTTP Response Structure
```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 123

{response body}
```

## Common HTTP Methods

1. **GET** - Retrieves data from server
   - Use case: Fetching web pages, API data
   - Example: `GET /users/123`

2. **POST** - Sends data to server to create new resource
   - Use case: Creating new user, submitting forms
   - Example: `POST /users` with user data

3. **PUT** - Updates entire resource on server
   - Use case: Updating user profile completely
   - Example: `PUT /users/123` with full user data

4. **DELETE** - Removes resource from server
   - Use case: Deleting user account, removing post
   - Example: `DELETE /users/123`

## Common HTTP Status Codes

1. **200 OK** - Request successful
   - Scenario: Successfully fetched user data

2. **404 Not Found** - Requested resource doesn't exist
   - Scenario: Accessing non-existent page or API endpoint

3. **401 Unauthorized** - Authentication required
   - Scenario: Accessing protected resource without login

4. **403 Forbidden** - Access denied despite authentication
   - Scenario: Regular user trying to access admin panel

5. **500 Internal Server Error** - Server encountered unexpected error
   - Scenario: Database connection failure, code exceptions