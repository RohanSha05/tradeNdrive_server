# 🚗 ISAMAUTO Full-Stack Platform Overview

## **Project Summary**
**Full-Stack Automotive E-Commerce & Fintech Platform**  
**Frontend:** React 18.3.1 + Vite 6.2.1  
**Backend:** Django 5.2 REST API  
**Database:** SQLite (Local) / MySQL (Production)  
**AI/ML:** OpenAI, Collaborative Filtering  
**Authentication:** Firebase + JWT  

---

## **1. FRONTEND TECHNOLOGY STACK**

### **1.1 Core Framework & Bundling**
| Technology | Version | Purpose |
|-----------|---------|---------|
| **React** | 18.3.1 | UI component library |
| **Vite** | 6.2.1 | Build tool with HMR |
| **React Router DOM** | 6.28.0 | Client-side routing |
| **React Helmet Async** | 1.3.0 | SEO meta tags management |

### **1.2 State Management & Data Fetching**
| Technology | Purpose |
|-----------|---------|
| **Context API** | AuthProvider, ApiProvider for global state |
| **Custom Hooks** | useApi, useAuth, useTrackInteraction |
| **JWT Decode** | 4.0.0 - Token parsing & validation |

### **1.3 Authentication & Backend Integration**
| Technology | Version | Purpose |
|-----------|---------|---------|
| **Firebase** | 11.3.1 | User auth (Email/Google OAuth) |
| **Backend API** | admin.isamauto.ca | REST API endpoints |
| **JWT Tokens** | Custom | Session management |

### **1.4 AI & Machine Learning**
| Technology | Version | Purpose |
|-----------|---------|---------|
| **OpenAI** | 6.10.0 | AI chatbot & recommendations |
| **react-chatbot-kit** | 2.2.2 | Chatbot UI framework |
| **Collaborative Filtering** | Custom | ML car recommendations |

### **1.5 UI & Styling**
| Technology | Version | Purpose |
|-----------|---------|---------|
| **Bootstrap** | 5.3.3 | CSS framework |
| **SASS** | 1.81.0 | CSS preprocessor |
| **FontAwesome** | 6.7.2 | Icon library |
| **Swiper** | 11.1.15 | Carousels & sliders |
| **PhotoSwipe** | 5.4.4 | Image gallery lightbox |
| **RC-Slider** | 11.1.7 | Range sliders |

### **1.6 Data Visualization & Additional Libraries**
| Technology | Version | Purpose |
|-----------|---------|---------|
| **Chart.js** | 4.4.6 | Data visualization |
| **EmailJS** | 4.4.1 | Email service integration |
| **Google Maps API** | 2.20.3 | Location services |
| **SweetAlert2** | Beautiful alerts & modals |
| **React Player** | 2.16.0 | Video player |
| **WOW.js** | Scroll animations |

---

## **2. BACKEND TECHNOLOGY STACK**

### **2.1 Core Framework**
| Technology | Version | Purpose |
|-----------|---------|---------|
| **Django** | 5.2 | Web framework |
| **Django REST Framework** | 3.16.0 | RESTful API |
| **Python** | 3.14.0 | Programming language |

### **2.2 Database**
| Environment | Database | Details |
|-----------|----------|---------|
| **Local Development** | SQLite 3 | File-based (db.sqlite3) |
| **Production** | MySQL 5.7+ | Remote (admin.isamauto.ca) |
| **Connector** | PyMySQL 1.1.1 | MySQL driver |

### **2.3 Admin & UI**
| Technology | Version | Purpose |
|-----------|---------|---------|
| **Jazzmin** | 3.0.1 | Enhanced Django admin |

### **2.4 API & Security**
| Technology | Version | Purpose |
|-----------|---------|---------|
| **django-cors-headers** | 4.7.0 | CORS support |
| **cryptography** | Latest | Secure authentication |

### **2.5 Utilities**
| Technology | Version | Purpose |
|-----------|---------|---------|
| **Pillow** | 11.2.1 | Image processing |
| **sqlparse** | 0.5.3 | SQL utilities |
| **asgiref** | 3.8.1 | ASGI utilities |

---

## **3. FRONTEND FEATURES & ARCHITECTURE**

### **3.1 Car Dealership Features**
```
✅ Car Listings
   - Grid/List views with 30+ vehicles
   - Pagination
   - Status indicators (On Sale, Featured, Sold)

✅ Advanced Filtering
   - Price range (RC-Slider)
   - Brand/Make selection
   - Model selection
   - Year range
   - Fuel type (Petrol, Diesel, Hybrid, Electric)
   - Transmission (Manual, Automatic)
   - Body type (Sedan, SUV, Hatchback, etc.)
   - Drive type (AWD, RWD, FWD)
   - Multiple features selection

✅ Car Details Page
   - Full specifications display
   - Image gallery (PhotoSwipe)
   - Video player (React Player)
   - 5 different detail layouts
   - Star rating display
   - User reviews aggregation
   - Related cars suggestions (ML-powered)
   - Financing options

✅ Car Comparison
   - Compare up to 3 cars side-by-side
   - Specification comparison table
   - Price comparison
   - Feature highlights

✅ Search Functionality
   - Search by title
   - Search by make/brand
   - Search by model
   - Real-time search suggestions

✅ Car Brands
   - Brand grid with logos
   - Brand-specific car listings

✅ Sold Cars Archive
   - View previously sold vehicles
   - Filter sold cars
```

### **3.2 AI & Machine Learning Features**
```
🤖 AI Chatbot (OpenAI Powered)
   - FAQ responses about cars, warranty, financing
   - Car recommendation based on budget
   - EMI/Finance calculation guidance
   - Service booking assistance
   - Order & warranty status tracking
   - 24/7 availability
   - Multi-turn conversations

🧠 ML Car Recommendations
   - Collaborative Filtering algorithm
   - Cosine similarity for user matching
   - Finding similar users by viewing patterns
   - Recommending cars liked by similar users
   - Popularity-based fallback for new users
   - Real-time personalization
   - Recommendation tracking
```

### **3.3 User Authentication (Firebase)**
```
🔐 Email/Password Registration
   - Form validation
   - Password strength requirements
   - Email verification (optional)

🔐 Google OAuth Integration
   - One-click Google sign-in
   - Auto-profile creation

🔐 Password Reset
   - Email-based reset flow
   - Secure token validation

🔐 Protected Routes
   - Dashboard access control
   - Review submission gating
   - Loan application protection

🔐 User Profile Management
   - Edit profile information
   - Change password
   - Profile picture upload
   - Account deletion
```

### **3.4 Finance & Applications**
```
💰 Loan Calculator
   - EMI calculation (Principal, Rate, Tenure)
   - Down payment calculation
   - Total interest calculation
   - Amortization schedule display

📝 Credit Application Form
   - Personal information
   - Employment details
   - Financial information
   - Co-applicant support
   - Document upload
   - Form validation

📝 Trade-In Application
   - Vehicle details
   - Condition assessment
   - Trade-in value estimation

💳 Secure Checkout
   - Payment integration ready
   - Multiple payment methods
   - Transaction tracking
```

### **3.5 Service Booking System**
```
🔧 Service Booking
   - Select service type
   - Choose available slots
   - Provide vehicle details
   - Schedule confirmation
   - Email notifications

📊 Service Status
   - Track repair progress
   - View service updates
   - Download service reports

👨‍💼 Service Admin Panel
   - Manage bookings
   - Update service status
   - Staff assignment
```

### **3.6 Review & Rating System**
```
⭐ Star Rating System
   - 1-5 star ratings
   - Visual star display
   - Rating distribution chart

💬 User Reviews
   - Text review submission
   - Review editing/deletion
   - Review sorting (newest, highest rated)

📊 Review Aggregation
   - Average rating calculation
   - Total review count
   - Rating breakdown (1-5 stars)

🔒 Authentication Required
   - Login wall for reviews
   - User identification
   - Review moderation ready
```

### **3.7 User Dashboard**
```
👤 My Profile
   - View profile information
   - Edit profile
   - Change password
   - Profile picture management

📝 My Reviews
   - View submitted reviews
   - Edit reviews
   - Delete reviews
   - Review history

🚗 Saved Cars (Wishlist)
   - Add/remove favorites
   - Quick access to saved listings
   - Wishlist notifications

📊 Activity History
   - View browsing history
   - Track interactions
   - Download activity report
   - Interaction-based recommendations
```

### **3.8 Content Management**
```
📰 Blog System
   - Article listings
   - Article detail pages
   - Categories
   - Search articles
   - Related articles

🖼️ Gallery
   - Photo gallery grid
   - PhotoSwipe lightbox
   - Image categories
   - High-resolution viewing

👥 Team Pages
   - Staff profiles
   - Agent listings
   - Contact information
   - Testimonials

📍 Contact Page
   - Contact form (EmailJS)
   - Google Maps integration
   - Address display
   - Business hours
   - Social media links

❓ FAQs
   - Accordion-style FAQs
   - Search within FAQs
   - Categorized questions
   - AI chatbot integration
```

### **3.9 Interactive Elements**
```
🎨 Hero Sliders
   - Swiper-based carousels
   - Auto-play with controls
   - Pagination indicators
   - Touch-friendly navigation

🔍 Image Galleries
   - PhotoSwipe lightbox
   - Thumbnail grid
   - Zoom functionality
   - Share options

📊 Charts & Visualizations
   - Price distribution charts
   - Brand popularity charts
   - Review rating charts
   - Chart.js integration

🎬 Video Player
   - React Player integration
   - YouTube video support
   - Car showcase videos
   - Tutorial videos

🗺️ Google Maps
   - Dealership location
   - Directions
   - Store hours
   - Street view
```

### **3.10 SEO & Performance**
```
🌐 Meta Tags Management
   - React Helmet for SEO
   - Dynamic meta descriptions
   - Open Graph tags
   - Twitter cards

⚡ Performance Optimization
   - Code splitting with Vite
   - Lazy loading for images
   - Route-based code splitting
   - Bundle size optimization

🚀 Development Experience
   - Fast HMR (Hot Module Replacement)
   - Instant dev server startup
   - Fast build times

📱 Responsive Design
   - Mobile-first approach
   - Bootstrap responsive grid
   - Touch-friendly interactions
   - Tablet optimization

🎭 Animations
   - WOW.js scroll animations
   - CSS transitions
   - Smooth page transitions
   - Loading states
```

---

## **4. REQUIRED BACKEND API ENDPOINTS**

### **4.1 Car Listing Endpoints** ✅ (Already Implemented)
```
GET     /api/car-listings/                      List all cars with filters
GET     /api/car-listings/<slug>/               Get car details with reviews
GET     /api/car-types/                         List car types
GET     /api/car-brands/                        List brands with logo URLs
GET     /api/body-types/                        List body types
GET     /api/fuel-types/                        List fuel types
GET     /api/drive-types/                       List drive types
GET     /api/gear-types/                        List transmission types
GET     /api/owner-types/                       List owner types
GET     /api/features/                          List available features
GET     /api/car-models/                        List car models
GET     /api/model-years/                       List production years
GET     /api/car-dealers/                       List dealerships
```

### **4.2 Review & Rating Endpoints** ✅ (Already Implemented)
```
POST    /api/reviews/                           Submit car review
GET     /api/reviews/<car_id>/                  Get reviews for a car
GET     /api/car-listings/<slug>/               Includes: average_rating, total_reviews, reviews[]
```

### **4.3 Loan Application Endpoints** ⚙️ (Needs Frontend Integration)
```
POST    /api/loan-applications/                 Submit loan application
GET     /api/loan-applications/                 List user's applications
GET     /api/loan-applications/<id>/            Get application details
PUT     /api/loan-applications/<id>/            Update application
DELETE  /api/loan-applications/<id>/            Cancel application
```

### **4.4 User Profile Endpoints** ❌ (NEEDS BACKEND IMPLEMENTATION)
```
GET     /api/auth/profile/                      Get current user profile
PUT     /api/auth/profile/                      Update user profile
POST    /api/auth/change-password/              Change password
DELETE  /api/auth/account/                      Delete account
```

### **4.5 Wishlist/Saved Cars Endpoints** ❌ (NEEDS BACKEND IMPLEMENTATION)
```
GET     /api/wishlist/                          Get user's saved cars
POST    /api/wishlist/                          Add car to wishlist
DELETE  /api/wishlist/<car_id>/                 Remove from wishlist
GET     /api/wishlist/<car_id>/                 Check if car is saved
```

### **4.6 User Reviews Endpoints** ❌ (NEEDS BACKEND IMPLEMENTATION)
```
GET     /api/reviews/my-reviews/                Get user's submitted reviews
PUT     /api/reviews/<review_id>/               Update own review
DELETE  /api/reviews/<review_id>/               Delete own review
```

### **4.7 Activity/Interaction Tracking** ❌ (NEEDS BACKEND IMPLEMENTATION)
```
POST    /api/interactions/                      Track user interaction (view, click, etc.)
GET     /api/interactions/history/              Get user activity history
GET     /api/interactions/stats/                Get interaction statistics
```

### **4.8 Service Booking Endpoints** ❌ (NEEDS BACKEND IMPLEMENTATION)
```
GET     /api/services/types/                    List service types
GET     /api/services/slots/                    Get available time slots
POST    /api/services/bookings/                 Create service booking
GET     /api/services/bookings/                 List user's bookings
GET     /api/services/bookings/<id>/            Get booking details
PUT     /api/services/bookings/<id>/            Update booking
DELETE  /api/services/bookings/<id>/            Cancel booking
GET     /api/services/bookings/<id>/status/     Get service status updates
```

### **4.9 Content Endpoints** ❌ (NEEDS BACKEND IMPLEMENTATION)
```
GET     /api/blog/posts/                        List blog articles
GET     /api/blog/posts/<slug>/                 Get article details
GET     /api/blog/categories/                   List article categories

GET     /api/gallery/albums/                    List photo albums
GET     /api/gallery/albums/<id>/photos/        Get album photos

GET     /api/team/members/                      List team members
GET     /api/team/members/<id>/                 Get member details

GET     /api/faqs/                              List FAQs
GET     /api/faqs/<category>/                   Get FAQs by category
```

### **4.10 Settings & Configuration** ✅ (Already Implemented)
```
GET     /api/settings/                          Get site settings
GET     /api/page-content/banners/              Get hero banners
GET     /api/page-content/about/                Get about content
```

### **4.11 Contact & Email** ❌ (NEEDS BACKEND IMPLEMENTATION)
```
POST    /api/contact/                           Submit contact form
POST    /api/email/contact/                     Send contact email
POST    /api/email/inquiry/                     Send inquiry email
```

### **4.12 AI & ML Endpoints** ❌ (NEEDS BACKEND IMPLEMENTATION)
```
POST    /api/ai/chat/                           Send message to chatbot
GET     /api/ai/recommendations/                Get ML recommendations
POST    /api/ai/interactions/track/             Track viewing pattern for ML
GET     /api/ai/similar-users/                  Get similar users (for ML)
```

### **4.13 Authentication Endpoints** ⚙️ (Partial - Firebase Frontend, JWT Backend)
```
POST    /api/auth/login/                        JWT token generation
POST    /api/auth/logout/                       Invalidate token
POST    /api/auth/register/                     Create new user
POST    /api/auth/refresh-token/                Refresh JWT token
POST    /api/auth/forgot-password/              Request password reset
POST    /api/auth/reset-password/               Reset password with token
```

### **4.14 Trade-In Application** ❌ (NEEDS BACKEND IMPLEMENTATION)
```
POST    /api/trade-in/                          Submit trade-in application
GET     /api/trade-in/                          List user's trade-in requests
GET     /api/trade-in/<id>/                     Get trade-in details
PUT     /api/trade-in/<id>/                     Update trade-in
```

### **4.15 Car Comparison** ✅ (Frontend Only - Uses existing endpoints)
```
GET     /api/car-listings/<slug1>/              Get car 1 specs
GET     /api/car-listings/<slug2>/              Get car 2 specs
GET     /api/car-listings/<slug3>/              Get car 3 specs
(Frontend handles comparison logic)
```

---

## **5. DATA FLOW & INTEGRATION POINTS**

### **5.1 Car Listing Flow**
```
Frontend (React)
    ↓ (React Router - /cars)
Display Cars List (Filter & Pagination)
    ↓ GET /api/car-listings/?brand=1&fuel=2&price_min=5000
Backend (Django)
    ↓ (Filter & Serialize CarListing)
Return car data + images + average_rating + total_reviews
    ↓
Frontend Renders Grid/List + Reviews Summary
    ↓ (User clicks car)
Navigate to Car Detail (/cars/<slug>)
    ↓ GET /api/car-listings/<slug>/
Get Full Details + All Reviews + Related Cars (ML)
    ↓
Display Detail Page with Gallery, Reviews, ML Recommendations
```

### **5.2 Review Submission Flow**
```
Frontend (React - Car Detail Page)
    ↓ (User clicks "Write Review" + logs in via Firebase)
Show Review Form (Rating + Comment)
    ↓ (Submit button clicked)
POST /api/reviews/ (car_id, rating, comment, user_email, user_name)
    ↓
Backend (Django)
    ↓ (Create CarReview + Calculate average)
Return: {review_id, average_rating, total_reviews}
    ↓
Frontend
    ↓ (Update UI + Show success alert)
Display new average rating + append review to list
```

### **5.3 Wishlist Flow**
```
Frontend (React - Car Card/Detail)
    ↓ (User clicks heart icon + authenticated)
POST /api/wishlist/ {car_id}
    ↓
Backend (Django)
    ↓ (Create Wishlist entry for user)
Return: {status: "added", car_id}
    ↓
Frontend
    ↓ (Update heart icon to filled + show toast)
Store in local state + update UI

Later on Dashboard:
    ↓ GET /api/wishlist/
Return list of saved cars
    ↓
Display Wishlist Grid with option to remove
```

### **5.4 Loan Application Flow**
```
Frontend (React - Loan Form)
    ↓ (User fills form + selects car)
POST /api/loan-applications/ {
  car_id, first_name, last_name, email, phone,
  dob, address, employment_info, co_applicant_flag
}
    ↓
Backend (Django)
    ↓ (Create LoanApplication + EmploymentInfo)
Return: {application_id, status, estimated_approval_date}
    ↓
Frontend
    ↓ (Store application_id in state)
Show confirmation + redirect to dashboard
    ↓ (User can track on Dashboard)
GET /api/loan-applications/<id>/
Display status + next steps
```

### **5.5 Service Booking Flow**
```
Frontend (React - Service Page)
    ↓ (User selects service type + date)
GET /api/services/slots/?service_type=repair&date=2025-01-15
    ↓
Backend (Django)
    ↓ (Query available ServiceSlot entries)
Return available time slots
    ↓
Frontend
    ↓ (Display calendar + time picker)
User selects slot
    ↓ POST /api/services/bookings/ {service_type, slot_id, vehicle_details}
Backend (Django)
    ↓ (Create ServiceBooking + Send confirmation email)
Return: {booking_id, confirmation_number}
    ↓
Frontend
    ↓ (Show confirmation modal)
Display booking ID + next steps
```

### **5.6 ML Recommendations Flow**
```
Frontend (React)
    ↓ (User views car detail or dashboard)
POST /api/ai/interactions/track/ {car_id, interaction_type: "view"}
    ↓
Backend (Django)
    ↓ (Store UserInteraction record)
    ↓ (Background: Update collaborative filtering model)
Later: GET /api/ai/recommendations/
    ↓
Backend (Django)
    ↓ (Run cosine similarity algorithm)
    ↓ (Find similar users + their liked cars)
Return: [{car_id, similarity_score, reason}, ...]
    ↓
Frontend
    ↓ (Display "You might also like" section)
Show recommended cars with reason
```

---

## **6. BACKEND IMPLEMENTATION CHECKLIST**

### **COMPLETED** ✅
- [x] Car Listing Model & Endpoints
- [x] Car Review Model & Endpoints
- [x] Loan Application Model & Endpoints
- [x] Site Settings & Page Content
- [x] Image Upload Support
- [x] Database Migrations
- [x] Admin Panel (Jazzmin)
- [x] CORS Configuration
- [x] API Response Standardization

### **REQUIRED FOR FRONTEND** ❌ (Priority Order)

**Phase 1: User Management (Critical)**
- [ ] User Profile Model (extend Django User)
- [ ] Wishlist Model
- [ ] User Review Management (Edit/Delete own reviews)
- [ ] Activity/Interaction Tracking Model
- [ ] JWT Authentication Endpoints
- [ ] Password Reset Endpoints
- [ ] Profile Update Endpoints

**Phase 2: Service Booking (Important)**
- [ ] ServiceType Model
- [ ] ServiceSlot Model
- [ ] ServiceBooking Model
- [ ] ServiceStatus Tracking
- [ ] Email Notifications
- [ ] Service Admin Views

**Phase 3: Content Management (Important)**
- [ ] BlogPost Model
- [ ] BlogCategory Model
- [ ] Gallery Model
- [ ] TeamMember Model
- [ ] FAQ Model
- [ ] ContactMessage Model

**Phase 4: AI/ML Integration (Nice to Have)**
- [ ] UserInteraction Model
- [ ] ML Recommendation Engine (Collaborative Filtering)
- [ ] OpenAI Integration Wrapper
- [ ] Interaction Tracking Endpoints

**Phase 5: Trade-In & Advanced (Enhancement)**
- [ ] TradeInApplication Model
- [ ] TradeInValuation Model
- [ ] Advanced Car Comparison API
- [ ] Email Service Integration (EmailJS)

---

## **7. DATABASE SCHEMA EXTENSIONS NEEDED**

### **New Models to Create:**

```python
# User Management
User (extend Django User)
UserProfile
Wishlist
UserReview (with edit/delete tracking)
UserInteraction
UserActivityLog

# Service Booking
ServiceType
ServiceSlot
ServiceBooking
ServiceUpdate
ServiceReport

# Content
BlogPost
BlogCategory
GalleryAlbum
GalleryImage
TeamMember
FAQ

# AI/ML
UserInteraction (enhanced)
UserSimilarity
RecommendationLog

# Other
TradeInApplication
ContactMessage
EmailLog
```

---

## **8. FRONTEND COMPONENT HIERARCHY**

```
App.jsx
├── AuthProvider (Firebase)
├── Router
│   ├── Layout
│   │   ├── Navbar
│   │   ├── Hero Slider
│   │   ├── Footer
│   │   └── MobileMenu
│   │
│   ├── Home Page
│   │   ├── Hero
│   │   ├── Featured Cars
│   │   ├── AI Chatbot (FloatingButton)
│   │   ├── Testimonials
│   │   └── CTA
│   │
│   ├── Cars Listing
│   │   ├── Filters (Price, Brand, Model, etc.)
│   │   ├── Search
│   │   ├── CarGrid/CarList
│   │   ├── Pagination
│   │   └── Sorting
│   │
│   ├── Car Detail
│   │   ├── ImageGallery (PhotoSwipe)
│   │   ├── Specifications
│   │   ├── ReviewsSection
│   │   │   ├── ReviewForm
│   │   │   └── ReviewList
│   │   ├── FinancingOptions
│   │   ├── RelatedCars (ML Recommendations)
│   │   └── ActionButtons
│   │
│   ├── Car Comparison
│   │   ├── SelectCars
│   │   ├── ComparisonTable
│   │   └── SpecsDiff
│   │
│   ├── Authentication
│   │   ├── LoginPage
│   │   ├── RegisterPage
│   │   ├── ForgotPassword
│   │   └── ProtectedRoute
│   │
│   ├── User Dashboard
│   │   ├── Profile
│   │   ├── MyReviews
│   │   ├── SavedCars
│   │   ├── ActivityHistory
│   │   ├── MyApplications
│   │   │   ├── LoanApplications
│   │   │   └── TradeInApplications
│   │   └── ServiceBookings
│   │
│   ├── Finance Section
│   │   ├── LoanCalculator
│   │   ├── LoanApplicationForm
│   │   └── TradeInForm
│   │
│   ├── Service Booking
│   │   ├── ServiceSelection
│   │   ├── SlotPicker
│   │   ├── BookingForm
│   │   └── ConfirmationPage
│   │
│   ├── Content Pages
│   │   ├── Blog
│   │   ├── Gallery
│   │   ├── Team
│   │   ├── Contact
│   │   ├── FAQ
│   │   └── About
│   │
│   └── Admin (Optional Frontend)
│       ├── Dashboard
│       ├── ServiceManagement
│       └── ContentManagement
│
├── ChatBot (OpenAI)
│   ├── ChatWindow
│   ├── MessageBubbles
│   └── InputForm
│
└── Utilities
    ├── API Client (axios/fetch wrapper)
    ├── Constants
    └── Helpers
```

---

## **9. API RESPONSE EXAMPLES**

### **Car Listing Response** ✅
```json
{
  "data": [
    {
      "id": 1,
      "title": "Toyota Camry 2023",
      "slug": "toyota-camry-2023",
      "selling_price": 25000,
      "mileage": 15000,
      "fuel_type": { "id": 1, "title": "Petrol" },
      "gear_type": { "id": 2, "title": "Automatic" },
      "featured_image": {
        "id": 5,
        "image_url": "https://admin.isamauto.ca/uploads/cars/1.jpg"
      },
      "average_rating": 4.5,
      "total_reviews": 24,
      "status": "On Sale"
    }
  ],
  "error": null
}
```

### **Car Detail Response** ✅
```json
{
  "data": {
    "id": 1,
    "title": "Toyota Camry 2023",
    "slug": "toyota-camry-2023",
    "selling_price": 25000,
    "mileage": 15000,
    "description": "...",
    "cylinders": 4,
    "engine_size": "2.5L",
    "doors": 4,
    "seats": 5,
    "interior_colors": "Black",
    "exterior_colors": "White, Silver, Black",
    "average_rating": 4.5,
    "total_reviews": 24,
    "reviews": [
      {
        "id": 1,
        "user_name": "John Doe",
        "rating": 5,
        "comment": "Excellent car!",
        "created_at": "2025-12-01"
      }
    ],
    "images": [
      {
        "id": 1,
        "image_url": "https://admin.isamauto.ca/uploads/cars/1.jpg",
        "is_featured": true
      }
    ],
    "dealer": {
      "id": 1,
      "name": "Isam Auto",
      "contact_number": "+1 306 974 4820",
      "whatsapp_link": "https://wa.me/..."
    }
  },
  "error": null
}
```

### **Review Submit Response** ✅
```json
{
  "data": {
    "review_id": 456,
    "average_rating": 4.5,
    "total_reviews": 24,
    "message": "Review submitted successfully"
  },
  "error": null
}
```

### **User Profile Response** ❌ (To be implemented)
```json
{
  "data": {
    "id": 1,
    "email": "user@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "phone": "+1 306 123 4567",
    "profile_picture": "https://admin.isamauto.ca/uploads/profiles/1.jpg",
    "address": "123 Main St, Saskatoon, SK",
    "created_at": "2025-01-01",
    "updated_at": "2025-12-01"
  },
  "error": null
}
```

### **Wishlist Response** ❌ (To be implemented)
```json
{
  "data": {
    "cars": [
      {
        "id": 1,
        "title": "Toyota Camry 2023",
        "slug": "toyota-camry-2023",
        "selling_price": 25000,
        "featured_image": { "image_url": "..." }
      }
    ],
    "total": 3
  },
  "error": null
}
```

---

## **10. DEVELOPMENT TIMELINE ESTIMATE**

### **Phase 1: Foundation (Weeks 1-2)**
- Backend User & Auth Models
- Wishlist System
- User Profile Endpoints
- Frontend Integration

### **Phase 2: Service Booking (Weeks 3-4)**
- Service Models
- Booking System
- Email Notifications
- Frontend UI

### **Phase 3: Content Management (Weeks 5-6)**
- Blog System
- Gallery
- FAQ
- Team Pages

### **Phase 4: AI/ML (Weeks 7-8)**
- Interaction Tracking
- ML Recommendation Engine
- OpenAI Chatbot Integration
- Frontend ML UI

### **Phase 5: Polish & Deployment (Weeks 9-10)**
- Testing & Bug Fixes
- Performance Optimization
- Security Audit
- Production Deployment

---

## **11. KEY INTEGRATION POINTS**

### **Firebase ↔ Django**
```
Firebase Frontend Auth Token
    ↓
Frontend sends token in Authorization header
    ↓ GET /api/auth/profile/ with token
Backend validates token + returns user data
    ↓
Frontend stores in Context API
```

### **OpenAI ↔ Django**
```
Frontend sends chat message
    ↓ POST /api/ai/chat/
Django calls OpenAI API with context
    ↓
Backend returns AI response
    ↓
Frontend displays in chatbot UI
```

### **Collaborative Filtering ↔ Frontend**
```
Frontend tracks user interactions
    ↓ POST /api/ai/interactions/track/
Backend stores interaction data
    ↓ (Periodically recalculate)
Run cosine similarity algorithm
    ↓ GET /api/ai/recommendations/
Return personalized recommendations
    ↓
Frontend displays as "You might also like"
```

---

## **12. SECURITY CONSIDERATIONS**

- [x] CORS properly configured
- [x] CSRF protection enabled
- [x] Authentication required for write operations
- [ ] JWT token expiration handling (Frontend + Backend)
- [ ] Rate limiting on API endpoints
- [ ] Input validation on all endpoints
- [ ] SQL injection prevention (Django ORM)
- [ ] XSS protection (React + sanitization)
- [ ] HTTPS enforcement in production
- [ ] Secure password hashing (Django built-in)
- [ ] Sensitive data encryption
- [ ] API key management for external services (OpenAI, EmailJS)

---

## **SUMMARY**

This is a **full-stack automotive platform** combining:
- **Rich frontend** with React, AI chatbot, ML recommendations
- **Robust backend** with Django REST API
- **Advanced features**: Reviews, Wishlists, Service Booking, Financing
- **Scalable architecture**: Ready for 1000s of cars, users, and transactions

**Ready to Start Development!** 🚀

Next Steps:
1. Finalize backend API contracts
2. Set up development environment
3. Begin Phase 1 implementation (User Management)
4. Integrate Frontend with existing endpoints
5. Build Phase-by-phase toward full feature completion
