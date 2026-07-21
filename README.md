<!DOCTYPE html>
<html lang="en" dir="ltr" id="htmlRoot">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DIJA Travels & Tours Ltd | Official Hajj & Umrah Portal</title> <!--[cite: 1] -->
    
    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Google Fonts: Playfair Display, Poppins, Amiri (Arabic) -->
    <link href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">

    <style>
        :root {
            --dija-navy: #0A1128;
            --dija-emerald: #0B5E3C;
            --dija-gold: #C5A059;
            --dija-gold-hover: #b38e46;
            --dija-black: #111111;
            --dija-white: #FFFFFF;
            --dija-bg-white: #FFFFFF;
        }

        /* Uniform White Background Across Desktop & Mobile */
        html, body {
            background-color: var(--dija-bg-white) !important;
            color: var(--dija-black);
            font-family: 'Poppins', sans-serif;
            overflow-x: hidden;
            width: 100%;
            margin: 0;
            padding: 0;
        }

        [dir="rtl"] body {
            font-family: 'Amiri', serif;
        }

        h1, h2, h3, .font-serif {
            font-family: 'Playfair Display', serif;
        }

        [dir="rtl"] h1, [dir="rtl"] h2, [dir="rtl"] h3 {
            font-family: 'Amiri', serif;
        }

        /* Color Utility Classes */
        .bg-dija-navy { background-color: var(--dija-navy) !important; }
        .bg-dija-emerald { background-color: var(--dija-emerald) !important; }
        .bg-dija-white { background-color: var(--dija-white) !important; }
        .text-dija-gold { color: var(--dija-gold) !important; }
        .text-dija-emerald { color: var(--dija-emerald) !important; }
        .text-dija-navy { color: var(--dija-navy) !important; }
        
        .btn-dija-gold {
            background-color: var(--dija-gold);
            color: #ffffff;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
            min-height: 44px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
        }
        .btn-dija-gold:hover {
            background-color: var(--dija-gold-hover);
            color: #ffffff;
            box-shadow: 0 4px 15px rgba(197, 160, 89, 0.4);
        }

        .top-bar-text {
            font-size: 0.825rem;
        }

        /* Hero Slider Custom Styling */
        .hero-slider .carousel-item {
            height: 80vh;
            min-height: 500px;
            max-height: 750px;
            overflow: hidden;
            background-color: var(--dija-black);
        }

        .hero-slider .carousel-item img {
            object-fit: cover;
            height: 100%;
            width: 100%;
            opacity: 0.8;
            transition: transform 6s ease, opacity 1s ease;
        }

        .hero-slider .carousel-item.active img {
            transform: scale(1.05);
            opacity: 0.85;
        }

        .hero-caption-card {
            background: rgba(10, 17, 40, 0.85);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(197, 160, 89, 0.3);
            border-radius: 12px;
            padding: 2rem;
        }

        .fluid-hero-title {
            font-size: clamp(1.75rem, 4.5vw, 3.2rem);
            line-height: 1.2;
        }

        /* Card Customization for Clean White Backgrounds */
        .package-card {
            transition: all 0.3s ease;
            border-radius: 12px;
            overflow: hidden;
            background-color: #FFFFFF !important;
            border: 1px solid #e2e8f0;
            box-shadow: 0 4px 12px rgba(0,0,0,0.04);
        }
        .package-card:hover {
            transform: translateY(-6px);
            box-shadow: 0 12px 28px rgba(0,0,0,0.1) !important;
        }

        .gold-border-top {
            border-top: 4px solid var(--dija-gold) !important;
        }

        /* Floating WhatsApp Button */
        .whatsapp-float {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: #25d366;
            color: #FFF;
            border-radius: 50px;
            width: 50px;
            height: 50px;
            text-align: center;
            font-size: 26px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.25);
            z-index: 1050;
            display: flex;
            align-items: center;
            justify-content: center;
            text-decoration: none;
            transition: all 0.3s ease;
        }
        .whatsapp-float:hover {
            transform: scale(1.1);
            color: #fff;
        }
        [dir="rtl"] .whatsapp-float { right: auto; left: 20px; }

        /* Mobile Breakpoints (< 768px) */
        @media (max-width: 767.98px) {
            html, body {
                background-color: #FFFFFF !important;
            }
            .hero-slider .carousel-item {
                height: auto;
                min-height: 480px;
            }
            .hero-caption-card {
                padding: 1.25rem;
                margin-top: 1rem;
                margin-bottom: 1rem;
            }
            .navbar-brand span {
                font-size: 1.15rem !important;
            }
            .navbar-brand small {
                font-size: 0.65rem !important;
            }
            .package-card {
                margin-bottom: 0.5rem;
            }
        }
    </style>
</head>
<body class="bg-dija-white">

    <!-- TOP BAR -->
    <div class="bg-dija-navy text-white py-2 border-bottom border-warning">
        <div class="container">
            <div class="row align-items-center gy-1 top-bar-text">
                <div class="col-12 col-md-8 d-flex align-items-center justify-content-center justify-content-md-start flex-wrap gap-2 text-center text-md-start">
                    <span><i class="fas fa-id-card text-dija-gold me-1"></i> RC: 618769 / 616768</span> <!--[cite: 1] -->
                    <span class="d-none d-sm-inline">|</span>
                    <span class="d-none d-sm-inline"><i class="fas fa-shield-alt text-dija-gold me-1"></i> NAHCON & IATA Accredited</span> <!--[cite: 1] -->
                </div>
                <div class="col-12 col-md-4 d-flex align-items-center justify-content-center justify-content-md-end gap-3">
                    <small><i class="fas fa-phone-alt text-dija-gold me-1"></i> +234 803 716 5500</small> <!--[cite: 1] -->
                    <!-- Language Switcher Engine -->
                    <select id="languageSelect" class="form-select form-select-sm bg-dark text-white border-warning py-0 px-2" onchange="translatePage(this.value)" style="width: auto; height: 28px;">
                        <option value="en" selected>English</option>
                        <option value="ar">العربية</option>
                        <option value="ha">Hausa</option>
                    </select>
                </div>
            </div>
        </div>
    </div>

    <!-- MAIN NAVBAR -->
    <nav class="navbar navbar-expand-lg sticky-top bg-white shadow-sm py-2 py-lg-3">
        <div class="container">
            <a class="navbar-brand d-flex align-items-center" href="#">
                <i class="fas fa-kaaba text-dija-gold fs-2 me-2"></i>
                <div>
                    <span class="fw-bold text-dija-navy fs-4 d-block lh-1">DIJA <span class="text-dija-emerald">TRAVELS</span></span> <!--[cite: 1] -->
                    <small class="text-muted fs-7 tracking-wide">HAJJ & UMRAH SPECIALIST</small> <!--[cite: 1] -->
                </div>
            </a>
            <button class="navbar-toggler border-0 fs-3" type="button" data-bs-toggle="collapse" data-bs-target="#mainNavbar">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="mainNavbar">
                <ul class="navbar-nav ms-auto mb-2 mb-lg-0 fw-semibold text-center text-lg-start">
                    <li class="nav-item"><a class="nav-link text-dark py-2" href="#about" data-key="nav_about">About Us</a></li>
                    <li class="nav-item"><a class="nav-link text-dark py-2" href="#packages" data-key="nav_packages">Packages</a></li>
                    <li class="nav-item"><a class="nav-link text-dark py-2" href="#visa" data-key="nav_visa">Visa Verification</a></li>
                    <li class="nav-item"><a class="nav-link text-dark py-2" href="#schedule" data-key="nav_schedule">Training Schedule</a></li>
                    <li class="nav-item"><a class="nav-link text-dark py-2" href="#track" data-key="nav_track">Track Booking</a></li>
                    <li class="nav-item"><a class="nav-link text-dark py-2" href="#contact" data-key="nav_contact">Contact</a></li>
                </ul>
                <div class="text-center text-lg-start my-2 my-lg-0">
                    <button class="btn btn-dija-gold ms-lg-3 px-4 rounded-pill shadow-sm w-100 w-lg-auto" data-bs-toggle="modal" data-bs-target="#visaModal" data-key="btn_apply">
                        Apply for Visa
                    </button>
                </div>
            </div>
        </div>
    </nav>

    <!-- HERO SLIDER SECTION -->
    <div id="heroSlider" class="carousel slide hero-slider carousel-fade" data-bs-ride="carousel" data-bs-interval="5000">
        <div class="carousel-inner">
            <!-- Slide 1: Makkah -->
            <div class="carousel-item active">
                <img src="https://images.unsplash.com/photo-1565552645632-d725f8bfc19a?auto=format&fit=crop&w=1600&q=80" alt="Holy Kaaba Makkah">
                <div class="carousel-caption d-flex align-items-center h-100 text-start px-0">
                    <div class="container">
                        <div class="row">
                            <div class="col-12 col-md-10 col-lg-7">
                                <div class="hero-caption-card text-white">
                                    <span class="badge bg-warning text-dark mb-2 px-3 py-2 fw-bold" data-key="hero_badge_1">LICENSED HAJJ OPERATOR</span> <!--[cite: 1] -->
                                    <h1 class="fw-bold text-dija-gold mb-2 mb-md-3 fluid-hero-title" data-key="hero_title_1">Blessed Journeys, Lifetime Memories</h1> <!--[cite: 1] -->
                                    <p class="lead mb-3 mb-md-4 text-light fs-6 fs-md-5" data-key="hero_desc_1">We make your Hajj & Umrah journey spiritual, comfortable, and memorable with trusted services.</p> <!--[cite: 1] -->
                                    <div class="d-flex flex-column flex-sm-row gap-2 gap-sm-3">
                                        <button class="btn btn-dija-gold btn-lg px-4 fs-6" data-bs-toggle="modal" data-bs-target="#visaModal" data-key="cta_apply">Apply for Hajj Visa</button>
                                        <a href="#packages" class="btn btn-outline-light btn-lg px-4 fs-6 text-center" data-key="cta_packages">Book Umrah</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- Slide 2: Madinah -->
            <div class="carousel-item">
                <img src="https://images.unsplash.com/photo-1591604129939-f1efa4d9f7fa?auto=format&fit=crop&w=1600&q=80" alt="Masjid an-Nabawi Madinah">
                <div class="carousel-caption d-flex align-items-center h-100 text-start px-0">
                    <div class="container">
                        <div class="row">
                            <div class="col-12 col-md-10 col-lg-7">
                                <div class="hero-caption-card text-white">
                                    <span class="badge bg-warning text-dark mb-2 px-3 py-2 fw-bold" data-key="hero_badge_2">PREMIUM ACCOMMODATIONS</span> <!--[cite: 1] -->
                                    <h1 class="fw-bold text-dija-gold mb-2 mb-md-3 fluid-hero-title" data-key="hero_title_2">Spiritual Peace in Madinah</h1> <!--[cite: 1] -->
                                    <p class="lead mb-3 mb-md-4 text-light fs-6 fs-md-5" data-key="hero_desc_2">Enjoy top-tier hotel stays steps away from the Prophet's Mosque with dedicated guides.</p> <!--[cite: 1] -->
                                    <div class="d-flex flex-column flex-sm-row gap-2 gap-sm-3">
                                        <a href="#packages" class="btn btn-dija-gold btn-lg px-4 fs-6 text-center" data-key="cta_explore">Explore Packages</a>
                                        <a href="#contact" class="btn btn-outline-light btn-lg px-4 fs-6 text-center" data-key="cta_contact">Contact Us</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <button class="carousel-control-prev d-none d-sm-flex" type="button" data-bs-target="#heroSlider" data-bs-slide="prev">
            <span class="carousel-control-prev-icon"></span>
        </button>
        <button class="carousel-control-next d-none d-sm-flex" type="button" data-bs-target="#heroSlider" data-bs-slide="next">
            <span class="carousel-control-next-icon"></span>
        </button>
    </div>

    <!-- OFFICIAL COMPLIANCE NOTICE -->
    <div class="bg-dija-navy text-white py-3 border-bottom border-warning">
        <div class="container text-center">
            <p class="mb-0 small px-2">
                <i class="fas fa-info-circle text-dija-gold me-1"></i>
                <span data-key="compliance_text">
                    <strong>Official Notice:</strong> Hajj & Umrah visa processing aligns with official Saudi Ministry digital workflows through authorized platforms (Nusuk / Nusuk Hajj). DIJA Travels facilitates application verification, document preparation, and portal submission.
                </span>
            </p>
        </div>
    </div>

    <!-- ABOUT COMPANY SECTION (Uniform White Background) -->
    <section id="about" class="py-4 py-lg-5 bg-dija-white">
        <div class="container py-2 py-lg-4">
            <div class="row align-items-center g-4 g-lg-5">
                <div class="col-12 col-lg-6">
                    <div class="position-relative">
                        <img src="https://images.unsplash.com/photo-1580418827493-f2b22c0a76cb?auto=format&fit=crop&w=800&q=80" alt="Pilgrims performing Tawaf at Makkah" class="img-fluid rounded-4 shadow border w-100">
                        <div class="position-absolute bottom-0 end-0 bg-dija-navy text-white p-3 p-md-4 rounded-4 shadow border border-warning m-2 m-md-3">
                            <h3 class="text-dija-gold mb-0 fw-bold fs-4 fs-md-3">15+ Years</h3>
                            <p class="mb-0 small" data-key="exp_text">Operating Hajj & Umrah since 2005</p> <!--[cite: 1] -->
                        </div>
                    </div>
                </div>
                <div class="col-12 col-lg-6">
                    <span class="text-dija-emerald fw-bold text-uppercase small" data-key="about_subtitle">Your Trusted Travel Partner</span> <!--[cite: 1] -->
                    <h2 class="display-6 fw-bold text-dija-navy mb-3 fs-3 fs-md-2" data-key="about_title">DIJA Travels & Tours Ltd</h2> <!--[cite: 1] -->
                    <p class="text-muted lead fs-6" data-key="about_desc">DIJA Travels & Tours Ltd is a leading Nigerian travel management company committed to delivering comprehensive, reliable, and customer-focused pilgrimage solutions.</p> <!--[cite: 1] -->
                    
                    <div class="row g-2 g-md-3 my-3">
                        <div class="col-6">
                            <div class="d-flex align-items-center">
                                <i class="fas fa-check-circle text-dija-gold fs-5 me-2"></i>
                                <span class="fw-semibold small">NAHCON Licensed</span> <!--[cite: 1] -->
                            </div>
                        </div>
                        <div class="col-6">
                            <div class="d-flex align-items-center">
                                <i class="fas fa-check-circle text-dija-gold fs-5 me-2"></i>
                                <span class="fw-semibold small">IATA Accredited</span> <!--[cite: 1] -->
                            </div>
                        </div>
                        <div class="col-6">
                            <div class="d-flex align-items-center">
                                <i class="fas fa-check-circle text-dija-gold fs-5 me-2"></i>
                                <span class="fw-semibold small">50,000+ Pilgrims</span> <!--[cite: 1] -->
                            </div>
                        </div>
                        <div class="col-6">
                            <div class="d-flex align-items-center">
                                <i class="fas fa-check-circle text-dija-gold fs-5 me-2"></i>
                                <span class="fw-semibold small">24/7 Support</span> <!--[cite: 1] -->
                            </div>
                        </div>
                    </div>

                    <blockquote class="blockquote bg-light p-3 border-start border-4 border-warning rounded fs-6 mt-3 mb-0">
                        <p class="mb-1 text-italic small">"We take care of every detail, so you can focus on what truly matters: your worship and spiritual journey."</p> <!--[cite: 1] -->
                        <footer class="blockquote-footer mt-1 fw-bold text-dija-navy small">Hajiya Halima Yakubu Ndanusa, <cite>Managing Director</cite></footer> <!--[cite: 1] -->
                    </blockquote>
                </div>
            </div>
        </div>
    </section>

    <!-- PACKAGES SECTION (Uniform White Background) -->
    <section id="packages" class="py-4 py-lg-5 bg-dija-white border-top border-bottom">
        <div class="container py-2 py-lg-4">
            <div class="text-center mb-4 mb-lg-5">
                <span class="text-dija-emerald fw-bold text-uppercase small">Spiritual Packages</span>
                <h2 class="display-6 fw-bold text-dija-navy fs-3 fs-md-2" data-key="pkg_heading">Our Popular Packages</h2> <!--[cite: 1] -->
                <div class="bg-dija-gold mx-auto mt-2" style="height: 3px; width: 80px;"></div>
            </div>

            <div class="row g-3 g-lg-4">
                <!-- Economy Package -->
                <div class="col-12 col-md-6 col-lg-4">
                    <div class="card h-100 package-card gold-border-top">
                        <div class="card-body p-3 p-md-4 text-center d-flex flex-column">
                            <span class="badge bg-secondary mb-3 align-self-center px-3 py-2">ECONOMY</span> <!--[cite: 1] -->
                            <h4 class="fw-bold text-dija-navy fs-5">Economy Package</h4> <!--[cite: 1] -->
                            <h2 class="text-dija-emerald my-2 my-md-3 fw-bold fs-3">₦1,250,000</h2> <!--[cite: 1] -->
                            <ul class="list-unstyled text-start my-3 lh-lg flex-grow-1 small">
                                <li><i class="fas fa-hotel text-dija-gold me-2"></i>3-Star Hotel Accommodation</li> <!--[cite: 1] -->
                                <li><i class="fas fa-bus text-dija-gold me-2"></i>Shared Ground Transport</li> <!--[cite: 1] -->
                                <li><i class="fas fa-users text-dija-gold me-2"></i>Group Ziyarah Sightseeing</li> <!--[cite: 1] -->
                                <li><i class="fas fa-file-invoice text-dija-gold me-2"></i>Official Visa Processing Support</li> <!--[cite: 1] -->
                            </ul>
                            <button class="btn btn-dija-gold rounded-pill w-100 py-2 mt-2" data-bs-toggle="modal" data-bs-target="#visaModal">Book Economy</button>
                        </div>
                    </div>
                </div>

                <!-- Standard Package -->
                <div class="col-12 col-md-6 col-lg-4">
                    <div class="card h-100 border-2 border-warning shadow-sm package-card gold-border-top position-relative">
                        <div class="position-absolute top-0 end-0 bg-warning text-dark fw-bold px-3 py-1 fs-7 rounded-bl">MOST POPULAR</div>
                        <div class="card-body p-3 p-md-4 text-center d-flex flex-column">
                            <span class="badge bg-dija-emerald mb-3 align-self-center px-3 py-2">STANDARD</span> <!--[cite: 1] -->
                            <h4 class="fw-bold text-dija-navy fs-5">Standard Package</h4> <!--[cite: 1] -->
                            <h2 class="text-dija-emerald my-2 my-md-3 fw-bold fs-3">₦1,850,000</h2> <!--[cite: 1] -->
                            <ul class="list-unstyled text-start my-3 lh-lg flex-grow-1 small">
                                <li><i class="fas fa-hotel text-dija-gold me-2"></i>4-Star Hotel Close to Haram</li> <!--[cite: 1] -->
                                <li><i class="fas fa-bus-alt text-dija-gold me-2"></i>Air-Conditioned Bus Transfers</li> <!--[cite: 1] -->
                                <li><i class="fas fa-utensils text-dija-gold me-2"></i>Guided Ziyarah & Catering</li> <!--[cite: 1] -->
                                <li><i class="fas fa-chalkboard-teacher text-dija-gold me-2"></i>Pre-Hajj Training Seminars</li> <!--[cite: 1] -->
                            </ul>
                            <button class="btn btn-dija-gold rounded-pill w-100 py-2 mt-2" data-bs-toggle="modal" data-bs-target="#visaModal">Book Standard</button>
                        </div>
                    </div>
                </div>

                <!-- VIP Package -->
                <div class="col-12 col-md-6 col-lg-4">
                    <div class="card h-100 package-card gold-border-top">
                        <div class="card-body p-3 p-md-4 text-center d-flex flex-column">
                            <span class="badge bg-dija-navy text-dija-gold mb-3 align-self-center px-3 py-2">VIP LUXURY</span> <!--[cite: 1] -->
                            <h4 class="fw-bold text-dija-navy fs-5">VIP Package</h4> <!--[cite: 1] -->
                            <h2 class="text-dija-emerald my-2 my-md-3 fw-bold fs-3">₦2,850,000</h2> <!--[cite: 1] -->
                            <ul class="list-unstyled text-start my-3 lh-lg flex-grow-1 small">
                                <li><i class="fas fa-star text-dija-gold me-2"></i>5-Star Hotel (Fairmont/Pullman)</li> <!--[cite: 1] -->
                                <li><i class="fas fa-car text-dija-gold me-2"></i>Private Executive Chauffeur</li> <!--[cite: 1] -->
                                <li><i class="fas fa-user-tie text-dija-gold me-2"></i>Personal Tour Guide & VIP Buffet</li> <!--[cite: 1] -->
                                <li><i class="fas fa-passport text-dija-gold me-2"></i>Priority Nusuk Portal Filing</li> <!--[cite: 1] -->
                            </ul>
                            <button class="btn btn-dija-gold rounded-pill w-100 py-2 mt-2" data-bs-toggle="modal" data-bs-target="#visaModal">Book VIP Luxury</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- TRAINING SCHEDULE & REQUIREMENTS (Uniform White Background) -->
    <section id="schedule" class="py-4 py-lg-5 bg-dija-white">
        <div class="container py-2 py-lg-4">
            <div class="row g-4 g-lg-5">
                <!-- Training Schedule -->
                <div class="col-12 col-lg-6">
                    <h3 class="fw-bold text-dija-navy mb-3 fs-4"><i class="fas fa-calendar-alt text-dija-gold me-2"></i>Hajj Training Schedule 2026</h3>
                    <div class="border-start border-3 border-warning ps-3 ps-md-4 ms-1">
                        <div class="mb-3">
                            <span class="badge bg-dija-navy mb-1">Module 1: Ihram & Niyyah</span>
                            <h5 class="fw-bold mb-1 fs-6">Introduction to Sacred Rituals</h5>
                            <p class="small text-muted mb-0">Saturday, April 11, 2026 | Abuja Head Office & Online Stream</p> <!--[cite: 1] -->
                        </div>
                        <div class="mb-3">
                            <span class="badge bg-dija-navy mb-1">Module 2: Health & Safety</span>
                            <h5 class="fw-bold mb-1 fs-6">Medical Guidelines & Crowd Navigation</h5>
                            <p class="small text-muted mb-0">Saturday, April 25, 2026 | Kano Branch Office</p> <!--[cite: 1] -->
                        </div>
                        <div class="mb-3">
                            <span class="badge bg-dija-navy mb-1">Module 3: Tawaf & Sa'i</span>
                            <h5 class="fw-bold mb-1 fs-6">Practical Simulation Exercises</h5>
                            <p class="small text-muted mb-0">Saturday, May 9, 2026 | National Mosque Complex, Abuja</p> <!--[cite: 1] -->
                        </div>
                    </div>
                </div>

                <!-- Visa Requirements Checklist -->
                <div class="col-12 col-lg-6">
                    <h3 class="fw-bold text-dija-navy mb-3 fs-4"><i class="fas fa-clipboard-list text-dija-gold me-2"></i>Visa Application Requirements</h3>
                    <div class="accordion accordion-flush shadow-sm rounded-3 border" id="reqAccordion">
                        <div class="accordion-item">
                            <h2 class="accordion-header">
                                <button class="accordion-button fw-semibold fs-6" type="button" data-bs-toggle="collapse" data-bs-target="#req1">
                                    Valid International Passport
                                </button>
                            </h2>
                            <div id="req1" class="accordion-collapse collapse show" data-bs-parent="#reqAccordion">
                                <div class="accordion-body small text-muted">
                                    Passport must have at least 6 months validity from the date of travel and contain at least 2 blank pages.
                                </div>
                            </div>
                        </div>
                        <div class="accordion-item">
                            <h2 class="accordion-header">
                                <button class="accordion-button collapsed fw-semibold fs-6" type="button" data-bs-toggle="collapse" data-bs-target="#req2">
                                    Vaccination & Health Certificates
                                </button>
                            </h2>
                            <div id="req2" class="accordion-collapse collapse" data-bs-parent="#reqAccordion">
                                <div class="accordion-body small text-muted">
                                    Yellow Fever card and Meningococcal Meningitis vaccination certificate issued by authorized health institutions.
                                </div>
                            </div>
                        </div>
                        <div class="accordion-item">
                            <h2 class="accordion-header">
                                <button class="accordion-button collapsed fw-semibold fs-6" type="button" data-bs-toggle="collapse" data-bs-target="#req3">
                                    Passport Photographs
                                </button>
                            </h2>
                            <div id="req3" class="accordion-collapse collapse" data-bs-parent="#reqAccordion">
                                <div class="accordion-body small text-muted">
                                    2 recent passport-size photos with a white background.
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- APPLICATION TRACKING SECTION -->
    <section id="track" class="py-4 py-lg-5 bg-dija-navy text-white">
        <div class="container py-2 py-lg-4">
            <div class="row justify-content-center">
                <div class="col-12 col-lg-8 text-center">
                    <h2 class="fw-bold text-dija-gold mb-2 fs-3 fs-md-2">Track Your Application Status</h2>
                    <p class="text-light mb-4 small fs-md-6">Enter your Reference Tracking Code (e.g., DIJA-8F92A) to verify your document submission and Nusuk visa processing stage.</p>
                    
                    <form id="trackingForm" onsubmit="trackBooking(event)" class="row g-2 justify-content-center">
                        <div class="col-12 col-md-8">
                            <input type="text" id="trackCode" class="form-control form-control-lg fs-6" placeholder="Enter Tracking Code (e.g. DIJA-12345)" required>
                        </div>
                        <div class="col-12 col-md-4">
                            <button type="submit" class="btn btn-dija-gold btn-lg w-100 fs-6">Check Status</button>
                        </div>
                    </form>

                    <!-- Tracker Result Box -->
                    <div id="trackerResult" class="mt-4 p-3 p-md-4 rounded-3 bg-white text-dark shadow d-none text-start">
                        <div class="d-flex justify-content-between align-items-center mb-3">
                            <h5 class="fw-bold mb-0 text-dija-navy fs-6 fs-md-5" id="resCode">DIJA-XXXXX</h5>
                            <span class="badge bg-success" id="resStatus">Verified</span>
                        </div>
                        <div class="progress mb-3" style="height: 10px;">
                            <div id="resProgress" class="progress-bar bg-warning" role="progressbar" style="width: 65%;"></div>
                        </div>
                        <p class="small mb-1"><strong>Applicant:</strong> <span id="resName">-</span></p>
                        <p class="small mb-0"><strong>Stage:</strong> <span id="resStage">Documents Submitted to Ministry of Hajj & Umrah</span></p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- FOOTER SECTION -->
    <footer id="contact" class="bg-dija-navy text-white pt-5 pb-3 border-top border-warning">
        <div class="container">
            <div class="row g-4 mb-4">
                <!-- Company Summary -->
                <div class="col-12 col-md-6 col-lg-4">
                    <h5 class="text-dija-gold fw-bold mb-3 fs-6">DIJA Travels & Tours Ltd</h5> <!--[cite: 1] -->
                    <p class="small text-light">Licensed by the National Hajj Commission of Nigeria (NAHCON) and accredited by IATA & NCAA for global travel and pilgrimage management.</p> <!--[cite: 1] -->
                    <div class="d-flex gap-3 fs-5 text-dija-gold mt-3">
                        <a href="#" class="text-dija-gold"><i class="fab fa-facebook"></i></a>
                        <a href="#" class="text-dija-gold"><i class="fab fa-instagram"></i></a>
                        <a href="#" class="text-dija-gold"><i class="fab fa-twitter"></i></a>
                        <a href="#" class="text-dija-gold"><i class="fab fa-whatsapp"></i></a>
                    </div>
                </div>

                <!-- Prayer Times Widget -->
                <div class="col-12 col-md-6 col-lg-4">
                    <h5 class="text-dija-gold fw-bold mb-3 fs-6"><i class="fas fa-mosque me-2"></i>Makkah Prayer Times</h5>
                    <ul class="list-unstyled small text-light mb-0">
                        <li class="d-flex justify-content-between py-1 border-bottom border-secondary"><span>Fajr:</span> <span>04:25 AM</span></li>
                        <li class="d-flex justify-content-between py-1 border-bottom border-secondary"><span>Dhuhr:</span> <span>12:22 PM</span></li>
                        <li class="d-flex justify-content-between py-1 border-bottom border-secondary"><span>Asr:</span> <span>03:45 PM</span></li>
                        <li class="d-flex justify-content-between py-1 border-bottom border-secondary"><span>Maghrib:</span> <span>07:04 PM</span></li>
                        <li class="d-flex justify-content-between py-1"><span>Isha:</span> <span>08:34 PM</span></li>
                    </ul>
                </div>

                <!-- Branch Offices & Contact -->
                <div class="col-12 col-md-12 col-lg-4">
                    <h5 class="text-dija-gold fw-bold mb-3 fs-6">Branch Offices</h5> <!--[cite: 1] -->
                    <p class="small mb-2">
                        <strong>Abuja Head Office:</strong> Suite 203, Grace Plaza, Plot 1456 Ahmadu Bello Way, Area 11, Garki, Abuja.<br> <!--[cite: 1] -->
                        <i class="fas fa-phone-alt text-dija-gold me-1"></i> +234 803 716 5500 | +234 802 309 0022 <!--[cite: 1] -->
                    </p>
                    <p class="small mb-2">
                        <strong>Kano Office:</strong> No. 12, Sultan Road, Kano, Nigeria.<br> <!--[cite: 1] -->
                        <i class="fas fa-phone-alt text-dija-gold me-1"></i> +234 806 123 4567 <!--[cite: 1] -->
                    </p>
                    <p class="small mb-0">
                        <i class="fas fa-envelope text-dija-gold me-1"></i> info@dijatravels.com <!--[cite: 1] -->
                    </p>
                </div>
            </div>

            <!-- Bottom Credits -->
            <div class="row align-items-center py-3 border-top border-secondary g-2">
                <div class="col-12 col-md-6 text-center text-md-start">
                    <span class="small text-muted me-2 d-block d-sm-inline mb-1 mb-sm-0">Payment Options:</span>
                    <span class="badge bg-light text-dark me-1">Paystack</span>
                    <span class="badge bg-light text-dark me-1">Flutterwave</span>
                    <span class="badge bg-light text-dark me-1">Bank Transfer</span>
                    <span class="badge bg-light text-dark me-1">Cards</span>
                </div>
                <div class="col-12 col-md-6 text-center text-md-end">
                    <small class="text-muted">&copy; 2026 DIJA Travels & Tours Ltd. All Rights Reserved.</small> <!--[cite: 1] -->
                </div>
            </div>
        </div>
    </footer>

    <!-- APPLICATION MODAL -->
    <div class="modal fade" id="visaModal" tabindex="-1">
        <div class="modal-dialog modal-lg modal-dialog-centered modal-dialog-scrollable">
            <div class="modal-content">
                <div class="modal-header bg-dija-navy text-white">
                    <h5 class="modal-header-title fw-bold text-dija-gold mb-0 fs-6 fs-md-5">Hajj & Umrah Visa Application Portal</h5>
                    <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body p-3 p-md-4">
                    <form id="visaApplicationForm" onsubmit="submitApplication(event)">
                        <div class="row g-3">
                            <div class="col-12 col-md-6">
                                <label class="form-label fw-semibold small">Full Name (as in Passport)</label>
                                <input type="text" class="form-control" required placeholder="e.g. Amina Ibrahim Yusuf">
                            </div>
                            <div class="col-12 col-md-6">
                                <label class="form-label fw-semibold small">Email Address</label>
                                <input type="email" class="form-control" required placeholder="name@example.com">
                            </div>
                            <div class="col-12 col-md-6">
                                <label class="form-label fw-semibold small">Phone Number (WhatsApp)</label>
                                <input type="tel" class="form-control" required placeholder="+234 803 000 0000">
                            </div>
                            <div class="col-12 col-md-6">
                                <label class="form-label fw-semibold small">International Passport Number</label>
                                <input type="text" class="form-control" required placeholder="A12345678">
                            </div>
                            <div class="col-12 col-md-6">
                                <label class="form-label fw-semibold small">Select Package Tier</label>
                                <select class="form-select" required>
                                    <option value="economy">Economy Package (₦1,250,000)</option>
                                    <option value="standard" selected>Standard Package (₦1,850,000)</option>
                                    <option value="vip">VIP Luxury Package (₦2,850,000)</option>
                                </select>
                            </div>
                            <div class="col-12 col-md-6">
                                <label class="form-label fw-semibold small">Passport Expiry Date</label>
                                <input type="date" class="form-control" required>
                            </div>
                            <div class="col-12">
                                <label class="form-label fw-semibold small">Upload Passport Data Page (PDF / JPG)</label>
                                <input type="file" class="form-control" accept=".pdf,.jpg,.jpeg,.png" required>
                                <small class="text-muted fs-7">Max file size: 5MB. Must be clear and readable.</small>
                            </div>
                            <div class="col-12 mt-3 mt-md-4">
                                <button type="submit" class="btn btn-dija-gold btn-lg w-100 fw-bold fs-6">Submit Application for Verification</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <!-- FLOATING WHATSAPP BUTTON -->
    <a href="https://wa.me/2348061234567" class="whatsapp-float" target="_blank" title="Chat with DIJA Travels">
        <i class="fab fa-whatsapp"></i>
    </a>

    <!-- BOOTSTRAP JS & MULTILINGUAL SCRIPT -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>

    <script>
        const translations = {
            en: {
                nav_about: "About Us",
                nav_packages: "Packages",
                nav_visa: "Visa Verification",
                nav_schedule: "Training Schedule",
                nav_track: "Track Booking",
                nav_contact: "Contact",
                btn_apply: "Apply for Visa",
                hero_badge_1: "LICENSED HAJJ OPERATOR",
                hero_title_1: "Blessed Journeys, Lifetime Memories",
                hero_desc_1: "We make your Hajj & Umrah journey spiritual, comfortable, and memorable with trusted services.",
                cta_apply: "Apply for Hajj Visa",
                cta_packages: "Book Umrah",
                hero_badge_2: "PREMIUM ACCOMMODATIONS",
                hero_title_2: "Spiritual Peace in Madinah",
                hero_desc_2: "Enjoy top-tier hotel stays steps away from the Prophet's Mosque with dedicated guides.",
                cta_explore: "Explore Packages",
                cta_contact: "Contact Us",
                about_subtitle: "Your Trusted Travel Partner",
                about_title: "DIJA Travels & Tours Ltd",
                about_desc: "DIJA Travels & Tours Ltd is a leading Nigerian travel management company committed to delivering comprehensive, reliable, and customer-focused pilgrimage solutions.",
                exp_text: "Operating Hajj & Umrah since 2005",
                pkg_heading: "Our Popular Packages"
            },
            ar: {
                nav_about: "من نحن",
                nav_packages: "البرامج",
                nav_visa: "التحقق من التأشيرة",
                nav_schedule: "جدول التدريب",
                nav_track: "متابعة الحجز",
                nav_contact: "اتصل بنا",
                btn_apply: "التقديم على التأشيرة",
                hero_badge_1: "مرخص من قبل NAHCON",
                hero_title_1: "رحلات مباركة ، وذكريات مدى الحياة",
                hero_desc_1: "نجعل رحلتك في الحج والعمرة مريحة ومباركة عبر أفضل الخدمات الفاخرة الموثوقة.",
                cta_apply: "التقديم على تأشيرة الحج",
                cta_packages: "حجز العمرة",
                hero_badge_2: "إقامة 5 نجوم",
                hero_title_2: "الطمأنينة والسكينة في المدينة المنورة",
                hero_desc_2: "استمتع بالإقامة في أفضل الفنادق على بعد خطوات من المسجد النبوي الشريف.",
                cta_explore: "استكشف الباقات",
                cta_contact: "تواصل معنا",
                about_subtitle: "شريكك الموثوق في السفر",
                about_title: "شركة ديجا للسفريات والسياحة",
                about_desc: "شركة ديجا للسفريات والسياحة هي شركة نيجيرية رائدة متخصصة في تقديم حلول الحج والعمرة المتكاملة.",
                exp_text: "خبرة في تنظيم الحج والعمرة منذ 2005",
                pkg_heading: "باقات الحج والعمرة المميزة"
            },
            ha: {
                nav_about: "Game da Mu",
                nav_packages: "Kunshaye-kunshaye",
                nav_visa: "Binciken Visa",
                nav_schedule: "Tsarin Horo",
                nav_track: "Bincika Littafin",
                nav_contact: "Tuntube Mu",
                btn_apply: "Nemi Visa",
                hero_badge_1: "MAI LASISI DAGA NAHCON",
                hero_title_1: "Tafiye-tafiye Masu Albarka, Tunani na Har Abada",
                hero_desc_1: "Muna gudanar da aikin Hajj da Umrah cikin sauki, jin dadi, da aminci ga duk iyali.",
                cta_apply: "Nemi Visa ta Hajj",
                cta_packages: "Yin Littafin Umrah",
                hero_badge_2: "MASALLATAI MASU TAURARI 5",
                hero_title_2: "Samu Kwanciyar Hankali a Madinah",
                hero_desc_2: "Kula da masallatai kusa da Masallacin Annabi tare da jagororin da ke jin harsuna daban-daban.",
                cta_explore: "Bincika Kunshaye-kunshaye",
                cta_contact: "Tuntube Mu",
                about_subtitle: "Abokin Tafiyarku Abin Dogaro",
                about_title: "DIJA Travels & Tours Ltd",
                about_desc: "DIJA Travels & Tours Ltd kamfani ne mai jagoranci a Najeriya wajen tsara tafiye-tafiyen Hajj da Umrah.",
                exp_text: "Fiye da shekaru 15 muna gudanar da Hajj da Umrah",
                pkg_heading: "Shirye-shiryenmu Masu Popularity"
            }
        };

        function translatePage(lang) {
            const htmlRoot = document.getElementById('htmlRoot');
            if (lang === 'ar') {
                htmlRoot.setAttribute('dir', 'rtl');
            } else {
                htmlRoot.setAttribute('dir', 'ltr');
            }

            document.querySelectorAll('[data-key]').forEach(elem => {
                const key = elem.getAttribute('data-key');
                if (translations[lang] && translations[lang][key]) {
                    elem.innerText = translations[lang][key];
                }
            });
        }

        function trackBooking(event) {
            event.preventDefault();
            const code = document.getElementById('trackCode').value;
            const resultBox = document.getElementById('trackerResult');
            
            document.getElementById('resCode').innerText = code.toUpperCase();
            document.getElementById('resName').innerText = "Amina Ibrahim Yusuf";
            document.getElementById('resStatus').innerText = "Document Verified";
            document.getElementById('resStage').innerText = "Submitted to Nusuk Portal for Visa Issuance";
            
            resultBox.classList.remove('d-none');
        }

        function submitApplication(event) {
            event.preventDefault();
            alert("Thank you! Your application and passport document have been received. Tracking code DIJA-" + Math.floor(10000 + Math.random() * 90000) + " has been sent to your email.");
            bootstrap.Modal.getInstance(document.getElementById('visaModal')).hide();
        }
    </script>
</body>
</html>
