🏠 Project Documentation
StayEase – Smart Property Booking System
1. Introduction

StayEase is a web-based property booking platform inspired by Airbnb. It allows users to list, discover, and book accommodations seamlessly. The system supports secure online payments via Khalti and enables real-time communication between guests and hosts.

2. Objectives
Provide a platform for property listing and booking
Enable secure online payments using Khalti
Allow real-time chat between guest and host
Ensure smooth user experience with role-based access
Maintain secure and scalable architecture
3. System Overview

The system consists of three main user roles:

👤 Guest
Register/Login
Browse properties
Book accommodations
Make payments
Chat with hosts
🏡 Host
Register/Login
List and manage properties
Accept or reject bookings
Chat with guests
⚙️ Admin
Manage users
Monitor listings
Handle disputes
Oversee transactions
4. Key Features
4.1 User Authentication
Secure registration and login
Role-based access (Guest/Host/Admin)
Password encryption
4.2 Property Management
Add/Edit/Delete property listings
Upload images and descriptions
Set price, availability, and location
4.3 Booking System
Select check-in and check-out dates
Real-time availability checking
Booking confirmation system
4.4 Payment Integration (Khalti)
Secure online payment gateway
Payment verification using Khalti API
Transaction history tracking

Flow:

User selects property → clicks “Book”
Redirect to Khalti payment
Payment verification via backend
Booking confirmed upon success
4.5 Real-Time Chat System 💬
One-to-one messaging (Guest ↔ Host)
Instant message delivery
Chat history stored in database

Implementation:

Use Django Channels (WebSockets)
Real-time updates without page refresh
Notifications for new messages
4.6 Search & Filter
Search by location
Filter by price, availability, ratings
Sort results
4.7 Reviews & Ratings
Guests can review properties
Rating system (1–5 stars)
Feedback visibility
5. System Architecture
Frontend
HTML, CSS, JavaScript
Bootstrap / Tailwind (optional)
Backend
Django Framework
Django REST Framework (optional API support)
Database
SQLite (development)
PostgreSQL (production)
Real-Time Communication
Django Channels
Redis (for WebSocket handling)
Payment Integration
Khalti API
6. Database Design (Main Models)
User Model
id
name
email
password
role (Guest/Host/Admin)
Property Model
id
title
description
price
location
host (Foreign Key)
images
Booking Model
id
user
property
check_in
check_out
total_price
status
Payment Model
id
booking
amount
payment_status
khalti_token
transaction_id
Chat Model
id
sender
receiver
message
timestamp
7. Workflow
Booking Flow
User searches property
Selects dates
Books property
Makes payment via Khalti
Booking confirmed
Chat Flow
Guest opens property
Clicks “Chat with Host”
WebSocket connection established
Messages exchanged instantly
8. Security Considerations
Use HTTPS
CSRF protection in Django
Secure payment verification
Authentication & authorization
Input validation
9. Future Enhancements
Mobile app version
AI-based property recommendations
Multi-language support
Advanced analytics dashboard
Email/SMS notifications
10. Conclusion

StayEase provides a complete booking solution with modern features like secure payments and real-time communication. Using Django ensures scalability, while Khalti integration makes it locally relevant. The addition of live chat enhances user experience and trust between guests and hosts.