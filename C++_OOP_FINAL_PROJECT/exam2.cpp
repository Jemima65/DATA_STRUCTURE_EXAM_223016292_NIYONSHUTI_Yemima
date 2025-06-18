#include <iostream>   // For input-output stream
#include <cstring>    // For string operations like strcpy, strcmp

using namespace std;

// Structure to store a date (day/month/year)
struct Date {
    int day, month, year;
};

// Structure to store each student's attendance record
struct AttendanceRec {
    char studentID[10];       // Unique ID of student
    char studentName[30];     // Full name of student
    Date* date;               // Pointer to the attendance date
    char present[10];         // "Present" or "Absent" as a string
};

// Abstract base class for different report types
class ReportBase {
public:
    virtual void generate(const AttendanceRec* recs, int size) = 0; // Pure virtual function
    virtual ~ReportBase() {} // Virtual destructor (required for base class with virtual method)
};

// Derived class: generates daily attendance report
class DailyReport : public ReportBase {
public:
    void generate(const AttendanceRec* recs, int size) override {
        cout << "\n Daily Report \n";
        cout << "=============\n";

        if (size == 0) return; // No records to display

        // Get the first date to begin comparison
        int currentDay = recs[0].date->day;
        int currentMonth = recs[0].date->month;
        int currentYear = recs[0].date->year;

        // Print the first date heading
        cout << "Date: " << currentDay << "/" << currentMonth << "/" << currentYear << "\n";

        // Loop through all records
        for (int i = 0; i < size; ++i) {
            // If date changes, print a new date heading
            if (recs[i].date->day != currentDay || 
                recs[i].date->month != currentMonth || 
                recs[i].date->year != currentYear) {

                cout << "\n"; // Separate different days with a newline

                // Update the current date
                currentDay = recs[i].date->day;
                currentMonth = recs[i].date->month;
                currentYear = recs[i].date->year;

                cout << "Date: " << currentDay << "/" << currentMonth << "/" << currentYear << "\n";
            }

            // Print attendance details of student for the current date
            cout << "ID: " << recs[i].studentID
                 << " | Name: " << recs[i].studentName
                 << " | Present: " << recs[i].present << endl;
        }
    }
};

// Derived class: generates attendance trend report (summary)
class TrendReport : public ReportBase {
public:
    void generate(const AttendanceRec* recs, int size) override {
        cout << "\nTrend Report\n";
        cout << "============\n";

        // Loop through each student
        for (int i = 0; i < size; ++i) {
            bool alreadyCounted = false;

            // Check if student already counted before
            for (int j = 0; j < i; ++j) {
                if (strcmp(recs[i].studentID, recs[j].studentID) == 0) {
                    alreadyCounted = true;
                    break;
                }
            }

            // If not counted, calculate attendance days
            if (!alreadyCounted) {
                int daysPresent = 0;

                // Count how many times this student was marked "Present"
                for (int k = 0; k < size; ++k) {
                    if (strcmp(recs[i].studentID, recs[k].studentID) == 0 &&
                        strcmp(recs[k].present, "Present") == 0)
                        daysPresent++;
                }

                // Display student's attendance summary
                cout << "Student ID: " << recs[i].studentID
                     << " | Student Name: " << recs[i].studentName
                     << " | Days Present: " << daysPresent << endl;
            }
        }
    }
};

// Function to add new attendance record dynamically
void addRecord(AttendanceRec*& recs, int& size, const AttendanceRec& newRec) {
    AttendanceRec* newArr = new AttendanceRec[size + 1]; // Create bigger array

    // Copy existing data to new array
    for (int i = 0; i < size; ++i)
        newArr[i] = recs[i];

    newArr[size] = newRec; // Add the new record

    delete[] recs; // Free old memory
    recs = newArr; // Update pointer to new array
    size++;        // Increase size count
}

// Function to remove a record from the array by index
void removeRecord(AttendanceRec*& recs, int& size, int index) {
    if (index < 0 || index >= size) return; // Invalid index

    AttendanceRec* newArr = new AttendanceRec[size - 1]; // Smaller array

    // Copy all except the one at index
    for (int i = 0, j = 0; i < size; ++i) {
        if (i != index)
            newArr[j++] = recs[i];
    }

    delete[] recs; // Free old memory
    recs = newArr; // Point to new array
    size--;        // Decrease size count
}

// Entry point of the program
int main() {
    int size = 0; // No attendance records yet
    AttendanceRec* recs = nullptr; // Dynamic array of attendance records

    // Create date objects for three days
    Date* d1 = new Date{15, 6, 2025};
    Date* d2 = new Date{16, 6, 2025};
    Date* d3 = new Date{17, 6, 2025};

    // Student IDs and names
    const char* ids[5] = {"A1", "B2", "C3", "D4", "E5"};
    const char* names[5] = {"Anne", "Ally", "Sheja", "Queen", "Elie"};

    // Attendance records: 5 students × 3 days
    const char* attendance[5][3] = {
        {"Present", "Present", "Absent"},
        {"Absent",  "Present", "Present"},
        {"Present", "Absent",  "Present"},
        {"Present", "Present", "Present"},
        {"Absent",  "Absent",  "Present"}
    };

    // Fill the attendance records dynamically
    for (int day = 0; day < 3; ++day) {
        Date* currentDate = (day == 0) ? d1 : (day == 1) ? d2 : d3;

        for (int i = 0; i < 5; ++i) {
            AttendanceRec rec;
            strcpy(rec.studentID, ids[i]);              // Copy student ID
            strcpy(rec.studentName, names[i]);          // Copy student name
            rec.date = currentDate;                     // Set date
            strcpy(rec.present, attendance[i][day]);    // Copy "Present"/"Absent"

            addRecord(recs, size, rec);                 // Add to records
        }
    }

    // Create two reports: daily and trend
    ReportBase** reports = new ReportBase*[2];
    reports[0] = new DailyReport();
    reports[1] = new TrendReport();

    // Generate both reports
    for (int i = 0; i < 2; ++i)
        reports[i]->generate(recs, size);

    // Cleanup: free all dynamically allocated memory
    for (int i = 0; i < 2; ++i)
        delete reports[i];
    delete[] reports;

    delete d1;
    delete d2;
    delete d3;
    delete[] recs;

    return 0;
}
