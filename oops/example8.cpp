#include <iostream>
using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
void greet(string name) {
    cout << "Hello, " << name << "!" << endl;
}

int main(int argc, char** argv) {
	greet("Alice");  // Calling the function
	return 0;
}