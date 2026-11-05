
# Experiment 10: Multi-Agent Travel Booking System
# Coordinator-Worker-Delegator Architecture
# Agentic AI Laboratory
# Malla Reddy University


# ---------------------------------------
# STEP 1: SAMPLE TRAVEL DATA
# ---------------------------------------

flights = [
    {
        "from": "Hyderabad",
        "to": "Delhi",
        "airline": "Air India",
        "price": 4500
    },
    {
        "from": "Hyderabad",
        "to": "Delhi",
        "airline": "IndiGo",
        "price": 3800
    },
    {
        "from": "Hyderabad",
        "to": "Mumbai",
        "airline": "Akasa Air",
        "price": 3200
    }
]

hotels = [
    {
        "city": "Delhi",
        "name": "Budget Stay Delhi",
        "price_per_night": 1800
    },
    {
        "city": "Delhi",
        "name": "City Comfort Hotel",
        "price_per_night": 2500
    },
    {
        "city": "Mumbai",
        "name": "Mumbai Budget Inn",
        "price_per_night": 2200
    }
]


# ---------------------------------------
# STEP 2: FLIGHT WORKER AGENT
# ---------------------------------------

class FlightAgent:

    def search_flight(self, source, destination):

        print("\n[Flight Agent] Searching flights...")

        available = [
            flight for flight in flights
            if flight["from"].lower() == source.lower()
            and flight["to"].lower() == destination.lower()
        ]

        if not available:
            return None

        selected = min(
            available,
            key=lambda flight: flight["price"]
        )

        print("[Flight Agent] Flight selected.")
        return selected


# ---------------------------------------
# STEP 3: HOTEL WORKER AGENT
# ---------------------------------------

class HotelAgent:

    def search_hotel(self, destination):

        print("\n[Hotel Agent] Searching hotels...")

        available = [
            hotel for hotel in hotels
            if hotel["city"].lower() == destination.lower()
        ]

        if not available:
            return None

        selected = min(
            available,
            key=lambda hotel: hotel["price_per_night"]
        )

        print("[Hotel Agent] Hotel selected.")
        return selected


# ---------------------------------------
# STEP 4: BUDGET WORKER AGENT
# ---------------------------------------

class BudgetAgent:

    def calculate_budget(self, flight, hotel, nights):

        print("\n[Budget Agent] Calculating expenses...")

        flight_cost = flight["price"]

        hotel_cost = (
            hotel["price_per_night"] * nights
        )

        total_cost = flight_cost + hotel_cost

        return {
            "flight_cost": flight_cost,
            "hotel_cost": hotel_cost,
            "total_cost": total_cost
        }


# ---------------------------------------
# STEP 5: DELEGATOR AGENT
# ---------------------------------------

class DelegatorAgent:

    def __init__(self):

        self.flight_agent = FlightAgent()
        self.hotel_agent = HotelAgent()
        self.budget_agent = BudgetAgent()

    def delegate_flight(self, source, destination):

        print("[Delegator] Assigning task to Flight Agent")

        return self.flight_agent.search_flight(
            source, destination
        )

    def delegate_hotel(self, destination):

        print("[Delegator] Assigning task to Hotel Agent")

        return self.hotel_agent.search_hotel(
            destination
        )

    def delegate_budget(self, flight, hotel, nights):

        print("[Delegator] Assigning task to Budget Agent")

        return self.budget_agent.calculate_budget(
            flight, hotel, nights
        )


# ---------------------------------------
# STEP 6: COORDINATOR AGENT
# ---------------------------------------

class CoordinatorAgent:

    def __init__(self):

        self.delegator = DelegatorAgent()

    def plan_trip(self, source, destination, nights, budget):

        print("\n[Coordinator] Travel request received.")

        # Delegate flight search
        flight = self.delegator.delegate_flight(
            source, destination
        )

        # Delegate hotel search
        hotel = self.delegator.delegate_hotel(
            destination
        )

        if flight is None or hotel is None:
            print("\nNo suitable travel options found.")
            return None

        # Delegate budget calculation
        expenses = self.delegator.delegate_budget(
            flight, hotel, nights
        )

        # Check budget
        within_budget = (
            expenses["total_cost"] <= budget
        )

        print("\n[Coordinator] Travel planning completed.")

        return {
            "source": source,
            "destination": destination,
            "nights": nights,
            "flight": flight,
            "hotel": hotel,
            "expenses": expenses,
            "budget": budget,
            "within_budget": within_budget
        }


# ---------------------------------------
# STEP 7: DISPLAY TRAVEL SUMMARY
# ---------------------------------------

def display_summary(result):

    if result is None:
        return

    print("\n" + "=" * 45)
    print("FINAL TRAVEL BOOKING SUMMARY")
    print("=" * 45)

    print("From:", result["source"])
    print("To:", result["destination"])
    print("Number of Nights:", result["nights"])

    print("\nFLIGHT DETAILS")
    print("Airline:", result["flight"]["airline"])
    print("Flight Cost: Rs.", result["expenses"]["flight_cost"])

    print("\nHOTEL DETAILS")
    print("Hotel:", result["hotel"]["name"])
    print(
        "Price per Night: Rs.",
        result["hotel"]["price_per_night"]
    )
    print("Hotel Cost: Rs.", result["expenses"]["hotel_cost"])

    print("\nBUDGET DETAILS")
    print("Available Budget: Rs.", result["budget"])
    print("Total Travel Cost: Rs.", result["expenses"]["total_cost"])

    if result["within_budget"]:
        print("Budget Status: WITHIN BUDGET")
    else:
        print("Budget Status: EXCEEDS BUDGET")

    print("\nNote: This is a simulated travel plan.")
    print("No real booking has been made.")


# ---------------------------------------
# STEP 8: MAIN PROGRAM
# ---------------------------------------

def main():

    print("EXPERIMENT 10: MULTI-AGENT TRAVEL SYSTEM")
    print("=" * 45)

    source = "Hyderabad"
    destination = "Delhi"
    nights = 3
    budget = 12000

    print("\nTravel Requirements")
    print("Source:", source)
    print("Destination:", destination)
    print("Nights:", nights)
    print("Budget: Rs.", budget)

    coordinator = CoordinatorAgent()

    result = coordinator.plan_trip(
        source,
        destination,
        nights,
        budget
    )

    display_summary(result)

    print("\nExperiment completed successfully.")


if __name__ == "__main__":
    main()
