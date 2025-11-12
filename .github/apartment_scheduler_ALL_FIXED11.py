"""
🏢 SCHEDULER of apartments
smart scheduling and callout system
"""

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

    # Loveland
    "Johnstown Plaza": {
        "city": "Johnstown",
        "type": "garden",
        "floors": 3,
        "indoor": False,
        "vehicle": "push cart",
        "crew_size": 1 
    },

    # Loveland Garden Style (Truck Drivers)
    "Vantage at Loveland": {
        "city": "Loveland",
        "type": "garden",
        "floors": 3,
        "indoor": False,
        "vehicle": "truck",
        "crew_size": 1
    },
    
    # Greeley Garden Style push cart and garage storage
    "Lariat": {
        "city": "Greeley",
        "type": "garden",
        "floors": 3,
        "indoor": False,
        "vehicle": "push cart",
        "crew_size": 1,
        "garage_site": True
    },
    
    # Garden Style Truck Driver 
    "Premier West Park": {
        "city": "Greeley",
        "type": "garden",
        "floors": 3,
        "indoor": False,
        "vehicle": "truck",
        "crew_size": 1
    },

    # Garden Style Truck Driver
    "Notch66": {
        "city": "Longmont",
        "type": "garden",
        "floors": 3,  # FIXED: Added missing field
        "indoor": False,
        "vehicle": "truck",
        "crew_size": 1
    },
    
    # Garden Style golf cart - Lafayette
    "Griffis Lafayette": {
        "city": "Lafayette",
        "type": "garden",
        "floors": 3,  # FIXED: Changed "flights" to "floors"
        "indoor": False,
        "vehicle": "golf cart",
        "crew_size": 1
    },

    # Garden Style golf cart - Longmont
    "Harvest Junction": {
        "city": "Longmont",
        "type": "garden",
        "floors": 3,  # FIXED: Changed "flights" to "floors"
        "indoor": False,
        "vehicle": "golf cart",
        "crew_size": 1
    },
    
    # Longmont areas from TE are: 
    "Moraine": {
        "city": "Longmont",
        "type": "garden",
        "floors": 0,  # FIXED: Changed "flights" to "floors"
        "indoor": False,
        "vehicle": None,
        "crew_size": 1
    },

    # Longmont
    "Clovis Point": {
        "city": "Longmont",
        "type": "garden",
        "floors": 3,  # FIXED: Changed "flights" to "floors"
        "indoor": False, 
        "vehicle": None,
        "crew_size": 1
    },

    # Boulder
    "3100": {
        "city": "Boulder",
        "te_city": "Boulder",
        "type": "garden",
        "floors": 3,  # FIXED: Changed "flights" to "floors"
        "indoor": False,
        "vehicle": None,
        "crew_size": 1 
    },

    # North at E470 crossing, etc
    "Arbour Commons": {
        "city": "Westminster",  # FIXED: Added closing quote
        "type": "garden",
        "floors": 3,  # FIXED: Changed "flights" to "floors", removed "outdoor"
        "indoor": False,  # FIXED: Changed "outdoor" to "indoor"
        "vehicle": "golf cart",
        "crew_size": 2
    },

    # Boondocks North Denver off 112th
    "Alexan": {
        "city": "Northglenn",
        "type": "city",
        "floors": 5,
        "indoor": True,
        "vehicle": "push cart",
        "crew_size": 1 
    },  
    
    # North at E470 crossing
    "Curate at Orchard Town": {
        "city": "Westminster",
        "type": "city",
        "floors": 5,
        "indoor": True,
        "vehicle": "push cart",
        "crew_size": 1 
    },

    # North at E470 crossing
    "Park 40": {
        "city": "Broomfield",
        "type": "garden",
        "floors": 3,
        "indoor": False,
        "vehicle": "push cart",
        "crew_size": 2 
    },

    # Thornton east of I25
    "Ridge at Thornton Station": {  # FIXED: Typo "Sation" → "Station"
        "city": "Thornton",
        "type": "garden",
        "floors": 3,
        "indoor": False,
        "vehicle": "push cart",
        "crew_size": 1 
    },

    # Downtown 
    "CoLab": {
        "city": "Denver",
        "type": "city",
        "floors": 5,
        "indoor": True,
        "vehicle": "push cart",
        "crew_size": 1 
    },

    # Downtown
    "Edison at Rino": {
        "city": "Denver",
        "type": "city",
        "floors": 5,
        "indoor": True, 
        "vehicle": "push cart",
        "crew_size": 1 
    },

    # Downtown
    "LoHi": {
        "city": "Denver",
        "type": "city",
        "floors": 5,
        "indoor": True, 
        "vehicle": "push cart",
        "crew_size": 1 
    },

    # Downtown 
    "Station at RiverFront": {
        "city": "Denver",
        "type": "city",
        "floors": 5,
        "indoor": True, 
        "vehicle": "push cart",
        "crew_size": 1 
    },

    # East Downtown Montclair, South park Hill, East Colfax
    "The Vixen": {
        "city": "Denver",
        "type": "city",
        "floors": 5,
        "indoor": True, 
        "vehicle": None, 
        "crew_size": 1
    },

    # East Colfax, West Aurora, Central Park, North Park Hill
    "Avantus": {
        "city": "Denver",
        "type": "city",
        "floors": 4,
        "indoor": True, 
        "vehicle": None, 
        "crew_size": 1
    },

    # Lakewood, Wheat Ridge, Applewood, West Denver, Green Mountain, Arvada
    "1600 Hoyt": {
        "city": "Lakewood",
        "type": "city",  # FIXED: Added closing quote
        "floors": 5,
        "indoor": True,
        "vehicle": "push cart",
        "crew_size": 1 
    },

    # West Denver, South Wheat Ridge, North Lakewood, Edgewater, Villa Park, Bel mar
    "14 & Jay": {
        "city": "Lakewood",
        "type": "city",
        "floors": 5,
        "indoor": True,
        "vehicle": "push cart",
        "crew_size": 1 
    },

    # Lakewood, Edgewater, West Denver, North Littleton, South Denver, West Englewood
    "Artwalk": {
        "city": "Englewood",
        "type": "garden",  # FIXED: Changed "outdoor" to "garden"
        "floors": 3,
        "indoor": False,
        "vehicle": "push cart",
        "crew_size": 1 
    },

    # West Englewood, Bow Mar, South Denver, South Lakewood, Bear Valley, Harvey Park, Fort Logan, north Littleton
    "Fielders Creek": {
        "city": "Denver",
        "type": "garden",
        "floors": 5,
        "indoor": False, 
        "vehicle": "push cart",
        "crew_size": 1 
    },

    #North Greenwood Village, Englewood, South Denver, Cherry Hills Village, Littleton
    "Kent Village": {
        "city": "Englewood",
        "type": "garden",
        "floors": 1,
        "indoor": False, 
        "vehicle": "truck",
        "crew_size": 1 
    },
    
    # Downtown, Capitol Hill, Congress Park, Denver Botanic
    "Griffis Cheeseman Park": {
        "city": "Denver",
        "type": "city",
        "floors": 6,
        "indoor": True, 
        "vehicle": "push cart",
        "crew_size": 1 
    },

    # Downtown, Capitol Hill, Congress Park, Denver Botanic
    "Montiview Manor": {  # FIXED: Typo "Montivew" → "Montiview"
        "city": "Denver",
        "type": "garden",
        "floors": 5,
        "indoor": False, 
        "vehicle": "push cart",
        "crew_size": 1 
    },

    # Aurora, 225&Colfax, Children's Hospital, 
    "Fellow at Fitzsimons": {
        "city": "Aurora",
        "type": "city",
        "floors": 5, 
        "indoor": True,
        "vehicle": "Push cart",
        "crew_size": 1
    },

    
    # Aurora, Aurora Mall, 225&Alameda, Sable, Public library
    "The Gild": {
        "city": "Aurora",
        "type": "city", 
        "floors": 5, 
        "indoor": True,
        "vehicle": "Push cart",
        "crew_size": 1
    },

    # South Glendale, Washington Park, South Denver, Virginia village
    "Asbury Plaza": {
        "city": "Denver",
        "type": "city",
        "floors": 5,
        "indoor": True, 
        "vehicle": "push cart",
        "crew_size": 1 
    },

    # South Glendale, Washington Park, South Denver, Virginia Village
    "Forest Cove": {
        "city": "Denver",
        "type": "city",
        "floors": 5,
        "indoor": True, 
        "vehicle": "push cart",
        "crew_size": 1 
    },

    #Englewood, South Denver, North Greenwood Village, Bow Mar east,  North Littleton, South Lakewood
    "Sequel": {
        "city": "Englewood",  # FIXED: Typo "Engelwood" → "Englewood"
        "type": "garden", 
        "floors": 3,
        "indoor": False,
        "vehicle": "push cart",
        "crew_size": 1 
    },

    # Bow Mar, FootHill Green, South Lakewood, Green Mountain, Columbine
    "M2": {
        "city": "Denver",
        "type": "garden",
        "floors": 3,
        "indoor": False,
        "vehicle": "truck",
        "crew_size": 1 
    },

    # Bow Mar, Columbine, South Lakewood, Green Mountain, Foothill Green
    "Ranch at Bear Creek": {
        "city": "Lakewood",
        "type": "garden",
        "floors": 2,
        "indoor": False, 
        "vehicle": "truck", 
        "crew_size": 1
    },
      


    # South Denver, Lone Tree, Highlands Ranch,
    "Regency": {
        "city": "Lone Tree",
        "type": "city", 
        "floors": 5, 
        "indoor": True,
        "vehicle": "Push cart",
        "crew_size": 1
    },

    # Aurora, Englewood east, " something village", Centennial?
    "Caliber at Cornerstar": {
        "city": "Aurora", 
        "type": "city", 
        "floors": 3, 
        "indoor": True,
        "vehicle": "Push cart",
        "crew_size": 1
    },

    # Parker, south, 
    "Twenty Mile":{
        "city": "Parker", 
        "type": "city", 
        "floors": 1, 
        "indoor": False,
        "vehicle": "golf cart",
        "crew_size": 1
    },

    # Castel pines, south lone tree
    "Citadel at Castle Pines": {
        "city": "Castle Pines", 
        "type": "city", 
        "floors": 1, 
        "indoor": False,
        "vehicle": "golf cart",
        "crew_size": 1
        },

    # Castle Pines, South Lone Tree, Castel Rock
    "Citadel at Castle Pines":{
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
        "vehicle": "Push cart",
        "crew_size": 1
    },

    # Monument, etc
    "Alta 25": {
        "city": "Monument",  # FIXED: Added closing quote and removed comma
        "type": "garden",
        "floors": 3,  # FIXED: Changed "flights" to "floors"
        "indoor": False,  # FIXED: Changed "outdoor" to "indoor"
        "vehicle": "golf cart",
        "crew_size": 1
    },

    # Colorado Springs etc
    "Broadmoor Ridge": {
        "city": "Colorado Springs",  # FIXED: Added closing quote, fixed name
        "type": "garden",
        "floors": 3,  # FIXED: Changed "flights" to "floors"
        "indoor": False,  # FIXED: Added opening quote, changed "outdoor" to "indoor"
        "vehicle": "truck",
        "crew_size": 1
    },

    # Colorado Springs etc
    "Edison at Chapel Hills": {
        "city": "Colorado Springs",  # FIXED: Added closing quote, fixed name
        "type": "garden",
        "floors": 3,  # FIXED: Changed "flights" to "floors"
        "indoor": False,  # FIXED: Changed "outdoor" to "indoor"
        "vehicle": None,
        "crew_size": 1
    },

    # Colorado Springs etc
    "Lodge at Black Forest": {
        "city": "Colorado Springs",  # FIXED: Added closing quote, fixed name
        "type": "garden",
        "floors": 3,  # FIXED: Changed "flights" to "floors"
        "indoor": False,  # FIXED: Changed "outdoor" to "indoor"
        "vehicle": "truck",
        "crew_size": 2
    },

    #Colorado Springs etc
    "Resort University": {
        "city": "Colorado Springs",  # FIXED: Added closing quote, fixed name
        "type": "garden",
        "floors": 3,  # FIXED: Changed "flights" to "floors"
        "indoor": False,  # FIXED: Changed "outdoor" to "indoor"
        "vehicle": "truck",
        "crew_size": 1
    },

    # Cimmarron Hills/Colorado Springs is near Upland Flats  
    "Upland Flats": {
        "city": "Colorado Springs",  # FIXED: Added closing quote, fixed name
        "type": "garden",
        "floors": 3,  # FIXED: Changed "flights" to "floors"
        "indoor": False,  # FIXED: Changed "outdoor" to "indoor"
        "vehicle": None,
        "crew_size": 1
    }
}

# ============================================
# EMPLOYEE DATABASE
# ============================================

employees = {
    # Add your real employees here!
    # Example format:
    "Example Employee": {
        "type": "regular",  # or "rotating" or "new"
        "days": ["Mon", "Tue", "Wed", "Thu", "Fri"],
        "sites": ["Quarry", "Lariat"],
        "vehicle_certified": ["truck"],  # or ["cart"] or ["push cart"] or []
        "phone": "970-555-0000",
        "reliability": "high"  # low, medium, high
    }
}


# ============================================
# HELPER FUNCTIONS
# ============================================

def get_todays_crew(day):
    """Get all employees working today"""
    working_today = []
    
    for name, info in employees.items():
        if day in info["days"]:
            working_today.append({
                "name": name,
                "sites": info["sites"],
                "phone": info["phone"],
                "type": info["type"]
            })
    
    return working_today


def get_site_info(site_name):
    """Get details about a specific site"""
    if site_name in sites:
        return sites[site_name]
    return None


def get_sites_by_city(city):
    """Get all sites in a specific city"""
    city_sites = []
    
    for site_name, info in sites.items():
        if info["city"] == city:
            city_sites.append(site_name)
    
    return city_sites


def get_sites_by_type(site_type):
    """Get all garden or city sites"""
    type_sites = []
    
    for site_name, info in sites.items():
        if info["type"] == site_type:
            type_sites.append(site_name)
    
    return type_sites


def get_sites_by_vehicle(vehicle_type):
    """Get all sites using a specific vehicle"""
    vehicle_sites = []
    
    for site_name, info in sites.items():
        if info.get("vehicle") == vehicle_type:
            vehicle_sites.append(site_name)
    
    return vehicle_sites


def find_callout_replacements(site_name, day):
    """Find available employees for emergency callout"""
    if site_name not in sites:
        return []
        
    site_info = sites[site_name]
    available = []
    
    for name, emp_info in employees.items():
        # Check if employee works this day
        if day in emp_info["days"]:
            # Check if they work at this site or nearby sites
            if site_name in emp_info["sites"]:
                available.append({
                    "name": name,
                    "phone": emp_info["phone"],
                    "priority": "HIGH - Regular at this site"
                })
            # Check if they work in same city
            elif any(s in emp_info["sites"] for s in get_sites_by_city(site_info["city"])):
                available.append({
                    "name": name,
                    "phone": emp_info["phone"],
                    "priority": "MEDIUM - Works in same city"
                })
    
    return available


def get_crew_by_site(site_name):
    """Get all employees assigned to a site"""
    crew = []
    
    for name, info in employees.items():
        if site_name in info["sites"]:
            crew.append(name)
    
    return crew


# ============================================
# DAILY SCHEDULE FUNCTIONS
# ============================================

def print_daily_schedule(day):
    """Print today's schedule"""
    print(f"\n{'='*70}")
    print(f"📅 DAILY SCHEDULE - {day}")
    print(f"{'='*70}\n")
    
    crew = get_todays_crew(day)
    
    if not crew:
        print("❌ No one scheduled today!")
        return
    
    # Group by site
    by_site = {}
    for person in crew:
        for site in person["sites"]:
            if site not in by_site:
                by_site[site] = []
            by_site[site].append(person)
    
    # Print each site
    for site_name, people in sorted(by_site.items()):
        if site_name not in sites:
            continue
        site_info = sites[site_name]
        vehicle_str = site_info.get('vehicle', 'None') if site_info.get('vehicle') else "No vehicle"
        print(f"🏢 {site_name}")
        print(f"   📍 {site_info['city']} | Type: {site_info['type'].upper()} | Vehicle: {vehicle_str}")
        print(f"   Crew:")
        for p in people:
            print(f"      • {p['name']} ({p['type']}) - {p['phone']}")
        print()


def handle_callout(site_name, day, employee_name):
    """Handle emergency callout - find replacements"""
    print(f"\n{'='*70}")
    print(f"🚨 CALLOUT ALERT - {site_name}")
    print(f"{'='*70}")
    print(f"Employee: {employee_name}")
    print(f"Day: {day}\n")
    
    replacements = find_callout_replacements(site_name, day)
    
    if not replacements:
        print("❌ No available replacements found!")
        return
    
    print("📞 CALL THESE PEOPLE (in order of priority):\n")
    
    # Sort by priority
    high = [r for r in replacements if "HIGH" in r["priority"]]
    medium = [r for r in replacements if "MEDIUM" in r["priority"]]
    
    for r in high:
        print(f"   🔥 {r['name']} - {r['phone']} ({r['priority']})")
    for r in medium:
        print(f"   ⚠️  {r['name']} - {r['phone']} ({r['priority']})")


# ============================================
# SEARCH & FILTER FUNCTIONS
# ============================================

def search_sites(city=None, site_type=None, vehicle=None):
    """Search sites by criteria"""
    results = []
    
    for site_name, info in sites.items():
        match = True
        
        if city and info["city"] != city:
            match = False
        if site_type and info["type"] != site_type:
            match = False
        if vehicle and info.get("vehicle") != vehicle:
            match = False
        
        if match:
            results.append(site_name)
    
    return results


def print_site_summary():
    """Print summary of all sites"""
    print(f"\n{'='*70}")
    print(f"🏢 SITE SUMMARY - {len(sites)} Locations")
    print(f"{'='*70}\n")
    
    # By city
    print("📍 BY CITY:")
    cities = {}
    for site_name, info in sites.items():
        city = info["city"]
        if city not in cities:
            cities[city] = []
        cities[city].append(site_name)
    
    for city in sorted(cities.keys()):
        print(f"   {city}: {len(cities[city])} sites")
        for site in sorted(cities[city]):
            vehicle = sites[site].get("vehicle", "None") if sites[site].get("vehicle") else "No vehicle"
            print(f"      • {site} ({vehicle})")
    
    print("\n🏗️ BY TYPE:")
    garden = get_sites_by_type("garden")
    city_type = get_sites_by_type("city")
    print(f"   Garden Style: {len(garden)} sites")
    print(f"   City (Indoor): {len(city_type)} sites")
    
    print("\n🚗 BY VEHICLE:")
    trucks = get_sites_by_vehicle("truck")
    golf_carts = get_sites_by_vehicle("golf cart")
    push_carts = get_sites_by_vehicle("push cart")
    none = get_sites_by_vehicle(None)
    print(f"   Trucks: {len(trucks)} sites")
    print(f"   Golf Carts: {len(golf_carts)} sites")
    print(f"   Push Carts: {len(push_carts)} sites")
    print(f"   No Vehicle: {len(none)} sites")


# ============================================
# EXAMPLE USAGE
# ============================================

if __name__ == "__main__":
    # Show site summary
    print_site_summary()
    
    # Example: Search for Denver sites
    print(f"\n{'='*70}")
    print("🔍 SEARCH: Denver Sites")
    print(f"{'='*70}")
    results = search_sites(city="Denver")
    for site in results:
        info = sites[site]
        print(f"   • {site} - {info.get('vehicle', 'No vehicle')}")
    
    # Example: Search for all truck sites
    print(f"\n{'='*70}")
    print("🔍 SEARCH: All Truck Driver Sites")
    print(f"{'='*70}")
    results = search_sites(vehicle="truck")
    for site in results:
        info = sites[site]
        print(f"   • {site} ({info['city']})")
