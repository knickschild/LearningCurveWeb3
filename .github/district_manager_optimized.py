"""
🏢 DISTRICT MANAGER OPTIMIZATION SYSTEM
Complete hiring, scheduling, and callout management system
Optimized for district manager daily operations
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional
import json

# ============================================
# SITE DATABASE
# ============================================

sites = {
    # Fort Collins Garden Style push cart
    "Quarry": {
        "city": "Fort Collins",
        "type": "garden",
        "floors": 3,
        "indoor": False,
        "vehicle": "push cart",
        "crew_size": 2
    },
    "Johnstown Plaza": {
        "city": "Johnstown",
        "type": "garden",
        "floors": 3,
        "indoor": False,
        "vehicle": "push cart",
        "crew_size": 1
    },
    "Vantage at Loveland": {
        "city": "Loveland",
        "type": "garden",
        "floors": 3,
        "indoor": False,
        "vehicle": "truck",
        "crew_size": 1
    },
    "Lariat": {
        "city": "Greeley",
        "type": "garden",
        "floors": 3,
        "indoor": False,
        "vehicle": "push cart",
        "crew_size": 1,
        "garage_site": True
    },
    "Premier West Park": {
        "city": "Greeley",
        "type": "garden",
        "floors": 3,
        "indoor": False,
        "vehicle": "truck",
        "crew_size": 1
    },
    "Notch66": {
        "city": "Longmont",
        "type": "garden",
        "floors": 3,
        "indoor": False,
        "vehicle": "truck",
        "crew_size": 1
    },
    "Griffis Lafayette": {
        "city": "Lafayette",
        "type": "garden",
        "floors": 3,
        "indoor": False,
        "vehicle": "golf cart",
        "crew_size": 1
    },
    "Harvest Junction": {
        "city": "Longmont",
        "type": "garden",
        "floors": 3,
        "indoor": False,
        "vehicle": "golf cart",
        "crew_size": 1
    },
    "Moraine": {
        "city": "Longmont",
        "type": "garden",
        "floors": 0,
        "indoor": False,
        "vehicle": None,
        "crew_size": 1
    },
    "Clovis Point": {
        "city": "Longmont",
        "type": "garden",
        "floors": 3,
        "indoor": False,
        "vehicle": None,
        "crew_size": 1
    },
    "3100": {
        "city": "Boulder",
        "type": "garden",
        "floors": 3,
        "indoor": False,
        "vehicle": None,
        "crew_size": 1
    },
    "Arbour Commons": {
        "city": "Westminster",
        "type": "garden",
        "floors": 3,
        "indoor": False,
        "vehicle": "golf cart",
        "crew_size": 2
    },
    "Alexan": {
        "city": "Northglenn",
        "type": "city",
        "floors": 5,
        "indoor": True,
        "vehicle": "push cart",
        "crew_size": 1
    },
    "Curate at Orchard Town": {
        "city": "Westminster",
        "type": "city",
        "floors": 5,
        "indoor": True,
        "vehicle": "push cart",
        "crew_size": 1
    },
    "Park 40": {
        "city": "Broomfield",
        "type": "garden",
        "floors": 3,
        "indoor": False,
        "vehicle": "push cart",
        "crew_size": 2
    },
    "Ridge at Thornton Station": {
        "city": "Thornton",
        "type": "garden",
        "floors": 3,
        "indoor": False,
        "vehicle": "push cart",
        "crew_size": 1
    },
    "CoLab": {
        "city": "Denver",
        "type": "city",
        "floors": 5,
        "indoor": True,
        "vehicle": "push cart",
        "crew_size": 1
    },
    "Edison at Rino": {
        "city": "Denver",
        "type": "city",
        "floors": 5,
        "indoor": True,
        "vehicle": "push cart",
        "crew_size": 1
    },
    "LoHi": {
        "city": "Denver",
        "type": "city",
        "floors": 5,
        "indoor": True,
        "vehicle": "push cart",
        "crew_size": 1
    },
    "Station at RiverFront": {
        "city": "Denver",
        "type": "city",
        "floors": 5,
        "indoor": True,
        "vehicle": "push cart",
        "crew_size": 1
    },
    "The Vixen": {
        "city": "Denver",
        "type": "city",
        "floors": 5,
        "indoor": True,
        "vehicle": None,
        "crew_size": 1
    },
    "Avantus": {
        "city": "Denver",
        "type": "city",
        "floors": 4,
        "indoor": True,
        "vehicle": None,
        "crew_size": 1
    },
    "1600 Hoyt": {
        "city": "Lakewood",
        "type": "city",
        "floors": 5,
        "indoor": True,
        "vehicle": "push cart",
        "crew_size": 1
    },
    "14 & Jay": {
        "city": "Lakewood",
        "type": "city",
        "floors": 5,
        "indoor": True,
        "vehicle": "push cart",
        "crew_size": 1
    },
    "Artwalk": {
        "city": "Englewood",
        "type": "garden",
        "floors": 3,
        "indoor": False,
        "vehicle": "push cart",
        "crew_size": 1
    },
    "Fielders Creek": {
        "city": "Denver",
        "type": "garden",
        "floors": 5,
        "indoor": False,
        "vehicle": "push cart",
        "crew_size": 1
    },
    "Kent Village": {
        "city": "Englewood",
        "type": "garden",
        "floors": 1,
        "indoor": False,
        "vehicle": "truck",
        "crew_size": 1
    },
    "Griffis Cheeseman Park": {
        "city": "Denver",
        "type": "city",
        "floors": 6,
        "indoor": True,
        "vehicle": "push cart",
        "crew_size": 1
    },
    "Montiview Manor": {
        "city": "Denver",
        "type": "garden",
        "floors": 5,
        "indoor": False,
        "vehicle": "push cart",
        "crew_size": 1
    },
    "Fellow at Fitzsimons": {
        "city": "Aurora",
        "type": "city",
        "floors": 5,
        "indoor": True,
        "vehicle": "push cart",
        "crew_size": 1
    },
    "The Gild": {
        "city": "Aurora",
        "type": "city",
        "floors": 5,
        "indoor": True,
        "vehicle": "push cart",
        "crew_size": 1
    },
    "Asbury Plaza": {
        "city": "Denver",
        "type": "city",
        "floors": 5,
        "indoor": True,
        "vehicle": "push cart",
        "crew_size": 1
    },
    "Forest Cove": {
        "city": "Denver",
        "type": "city",
        "floors": 5,
        "indoor": True,
        "vehicle": "push cart",
        "crew_size": 1
    },
    "Sequel": {
        "city": "Englewood",
        "type": "garden",
        "floors": 3,
        "indoor": False,
        "vehicle": "push cart",
        "crew_size": 1
    },
    "M2": {
        "city": "Denver",
        "type": "garden",
        "floors": 3,
        "indoor": False,
        "vehicle": "truck",
        "crew_size": 1
    },
    "Ranch at Bear Creek": {
        "city": "Lakewood",
        "type": "garden",
        "floors": 2,
        "indoor": False,
        "vehicle": "truck",
        "crew_size": 1
    },
    "Regency": {
        "city": "Lone Tree",
        "type": "city",
        "floors": 5,
        "indoor": True,
        "vehicle": "push cart",
        "crew_size": 1
    },
    "Caliber at Cornerstar": {
        "city": "Aurora",
        "type": "city",
        "floors": 3,
        "indoor": True,
        "vehicle": "push cart",
        "crew_size": 1
    },
    "Twenty Mile": {
        "city": "Parker",
        "type": "city",
        "floors": 1,
        "indoor": False,
        "vehicle": "golf cart",
        "crew_size": 1
    },
    "Citadel at Castle Pines": {
        "city": "Castle Pines",
        "type": "city",
        "floors": 1,
        "indoor": False,
        "vehicle": "golf cart",
        "crew_size": 1
    },
    "Vistas at Plum Creek": {
        "city": "Castle Rock",
        "type": "city",
        "floors": 1,
        "indoor": False,
        "vehicle": "push cart",
        "crew_size": 1
    },
    "Alta 25": {
        "city": "Monument",
        "type": "garden",
        "floors": 3,
        "indoor": False,
        "vehicle": "golf cart",
        "crew_size": 1
    },
    "Broadmoor Ridge": {
        "city": "Colorado Springs",
        "type": "garden",
        "floors": 3,
        "indoor": False,
        "vehicle": "truck",
        "crew_size": 1
    },
    "Edison at Chapel Hills": {
        "city": "Colorado Springs",
        "type": "garden",
        "floors": 3,
        "indoor": False,
        "vehicle": None,
        "crew_size": 1
    },
    "Lodge at Black Forest": {
        "city": "Colorado Springs",
        "type": "garden",
        "floors": 3,
        "indoor": False,
        "vehicle": "truck",
        "crew_size": 2
    },
    "Resort University": {
        "city": "Colorado Springs",
        "type": "garden",
        "floors": 3,
        "indoor": False,
        "vehicle": "truck",
        "crew_size": 1
    },
    "Upland Flats": {
        "city": "Colorado Springs",
        "type": "garden",
        "floors": 3,
        "indoor": False,
        "vehicle": None,
        "crew_size": 1
    }
}


# ============================================
# APPLICANT DATABASE
# ============================================

applicants = {
    # Example applicant structure:
    # "John Doe": {
    #     "phone": "970-555-1234",
    #     "email": "john.doe@example.com",
    #     "status": "phone_screen",  # applied, phone_screen, interview_scheduled, interviewed, hired, rejected
    #     "applied_date": "2025-01-15",
    #     "preferred_cities": ["Denver", "Aurora"],
    #     "vehicle_certified": ["truck"],
    #     "availability": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    #     "interview_date": "2025-01-20",
    #     "interview_time": "10:00 AM",
    #     "notes": "Good phone screen, experienced",
    #     "rejection_reason": None  # If rejected
    # }
}


# ============================================
# EMPLOYEE DATABASE (Enhanced with shift tracking)
# ============================================

employees = {
    # Example employee with shift tracking:
    # "Jane Smith": {
    #     "type": "regular",  # regular, rotating, new
    #     "days": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    #     "sites": ["Quarry", "Lariat"],
    #     "vehicle_certified": ["truck", "golf cart"],
    #     "phone": "970-555-0000",
    #     "email": "jane.smith@example.com",
    #     "reliability": "high",  # low, medium, high
    #     "hire_date": "2024-06-01",
    #     "total_shifts_completed": 145,  # KEY: Track total shifts
    #     "shifts_this_month": 18,
    #     "callouts_this_month": 1,
    #     "last_callout_date": "2025-01-10",
    #     "available_for_extra_shifts": True,  # KEY: Availability flag
    #     "preferred_extra_shift_sites": ["Quarry", "Lariat", "Premier West Park"]
    # }
}


# ============================================
# JOB POSTINGS DATABASE
# ============================================

job_postings = {
    # "Posting-001": {
    #     "title": "Trash Valet - Fort Collins Area",
    #     "sites": ["Quarry", "Vantage at Loveland"],
    #     "cities": ["Fort Collins", "Loveland"],
    #     "vehicle_required": "push cart",
    #     "schedule": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    #     "posted_date": "2025-01-10",
    #     "status": "active",  # active, filled, closed
    #     "applicants": []  # List of applicant names
    # }
}


# ============================================
# SHIFT HISTORY DATABASE
# ============================================

shift_history = {
    # Track every shift for analytics
    # "2025-01-15": {
    #     "Quarry": ["Jane Smith", "Bob Johnson"],
    #     "Lariat": ["Mike Davis"]
    # }
}


# ============================================
# APPLICANT MANAGEMENT FUNCTIONS
# ============================================

def add_applicant(name: str, phone: str, email: str, availability: List[str],
                  preferred_cities: List[str], vehicle_certified: List[str] = None):
    """Add new applicant to system"""
    applicants[name] = {
        "phone": phone,
        "email": email,
        "status": "applied",
        "applied_date": datetime.now().strftime("%Y-%m-%d"),
        "preferred_cities": preferred_cities,
        "vehicle_certified": vehicle_certified or [],
        "availability": availability,
        "interview_date": None,
        "interview_time": None,
        "notes": "",
        "rejection_reason": None
    }
    print(f"✅ Applicant {name} added to system")
    return applicants[name]


def schedule_interview(applicant_name: str, date: str, time: str):
    """Schedule interview for applicant"""
    if applicant_name not in applicants:
        print(f"❌ Applicant {applicant_name} not found")
        return False

    applicants[applicant_name]["status"] = "interview_scheduled"
    applicants[applicant_name]["interview_date"] = date
    applicants[applicant_name]["interview_time"] = time
    print(f"✅ Interview scheduled for {applicant_name} on {date} at {time}")
    return True


def update_applicant_status(applicant_name: str, status: str, notes: str = ""):
    """Update applicant status"""
    valid_statuses = ["applied", "phone_screen", "interview_scheduled", "interviewed", "hired", "rejected"]

    if applicant_name not in applicants:
        print(f"❌ Applicant {applicant_name} not found")
        return False

    if status not in valid_statuses:
        print(f"❌ Invalid status. Must be one of: {', '.join(valid_statuses)}")
        return False

    applicants[applicant_name]["status"] = status
    if notes:
        applicants[applicant_name]["notes"] = notes

    print(f"✅ {applicant_name} status updated to: {status}")
    return True


def reject_applicant(applicant_name: str, reason: str):
    """Reject an applicant"""
    if applicant_name not in applicants:
        print(f"❌ Applicant {applicant_name} not found")
        return False

    applicants[applicant_name]["status"] = "rejected"
    applicants[applicant_name]["rejection_reason"] = reason
    print(f"❌ {applicant_name} rejected. Reason: {reason}")
    return True


def hire_applicant(applicant_name: str, sites: List[str], days: List[str], employee_type: str = "new"):
    """Convert applicant to employee"""
    if applicant_name not in applicants:
        print(f"❌ Applicant {applicant_name} not found")
        return False

    applicant = applicants[applicant_name]

    # Create employee record
    employees[applicant_name] = {
        "type": employee_type,
        "days": days,
        "sites": sites,
        "vehicle_certified": applicant["vehicle_certified"],
        "phone": applicant["phone"],
        "email": applicant["email"],
        "reliability": "medium",  # Start as medium, update later
        "hire_date": datetime.now().strftime("%Y-%m-%d"),
        "total_shifts_completed": 0,
        "shifts_this_month": 0,
        "callouts_this_month": 0,
        "last_callout_date": None,
        "available_for_extra_shifts": True,
        "preferred_extra_shift_sites": sites
    }

    # Update applicant status
    applicants[applicant_name]["status"] = "hired"

    print(f"🎉 {applicant_name} hired! Welcome to the team!")
    return True


def get_applicants_by_status(status: str) -> List[str]:
    """Get all applicants with specific status"""
    return [name for name, info in applicants.items() if info["status"] == status]


def get_todays_interviews(date: str = None) -> List[Dict]:
    """Get all interviews scheduled for today"""
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")

    interviews = []
    for name, info in applicants.items():
        if info.get("interview_date") == date and info["status"] == "interview_scheduled":
            interviews.append({
                "name": name,
                "time": info["interview_time"],
                "phone": info["phone"],
                "cities": info["preferred_cities"]
            })

    return sorted(interviews, key=lambda x: x["time"])


def print_applicant_pipeline():
    """Show hiring pipeline status"""
    print(f"\n{'='*70}")
    print("📋 HIRING PIPELINE")
    print(f"{'='*70}\n")

    statuses = ["applied", "phone_screen", "interview_scheduled", "interviewed"]

    for status in statuses:
        applicants_in_status = get_applicants_by_status(status)
        print(f"📌 {status.upper().replace('_', ' ')}: {len(applicants_in_status)} applicants")

        for name in applicants_in_status:
            info = applicants[name]
            print(f"   • {name}")
            print(f"     Phone: {info['phone']}")
            print(f"     Cities: {', '.join(info['preferred_cities'])}")
            if info.get("interview_date"):
                print(f"     Interview: {info['interview_date']} at {info['interview_time']}")
            print()


# ============================================
# JOB POSTING FUNCTIONS
# ============================================

def create_job_posting(posting_id: str, title: str, sites: List[str],
                       cities: List[str], vehicle: str, schedule: List[str]):
    """Create new job posting"""
    job_postings[posting_id] = {
        "title": title,
        "sites": sites,
        "cities": cities,
        "vehicle_required": vehicle,
        "schedule": schedule,
        "posted_date": datetime.now().strftime("%Y-%m-%d"),
        "status": "active",
        "applicants": []
    }
    print(f"✅ Job posting created: {posting_id}")
    return job_postings[posting_id]


def close_job_posting(posting_id: str):
    """Close job posting"""
    if posting_id not in job_postings:
        print(f"❌ Posting {posting_id} not found")
        return False

    job_postings[posting_id]["status"] = "closed"
    print(f"✅ Posting {posting_id} closed")
    return True


# ============================================
# SHIFT TRACKING FUNCTIONS (KEY OPTIMIZATION)
# ============================================

def record_shift_completion(employee_name: str, site: str, date: str = None):
    """Record that an employee completed a shift"""
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")

    if employee_name not in employees:
        print(f"❌ Employee {employee_name} not found")
        return False

    # Update employee shift counts
    employees[employee_name]["total_shifts_completed"] += 1
    employees[employee_name]["shifts_this_month"] += 1

    # Update shift history
    if date not in shift_history:
        shift_history[date] = {}
    if site not in shift_history[date]:
        shift_history[date][site] = []

    shift_history[date][site].append(employee_name)

    print(f"✅ Shift recorded: {employee_name} at {site} on {date}")
    print(f"   Total shifts: {employees[employee_name]['total_shifts_completed']}")
    return True


def get_employees_ranked_by_shifts(available_for_extra: bool = True) -> List[Dict]:
    """
    KEY FUNCTION: Get employees ranked by most shifts completed
    This helps district manager know who to call first for callouts
    """
    ranked = []

    for name, info in employees.items():
        # Filter by availability if requested
        if available_for_extra and not info.get("available_for_extra_shifts", False):
            continue

        ranked.append({
            "name": name,
            "phone": info["phone"],
            "total_shifts": info["total_shifts_completed"],
            "shifts_this_month": info["shifts_this_month"],
            "callouts_this_month": info["callouts_this_month"],
            "reliability": info["reliability"],
            "sites": info["sites"],
            "days": info["days"],
            "available_for_extra": info.get("available_for_extra_shifts", False)
        })

    # Sort by total shifts completed (descending)
    ranked.sort(key=lambda x: x["total_shifts"], reverse=True)

    return ranked


def print_shift_rankings(top_n: int = 20):
    """Display shift rankings for quick reference"""
    print(f"\n{'='*70}")
    print("🏆 EMPLOYEE SHIFT RANKINGS (Top Performers)")
    print(f"{'='*70}\n")

    ranked = get_employees_ranked_by_shifts()

    for i, emp in enumerate(ranked[:top_n], 1):
        print(f"#{i} {emp['name']}")
        print(f"   📞 {emp['phone']}")
        print(f"   📊 Total Shifts: {emp['total_shifts']} | This Month: {emp['shifts_this_month']}")
        print(f"   📍 Sites: {', '.join(emp['sites'][:3])}")
        print(f"   ⭐ Reliability: {emp['reliability'].upper()}")
        print(f"   ✅ Available for extra shifts: {'YES' if emp['available_for_extra'] else 'NO'}")
        print()


# ============================================
# OPTIMIZED CALLOUT REPLACEMENT (KEY FUNCTION)
# ============================================

def find_best_callout_replacement(site_name: str, day: str, top_n: int = 10) -> List[Dict]:
    """
    OPTIMIZED: Find best replacement using shift rankings + availability

    Priority system:
    1. HIGH: Works at this site regularly + high shift count
    2. MEDIUM-HIGH: Same city + high shift count
    3. MEDIUM: Works this day + available for extra
    4. LOW: Everyone else available
    """
    if site_name not in sites:
        return []

    site_info = sites[site_name]
    replacements = []

    # Get all employees ranked by shift count
    ranked_employees = get_employees_ranked_by_shifts(available_for_extra=True)

    for emp in ranked_employees:
        # Skip if doesn't work this day
        if day not in emp["days"]:
            continue

        priority_score = 0
        priority_label = ""

        # HIGH PRIORITY: Regular at this site
        if site_name in emp["sites"]:
            priority_score = 100 + emp["total_shifts"]  # Add shift bonus
            priority_label = f"🔥 HIGH - Regular at site ({emp['total_shifts']} total shifts)"

        # MEDIUM-HIGH: Same city worker
        elif site_info["city"] in [sites[s]["city"] for s in emp["sites"] if s in sites]:
            priority_score = 50 + emp["total_shifts"]
            priority_label = f"⚡ MEDIUM-HIGH - Same city ({emp['total_shifts']} total shifts)"

        # MEDIUM: Available for extra, works this day
        elif emp["available_for_extra"]:
            priority_score = 25 + emp["total_shifts"]
            priority_label = f"✅ MEDIUM - Available ({emp['total_shifts']} total shifts)"

        # LOW: Available but less ideal
        else:
            priority_score = emp["total_shifts"]
            priority_label = f"⚠️  LOW - Available ({emp['total_shifts']} total shifts)"

        replacements.append({
            "name": emp["name"],
            "phone": emp["phone"],
            "priority_score": priority_score,
            "priority_label": priority_label,
            "total_shifts": emp["total_shifts"],
            "shifts_this_month": emp["shifts_this_month"],
            "reliability": emp["reliability"]
        })

    # Sort by priority score (higher is better)
    replacements.sort(key=lambda x: x["priority_score"], reverse=True)

    return replacements[:top_n]


def handle_callout_optimized(site_name: str, day: str, employee_name: str):
    """
    OPTIMIZED callout handler with shift-based ranking
    """
    print(f"\n{'='*70}")
    print(f"🚨 CALLOUT ALERT - {site_name}")
    print(f"{'='*70}")
    print(f"Employee: {employee_name}")
    print(f"Day: {day}")
    print(f"Time: {datetime.now().strftime('%I:%M %p')}\n")

    # Record the callout
    if employee_name in employees:
        employees[employee_name]["callouts_this_month"] += 1
        employees[employee_name]["last_callout_date"] = datetime.now().strftime("%Y-%m-%d")

    # Find replacements using optimized system
    replacements = find_best_callout_replacement(site_name, day, top_n=10)

    if not replacements:
        print("❌ No available replacements found!")
        print("⚠️  Suggestion: Check applicant pool or contact part-time workers")
        return

    print("📞 CALL THESE PEOPLE (RANKED BY SHIFTS + PRIORITY):\n")

    for i, r in enumerate(replacements, 1):
        print(f"{i}. {r['name']} - {r['phone']}")
        print(f"   {r['priority_label']}")
        print(f"   Reliability: {r['reliability'].upper()} | Shifts this month: {r['shifts_this_month']}")
        print()

    print(f"{'='*70}")
    print("💡 TIP: Start from the top - they have the most experience!")
    print(f"{'='*70}\n")


# ============================================
# AVAILABILITY MANAGEMENT
# ============================================

def update_employee_availability(employee_name: str, available_for_extra: bool,
                                 preferred_sites: List[str] = None):
    """Update employee's availability for extra shifts"""
    if employee_name not in employees:
        print(f"❌ Employee {employee_name} not found")
        return False

    employees[employee_name]["available_for_extra_shifts"] = available_for_extra

    if preferred_sites:
        employees[employee_name]["preferred_extra_shift_sites"] = preferred_sites

    status = "AVAILABLE" if available_for_extra else "NOT AVAILABLE"
    print(f"✅ {employee_name} availability updated: {status}")
    return True


def get_available_employees_for_day(day: str) -> List[Dict]:
    """Get all employees available on a specific day"""
    available = []

    for name, info in employees.items():
        if day in info["days"] and info.get("available_for_extra_shifts", False):
            available.append({
                "name": name,
                "phone": info["phone"],
                "sites": info["sites"],
                "total_shifts": info["total_shifts_completed"]
            })

    # Sort by shift count
    available.sort(key=lambda x: x["total_shifts"], reverse=True)

    return available


# ============================================
# DISTRICT MANAGER DASHBOARD
# ============================================

def print_district_manager_dashboard():
    """Complete dashboard for district manager daily operations"""
    print("\n" + "="*70)
    print("👔 DISTRICT MANAGER DASHBOARD")
    print("="*70 + "\n")

    today = datetime.now().strftime("%Y-%m-%d")
    day_name = datetime.now().strftime("%A")[:3]

    # 1. Today's interviews
    print("📅 TODAY'S INTERVIEWS:")
    interviews = get_todays_interviews(today)
    if interviews:
        for interview in interviews:
            print(f"   • {interview['time']} - {interview['name']} ({interview['phone']})")
            print(f"     Cities: {', '.join(interview['cities'])}")
    else:
        print("   ✅ No interviews scheduled today")
    print()

    # 2. Hiring pipeline summary
    print("📋 HIRING PIPELINE SUMMARY:")
    for status in ["applied", "phone_screen", "interview_scheduled", "interviewed"]:
        count = len(get_applicants_by_status(status))
        print(f"   • {status.replace('_', ' ').title()}: {count}")
    print()

    # 3. Active job postings
    print("📢 ACTIVE JOB POSTINGS:")
    active_postings = [pid for pid, info in job_postings.items() if info["status"] == "active"]
    if active_postings:
        for pid in active_postings:
            info = job_postings[pid]
            print(f"   • {pid}: {info['title']}")
            print(f"     Sites: {', '.join(info['sites'][:3])}")
    else:
        print("   ℹ️  No active postings")
    print()

    # 4. Top performers (for callout reference)
    print("🏆 TOP 5 PERFORMERS (Call first for callouts):")
    top_performers = get_employees_ranked_by_shifts(available_for_extra=True)[:5]
    for i, emp in enumerate(top_performers, 1):
        print(f"   {i}. {emp['name']} - {emp['phone']}")
        print(f"      {emp['total_shifts']} shifts | Works: {', '.join(emp['days'])}")
    print()

    # 5. Today's availability
    print(f"✅ AVAILABLE TODAY ({day_name}):")
    available_today = get_available_employees_for_day(day_name)
    print(f"   {len(available_today)} employees available for extra shifts")
    print()

    # 6. Recent callouts
    print("⚠️  RECENT CALLOUTS (This month):")
    callout_employees = [(name, info["callouts_this_month"])
                         for name, info in employees.items()
                         if info["callouts_this_month"] > 0]
    callout_employees.sort(key=lambda x: x[1], reverse=True)

    if callout_employees:
        for name, count in callout_employees[:5]:
            print(f"   • {name}: {count} callouts")
    else:
        print("   ✅ No callouts this month - great team!")
    print()

    print("="*70 + "\n")


# ============================================
# SITE HELPER FUNCTIONS (From original)
# ============================================

def get_site_info(site_name):
    """Get details about a specific site"""
    return sites.get(site_name)


def get_sites_by_city(city):
    """Get all sites in a specific city"""
    return [name for name, info in sites.items() if info["city"] == city]


def get_sites_by_type(site_type):
    """Get all garden or city sites"""
    return [name for name, info in sites.items() if info["type"] == site_type]


def get_sites_by_vehicle(vehicle_type):
    """Get all sites using a specific vehicle"""
    return [name for name, info in sites.items() if info.get("vehicle") == vehicle_type]


# ============================================
# REPORTING FUNCTIONS
# ============================================

def generate_weekly_report():
    """Generate weekly performance report"""
    print(f"\n{'='*70}")
    print("📊 WEEKLY PERFORMANCE REPORT")
    print(f"{'='*70}\n")

    # Top performers
    print("🏆 TOP PERFORMERS THIS WEEK:")
    ranked = get_employees_ranked_by_shifts()
    for i, emp in enumerate(ranked[:10], 1):
        print(f"   {i}. {emp['name']}: {emp['shifts_this_month']} shifts this month")
    print()

    # Reliability concerns
    print("⚠️  RELIABILITY CONCERNS:")
    concerns = [(name, info) for name, info in employees.items()
                if info["callouts_this_month"] > 2 or info["reliability"] == "low"]

    if concerns:
        for name, info in concerns:
            print(f"   • {name}: {info['callouts_this_month']} callouts, "
                  f"reliability: {info['reliability']}")
    else:
        print("   ✅ No concerns - team performing well!")
    print()


def export_data_to_json(filename: str = "district_manager_data.json"):
    """Export all data to JSON file"""
    data = {
        "applicants": applicants,
        "employees": employees,
        "job_postings": job_postings,
        "shift_history": shift_history,
        "sites": sites
    }

    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"✅ Data exported to {filename}")


# ============================================
# EXAMPLE USAGE & DEMO
# ============================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("🏢 DISTRICT MANAGER OPTIMIZATION SYSTEM")
    print("   Streamlined hiring, scheduling, and callout management")
    print("="*70)

    # Demo: Add some sample employees
    print("\n📝 DEMO: Adding sample employees...\n")

    employees["Sarah Johnson"] = {
        "type": "regular",
        "days": ["Mon", "Tue", "Wed", "Thu", "Fri"],
        "sites": ["Quarry", "Lariat"],
        "vehicle_certified": ["truck", "push cart"],
        "phone": "970-555-1001",
        "email": "sarah.j@example.com",
        "reliability": "high",
        "hire_date": "2024-03-15",
        "total_shifts_completed": 187,
        "shifts_this_month": 22,
        "callouts_this_month": 0,
        "last_callout_date": None,
        "available_for_extra_shifts": True,
        "preferred_extra_shift_sites": ["Quarry", "Lariat", "Premier West Park"]
    }

    employees["Mike Rodriguez"] = {
        "type": "regular",
        "days": ["Mon", "Tue", "Wed", "Thu", "Fri"],
        "sites": ["CoLab", "Edison at Rino", "LoHi"],
        "vehicle_certified": ["push cart"],
        "phone": "303-555-2002",
        "email": "mike.r@example.com",
        "reliability": "high",
        "hire_date": "2024-01-10",
        "total_shifts_completed": 234,
        "shifts_this_month": 20,
        "callouts_this_month": 0,
        "last_callout_date": None,
        "available_for_extra_shifts": True,
        "preferred_extra_shift_sites": ["CoLab", "Edison at Rino", "LoHi", "Station at RiverFront"]
    }

    employees["Jessica Chen"] = {
        "type": "rotating",
        "days": ["Tue", "Wed", "Thu", "Fri", "Sat"],
        "sites": ["Fellow at Fitzsimons", "The Gild"],
        "vehicle_certified": ["push cart"],
        "phone": "720-555-3003",
        "email": "jessica.c@example.com",
        "reliability": "high",
        "hire_date": "2024-05-20",
        "total_shifts_completed": 156,
        "shifts_this_month": 18,
        "callouts_this_month": 1,
        "last_callout_date": "2025-01-05",
        "available_for_extra_shifts": True,
        "preferred_extra_shift_sites": ["Fellow at Fitzsimons", "The Gild", "Caliber at Cornerstar"]
    }

    employees["Brandon Lee"] = {
        "type": "new",
        "days": ["Mon", "Wed", "Fri"],
        "sites": ["Notch66", "Harvest Junction"],
        "vehicle_certified": ["truck", "golf cart"],
        "phone": "970-555-4004",
        "email": "brandon.l@example.com",
        "reliability": "medium",
        "hire_date": "2024-12-01",
        "total_shifts_completed": 45,
        "shifts_this_month": 12,
        "callouts_this_month": 2,
        "last_callout_date": "2025-01-08",
        "available_for_extra_shifts": False,
        "preferred_extra_shift_sites": []
    }

    # Demo: Add sample applicants
    add_applicant(
        "David Martinez",
        "303-555-5005",
        "david.m@example.com",
        ["Mon", "Tue", "Wed", "Thu", "Fri"],
        ["Denver", "Aurora"],
        ["push cart"]
    )

    schedule_interview("David Martinez", "2025-01-16", "2:00 PM")

    # Show the dashboard
    print_district_manager_dashboard()

    # Demo: Show shift rankings
    print_shift_rankings(top_n=4)

    # Demo: Handle a callout
    print("\n📞 DEMO: Simulating a callout...\n")
    handle_callout_optimized("Quarry", "Mon", "Sarah Johnson")

    # Show hiring pipeline
    print_applicant_pipeline()

    print("\n✅ Demo complete! System is ready for use.")
    print("\nKEY FEATURES:")
    print("   • Applicant tracking and interview scheduling")
    print("   • Shift-based ranking for optimal callout replacements")
    print("   • Availability management")
    print("   • District manager dashboard")
    print("   • Performance tracking and reporting")
    print("\n" + "="*70 + "\n")
