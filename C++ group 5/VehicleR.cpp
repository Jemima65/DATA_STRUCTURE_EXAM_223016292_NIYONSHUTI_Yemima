#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Base class
class Vehicle {
public:
    string model;
    string registrationNumber;
    bool isAvailable;

    Vehicle(string m, string regNo) {
        model = m;
        registrationNumber = regNo;
        isAvailable = true;
    }

    virtual void display() {
        cout << "Model: " << model 
             << ", \tReg No: " << registrationNumber 
             << ", \tStatus: " << (isAvailable ? "AVAILABLE" : "RENTED") << endl;
    }
};

// Single Inheritance
class Car : public Vehicle {
public:
    int numSeats;

    Car(string m, string regNo, int seats) : Vehicle(m, regNo) {
        numSeats = seats;
    }

    void display() override {
        Vehicle::display();
        cout << "Type: Car, \tSeats: " << numSeats << endl;
    }
};

// Multilevel Inheritance
class LuxurySUV : public Car {
public:
    bool hasWiFi;

    LuxurySUV(string m, string regNo, int seats, bool wifi) : Car(m, regNo, seats) {
        hasWiFi = wifi;
    }

    void display() override {
        Car::display();
        cout << "Luxury SUV with WiFi: " << (hasWiFi ? "Yes" : "No") << endl;
    }
};

// Hierarchical Inheritance
class Motorbike : public Vehicle {
public:
    bool hasHelmet;

    Motorbike(string m, string regNo, bool helmet) : Vehicle(m, regNo) {
        hasHelmet = helmet;
    }

    void display() override {
        Vehicle::display();
        cout << "Type: Motorbike, \tHelmet Included: " << (hasHelmet ? "Yes" : "No") << endl;
    }
};

class Truck : public Vehicle {
public:
    int loadCapacity; 

    Truck(string m, string regNo, int capacity) : Vehicle(m, regNo) {
        loadCapacity = capacity;
    }

    void display() override {
        Vehicle::display();
        cout << "Type: Truck, \tLoad Capacity: " << loadCapacity << " tons" << endl;
    }
};

// Multiple Inheritance example
class Insurance {
public:
    bool isInsured;

    Insurance() {
        isInsured = true;
    }

    void showInsurance() {
        cout << "Insurance: " << (isInsured ? "Covered" : "Not Covered") << endl;
    }
};

// Hybrid Inheritance (LuxurySUV inherits from Car, which inherits Vehicle, and also uses Insurance)
class LuxurySUVWithInsurance : public LuxurySUV, public Insurance {
public:
    LuxurySUVWithInsurance(string m, string regNo, int seats, bool wifi) 
        : LuxurySUV(m, regNo, seats, wifi) {}
};

class RentalSystem {
private:
    vector<Vehicle*> fleet;

public:
    void addSampleData() {
        fleet.push_back(new Car("Toyota Corolla", "CAR123", 5));
        fleet.push_back(new LuxurySUV("Range Rover", "SUV999", 7, true));
        fleet.push_back(new Motorbike("Yamaha MT-15", "BIKE456", true));
        fleet.push_back(new Truck("Volvo Truck", "TRUCK789", 10));
        fleet.push_back(new LuxurySUVWithInsurance("BMW X7", "SUV777", 7, true));
    }

    void listAvailableVehicles() {
        cout << "\nAvailable Vehicles:\n\n";
        bool found = false;
        for (auto v : fleet) {
            if (v->isAvailable) {
                v->display();
                found = true;
            }
        }
        if (!found) cout << "No vehicles available.\n";
    }

    void rentVehicle() {
        string regNo;
        cout << "Enter registration number to rent: ";
        cin.ignore();
        getline(cin, regNo);

        for (auto v : fleet) {
            if (v->registrationNumber == regNo && v->isAvailable) {
                v->isAvailable = false;
                cout << "Vehicle rented successfully!\n";
                return;
            }
        }
        cout << "Vehicle not found or already rented.\n";
    }

    void returnVehicle() {
        string regNo;
        cout << "Enter registration number to return: ";
        cin.ignore();
        getline(cin, regNo);

        for (auto v : fleet) {
            if (v->registrationNumber == regNo && !v->isAvailable) {
                v->isAvailable = true;
                cout << "Vehicle returned successfully!\n";
                return;
            }
        }
        cout << "Vehicle not found or was not rented.\n";
    }

    void showFleet() {
        cout << "\nFull Fleet of vehicles:\n";
        for (auto v : fleet) {
            v->display();
        }
    }

    ~RentalSystem() {
        for (auto v : fleet) {
            delete v;
        }
    }
};

int main() {
    RentalSystem system;
    system.addSampleData();

    int choice;
    do {
        cout << "\nVEHICLE RENTAL SYSTEM \n"<< "=====================\n";
        cout << "1. List Available Vehicles\n";
        cout << "2. Rent a Vehicle\n";
        cout << "3. Return a Vehicle\n";
        cout << "4. Show All Vehicles\n";
        cout << "0. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                system.listAvailableVehicles();
                break;
            case 2:
                system.rentVehicle();
                break;
            case 3:
                system.returnVehicle();
                break;
            case 4:
                system.showFleet();
                break;
            case 0:
                cout << "Thank you! Exiting system.\n";
                break;
            default:
                cout << "Invalid choice. Try again.\n";
        }
    } while (choice != 0);

    return 0;
}
